from visual import sphere, display
import numpy as np


#Exercise a.) NaCl crystal
scene1 = display (title = 'Sodium Chloride Crystal')
for i in range(6):
    for j in range(6):
        for k in range(6):
            if k % 2 == 0:
                if (i + j )%2 == 0:
                    atom1 = sphere(pos=(i-3, j-3, k-3), radius=0.1, color = (0,1,1) )
                else:
                    atom2 = sphere(pos=(i-3, j-3, k-3), radius=0.16, color = (1,1,0), opacity = 0.8)
            else:
                if (i+j)%2 ==0:
                    atom2 = sphere(pos=(i-3, j-3, k-3), radius=0.16, color = (1,1,0), opacity = 0.8)
                else:
                    atom1 = sphere(pos=(i-3, j-3, k-3), radius=0.1, color = (0,1,1))




#Exercise b.) fcc lattice

scene2 = display (title = 'Face Centered Cubic Lattice')
for i in range(3):
    for j in range(3):
        for k in range(3):
            if k % 2 == 0:
                if (i + j )%2 == 0:
                    sphere(pos=(i,j,k), radius=0.1, color = (0,1,1))
            if k % 2 == 1:
                if (i + j)%2 == 1:
                    sphere(pos=(i,j,k), radius=0.1, color = (0,1,1))
