import numpy as np
import numpy.linalg as LA
B = np.array([[9, 5], 
              [1, 5]])

# Task 1 variables
"""
n = B.shape[0]
b = np.random.rand(n)
"""
# Task 2 varaibles
A = np.random.rand(500, 500)
B_2 = A + A.T
n = B_2.shape[0]
b = np.random.rand(n)





def normalise(b):
    return b / LA.norm(b)

def Rayleight(B, b):
    b = normalise(b)
    return b.T @ B @ b

def powerIteration(B, p):
    b_old = normalise(B @ b)
    rayl_old = Rayleight(B, b_old)

    while True:
        b_new = normalise(B @ b_old)
        rayl_new = Rayleight(B, b_new)

        res = LA.norm(rayl_new - rayl_old)
        if (res < 10**(-p)):
            print("Yeah")
            return rayl_new, b_new
        else:
            b_old = b_new
            rayl_old = rayl_new





#print(LA.eig(B))

#print(powerIteration(B, 10))

lamTask2, BTask2 = powerIteration(B_2, 10)
        
check = LA.norm((B_2 @ BTask2) - lamTask2 * BTask2  )  
print(check)       