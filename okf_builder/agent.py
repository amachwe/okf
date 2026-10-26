"""Agent definition for the OKF Builder.

Loads configuration and the instruction prompt from YAML files, then wires
up a Google ADK agent backed by an OpenAI or local Ollama model (via
litellm) with file-system and web-search tools.
"""

import os

import google.adk.agents as agents
import google.adk.models.lite_llm as llm
import pypdf
import pypdf.errors
import requests
import yaml
from bs4 import BeautifulSoup
from tavily import TavilyClient

USE_LITE_LLM = True

MODEL_GEMMA4 = "ollama_chat/gemma4:12b"
MODEL_OPENAI = "gpt-5.6-terra"
MODEL = MODEL_OPENAI

TAVILY_API_KEY_ENV_VAR = "TAVILY_API_KEY"

FETCH_TIMEOUT_SECONDS = 10
MAX_PAGE_CHARS = 4000

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

with open("prompt.yaml", "r") as f:
    prompt = yaml.safe_load(f)

model = MODEL
if USE_LITE_LLM:
    model = llm.LiteLlm(model=MODEL)

# Instruction assembly
instruction = prompt["skills"] + "\nFollow user instructions."


def _resolve_path(path: str, name: str = "") -> str:
    """Resolve a path under the configured root, rejecting escapes."""
    root = os.path.realpath(config["path-root"])
    full_path = os.path.realpath(os.path.join(root, path, name))
    try:
        common_path = os.path.commonpath((root, full_path))
    except ValueError:
        raise ValueError("path is outside the configured root") from None
    if os.path.normcase(common_path) != os.path.normcase(root):
        raise ValueError("path is outside the configured root")
    return full_path


def write_file(path: str, name: str, content: str) -> str:
    """Write text content to a file, creating the directory if needed.

    Overwrites the file if it already exists.

    Args:
        path: Location of the file relative to the configured path-root.
            Must end in "/" and must not include the filename itself.
        name: Name of the file to write (e.g. "notes.md").
        content: Text content to write to the file.

    Returns:
        A message confirming the file was written, or an error message if
        the path was outside the configured root or the write failed.
    """
    try:
        full_path = _resolve_path(path, name)
        directory = os.path.dirname(full_path)
        os.makedirs(directory, exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Wrote: {full_path}"
    except ValueError as e:
        return f"Error writing file: {e}"
    except OSError as e:
        return f"Error writing file: {e}"


def read_file(path: str, name: str) -> str:
    """Read and return the text content of a plain-text file (e.g. .md, .txt, .csv).

    Args:
        path: Location of the file relative to the configured path-root.
            Must end in "/" and must not include the filename itself.
        name: Name of the file to read (e.g. "notes.md").

    Returns:
        The file's text content, or a message describing why it could not
        be read (not found, an I/O error, or invalid UTF-8 text).
    """
    try:
        full_path = _resolve_path(path, name)
        if not os.path.exists(full_path):
            return f"File: {name} not found at path {path}"
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeError as e:
        return f"Error reading file: {e}"
    except ValueError as e:
        return f"Error reading file: {e}"
    except OSError as e:
        return f"Error reading file: {e}"


def read_pdf_file(path: str, name: str) -> str:
    """Read and return the text content of a pdf file. Extension: .pdf

    Args:
        path: Location of the file relative to the configured path-root.
            Must end in "/" and must not include the filename itself.
        name: Name of the file to read (e.g. "file.pdf").

    Returns:
        The file's text content, or a message describing why it could not
        be read (not found, or an unreadable/corrupt/encrypted PDF).
    """
    try:
        full_path = _resolve_path(path, name)
        if not os.path.exists(full_path):
            return f"File: {name} not found at path {path}"
        reader = pypdf.PdfReader(full_path)
        text = ""
        for idx, page in enumerate(reader.pages):
            text += (page.extract_text() or "") + f"\n\n {idx}  \n\n"
        return text
    except ValueError as e:
        return f"Error reading file: {e}"
    except (OSError, pypdf.errors.PyPdfError) as e:
        return f"Error reading file: {e}"
    except Exception as e:  # malformed PDFs can raise KeyError, struct.error, etc.
        return f"Error reading file: {e}"


def read_directory(path: str) -> str:
    """List the names of files and subdirectories at a path.

    Args:
        path: Location to list, relative to the configured path-root. Must
            end in "/".

    Returns:
        Newline-separated entry names, or a message if the path does not
        exist or could not be read.
    """
    try:
        full_path = _resolve_path(path)
        if not os.path.exists(full_path):
            return f"Path not found: {full_path}"
        return "\n".join(os.listdir(full_path))
    except ValueError as e:
        return f"Error reading path: {e}"
    except OSError as e:
        return f"Error reading path: {e}"


def remove_file(path: str, name: str) -> str:
    """Delete a file. This cannot be undone.

    Args:
        path: Location of the file relative to the configured path-root.
            Must end in "/" and must not include the filename itself.
        name: Name of the file to remove (e.g. "notes.md").

    Returns:
        A message confirming the removal, or an error message if the file
        was not found or could not be removed.
    """
    try:
        full_path = _resolve_path(path, name)
        if not os.path.exists(full_path):
            return f"File: {name} not found at path {path}"
        os.remove(full_path)
        return f"File removed: {full_path}"
    except ValueError as e:
        return f"Error removing the file: {e}"
    except OSError as e:
        return f"Error removing the file: {e}"


def _fetch_page_text(url: str) -> str:
    """Fetch a page and return its visible text, trimmed to MAX_PAGE_CHARS."""
    response = requests.get(url, timeout=FETCH_TIMEOUT_SECONDS)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()

    text = " ".join(soup.get_text(separator=" ").split())
    return text[:MAX_PAGE_CHARS]


def search(query: str) -> str:
    """Search the web via Tavily and return content from .edu/Wikipedia hits.

    Runs an advanced Tavily search, keeps only results whose URL contains
    "edu" or "wikipedia", and for each one fetches the live page text
    (falling back to Tavily's own snippet if the fetch fails).

    Args:
        query: The search query.

    Returns:
        Concatenated "URL: ...\\nContent: ..." blocks for each matching
        result, "No results" if none matched, or an error message if the
        Tavily request itself failed (e.g. missing API key).
    """
    api_key = os.environ.get(TAVILY_API_KEY_ENV_VAR)
    if not api_key:
        return f"Error: {TAVILY_API_KEY_ENV_VAR} environment variable is not set"

    try:
        client = TavilyClient(api_key=api_key)
        response = client.search(query=query, search_depth="advanced")
        results = response["results"]
    except Exception as e:
        return f"Error accessing websites: {e}"

    candidates = ""
    for r in results:
        url = r.get("url", "")
        if "edu" in url or "wikipedia" in url:
            try:
                content = _fetch_page_text(url)
            except requests.RequestException:
                content = r.get("content", "")  # fall back to Tavily's own snippet
            candidates += f"\nURL: {url}\nContent: {content}\n"

    return candidates if candidates else "No results"


root_agent = agents.Agent(
    name="OKF_Builder",
    description="Build OKF bundles",
    instruction=instruction,
    model=model,
    tools=[write_file, read_directory, read_file, remove_file, search, read_pdf_file],
)
