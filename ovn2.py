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
        # (a,b,c) och (d,e,f) == a/d = b/e = c/f sa ar den paralell 
        iterationObject = [p,q,r]
        v1 = np.dot(p, q)
        v2 = np.dot(p, r)

        vp = np.dot(p[0:2],p[-1])
        print(vp)
        print(np.cross(p, q), "q")
        print(np.cross(p, r), "r")  # -> 
                                    #x = [1, 2, 3]
                                    #y = [4, 5, 6]
                                    #np.cross(x, y)
                                    #array([-3,  6, -3]) 
        
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

def plotTriangle():
    # TODO se PLottar upp triangeln 
    pass

def generatePlane():
    # TODO Ger en punkt och two vektorer som genererar planet 
    pass

def normVector():
    # TODO ger den normaliserade normalvektorn enligt formeln i uppgiften   
    pass



threePoints([0,0,0],[2,1,3],[91,2,2]) 