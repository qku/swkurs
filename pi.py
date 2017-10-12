import numpy as np

amount = input("number: ")

x = np.random.random(size=amount)
y = np.random.random(size=amount)

distance = np.sqrt((x*x) + (y*y))

pi = 4*(float(len(distance[distance<=1]))/len(distance))
print("Pi: " + str(pi))
print(pi/np.pi)
