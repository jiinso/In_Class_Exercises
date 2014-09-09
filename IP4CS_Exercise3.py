#In class practice for code!
#2014/09/09

#Exercise 1
from numpy import array, dot, sqrt
#import functions from numpy needed for vector calculations

d1 = [3,-4,2]
d2 = [2,1,-1.5]
#define two vectors

d1 = array(d1)
d2 = array(d2)
#make the two vectors (which are currently lists) into arrays.


sum_d1=0
sum_d2=0

for item  in d1:
    sum_d1 += (item)**2
mag_d1 = sqrt(sum_d1)

for item in d2:
    sum_d2 += (item)**2
mag_d2 = sqrt(sum_d2)

#use for loops to calculate the magnitude of the vectors.


'''
# This is an alternate way to calculate the magnitudes of the vectors; it does not use for loops.
mag_d1 = sqrt(d1[0]**2 + d1[1]**2 + d1[2]**2 )
mag_d2 = sqrt(d2[0]**2 + d2[1]**2 + d2[2]**2 )
#calculate the magnitude of the vectors by taking the sum of squares of each element and square rooting it.
'''


dot_product = dot(d1,d2)
#use the dot function from numpy to find the dot product between vector d1 and vector d2

print d1
print d2
print mag_d1
print mag_d2
print dot_product
#print the vectors, magnitudes of vectors and the dot product of the two vectors.
