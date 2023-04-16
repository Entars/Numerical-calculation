import numpy as np

def Doolittle(A,b):
    size1=A.shape[0]
    size2=A.shape[1]
    #初始化L和U矩阵
    U=np.zeros((size1,size2))
    L=np.eye(size1,size2)
    for i in range(size1):
        #通过遍历给U矩阵赋值
        for k in range(i,size1):
            z1=0
            count=0
            while True:
                if(count==i):
                    break
                else:
                    z1=z1+L[i][count]*U[count][k]
                    count+=1
            U[i][k]=A[i][k]-z1
            # 通过遍历给L矩阵赋值
        for j in range(i+1,size1):
            z2=0
            count1=0
            while True:
                if(count1==i):
                    break
                else:
                    z2=z2+L[j][count1]*U[count1][i]
                    count1+=1
            L[j][i]=(A[j][i]-z2)/U[i][i]
    x=np.zeros((size2,1))

#先计算LY=b中的Y，Y=UX
    p=q=0
    while p<size2:
        if(q==p):
            x[p]+=b[p]
            p+=1
            q=0
        else:
            x[p]=x[p]-L[p][q]*x[q]
            q+=1
#再计算Y=UX中的X
    t = s = size2 - 1
    while t >= 0:
        if(s==t):
            x[t]=x[t]/U[t][t]
            t-=1
            s=size2-1
        else:
            x[t]=x[t]-U[t][s]*x[s]
            s-=1
    return x