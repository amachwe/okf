# Related Statistical & Information Concepts

This document explores the broader concepts that bridge and extend the theories of Probability Distributions and Maximum Likelihood Estimation.

## 1. Bayesian Inference
While MLE provides a "point estimate" based solely on the likelihood of the data, Bayesian inference provides a distribution of possible values for the parameters.

### Bayesian Theorem
$$P(\theta|x) = \frac{P(x|\theta)P(\theta)}{P(x)}$$
- **Prior $P(\theta)$**: Your belief about the parameter before seeing data.
- **Likelihood $P(x|\theta)$**: The probability of the data given the parameters (the core of MLE).
- **Posterior $P(\theta|x)$**: Your updated belief about the parameters after seeing the data.
- **Evidence $P(x)$**: A normalization constant.

### Connection to MLE/MAP
- **MLE** is equivalent to a **MAP** estimate where the prior $P(\theta)$ is uniform.
- **Variational Inference (VI)**: Used when the posterior is too complex to calculate directly; it turns the inference problem into an optimization problem (similar to MLE).

## 2. Information Theory
Information theory provides the mathematical framework for quantifying "uncertainty" and "information" in a system.

### Entropy ($H$)
A measure of the average uncertainty in a random variable $X$:
$$H(X) = -\sum p(x) \log p(x)$$
- **Maximum Entropy Principle**: Choosing a distribution that maximizes entropy subject to known constraints (e.g., the Normal distribution is the maximum entropy distribution for a given mean and variance).

### Kullback-Leibler (KL) Divergence
A measure of how one probability distribution $Q$ differs from a reference probability distribution $P$:
$$D_{KL}(P || Q) = \sum P(x) \log \frac{P(x)}{Q(x)}$$
- **Relationship to MLE**: Minimizing the KL divergence between the empirical distribution and the model distribution is mathematically equivalent to maximizing the log-likelihood.

## 3. Generalized Linear Models (GLMs)
GLMs provide the framework for applying MLE to various types of data by linking the mean of a distribution to a linear predictor.

### Components of a GLM:
1.  **Random Component**: The dependent variable $y$ follows a distribution from the exponential family (e.g., Binomial, Poisson, Normal).
2.  **Systematic Component**: A linear predictor $\eta = \beta_0 + \beta_1x_1 + ...$
3.  **Link Function**: A function $g(\mu) = \eta$ that maps the mean of the distribution $\mu$ to the linear predictor.
    - *Logistic Regression*: Binomial distribution + Logit link.
    - *Poisson Regression*: Poisson distribution + Log link.

## 4. Hypothesis Testing
While MLE is about **estimation** (finding the best $\theta$), Hypothesis Testing is about **inference** (deciding if a specific $\theta$ is plausible).

### Key Concepts:
- **Null Hypothesis ($H_0$)**: The assumption of "no effect" or "no difference."
- **P-value**: The probability of observing the results (or more extreme) assuming $H_0$ is true.
- **Confidence Intervals**: A range of values that is likely to contain the true parameter $\theta$ with a certain probability (e.g., 95%).
- **Type I & Type II Errors**:
    - **Type I ($\alpha$)**: False positive (rejecting $H_0$ when it is true).
    - **Type II ($\beta$)**: False negative (failing to reject $H_0$ when it is false).

## 5. Summary of Connections

| Concept | Relation to Distributions | Relation to MLE |
| :--- | :--- | :--- |
| **Bayesian** | Uses distributions as priors/posteriors | MAP is the "Bayesian version" of MLE |
| **Info Theory** | Entropy measures distribution "spread" | KL Divergence is the engine of ML loss |
| **GLM** | Defines the "Type" of distribution | Provides the structure for MLE optimization |
| **Hypothesis Testing** | Tests parameters of the distribution | Uses MLE as the point estimate for testing |
