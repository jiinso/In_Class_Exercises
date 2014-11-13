# jiin so
# IP4CS
# 2014/11/13
# In Class Exercise 15
# Monte Carlo Integration to find value of pi

# import the module random
import random

# ask the user to input a number of times to drop a particle on a square area.
N = int(raw_input("Number of times to drop a particle on the square surface: "))

# initial value of particles on area is zero
value = 0

# run through the code N times
for i in range(N):
    x = random.uniform(-1,1)					# generate a random floating point number N between -1 and 1 for x
    y = random.uniform(-1,1)					# do the same for y
    if x**2+y**2 <= 1:						# if the length of the radius of the random point (x, y) is less than or equal to 1
    	value += 1							# the particle lies on the circle so add 1 to the value
    else:									# if the random point lies outside of the circle
    	pass									# don't change anything and keep going

area = 4.0* float(value)/float(N)				# the area of the circle is the 4 time the number of particles on circle divided by the number of particles
print area									# area should equal pi
