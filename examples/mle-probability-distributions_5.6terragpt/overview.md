# Maximum Likelihood Estimation and Probability Distributions

## Audience and prerequisites

This bundle is for an introductory mathematical statistics course or a quantitatively oriented self-study learner. Learners should be comfortable with logarithms, differentiation, sums, and basic probability. Familiarity with random variables, expectation, variance, and independence is assumed.

## Learning objectives

After completing the bundle, a learner can:

1. Write a probability mass function (pmf) or probability density function (pdf) for an independent sample.
2. Treat observed values as fixed and the parameter as variable to form a likelihood.
3. Obtain and assess an MLE using the log-likelihood, derivatives, constraints, and endpoints.
4. Derive MLEs for Bernoulli, Poisson, normal, and exponential models.
5. Explain why an MLE is not automatically unbiased and how large-sample standard errors are obtained.

## Suggested sequence

1. Read `lesson.md` and reproduce each derivation.
2. Work the problems in `exercises.md` without consulting notes.
3. Compare with `solutions.md`; identify whether any error was algebraic, conceptual, or a missed constraint.
4. Use `references.md` for deeper treatment.

## Notation

Let X_1, ..., X_n be an independent and identically distributed (iid) sample from a model with parameter theta. The realized observations are x_1, ..., x_n. A parameter space is written Theta. The sample mean is x-bar = (1/n) sum_i x_i.

Probability statements concern random variables, for example P_theta(X=x). Likelihood compares parameter values after data have been observed: L(theta; x). It need not integrate or sum to one as a function of theta.
