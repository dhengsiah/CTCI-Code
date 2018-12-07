import math
import numpy as np

def rotateMatrix(m):

    N = int(m.shape[0])
    rotate = np.zeros((N,N))
        
    for x in range(int(math.ceil(N/2.))):
        for y in range(x,N-x,1):
            rotate[y][N-1-x] = m[x][y]
            rotate[N-1-x][N-1-y] = m[y][N-1-x]
            rotate[N-1-y][x] = m[N-1-x][N-1-y]
            rotate[x][y] = m[N-1-y][x]
            
            
    return rotate