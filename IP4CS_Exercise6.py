import pylab as pl
import numpy as np
import math as m
from scipy import optimize

data = np.loadtxt('fitting.txt', float)
x = data[:,0]
y = data[:,1]

def fitfunc(x,a,b,c):
    return c* np.exp(a*x)+b

guess = [-10, 1, 1]

params, params_covariance = optimize.curve_fit(fitfunc, x, y, guess)
print params
print params_covariance


pl.scatter(x,y,label = 'Data Points')
pl.plot(x, fitfunc(x, params[0], params[1], params[2]), label = 'fitting')
pl.legend(loc = 'upper left')
pl.show()

