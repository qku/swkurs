import numpy as np
import pylab as pl

x,y = np.loadtxt("rohr2.dat", unpack=True)

print(x.mean(), x.std(), y.mean(), y.std())
print np.corrcoef([x,y])

pl.plot(x,y,".")
pl.show()
