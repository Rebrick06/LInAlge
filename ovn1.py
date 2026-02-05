'''
Skapa en funktion f (P ) som tar en punkt P, och först reflekterar den i
planet (genom origo) vinkelrätt mot (1, 2, 2) och sedan i planet (genom
origo) vinkelrätt mot (−1, 3, −1).
L˚at P = (1, 1, 1), och f (n)(P ) = f (f (· · · f (P ))), d.v.s. f applicerad n
g˚anger p˚a P. Plotta punkterna P, f (P ), f (f (P )), . . . , f (n)(P ) (i en 3D-
plot), d˚
''' 

import matplotlib.pyplot as plt
import numpy as np

n1 = 5
n2=20
n3=100
x1 = np.array([1,2,2])
x2 = np.array([-1,3,-1])
P = np.array([1,1,1])
E= None

def reflect(P, n):
    # y = x - 2 * ((x * n) / |n|^2) * n [2]
    return P - 2*(np.dot(P, n) / np.dot(n, n))*n

    
def f(P):
    P = reflect(P, x1)
    return reflect(P, x2)

def loop(n, P):
    for i in range(n):
        P = f(P)
    return P
    
fig=plt.figure()
ax=fig.add_subplot(projection="3d")
P1= loop(n1, P)    
ax.plot3D(P1[0],P1[1],P1[2], '-o')
P2= loop(n2, P)    
ax.plot3D(P2[0],P2[1],P2[2], '-o')
P3= loop(n3, P)    
ax.plot3D(P3[0],P3[1],P3[2], '-o')
plt.show()
    