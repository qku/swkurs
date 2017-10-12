import numpy as np
import pylab as pl

data = np.loadtxt("rohr1.dat")

print(data.mean(), data.std())

n, bins, patches = pl.hist(data, 50, normed=1, facecolor="blue", alpha=0.75)

pl.show()
