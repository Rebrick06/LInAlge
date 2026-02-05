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


def threePoints (p, q, r):
    # TODO se ifall alla punkter inte är på samma linje 
    try:       
        """ax = plt.figure().add_subplot(projection='3d')
        plt.scatter(p,q,r)
        ax.quiver(0,0,0,p[0],p[1],p[2],color="r",arrow_length_ratio=0.1)
        ax.quiver(0,0,0,q[0],q[1],q[2],color="r",arrow_length_ratio=0.1)
        ax.quiver(0,0,0,r[0],r[1],r[2],color="r",arrow_length_ratio=0.1)
        
        ax.set_xlim([0,5])
        ax.set_ylim([0,5])
        ax.set_zlim([0,5])
        
        plt.show()"""
        
        # (a,b,c) och (d,e,f) == a/d = b/e = c/f sa ar den paralell 
        iterationObject = [p,q,r]
        n = 1
        diff = None
        for i in iterationObject: # [ [1,1,2], [1,2,3], [-1,2,-1] ]
            # i = [1,1,2]
            for j in range(len(i)): 
                if n == len(iterationObject):
                    n = 0
                    if diff == iterationObject[n][j] / i[j]:
                        diff = iterationObject[n][j] / i[j]
                    else:
                        raise ValueError   
                else: 
                    diff = i[j] / iterationObject[n][j]

                #print(diff)
            #print(i, iterationObject[n])
            n += 1
        
    except ValueError: 
        print("Error: a/d = b/e = c/f -> inget plan")
        # i / iterationObject[n]   # p / q 
    
    #pass  #p[j] == q[j] or q[j] == r[j] or p[j] == r[j

def plotTriangle(p,q,r):
    ## Append behövs för att det ska bli triangel, annars bara 2 linjer.
    p.append(p[0])
    q.append(q[0])
    r.append(r[0])
    
    fig=plt.figure()
    ax=fig.add_subplot(projection="3d")
    ax.plot3D(p,q,r, '-o')

    plt.show()



def generatePlane(p,q,r):
    # TODO Ger en punkt och two vektorer som genererar planet 
    ## Bygger 3d plan ##
    fig=plt.figure()
    ax = fig.add_subplot(111, projection='3d')

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

    X = p[0] + S*aq[0] + T*ar[0]
    Y = p[1] + S*aq[1] + T*ar[1]
    Z = p[2] + S*aq[2] + T*ar[2]

    ax.scatter(p[0], p[1], p[2], color='purple') # Punkten #
    
    # Vektorer #
    ax.quiver(ap[0], ap[1], ap[2], aq[0], aq[1], aq[2], color='red', arrow_length_ratio=0.1)
    ax.quiver(ap[0], ap[1], ap[2], ar[0], ar[1], ar[2], color='blue', arrow_length_ratio=0.1)
    ax.plot_surface(X, Y, Z, alpha=0.5, color='white') # Planet #
    
    #plt.title("3D Vector Plot")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    point = (p[0] + q[0] + r[0])*(1/3), (p[1] + q[1] + r[1])*(1/3), (p[2] + q[2] + r[2])*(1/3)
    ax.plot3D(point[0], point[1], point[2], '-o')
    plt.show()


def normVector(p, q, r):
    # TODO ger den normaliserade normalvektorn enligt formeln i uppgiften   
    point = (p[0] + q[0] + r[0])*(1/3), (p[1] + q[1] + r[1])*(1/3), (p[2] + q[2] + r[2]) * (1/3)
    
    fig=plt.figure()
    ax=fig.add_subplot(projection="3d")
    ax.plot3D(point[0], point[1], point[2], '-o')

    plt.show()



#threePoints([1,2,3],[4,5,6],[1,2,0]) 
#plotTriangle([1,2,3],[4,5,6],[1,2,0])
generatePlane([1,2,3],[4,5,6],[1,2,0])
#normVector([1,2,3],[4,5,6],[1,2,0])