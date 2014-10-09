# Derivatives: Forward Difference, Central Difference, and Euler's Method
# author: jiinso
# date: 10/7/2014

import numpy as np
import pylab as pl


# EXERCISE 1

def f(x):
    return x**3 - np.sin(x)

x = 2.0
h= 10e-6
exact = 3*x**2 - np.cos(x)

#forward difference
deriv_f = f(x+h) - f(x)
deriv_f /= h
print 'The forward difference derivative is %2.15f, the error is %2.15f, and the relative error is %2.15f.' %(deriv_f, deriv_f - exact, (deriv_f - exact)/exact )


#central difference
deriv_c = f(x+(h/2)) - f(x-(h/2))
deriv_c /= h
print 'The central difference derivative is %2.15f, the error is %2.15f, and the relative error is %2.15f.' %(deriv_c, deriv_c - exact, (deriv_c - exact)/exact )







# EXERCISE 2
def f_2(t):
    return 3*t**2 - 2*t +1

t = 1.5

deriv2_c = ( f_2(t+h) - 2.0*f_2(t) + f_2(t -h)) / h**2
print 'The force exerted on a book of mass 0.8kg is %2.10f N.' %(deriv2_c*0.8)







#EXERCISE 3
def f3(x,t):
    return -x**3 +x*np.sin(t) +1

a = 1.0
b = 10.0
N = 1000
h = (b-a)/N        #step sizes
t = 0.0
x = 0.0

tpoints = np.arange(a, b, h)
xpoints = []

for t in tpoints:
    xpoints.append(x)        # add an x point to the list xpoints
    x += h*f3(x,t)              # find the next x point

pl.plot(tpoints, xpoints)
pl.xlabel("t")
pl.ylabel("x(t)")
pl.show()

