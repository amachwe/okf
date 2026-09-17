# Exercises

Use natural logarithms. State parameter spaces and justify maxima.

## 1. Bernoulli likelihood

Six independent Bernoulli observations are (1, 0, 1, 1, 0, 1).

1. Write L(p) and ell(p), ignoring only factors independent of p.
2. Find the MLE of p.
3. Give the large-sample plug-in standard error.

## 2. Boundary case

An iid Bernoulli sample of size 12 contains no successes.

1. Find the MLE when p is allowed to lie in [0,1].
2. What changes if the parameter space is stated as 0 < p < 1?

## 3. Poisson counts

Four independent Poisson counts are 3, 0, 2, and 7.

1. Derive the log-likelihood up to an additive constant.
2. Find the MLE of lambda.
3. Find the observed-information standard-error approximation using -ell''(lambda-hat).

## 4. Normal measurements

For observations 2, 4, and 9 assumed iid Normal(mu, sigma^2), estimate mu and sigma^2 by maximum likelihood. Contrast the MLE of sigma^2 with the usual unbiased sample variance.

## 5. Exponential reliability model

Five independent lifetimes have total observed time 40 hours and are modeled as Exponential(rate lambda).

1. Find lambda-hat and the estimated mean lifetime.
2. Re-express the result if the model is parameterized by mean beta=1/lambda.

## 6. Likelihood versus probability

Explain in two or three sentences why L(p; x) is not generally a probability distribution for p. Then identify what additional ingredient is needed to obtain a posterior distribution for p.

## 7. Model check prompt

A team applies a Poisson model to daily customer arrivals but observes that the sample variance is much larger than the sample mean. What model assumption is questionable, and why might the Poisson MLE standard error be misleading?
