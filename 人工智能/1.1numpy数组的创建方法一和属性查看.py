# numpy数组的创建，导入numpy库
import numpy as np
# 1.1一维单类型数组的创建和查看
a = np.array([1,2,3,4,5])
print(a)
print(type(a))
print(a.dtype)
print(a.size) # 查看数组内部多少个元素
print(a.shape) # 查看数组行列为多少

# 1.2一维多类型数组的创建和查看
b = np.array(["hello",1,2,6.5])
print(b)
print(type(b))
print(b.dtype)  # dtype实际上是指示数组内部的所有数据类型，type是指整个数组的类型
print(b.size)
print(b.shape)

# 2. 多维数组的创建和查看
c = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(c)
print(type(c))
print(c.dtype)
print(c.size)
print(c.shape)

# 3.1数组的dtype类型指定,在内部加入dtype函数就可以
b = np.array([1,2,3.2], dtype=np.int64)
print(b.dtype)

# 3.2numpy数组内容文件的调用
m = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
np.save("newfile",m)
y = np.load("newfile.npy")
print(y)


# 4.查看numpy的处理事件