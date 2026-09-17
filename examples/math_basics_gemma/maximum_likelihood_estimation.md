# Advanced Maximum Likelihood Estimation (MLE)

Maximum Likelihood Estimation (MLE) is the cornerstone of statistical inference, providing a framework for parameter estimation by maximizing the probability of observed data.

## 1. Core Mathematical Foundations

### Likelihood vs. Probability
- **Probability**: $P(x|\theta)$ - The probability of data $x$ given a fixed parameter $\theta$.
- **Likelihood**: $L(\theta) = P(x|\theta)$ - The probability of the observed data as a function of the unknown parameters $\theta$.
- **Log-Likelihood**: $\ell(\theta) = \ln L(\theta)$. Because the natural logarithm is strictly monotonic, $\arg\max_{\theta} L(\theta) = \arg\max_{\theta} \ell(\theta)$.

## 2. Fisher Information & Geometry
The curvature of the log-likelihood surface provides information about the precision of the estimate.

### Fisher Information Matrix
$$\mathcal{I}(\theta) = -E\left[ \frac{\partial^2}{\partial \theta^2} \ell(\theta) \right]$$
- **Interpretation**: High curvature (large $\mathcal{I}$) implies a "sharp" peak in likelihood, meaning the data provides a lot of information about $\theta$.
- **Fisher Scoring**: An iterative method for MLE where the Hessian is replaced by the expected Fisher Information. This is more stable than the standard Newton-Raphson method when the observed Hessian is near-singular.

### Cramér-Rao Lower Bound (CRLB)
For any unbiased estimator $\hat{\theta}$, the variance is bounded:
$$\text{Var}(\hat{\theta}) \geq \frac{1}{\mathcal{I}(\theta)}$$
An estimator achieving this bound is **efficient**.

## 3. Asymptotic Properties
For large sample sizes $n$, MLE estimators typically exhibit:
1.  **Consistency**: $\hat{\theta} \xrightarrow{p} \theta_0$ as $n \to \infty$.
2.  **Asymptotic Normality**: $\sqrt{n}(\hat{\theta} - \theta_0) \xrightarrow{d} \mathcal{N}(0, \mathcal{I}(\theta_0)^{-1})$.

## 4. Estimation in Complex Scenarios

### The Delta Method
Used to find the variance of a function of an MLE, $g(\hat{\theta})$. If $\hat{\theta}$ is asymptotically normal, then:
$$\text{Var}(g(\hat{\theta})) \approx \nabla g(\theta)^T \mathcal{I}(\theta)^{-1} \nabla g(\theta)$$
This is vital for constructing confidence intervals for non-linear metrics.

### Expectation-Maximization (EM) Algorithm
Used when the likelihood is difficult to maximize directly because the data contains **latent variables** (hidden variables).
1.  **E-Step**: Compute the expected value of the log-likelihood given the current parameter estimate.
2.  **M-Step**: Maximize that expectation to update the parameters.
*Primary application: Gaussian Mixture Models (GMM).*

## 5. Regularized Likelihood (MAP)
When $n$ is small or the parameter space is high-dimensional, MLE can overfit.
**Maximum A Posteriori (MAP)** introduces a prior $P(\theta)$:
$$P(\theta|x) \propto L(\theta)P(\theta)$$
- **L2 Regularization (Ridge)**: Corresponds to a Gaussian prior.
- **L1 Regularization (Lasso)**: Corresponds to a Laplace prior.

## 6. Comparison Table

| Metric | MLE | MAP | GMM/EM |
| :--- | :--- | :--- | :--- |
| **Input** | Likelihood $P(x\|\theta)$ | Likelihood + Prior $P(\theta)$ | Likelihood + Hidden Variables |
| **Robustness** | Low (overfits) | High (regularized) | High (handles complexity) |
| **Key Use Case** | Standard estimation | Sparse models, small $n$ | Clustering, Latent variables |
| **Complexity** | Low | Medium | High |
