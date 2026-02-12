import matplotlib.pyplot as plt
import numpy as np


def abc(A, v0, n):

    vk0 = np.matmul(A, v0)
    plt.plot(vk0)
    
    k = 1
    while k < (n):
        vk0 = np.matmul(A, vk0)

        vk1 = vk0
        print(vk0)
        k += 1

        plt.plot(vk1)
    plt.show()

A = np.array([[2,7],[3,9]])
v0 = np.array([5, 9])
abc(A, v0, 6)
