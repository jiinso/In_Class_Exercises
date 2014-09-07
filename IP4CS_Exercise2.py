#This is a script for calculating the time for a falling ball from the top of a tower.

# assume initial velocity is zero.
# a = acceleration is in m/s^2
# h = height is in meters
# t = time is in seconds

a = 9.8
h = input("Please enter the height of the tower in meters: ")
h = float(h)

#import function 'sqrt' from package 'math'
from math import sqrt

#this is the time function
def t(h):
    t = sqrt((2*h)/a)
    return t


print ("It takes a  ball %f seconds to fall to the ground from a tower that is %f meters tall." %(t(h), h) )
