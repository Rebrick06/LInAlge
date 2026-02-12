'''
Skriv ett program som tar tre punkter P, Q, R i rummet och:
• Ger ett felmeddelande om alla punkter ligger p˚a samma linje (d.v.s.
inte sp¨anner upp ett plan).
• Plottar upp triangeln med hörn i punkterna,
• Ger en punkt och tv˚a vektorer som genererar planet,
• Ger den normaliserade normalvektorn till planet och plottar den i
mittenpunkten av triangeln (givet som 1
3 (P + Q + R)). 
'''

import matplotlib.pyplot as plt
import numpy as np


def threePoints (p, q, r):
    # TODO se ifall alla punkter inte är på samma linje 
    try:

        vectorPQ = np.cross(p,q) # [1,2,3] och [4,5,6] --> [-3,6,-3] 
        vectorPR = np.cross(p,r) # [4,5,6] och [1,2,0] --> [-12,6,3]
        vectorQR = np.cross(q,r) # [4,5,6] och [1,2,0] --> [-12,6,3]
        zeroVector = np.cross([0,0,0],[1,1,1])
        print(zeroVector)
        print(f'This is the crossVector {vectorPQ,vectorPR, vectorQR}')

        if vectorPQ == zeroVector or vectorPR == zeroVector or vectorQR == zeroVector:
            raise ValueError
        else: 
            print(f'This is the crossVector {vectorPQ,vectorPR, vectorQR}')
            return vectorPQ, vectorPR, vectorQR
            
    
    except ValueError: 
        print("Error: a/d = b/e = c/f -> inget plan") 
    
def plotTriangle():
    # TODO se PLottar upp triangeln 

    pass

def generatePlane():
    # TODO Ger en punkt och two vektorer som genererar planet 
    pass

def normVector():
    # TODO ger den normaliserade normalvektorn enligt formeln i uppgiften   
    pass



threePoints([1,2,3],[4,5,6],[1,2,0]) 