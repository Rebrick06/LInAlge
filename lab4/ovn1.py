import numpy as np
from scipy import linalg as LA
from sympy import Matrix

A = Matrix([[1,2,1,-1,2],[3,4,5,2,0],[2,2,1,0,2]])

y = Matrix([1, 2, 3]) # Ger y ett värde för test 

T = A.row_join(y)
T_rref, pivots = T.rref()


print(T_rref)
print("Pivotkolonner:", pivots)