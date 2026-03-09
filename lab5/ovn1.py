import numpy as np
import numpy.linalg as LA

def normalise(b):
    return b / LA.norm(b)

def Rayleight(B, b):
    b = normalise(b)
    return b.T @ B @ b

def powerIteration(B, p):
    b_old = normalise(B @ b)
    rayl_old = Rayleight(B, b_new)
    
    while True:
        b_new = normalise(B @ b_old)
        rayl_new = Rayleight(B, b_new)

        if (LA.norm(rayl_new - rayl_old) < 10**(-p)):
            break
        else:
            b_old = b_new
            rayl_old = rayl_new

        

        