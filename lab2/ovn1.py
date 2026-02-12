import matplotlib.pyplot as plt
import numpy as np


def abc(A, v0, n):

    vk = A*v0
    plt.plot(vk)
    k = 1
    
    while k < (n+1):
        vk = A*vk
        k += 1
        plt.plot(vk)
    plt.show()


A = np.array([[1,2],[3,4]])
v0 = np.array([1, 2])
abc(A, v0, 3)
