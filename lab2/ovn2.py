import matplotlib.pyplot as plt
import numpy as np

A = None  

A1 = np.array([0, 0, 0, 0.16])
A2 = np.array([0.85, -0.05, 0.05, 0.85])
A3 = np.array([0.2, -0.26, 0.23, 0.22]) 
A4 = np.array([-0.15, 0.26, 0.28, 0.24]) 

B = None 

B1 = np.array([0, 0])
B2 = np.array([0, 1.6])
B3 = np.array([0, 1.2]) 
B4 = np.array([0, 0.44]) 


## Formula v(n) = Ai * v(n-1) + bi       n >= 1

def fractal(n): 
    
    v_last = np.array([0,0]) 
    for i in range(n):     
        randomFloat = np.random.rand() 

        if randomFloat <= 0.04: # A1 B1
            A = A1 
            B = B1  
        elif randomFloat <= 0.86: # A2 B2
            A = A2
            B = B2         
        elif randomFloat <= 0.93: # A3 B3
            A = A3 
            B = B3 
        else: # A4 B4
            A = A4 
            B = B4   

        v_next = np.matmul(A, v_last) + B  
        v_last = v_next 
        plt.scatter(v_next)

fractal(25)