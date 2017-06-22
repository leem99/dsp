[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

 ```python

firsts['totalwgt_lb'].mean(), others['totalwgt_lb'].mean()

birth_weight_diff = CohenEffectSize(firsts['totalwgt_lb'],others['totalwgt_lb'])
birth_weight_diff

```
birth_weight_diff = -0.088672927072602006


First born babies tend to be smaller than other babies. However, like the difference in pregancy length, this effect is insignificant. Cohen's d values below 0.2 tend to indicate that the effect is small.

[http://www.uv.es/~friasnav/EffectSizeBecker.pdf](http://www.uv.es/~friasnav/EffectSizeBecker.pdf)
