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
    # TODO se ifall alla punkter inte 'r pa samma linje 
    # TODO se PLottar upp triangeln 
    # TODO Ger en punkt och two vektorer som genererar planet 
    # TODO ger den normaliserade normalvektorn enligt formeln i uppgiften  
    
    # (a,b,c) och (d,e,f) == a/d = b/e = c/f sa ar den paralell 
    iterationObject = [p,q,r]

    n = 1 
    for i in iterationObject: 
         
        i / iterationObject[n]   # p / q 

    pass  

threePoints([1,1,2],[1,2,3],(-1,2,-1)) 