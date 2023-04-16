import numpy as np
def Crout(A,b):
    size1=A.shape[0]
    size2=A.shape[1]
    L=np.zeros((size1,size2))
    U=np.eye(size1,size2)
    for i in range(size1):
        for j in range(i,size1):
            z1=A[j][i]
            count1=0
            while True:
                if(count1==i):
                    break
                else:
                    z1=z1-L[j][count1]*U[count1][i]
                    count1+=1
            L[j][i]=z1

        for n in range(i,size2):
            z2 = A[i][n]
            count2 = 0
            while True:
                if (count2 == i):
                    break
                else:
                    z2 = z2 - L[i][count2] * U[count2][n]
                    count2+=1
            U[i][n]=z2/L[i][i]

    x = np.zeros((size2, 1))
    p = q = 0
    while p < size2:
        if (q == p):
            x[p]=(x[p]+b[p])/L[p][p]
            p += 1
            q = 0
        else:
            x[p] = x[p] - L[p][q] * x[q]
            q += 1


    t = s = size2 - 1
    while t >= 0:
        if(s==t):
            x[t]=x[t]
            t-=1
            s=size2-1
        else:
            x[t]=x[t]-U[t][s]*x[s]
            s-=1
    return x