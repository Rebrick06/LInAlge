import matplotlib.pyplot as plt
import numpy as np

n1 = 5
n2=20
n3=100
x1 = np.array([1,2,2])
x2 = np.array([-1,3,-1])
P = np.array([1,1,1])
E = None

## reflecterar pungten genom plant genom origo ##
def reflect(P, n):
    # y = x - 2 * ((x * n) / |n|^2) * n [2]
    return P - 2*(np.dot(P, n) / np.dot(n, n))*n

    
## utför funktionenn##
def f(P):
    P = reflect(P, x1)
    return reflect(P, x2)

##loopa n gånger##
def loop(n, P):
    for i in range(n):
        P = f(P)
        ax.plot3D(P[0], P[1], P[2], '-o')
    return P
    
fig=plt.figure()
ax=fig.add_subplot(projection="3d")
loop(n1, P)    
loop(n2, P)    
loop(n3, P)    
plt.show()
    