import numpy as np

def Cholesky(A,b):
    #初始化
    size=A.shape[0]
    L=np.zeros((size,size))
    #通过矩阵乘法求L
    for i in range(size):
        for j in range(i,size):
            count=0
            z=0
            while True:
                if(count==i):
                    break
                else:
                    z=z+L[i][count]*L[j][count]
                    count+=1
            if(i==j):
                L[j][i]=(A[i][j]-z)**(1/2)
            else:
                L[j][i] = (A[i][j] - z) / L[i][i]
    L1=L.T
    x = np.zeros((size, 1))
    p = q = 0
    #通过追赶法求解x
    while p < size:
        if (q == p):
            x[p]=(x[p]+b[p])/L[p][p]
            p += 1
            q = 0
        else:
            x[p] = x[p] - L[p][q] * x[q]
            q += 1

    t = s = size - 1
    while t >= 0:
        if(s==t):
            x[t]=x[t]/L1[t][t]
            t-=1
            s=size-1
        else:
            x[t]=x[t]-L1[t][s]*x[s]
            s-=1
    return x