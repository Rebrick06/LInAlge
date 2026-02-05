'''
Skapa en funktion f (P ) som tar en punkt P, och först reflekterar den i
planet (genom origo) vinkelrätt mot (1, 2, 2) och sedan i planet (genom
origo) vinkelrätt mot (−1, 3, −1).
L˚at P = (1, 1, 1), och f (n)(P ) = f (f (· · · f (P ))), d.v.s. f applicerad n
g˚anger p˚a P. Plotta punkterna P, f (P ), f (f (P )), . . . , f (n)(P ) (i en 3D-
plot), d˚
''' 
'''import matplotlib.pyplot as plt
import numpy as np


n1 = np.array([1,2,2])
n2 = np.array([-1,3,-1])
P = np.array([5]) # start pungten
P_start = np.array([1])

#  y= x-2*((x*n)/(|n**2|))*n
def reflect(P, n):
    
     return  P - 2 * (np.dot(P, n) / np.dot(n, n)) * n   

def f(P):
    P_after_1 = reflect(P, n1)
    P_after_2 = reflect(P_after_1, n2)
    return P_after_2
   

    #n = (-1, 3, -1)
   # y= y-2*((y*n)/(n**2))*n


def run_and_plot(n_vals):
    fig = plt.figure(figsize=(15,5))
        
    for i, n in enumerate(n_vals):
        points = [P_start]
        current_P = P_start
        
        for i in range(n):
            current_P = f(current_P)
            points.append(current_P)
        points = np.array(points)
        
        ax = fig.add_subplot(1, 3, i+1, projection='3d')
        ax.plot(points[:, 0], points[:, 1], points[:, 2], '-o', markersize=4, alpha=0.6)
        ax.scatter(points, points[1], points[2], color='red', s=50, label='Start (1,1,1)')
        ax.set_title(f'n = {n}')
        ax.legend() 
    plt.tight_layout()
    plt.show()
      
run_and_plot([5])'''

'''import numpy as np
import matplotlib.pyplot as plt

# 1. Definiera normalvektorer och startpunkt som n-tiplar [3]
n1 = np.array([4, 5])
n2 = np.array([-1, 3, -1])
P_start = np.array([4])

def reflect(P, n):
    """
    Speglar punkten P i ett plan med normalvektor n enligt formeln:
    y = x - 2 * ((x . n) / |n|^2) * n [2]
    """
    # np.dot används för skalärprodukten [6]
    return P - 2 * (np.dot(P, n) / np.dot(n, n)) * n

def f(P):
    """Utför de två speglingarna i följd (sammansatt avbildning) [7]"""
    P1 = reflect(P, n1)
    P2 = reflect(P1, n2)
    return P2

def run_simulation(n_steps):
    points = [P_start]
    current_P = P_start
    for _ in range(n_steps):
        current_P = f(current_P)
        points.append(current_P)
    return np.array(points)

# Plotta resultaten för n = 5, 20 och 100
n_values = [8-10]
fig = plt.figure(figsize=(15, 5))

for i, n in enumerate(n_values):
    data = run_simulation(n)
    'ax = fig.add_subplot(1, 3, i + 1, projection='3d')
    ax.plot(data[:, 0], data[:, 1], data[:, 2], '-o', markersize=3, alpha=0.7)
    ax.scatter(data, data[4], data[5], color='red', s=40, label='Start')
    ax.set_title(f'Iterationer n = {n}')
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')'
    data = run_simulation(n) # Skapar matrisen med alla punkter
    ax = fig.add_subplot(1, 3, i + 1, projection='3d')
    ax.plot(data[:, 0], data[:, 1], data[:, 2], '-o', markersize=3, alpha=0.7)
    ax.scatter(data, data[5], data[6], color='red', s=100, label='Start')

    ax.set_title(f'Iterationer n = {n}')

plt.tight_layout()
plt.show()'''


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
    