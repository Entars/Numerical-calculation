import numpy as np

def Iterative_Jacobi(A,b):
    #通过矩阵A得到迭代矩阵G和尾项
    size=A.shape[0]
    D=np.zeros((size,size))
    for i in range(size):
        D[i][i]=A[i][i]
    I=np.eye(size)
    D_Inv=np.linalg.inv(D)
    G=I-np.dot(D_Inv,A)
    X=np.zeros(size).T
    deta=1
    #迭代，并防止矩阵不收敛使溢出
    while deta>=0.00000001:
        if(deta>100):
            return "矩阵不收敛"
        p=X
        X=np.dot(G,X)+np.dot(D_Inv,b)
        deta=np.linalg.norm(X-p,ord=2)
    return X