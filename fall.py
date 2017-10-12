# falling object with friction
# using odeint

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Luftwiderstandskraft Fussball
rho = 1.184 # Luftdichte (kg/m^3)
r  =  0.11 # Fussballradius (m)
cw =  0.45 # Kugel CW-Wert
mass  =  0.43 # Masse Fussball (kg)
g = 9.81 # Erdbeschleunigung

area = np.pi * r**2

def F(y, t):
        """
        Return derivatives for 2nd order ODE y'' = -g + friction/mass.
        """
        v = np.sqrt(y[1]**2+y[3]**2) # Geschwindigkeit
        frforce = 0.5 * cw * rho * area * (y[1]**2)
        
        dy = [0, 0, 0, 0]                     		 # preallocate list to store derivatives
        dy[0] = y[1]                                 # first derivative of x(t)
        dy[1] = -(y[1]/v) * frforce/mass             # second derivative of x(t)
        dy[2] = y[3]                                 # first derivative of y(t)
        dy[3] = -g -(y[3]/v) * frforce/mass          # second derivative of y(t)
        return dy

# array of time values to study
t_min = 0.0; t_max = 5.0; dt = 0.05
t = np.arange(t_min, t_max+dt, dt)

# initial conditions
v0 = 140.0 / 3.6 # 140 km/h
angle = 45. * np.pi / 180.
y0 = (0.0, v0 * np.cos(angle), 0.0, v0 * np.sin(angle))

# get series of points 
# y[:,0] corresponds to position (= distance from player over ground)
# y[:,1] corresponds to velocity in x
# y[:,2] corresponds to position (=height)
# y[:,3] corresponds to velocity in y
y = odeint(F, y0, t)

# display result 
fig = plt.figure() # Create figure; then, add plots.
fig.canvas.set_window_title('A Falling Football')
xyplot = fig.add_subplot(211)
plt.plot(y[:,0], y[:, 2], linewidth=2)
xyplot.text(0.5, 0.95, "xy-Position", ha="center", va="top", transform = xyplot.transAxes)

# x-axis
z = np.zeros(len(t))
plt.plot(y[:,0], z, 'r-')

skip = 5
t_test = t[::skip]   # compare at a subset of points
#plt.plot(t_test, y0[0]-0.5*9.81*t_test**2, 'bo') # exact solution for y0 = (1,0)

vel = fig.add_subplot(212)    # Velocity Create figure; then, add plots.
plt.plot(t, y[:, 1], linewidth=2)
vel.text(0.5, 0.95, "Velocity (m/s)", ha="center", va="top", transform = vel.transAxes)

plt.plot(t_test, y0[1]-9.81*t_test, 'bo') # exact solution for y0 = (1,0)

plt.show()

