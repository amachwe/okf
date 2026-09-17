# Lesson: likelihood and common probability models

## 1. From a distribution to a likelihood

A parametric model specifies a family of distributions {f(x | theta): theta in Theta}. For an iid sample, the joint pmf/pdf is

L(theta; x) = product from i=1 to n of f(x_i | theta).

Once x is observed, the same algebraic expression is viewed as a function of theta and is called the **likelihood**. A maximum likelihood estimator (MLE) is any value

hat(theta) in argmax over theta in Theta of L(theta; x).

Products can underflow numerically and are tedious to differentiate. Because log is strictly increasing, maximize the log-likelihood

ell(theta) = log L(theta; x) = sum from i=1 to n log f(x_i | theta)

instead. A stationary point is only a candidate: verify it lies in Theta, compare boundaries where relevant, and check curvature or direct likelihood values.

## 2. Bernoulli and binomial models

For X_i ~ Bernoulli(p), with p in [0, 1],

P(X_i=x_i | p) = p^(x_i)(1-p)^(1-x_i), where x_i is 0 or 1.

Let S = sum_i x_i. Then

L(p) = p^S (1-p)^(n-S),
ell(p) = S log p + (n-S) log(1-p).

For 0 < S < n, differentiating gives ell'(p) = S/p - (n-S)/(1-p), so hat(p) = S/n = x-bar. Since ell''(p) = -S/p^2 - (n-S)/(1-p)^2 < 0, it is a maximum. If S=0, the maximum is at p=0; if S=n, it is at p=1. These boundary cases are why the parameter space matters.

A binomial count Y ~ Binomial(m, p) has pmf choose(m,y)p^y(1-p)^(m-y). For independent observations with possibly different m_i, the MLE is total successes divided by total trials.

## 3. Poisson model

For X_i ~ Poisson(lambda), lambda > 0,

P(X_i=x_i | lambda) = exp(-lambda) lambda^(x_i) / x_i!.

Ignoring terms not involving lambda,

ell(lambda) = -n lambda + (sum_i x_i) log lambda + constant.

The score equation is -n + (sum_i x_i)/lambda = 0, giving hat(lambda)=x-bar. The second derivative is -(sum_i x_i)/lambda^2, negative when the total count is positive. If every observation is zero and the parameter space is lambda >= 0, the maximum occurs at lambda=0; under the open space lambda>0, there is a supremum as lambda approaches zero but no attained MLE.

## 4. Normal model

Suppose X_i ~ Normal(mu, sigma^2), where sigma^2>0. The log-likelihood, up to no omitted parameter-dependent terms, is

ell(mu, sigma^2) = -(n/2) log(sigma^2) - [1/(2 sigma^2)] sum_i (x_i-mu)^2 + constant.

For a fixed sigma^2, differentiating in mu gives hat(mu)=x-bar. Substitution yields

hat(sigma^2)_MLE = (1/n) sum_i (x_i-x-bar)^2.

The denominator is n, not n-1. The familiar n-1 sample variance is unbiased for sigma^2, whereas the normal-model MLE is generally biased downward. Different estimation criteria can legitimately produce different estimators.

If sigma^2 is known, the MLE of mu is x-bar and its exact distribution is Normal(mu, sigma^2/n).

## 5. Exponential model and parameterization

For a waiting time X_i ~ Exponential(rate lambda), lambda>0,

f(x_i | lambda) = lambda exp(-lambda x_i), x_i >= 0.

Thus ell(lambda)=n log lambda - lambda sum_i x_i, and hat(lambda)=n/(sum_i x_i)=1/x-bar, provided the sum is positive.

Some texts use a scale parameter beta=1/lambda, with density (1/beta) exp(-x/beta). Under that parameterization, hat(beta)=x-bar. Always state the distribution and parameterization before interpreting an estimate.

## 6. Invariance and transformations

If hat(theta) maximizes L(theta), then for a one-to-one transformation tau=g(theta), the MLE of tau is g(hat(theta)). For example, if lambda-hat estimates an exponential rate, 1/lambda-hat estimates the mean waiting time. The rule concerns MLEs, not arbitrary procedures such as unbiased estimation.

## 7. Standard errors and Fisher information

Under suitable regularity conditions and for large n,

hat(theta) is approximately Normal(theta, 1 / I_n(theta)),

where I_n(theta) is Fisher information for the full sample. In one dimension it is often computed as

I_n(theta) = -E_theta[ell''(theta)].

A practical estimated standard error replaces theta by hat(theta). For a Poisson iid sample, I_n(lambda)=n/lambda, so SE(lambda-hat) is approximately sqrt(lambda-hat/n). For Bernoulli data, SE(p-hat) is approximately sqrt(p-hat(1-p-hat)/n). These normal approximations may be poor for small samples or estimates near a boundary.

## 8. A reliable MLE workflow

1. State the support and parameter space.
2. Write the joint likelihood, using independence only when justified.
3. Simplify with the log-likelihood, retaining all parameter-dependent terms.
4. Solve score equations.
5. Check second derivatives, boundaries, and constraints.
6. Report the estimate with its units and parameterization.
7. If uncertainty is needed, use model-based exact results, information, or an appropriate resampling/interval method.

## 9. Common pitfalls

- Dropping a factor that contains the parameter is invalid; dropping a data-only factor is safe for maximization.
- A pdf value can exceed one. Probabilities are integrals or sums, not pointwise density heights.
- Likelihood is not a posterior probability distribution over theta unless a prior and Bayes' rule have been introduced.
- Independence is an assumption, not a consequence of observing multiple values.
- An interior derivative calculation alone does not establish a global maximum.
