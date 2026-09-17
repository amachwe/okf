# Solutions

## 1. Bernoulli likelihood

There are S=4 successes and n-S=2 failures. Thus L(p)=p^4(1-p)^2 and ell(p)=4 log p + 2 log(1-p). The MLE is p-hat=4/6=2/3. Its plug-in large-sample standard error is sqrt[(2/3)(1/3)/6]=sqrt(1/27), approximately 0.192.

## 2. Boundary case

With S=0, L(p)=(1-p)^12, which is maximized at p-hat=0 on [0,1]. On the open parameter space 0<p<1, no MLE exists: likelihood can be made arbitrarily close to one as p approaches zero but never reaches one.

## 3. Poisson counts

The total is 12 and n=4. Up to a constant, ell(lambda)=-4lambda+12 log lambda. Setting the derivative -4+12/lambda to zero gives lambda-hat=3. Since ell''(lambda)=-12/lambda^2, observed information at 3 is 12/9=4/3. The standard-error approximation is 1/sqrt(4/3)=sqrt(3/4), approximately 0.866. Equivalently, sqrt(lambda-hat/n)=sqrt(3/4).

## 4. Normal measurements

The mean is x-bar=5. The squared deviations are 9, 1, and 16, totaling 26. Therefore mu-hat=5 and sigma^2-hat_MLE=26/3, approximately 8.667. The unbiased sample variance is 26/(3-1)=13. The estimators differ because unbiasedness is not the criterion defining the MLE.

## 5. Exponential reliability model

For n=5 and total time 40, lambda-hat=n/sum x_i=5/40=0.125 per hour. By invariance, the estimated mean is 1/lambda-hat=8 hours. If beta is the mean/scale parameter, beta-hat=x-bar=40/5=8 hours.

## 6. Likelihood versus probability

After data are fixed, L(p;x) is a relative support function over possible p values and generally does not integrate to one over p in [0,1]. A prior distribution for p, combined with the likelihood through Bayes' rule and normalization, produces a posterior distribution.

## 7. Model check prompt

A Poisson model imposes equality of mean and variance. Substantially larger variance indicates overdispersion, possibly due to unobserved heterogeneity, dependence, or a changing arrival rate. A Poisson-based standard error may then be too small because it relies on the incorrect variance assumption.
