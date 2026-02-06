'''''
Skriv ett program som tar tre punkter P, Q, R i rummet och:
• Ger ett felmeddelande om alla punkter ligger p˚a samma linje (d.v.s.
inte sp¨anner upp ett plan).
• Plottar upp triangeln med hörn i punkterna,
• Ger en punkt och tv˚a vektorer som genererar planet,
• Ger den normaliserade normalvektorn till planet och plottar den i
mittenpunkten av triangeln (givet som 1
3 (P + Q + R)). 
'''''
import matplotlib.pyplot as plt
import numpy as np

def threemiddles(p,q,r):
    AB = q[0] - p[0], q[1] - p[1], q[2] - p[2]
    AC = r[0] - p[0], r[1] - p[1], r[2] - p[2]
    
    result = np.cross(AB, AC) 
    if np.all(result == 0):
        print("error")

def plotTriangle(p, q, r):
    ## Append behövs för att det ska bli triangel, annars bara 2 linjer.
    p.append(p[0])
    q.append(q[0])
    r.append(r[0])
    
    fig=plt.figure()
    ax=fig.add_subplot(projection="3d")
    ax.plot3D(p, q, r, '-o') # Lägger ut p, q, r, p. Ritar p->q->r->p
    # '-o' är hur den byggs upp. Alltså sträck mellan punkterna och punkterna är runda. -* blir punkterna stjärnor
    # --o blir linjerna ex: O - - - - - O
    plt.show()


def generatePlane(p, q, r):
    # TODO Ger en punkt och two vektorer som genererar planet 
    ## Bygger 3d plan ##
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ## Matten bakom vektorerna och planet ##
    ap = np.array(p) 
    aq = np.array([q[0]-p[0], q[1]-p[1], q[2]-p[2]])
    len_aq = np.linalg.norm(aq) # Längd av aq för s
    ar = np.array([r[0]-p[0], r[1]-p[1], r[2]-p[2]])
    len_ar = np.linalg.norm(ar) # Längd av ar för t

    extent = 1 * max(len_aq, len_ar) 
    s = np.linspace(-extent/len_aq, extent/len_aq, 20)
    t = np.linspace(-extent/len_ar, extent/len_ar, 20)
    S, T = np.meshgrid(s, t)

    X = ap[0] + S*aq[0] + T*ar[0]
    Y = ap[1] + S*aq[1] + T*ar[1]
    Z = ap[2] + S*aq[2] + T*ar[2]

    ax.scatter(ap[0], ap[1], ap[2], color='purple') # Punkten #
    
    # Vektorer #
    ax.quiver(ap[0], ap[1], ap[2], aq[0], aq[1], aq[2], color='red', arrow_length_ratio=0.1)
    ax.quiver(ap[0], ap[1], ap[2], ar[0], ar[1], ar[2], color='blue', arrow_length_ratio=0.1)
    ax.plot_surface(X, Y, Z, alpha=0.5, color='white') # Planet #
    
    #plt.title("3D Vector Plot")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    middle = (p[0] + q[0] + r[0])*(1/3), (p[1] + q[1] + r[1])*(1/3), (p[2] + q[2] + r[2])*(1/3)
    #ax.plot3D(middle[0], middle[1], middle[2], '-o')
    ax.scatter(middle[0], middle[1], middle[2], color='brown', s = 4)
    plt.show()

"""
# Satte in i generatePlane då den passar bättre där. Behövs ens funktionerna? Tror inte det ska börja viba som faaa aaan
def normVector(p, q, r):
    # TODO ger den normaliserade normalvektorn enligt formeln i uppgiften   
    middle = (p[0] + q[0] + r[0])*(1/3), (p[1] + q[1] + r[1])*(1/3), (p[2] + q[2] + r[2]) * (1/3)
    
    fig=plt.figure()
    ax=fig.add_subplot(projection="3d")
    ax.plot3D(middle[0], middle[1], middle[2], '-o', 1)

    plt.show()
"""


#threemiddles([1,2,3],[4,5,6],[7,8,9]) 
#plotTriangle([1,2,3],[4,5,6],[1,2,0])
#main([1,2,3],[5,1,2],[0,2,-1])

#generatePlane([1,2,3],[4,5,6],[1,2,0])


### RENSKRIVNING??? ###
# Absolit inte inpererad från Novas kod 100% absolut (trust)
# Tror ho ha rätt nämligen
def main(P, Q, R):
    
    P = np.array(P) # Gör P (lista) till en np array(lista). 
    Q = np.array(Q) # Banger för att np ska funka ye ye
    R = np.array(R)

    v1 = Q - P # Exakt samma som innan bara gjord så att resten av programmet ska kunna använda sig av P Q och R
    v2 = R - P

    n = np.cross(v1, v2)

    if np.linalg.norm(n) == 0: # linalg.norm ger vektorns längd. all kollar varje komponent exakt 0. Ingen skillnad mer än linalg ska vara mer exakt enligt dokument om jag fattar rätt?
        print("Error: Samma linje dretunge") #
        exit()

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    ## Skapar triangel ##
    X = [P[0], Q[0], R[0], P[0]]
    Y = [P[1], Q[1], R[1], P[1]]
    Z = [P[2], Q[2], R[2], P[2]]
    ax.plot3D(X, Y, Z, "-o", color="#09cdda")

    ## Planet skap ##
    s = np.linspace(0, 1, 10)
    t = np.linspace(0, 1, 10)
    S, T = np.meshgrid(s, t)
    
    X_plane = P[0] + S*v1[0] + T*v2[0]
    Y_plane = P[1] + S*v1[1] + T*v2[1]
    Z_plane = P[2] + S*v1[2] + T*v2[2]
    
    # Plottar bara planet inuti triangeln hehehehhahaha fuck
    mask = (S + T <= 1)
    X_plane = np.where(mask, X_plane, np.nan)
    Y_plane = np.where(mask, Y_plane, np.nan)
    Z_plane = np.where(mask, Z_plane, np.nan)
    
    ## Skapar planet ##
    ax.plot_surface(X_plane, Y_plane, Z_plane, alpha=0.5, color="green")
    ## slut planet skapis skapis ##


    n_hat = n / np.linalg.norm(n) # hat som i "hatt": ^ ?? Tror rätt?? vad matte?
    middle = ((P + Q + R) / 3)
    # https://media1.tenor.com/m/WgeII1uDIN0AAAAd/viktor-viktor-arcane.gif ut ur mitten #
    ax.quiver(middle[0], middle[1], middle[2], n_hat[0], n_hat[1], n_hat[2], color="#09babe")
    # Dot in middle #
    ax.scatter(middle[0], middle[1], middle[2], color="#09babe")

    # Se vad är xyz på axlar
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    
    plt.show()

main([1,2,3],[4,5,6],[1,2,1])