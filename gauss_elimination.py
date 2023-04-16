import numpy as np

def gauss_elimination(A, b):
    A=A.astype(float)
    b=b.astype(float)
    # 将增广矩阵[A|b]中的系数矩阵A和常数向量b进行列主元消去
    n = len(A)
    for i in range(n):
        # 选取第i列中绝对值最大的元素所在的行j
        j = i + np.argmax(np.abs(A[i:, i]))
        # 交换第i行和第j行
        A[[i, j], :] = A[[j, i], :]
        b[[i, j]] = b[[j, i]]
        # 将第i列下面的元素都消为0
        for k in range(i+1, n):
            factor = A[k, i] / A[i, i]
            A[k, i:] -= factor * A[i, i:]
            b[k] -= factor * b[i]
    # 回带求解x向量
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x