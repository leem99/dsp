[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

__Solution__


PMF

```python
rand_nums = np.random.random(1000)

rand_nums_pmf = thinkstats2.Pmf(rand_nums,label='Random Numbers PMF')
thinkplot.pmf(rand_nums_pmf,linewidth=0.1)
thinkplot.Config(xlabel='Random Number', ylabel='PMF')
```

Nothing looks particulary "wrong" with the pmf. However, instead of being completely uniform, there are some gaps in the distribution. This is a discrete data set with a finite number of values. For some interval, a random number had not been drawn.

![PMF](https://github.com/leem99/dsp/blob/master/statistics/p42_pmf.png)

CDF

```python
rand_nums_cdf = thinkstats2.Cdf(rand_nums,label = 'Random Numbers CDF')
thinkplot.cdf(rand_nums_cdf)
thinkplot.Config(xlabel='Random Number', ylabel='CDF')
```

![CDF](https://github.com/leem99/dsp/blob/master/statistics/p42_cdf.png)

Because the CDF is approximately linear, one can infer that the distribution is uniform.

