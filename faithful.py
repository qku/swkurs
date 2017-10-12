import numpy as np
import pylab as pl

data = np.loadtxt('faithful.csv',delimiter=',',skiprows=1)

print("mean length: " + str(data[:,1].mean()))
print("std length: " + str(data[:,1].std())) 
print("mean wait: " + str(data[:,2].mean()))
print("std wait: " + str(data[:,2].std()))

fig = pl.figure(1, figsize=(9,8))

hist1 = fig.add_subplot(221)
n, bins, patches = hist1.hist(data[:,1], 50, normed=1, facecolor="blue", alpha=0.75)
hist1.text(0.5, 0.95, "Eruption length (mins)", ha="center", va="top", transform = hist1.transAxes)

hist2 = fig.add_subplot(222)
n, bins, patches = hist2.hist(data[:,2], 50, normed=1, facecolor="red", alpha=0.75)
hist2.text(0.5, 0.95, "Eruption wait (mins)", ha="center", va="top", transform = hist2.transAxes)

plot3 = fig.add_subplot(223)
plot3.plot(data[:,2], data[:,1], ".")
plot3.text(0.5, 0.95, "Wait/Length corr", ha="center", va="top", transform = plot3.transAxes)

plot4 = fig.add_subplot(224)
plot4.plot(data[:,0], data[:,1], ".")
plot4.text(0.5, 0.95, "Length corr", ha="center", va="top", transform = plot4.transAxes)

pl.show()
