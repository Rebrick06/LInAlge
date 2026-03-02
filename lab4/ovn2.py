import numpy as np
from scipy import linalg as LA
from sympy import Matrix
import time

# skapar matriserna 
A = np.random.rand(100,100)
y = np.random.rand(100)
m_A = Matrix(A)
m_y = Matrix(y)

# Del I 
T = m_A.row_join(m_y)
t = time.time()
res = T.rref() 
print("Time taken:", time.time()-t)

# kontrollera lösning 
controller = res[0][:,-1] 
solutionChecker = np.array(controller).astype(np.float64).reshape(-1,1) 

diff = np.linalg.norm(A @ solutionChecker - y)
print(diff)

if diff < 1e-10: 
    print("lösningen är korrekt") 
else: 
    print("Lösningen är inte helt korrekt")


# Del II
t = time.time()
x = LA.solve(A, y)
A_inv = LA.inv(A)
x = A_inv @ y


print("Time taken:", time.time()-t)