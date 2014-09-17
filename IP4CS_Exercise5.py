# author: jiinso
# 2014/09/17
#IP4CS In Class Exercise 5

# Import needed functions from packages visual and numpy.
from visual import sphere, display
import numpy as np


# Start first part of exercise: a.) NaCl crystal
# scene1 functions like figure1 in MATLAB; it creates one window for the following objects
# display can change things like foreground/background color, size of window, and title of graph
scene1 = display (title = 'Exercise a.) Sodium Chloride Crystal')
# Create a cubic array of spheres ranging from the 0 to 5 in the x, y, z coordinates.
for i in range(6):
    for j in range(6):
        for k in range(6):
            # If k is even, and if i + j is also even, create a spherical object called 'Na' for sodium.
            # If k is even and i + j is not even, create a spherical object at those coordinates called 'Cl' for choride.
            # Also note that the two atoms, Na and Cl are given different colors and radius to differentiate them
            if k % 2 == 0:
                if (i + j )%2 == 0:
                    Na = sphere(pos=(i-3, j-3, k-3), radius=0.1, color = (0,1,1) )
                else:
                    Cl = sphere(pos=(i-3, j-3, k-3), radius=0.16, color = (1,1,0), opacity = 0.8)
            # If k is odd
            else:
                # and if i + j is even, create a spherical object at those coordinates called 'Cl' for choride.
                if (i+j)%2 ==0:
                    Cl = sphere(pos=(i-3, j-3, k-3), radius=0.16, color = (1,1,0), opacity = 0.8)
                # if i + j is odd, create a spherical object called 'Na' for sodium.
                else:
                    Na = sphere(pos=(i-3, j-3, k-3), radius=0.1, color = (0,1,1))
# Note that the position is not (i, j, k) but (i-3, j-3, k-3) so that the crystal will be more centered for the user to see.





# Start first part of exercise: b.) fcc lattice
# scene2 will create a second display. You may have to move the second window to see the first one beneath it.
scene2 = display (title = 'Exercise b.) Face Centered Cubic Lattice')

# create an cubic array of spheres 3 * 3 * 3:
# but only so that the corners and center of the faces have a sphere.
for i in range(3):
    for j in range(3):
        for k in range(3):
            if k % 2 == 0:
                if (i + j )%2 == 0:
                    sphere(pos=(i,j,k), radius=0.1, color = (0,1,1))
            if k % 2 == 1:
                if (i + j)%2 == 1:
                    sphere(pos=(i,j,k), radius=0.1, color = (0,1,1))
