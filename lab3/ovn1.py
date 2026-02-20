import matplotlib.pyplot as plt
import numpy as np

def berakna_regressions_polynom(punkter):
    a = punkter[:, 0]
    b = punkter[:, 1]
    
    A = np.column_stack([a**3, a**2, a, np.ones(len(a))])

    Y = b.reshape(-1, 1)
    
    # Beräkna X med minsta kvadratmetoden: X = (A^T * A)^-1 * A^T * Y
    AT = A.T
    ATA_inv = np.linalg.inv(np.matmul(AT, A))

    ATY = np.matmul(AT, Y)
    X = np.matmul(ATA_inv, ATY)
    
    return X.flatten() # Returnerar [p3, p2, p1, p0]

punkter = 1 + 2 * np.array([[0.2, 0.1], [0.5, 0.1], [0.4, 0.7], [0.9, 0.9]])
p3, p2, p1, p0 = berakna_regressions_polynom(punkter)
plt.scatter(punkter[:, 0], punkter[:, 1], color='red', label='Datapunkter') # Punkterna

## UPPGIFT 2 ## 
"""
# Skapar en 8x2 matris med slumpvärden i intervallet [3, 4]
slump_punkter = 1 + 2 * np.random.rand(8, 2)
# 1. Beräkna koefficienterna för slump_punkter
p3, p2, p1, p0 = berakna_regressions_polynom(slump_punkter)

plt.scatter(slump_punkter[:, 0], slump_punkter[:, 1], color='red', label='Datapunkter') # Punkterna
"""
## SLUT UPPGIFT 2 ##

# Skapar x-värden kurva
x_kurva = np.linspace(1, 3, 100)

# Beräknar polynomets y-värden: P(x) = p3*x^3 + p2*x^2 + p1*x + p0
y_kurva = p3*x_kurva**3 + p2*x_kurva**2 + p1*x_kurva + p0

plt.plot(x_kurva, y_kurva, label='Grad 3 polynom') # Kurvan
plt.legend()
plt.show()