import numpy as np 
a = np.random.randint(2,36,(4,3))
print(a)

# 数组切片
b = a[2:4,1:3] # 这里的：左右代表上下限，其中冒号左可以取到，冒号右取不到;左右的数字都可以省略
print(b)
b[1,1] = 100
print(b)
print(a)      # 对b改动时候，a也改动了，因为b与a此时是不同视角的关系，还是一个数组，所以需要建立切片副本防止改动
b1 = a[2:4,1:3].copy()
b1[1,1] = 800
print(b1)
print(a)

# 使用索引数组选择数组
m = np.array([1,3])
n = a[m,:].copy()
print(n)

# numpy特殊的内置函数，diag提取对角线元素，提取对角线上下的元素；unique提取独一无二的元素
x = np.diag(a) # diag提取了对角线上的数值，此时默认k=0
print(x)
y = np.diag(a,k=1) # k=1意思为提取对角线上一行的值
print(y)
y = np.diag(a,k=-1) # k=1意思为提取对角线上一行的值
print(y)

h = np.array([1,2,1,2,5,6]) # unique可以去除重复的元素，只显示那些出现一次的元素
h = h.reshape(3,2)
print(h)
g = np.unique(h)
print(g)
