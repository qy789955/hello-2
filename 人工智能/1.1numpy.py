import numpy as np 
'''import time
x = np.random.random(10000)
sum(x)/len(x)
start = time.time()
print(time.time() - start)
np.mean(x)
print(time.time() - start)  # 利用start=time.time()，print（time.time() - start） 来查看运算时间'''

'''# 创建一个数组
a = np.array([1,2,3,4,5])
# 查看数组和类型
print(a)
print(type(a))
# 查看数组的dtype
print(a.dtype)
# 查看数组行列
print(a.shape)'''

'''# 创建一个多维数组
b = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(b)
print(b.shape)
# 看数组总共有多少元素
print(b.size)'''

# 创建一个包含多个内容类型的数组
'''b = np.array(["hello",1,2,6.5])
print(b)
print(type(b))
print(b.dtype) # numpy会自动将所有数据类型处理为一样，所以dtype可以显示经过处理后的数据类型，与type不一样'''

'''# 使用dtype指定所有数据类型
c = np.array([1,2,6.5],dtype=np.int64)
print(c)
print(type(c))
print(c.dtype)'''

# 将numpy的内容导入一个文件中进行使用
d = np.array([1,2,6.5],dtype=np.int64)
np.save("newfile",d)
y = np.load("newfile.npy")
print(y)

