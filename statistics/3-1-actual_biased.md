[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

__Solution__
```python
resp = nsfg.ReadFemResp()
childern_per_household = resp['numkdhh']

# True PMF 
childern_per_household_pmf = thinkstats2.Pmf(childern_per_household,label='Unbiased')

# Biased PMF
childern_per_household_pmf_biased = BiasPmf(childern_per_household_pmf,'Biased')

# Plot Results
thinkplot.PrePlot(2)
thinkplot.Pmfs([childern_per_household_pmf, childern_per_household_pmf_biased])
thinkplot.Show(xlabel='Children in Household', ylabel='PMF')

# Compute PMF means
cph_pmf_mean = childern_per_household_pmf.Mean()
cph_pmf_biased_mean = childern_per_household_pmf_biased.Mean()

cph_pmf_mean, cph_pmf_biased_mean
# output (1.0242051550438309, 2.4036791006642821))
```

The unbiased mean number of children per household is ~1.0. The biased mean number of children per household is ~ 2.4.

__Distributions__

![P3.1 Distribution](https://github.com/leem99/dsp/blob/master/statistics/stats_p3_1.png)

