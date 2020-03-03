import numpy as np
# np.matmul() np.dot()都可以表示矩阵乘法,np.matmul()禁止标量和矩阵相乘
a = np.array([-1,2])
ij = np.array([[3,1],[1,2]]) # 两个向量需要双重【】，代表合为一体
c = np.matmul(ij,a)
print(c)