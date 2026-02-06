
import matplotlib.pyplot as plt
import numpy as np

def main(P, Q, R):
    
    P = np.array(P) # Gör P (lista) till en np array(lista). 
    Q = np.array(Q) 
    R = np.array(R)

    v1 = Q - P 
    v2 = R - P

    n = np.cross(v1, v2)

    if np.linalg.norm(n) == 0:
        print("Error: Samma linje") #
        exit()

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    ## Skapar triangel ##
    X = [P[0], Q[0], R[0], P[0]]
    Y = [P[1], Q[1], R[1], P[1]]
    Z = [P[2], Q[2], R[2], P[2]]
    ax.plot3D(X, Y, Z, "-o", color="#09cdda")

    ## Planet skapas ##
    s = np.linspace(0, 1, 10)
    t = np.linspace(0, 1, 10)
    S, T = np.meshgrid(s, t)
    
    X_plane = P[0] + S*v1[0] + T*v2[0]
    Y_plane = P[1] + S*v1[1] + T*v2[1]
    Z_plane = P[2] + S*v1[2] + T*v2[2]
    
    # Plottar planet inuti triangel
    mask = (S + T <= 1)
    X_plane = np.where(mask, X_plane, np.nan)
    Y_plane = np.where(mask, Y_plane, np.nan)
    Z_plane = np.where(mask, Z_plane, np.nan)
    
    ## Planet ritas ut ##
    ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.5, color="green")


    n_hat = n / np.linalg.norm(n)
    middle = ((P + Q + R) / 3)
    ax.quiver(middle[0], middle[1], middle[2], n_hat[0], n_hat[1], n_hat[2], color="#09babe")
    # Dot in middle #
    ax.scatter(middle[0], middle[1], middle[2], color="#09babe")

    # Se vad är xyz på axlar
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    
    plt.show()

main([1,2,3],[4,5,6],[1,2,1])