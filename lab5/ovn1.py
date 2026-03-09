import numpy as np
import numpy.linalg as LA

# Task 1 variables
"""
B = np.array([[9, 5], 
              [1, 5]])
n = B.shape[0]
b = np.random.rand(n)
"""

# Task 2 varaibles
A = np.random.rand(500, 500)
B_2 = A + A.T
n = B_2.shape[0]
b = np.random.rand(n)

def randomVectorb(B): 
    n = B.shape[0] 
    return np.random.rand(n)

# Function to normalise 
def normalise(b):
    return b / LA.norm(b)

# Function to calculate Rayleigh function 
def Rayleight(B, b):
    b = normalise(b)
    return b.T @ B @ b

# Function to calculate PowerIteration 
def powerIteration(B, p):
    b_old = normalise(B @ b)
    rayl_old = Rayleight(B, b_old)

    while True:
        b_new = normalise(B @ b_old)
        rayl_new = Rayleight(B, b_new)
        res = LA.norm(rayl_new - rayl_old)

        if (res < 10**(-p)):
            return rayl_new, b_new
        else:
            b_old = b_new
            rayl_old = rayl_new

# Task 1 prints
"""
print(LA.eig(B))
print(powerIteration(B, 10))
"""

# Task 2 prints 
lamTask2, BTask2 = powerIteration(B_2, 10)
task2Result = LA.norm((B_2 @ BTask2) - lamTask2 * BTask2  )  
print(task2Result)       