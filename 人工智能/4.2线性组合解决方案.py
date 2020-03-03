import numpy as np
# 定义检查线性的方法
def check_vector_span(set_of_vectors,vector_to_check):
    # 创建一个正确尺寸的空向量(标向量)
    #vector_of_scalars = np.asarray([None]*set_of_vectors.shape[0]) # np.asarray([None])是将对象不要进行copy，np.array(）则将对象进行了copy
    # 如果向量在空间中就进行计算解出线性解
    try:
        # np.linalg.solve(a,b)利用linalg.solve方法求解a与b的线性解，但是如果没有解，会报错
        vector_of_scalars=np.linalg.solve(set_of_vectors,vector_to_check)
        #if not (vector_of_scalars is None):
        print("\n Vector is within span. \n Scalars is s:",vector_of_scalars)
    except Exception as exception_type:
        if str(exception_type) == "Singular matrix": # Singular matrix 奇异矩阵，就是值为0，没有解
            print("\n No single solution/vector is not within span")
        else:
            print("\n Unexpected Exception Error",exception_type)
    return vector_of_scalars
vw2 = np.array([[1,2],[3,4]])
t2 = np.array([6,12])
a2 = check_vector_span(vw2,t2)  # np.linalg.solve()可以用来计算线性参数，但是如果没有解时候会报错，为了防止报错，使用try定义不同类型解的输出内容
print(a2)

