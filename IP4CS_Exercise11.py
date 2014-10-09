# In Class Exercise
# Derivatives: Runge Kutta Method & Leap Frog Method
# author: jiinso
# date: 10/9/2014

import numpy as np
import pylab as pl

# This problem deals with the motion of a swinging pendulum.
# Plot the change in the angle theta with time using the Runge Kutta Method and the Leap Frog Method.


# Define the angular acceleration of the system as 'acc' that takes the argument 'theta'.
def acc(theta):
    return -9.8*np.sin(theta)            


# --------------------------Part 1: Runge Kutta Method ----------------------------------------------------------------------------------------
theta = np.pi / 6.0                      # angle of the pendulum in radians (initial angle pendulum is pulled to)
omega = 0.0                                # initial angular velocity
a = 0.0                                         # a = start of time
b = 10.0                                       # b = end of time
N = 1000                                   # number of steps
h = (b-a)/N                                 # step sizes
L = 1.0                                         # length of string (trivial in this case)
tpoints = np.arange(a, b, h)        # list of time points from 0 to 10 seconds
omegapoints = []
thetapoints = []                           # empty list of thetapoints

for t in tpoints:
    omegapoints.append(omega)
    thetapoints.append(theta)
    omega += h*acc(theta)
    theta += h*omega


pl.plot(tpoints, omegapoints, label='Omega')
pl.plot(tpoints, thetapoints, label='Theta')
pl.xlabel("t")
pl.ylabel("x(t)")



# --------------------------Part 2: Leap Frog Method ----------------------------------------------------------------------------------------
a = 0.0                                         # a = start of time
b = 10.0                                       # b = end of time
N = 1000                                  # number of steps
h = (b-a)/N                                 # step sizes
L = 1.0                                         # length of string (trivial in this case)
tpoints = np.arange(a, b, h)        # list of time points from 0 to 10 seconds
theta_lf = np.pi /6.0                        # angle of the pendulum in radians (initial angle pendulum is pulled to)
omega_lf = -0.5*(h/2)*acc(theta_lf)          # initial angular velocity
omega_lf_points = []
theta_lf_points = []                           # empty list of thetapoints

for t in tpoints:
    theta_lf_points.append(theta_lf)
    omega_sync = omega_lf + 0.5*h*acc(theta_lf)
    omega_lf_points.append(omega_sync)
    omega_lf += h*acc(theta_lf)
    theta_lf += h*omega_lf
    

    


pl.plot(tpoints, omega_lf_points, label='Omega Leap Frog')
pl.plot(tpoints, theta_lf_points, label='Theta Leap Frog')
pl.xlabel("t")
pl.ylabel("x(t)")
pl.legend()
pl.show()

