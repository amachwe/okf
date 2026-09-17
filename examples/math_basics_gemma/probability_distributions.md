# Advanced Theory of Probability Distributions

This document provides an advanced mathematical treatment of probability distributions, including concentration inequalities, generating functions, and special distributions used in advanced inference.

## 1. Foundational Theory & Concentration
### Law of Large Numbers (LLN) & Central Limit Theorem (CLT)
- **LLN**: Ensures sample means converge to the population mean $\mu$.
- **CLT**: Provides the basis for frequentist inference; $ \frac{\sum X_i - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} \mathcal{N}(0,1) $.

### Concentration Inequalities
Used to bound the probability that a random variable deviates from its expectation:
- **Markov’s Inequality**: $P(X \geq a) \leq \frac{E[X]}{a}$ for non-negative $X$.
- **Chebyshev’s Inequality**: $P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}$.
- **Chernoff Bound**: Provides exponentially decreasing bounds on the tail probabilities of sums of independent variables, crucial for deriving sample complexity in randomized algorithms.

## 2. Generating Functions
- **Moment Generating Function (MGF)**: $M_X(t) = E[e^{tX}]$. Useful for finding moments: $E[X^n] = M^{(n)}(0)$.
- **Characteristic Function**: $\phi_X(t) = E[e^{itX}]$. Always exists and is the Fourier transform of the PDF.

## 3. Advanced Distribution Classes
### The Exponential Family
A class of distributions that can be expressed in the form $f(x|\theta) = h(x) \exp(\eta(\theta) \cdot T(x) - A(\eta))$.
- **Includes**: Normal, Bernoulli, Poisson, Binomial, Gamma, and Multinomial.
- **Significance**: Provides a unified framework for maximum likelihood estimation and conjugate priors.

### Heavy-Tailed Distributions
- **Student’s t-Distribution**: $f(x) \propto (1 + \frac{x^2}{\nu})^{-\frac{\nu+1}{2}}$. Used when data has "outliers" or the variance is unknown.
- **Cauchy Distribution**: A special case of the Student's t with $\nu=1$. It has no defined mean or variance.

### Multi-dimensional Distributions
- **Dirichlet Distribution**: The multivariate generalization of the Beta distribution.
- **Multivariate Normal**: The cornerstone of Gaussian processes and Kalman filters.

## 4. Sampling & Simulation
- **Importance Sampling**: Estimating $E[f(x)]$ by sampling from a different distribution $q(x)$ and weighting by $p(x)/q(x)$.
- **Markov Chain Monte Carlo (MCMC)**: Sampling from complex posterior distributions using random walks (Metropolis-Hastings, Gibbs Sampling).
