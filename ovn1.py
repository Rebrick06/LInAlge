'''
Skapa en funktion f (P ) som tar en punkt P, och först reflekterar den i
planet (genom origo) vinkelrätt mot (1, 2, 2) och sedan i planet (genom
origo) vinkelrätt mot (−1, 3, −1).
L˚at P = (1, 1, 1), och f (n)(P ) = f (f (· · · f (P ))), d.v.s. f applicerad n
g˚anger p˚a P. Plotta punkterna P, f (P ), f (f (P )), . . . , f (n)(P ) (i en 3D-
plot), d˚
''' 
import numpy as np

n1 = np.array([5,6])
n2 = np.array([-1,3,1])
P = np.array([5]) # start pungten

#  y= x-2*((x*n)/(|n**2|))*n
def reflect(x, n):
    dot_product = np.dot(x, n)
    n_norm_sq = np.dot(n, n)
    return x-2(dot_product/n_norm_sq) *n
        

def f(P):
    P_after_first = reflect(P, n1)
    P_after_second = reflect(P_after_first, n2)
    return P_after_second
   

    #n = (-1, 3, -1)
   # y= y-2*((y*n)/(n**2))*n


points = [P]
current_P = P 

for i in range(20):
    current_P = f(current_P)
    points.append(current_P)
    
    