[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

__Solution__

```python
below61 = dist.cdf(185.42)
below510 = dist.cdf(177.8)
between_perc = below61 - below510
between_perc
```
Approximately 34.3 percent of men are within the 5'10" to 6'1" range.
