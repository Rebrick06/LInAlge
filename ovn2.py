'''''
Skriv ett program som tar tre punkter P, Q, R i rummet och:
• Ger ett felmeddelande om alla punkter ligger p˚a samma linje (d.v.s.
inte sp¨anner upp ett plan).
• Plottar upp triangeln med h¨orn i punkterna,
• Ger en punkt och tv˚a vektorer som genererar planet,
• Ger den normaliserade normalvektorn till planet och plottar den i
mittenpunkten av triangeln (givet som 1
3 (P + Q + R)). 
'''''

def threePoints (p, q, r):
    # TODO se ifall alla punkter inte är på samma linje 
    # TODO se PLottar upp triangeln 
    # TODO Ger en punkt och two vektorer som genererar planet 
    # TODO ger den normaliserade normalvektorn enligt formeln i uppgiften  
    try:
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

                print(diff)
            print(i, iterationObject[n])
            n += 1
            
    except ValueError: 
        print("Error: a/d = b/e = c/f -> inget plan")
        # i / iterationObject[n]   # p / q 
    
    #pass  #p[j] == q[j] or q[j] == r[j] or p[j] == r[j
def plotTriangle():
    pass

def generatePlane():
    pass

def normVector():
    pass



threePoints([1,1,2],[1,2,3],[-1,2,-1]) 