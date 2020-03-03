import numpy as np 
# 两个数组元素的加减乘除.注意这里的加减乘除只是针对元素的运算，并不是矩阵的加减乘除
x = np.array([1,4,16,36]).reshape([2,2])
y = np.array([2,4,9,16]).reshape([2,2])
'''print(x)
print(y)
print(x+y)
print(np.add(x,y))
print(x-y)
print(np.subtract(x,y))
print(x*y)
print(np.multiply(x,y))
print(x/y)
print(np.divide(x,y))

# 一个一维数组元素的开方，幂。只是针对元素的运算，不是矩阵的加减乘除
print(np.sqrt(x))
print(np.power(x,2))'''

# 一个二维数组求平均值,标准差，最大值，最小值，数组元素的加减乘除。
print(x.mean(axis=0)) # mean，std，max，min是方法，数组可以调用，而add，subtract，multiply，divide，sqrt，power是函数，numpy库来调用
print(x.std())
print(x.max())
print(x.min())

# 广播，两个不对应的数组的加减处理,numpy会直接将小数组广播成可以运算的大数组
m = np.array([1,2,3])
n = np.arange(1,7).reshape([2,3])
print(m)
print(n)
print(m+n)