import numpy as np



        
def threePoints(p,q,r):
    AB = q[0] - p[0], q[1] - p[1], q[2] - p[2]
    AC = r[0] - p[0], r[1] - p[1], r[2] - p[2]
    print(AB, AC)
    result = np.cross(AB, AC, axisa=-1, axisb=-1, axisc=-1, axis=None) 
    print(result)
    if np.all(result == 0):
        print("error")







threePoints([1,2,3],[4,5,6],[7,8,9]) 
#plotTriangle([1,2,3],[4,5,6],[1,2,0])
#generatePlane([1,2,3],[4,5,6],[1,2,0])