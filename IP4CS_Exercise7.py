# Trapezoidal Rule Integration
# author: jiinso
# date: 9/23/2014

import numpy as np
import pylab as pl

velocities = np.loadtxt('velocities.txt',float)


a = 0.0
b = 100.0
N = 101
t = velocities[:,0]
v = velocities[:,1]
S = 0.5*(v[a]+v[b])
step = (b-a)/N
x = [0] * N

for counter in range(1, N):
    new_t = a + counter*step
    S += v[new_t]
    x[counter] = S

S *= step


print "Approximate displacement of particle: %5.8f." %S
pl.figure(1)
pl.plot(t,x, label='displacement')
pl.plot(t,v, label='velocity')
pl.title('Velocity versus time')
pl.xlabel('Time(s)')
pl.ylabel('Velocity (m/s)')
pl.legend()
pl.show()
