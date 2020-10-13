
# coding: utf-8

from scipy import stats
import numpy as np
from itertools import chain
from scipy.stats import chi2_contingency
import jpegio as jio
import collections

img = jio.read('00576.jpg')
g = img.coef_arrays[0]
g = g.reshape(g.shape[0]*g.shape[1])

for ind in range(30):
    g1 = g[0.03*len(g)*i:0.03*len(g)*(i+1)]
    num = collections.Counter(g)
    deg, cnt = zip(*num.items())

    print(deg)
    print(cnt)

    t = 2**11
    pairnum = int(t/2)
    print(pairnum)
    y = np.ones((pairnum, 1))
    yy = np.ones((pairnum, 1))

    deg = list(deg)
    cnt = list(cnt)

    o = []
    for i in range(-1024, 1023, 2):
        j = int(i/2)
        if i in deg:
            add = deg.index(i)
            h1 = cnt[add]
        else:
            h1 = 0
        if i+1 in deg:
            add = deg.index(i+1)
            h2 = cnt[add]
        else:
            h2 = 0
        if h1+h2 > 0:
            y[j] = (h1+h2)/2.0
            yy[j] = h1
            o.append([h1, h2])
        else:
            t = t-2
    print(o)

    t, p = stats.chisquare(yy, f_exp=y)
    print(t)
    print(p)

    chi2, p, dof, ex = chi2_contingency(o, correction=False)
    print(chi2)
    print(p)
