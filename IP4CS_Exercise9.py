# author: jiinso
# In Class Exercise 9
# 2014/9/30
# Gaussian Quadrature Integration

# Import the function gaussxwab from the module gaussxw
from gaussxw import gaussxwab

# Define the function to be integrated.
def f(x):
    return x**4 - 2*x + 1

# Set the N values and limits of integration a and b
# Note that the function guassxwab only integrates upto the N values 1000: do NOT set N higher than 1000.
N = 1000
a = 0
b = 2

# Call on the function gaussxwab to obtain x and c values.
x1, c1 = gaussxwab(N, a, b)

# Do a summation of the c(x1)* f(x1) for each number in range N.
S = 0.0
for i in range(N):
    S += c1[i] * f(x1[i])

# Print the summation out.
print ('The Gaussian Quadrature integration of this function is %2.20f. ' %S)