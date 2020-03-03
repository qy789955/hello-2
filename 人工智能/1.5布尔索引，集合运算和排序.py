import numpy as np 
a = np.arange(25).reshape([5,5])
# 1.具有逻辑运算的布尔索引
#1.1 使用布尔索引筛选
print(a[(a>10)&(a<13)])
print(a[a>10])
#1.2 使用布尔索引批量赋值
a[a>10] = -1
print(a)

# 2.集合运算，交，差，并
b = np.array([1,2,3,4,6,6])
c = np.array([8,2,1,5,9,9])
print(np.intersect1d(b,c))
print(np.setdiff1d(b,c))
print(np.union1d(b,c))

# 3，排序函数,sort当函数和当方法用，当函数用不改动原数组，当方法用会改动原数组
m = np.sort(c) # sort当做函数被np库调用，不会改变原来的数组
print(m)
print(c)
c.sort() # sort被数组当做方法调用，会改变数组
print(c)


