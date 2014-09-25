# author: jiinso
# In Class Exercise 8
# 2014/09/25
# Error of integration: trapezoidal rule/ simpson's rule

# define function
def f(x):
    return x**4 - 2*(x**2) -1


# define variables
a = 0.0
b = 2.0
N = 10000
h = (b-a)/N


# Trapezoidal Rule ---------------------------------------------------------------------------------------------------------------------
S = 0.5*(f(a)+f(b))

for counter in range (1, N):
    new_x = a + counter*h
    S += f(new_x)
S *= h

# Trapezoidal Rule Error 1(True Value - Estimated Value)
e_trap1 = (-14.0/15.0) - S


#Trapezoidal Rule Error 2
S_2 = 0.5*(f(a)+f(b))
h_2 = (b-a)/(2*N)
for counter in range (1, 2*N):
    new_x = a + counter*h_2
    S_2 += f(new_x)
S_2 *= h_2
e_trap2 = (1.0/3.0)*(S_2 - S)


print "The Trapezoidal Rule integral equals: %f." %S
print "The number of steps are %f." %N
print "The error for the trapezoidal rule with %f steps is %2.16f." %(S, e_trap1)
print "Another calculated error is %2.16f." %e_trap2



# Simpson's Rule ---------------------------------------------------------------------------------------------------------------------
S_s = f(a)+f(b)

for counter in range (1,N):
    new_x = a + counter*h
    if counter%2==0:
        S_s += 2.0*f(new_x)
    else:
        S_s += 4.0*f(new_x)
S_s *= h
S_s /= 3.0

# Simpson's Rule Error
e_simp1 = (-14.0/15.0) - S_s

# Simpson's Rule Error 2
S_s2 = f(a)+f(b)
h_2 = (b-a)/(2*N)
for counter in range (1, 2*N):
    new_x = a + counter*h_2
    if counter%2==0:
        S_s2 += 2.0*f(new_x)
    else:
        S_s2 += 4.0*f(new_x)
S_s2 *= h_2
S_s2 /= 3.0

e_simp2 = (1.0/15.0)*(S_s2 - S_s)

print "The Simpson's Rule integral equals: %f." %S_s
print "The number of steps are %f." %N
print "The error for the Simpson's Rule is %2.20f." %e_simp1
print "An alternate way of calculating error for the Simpson's Rule yields the error %2.20f." %e_simp2