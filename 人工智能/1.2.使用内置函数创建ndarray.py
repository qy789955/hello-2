# 1 创建全为某个数字的数组
import numpy as np
# 1.1 zeros内置函数创建全为0的数组，dtype为float64
a = np.zeros((3,5))
print(a)
# 1.2 ones内置函数创建全为1的数组，dtype为浮点型
b = np.ones((3,5)) 
print(b)
print(b.dtype)
# 1.3 full内置函数创建全为5的数组
c = np.full((3,5),5)
print(c)

# 2 用eye内置函数创建单位矩阵
e = np.eye(3)
print(e)

# 3 创建对角矩阵
f = np.diag([10,20,30])
print(f)

# 4 创建等差矩阵
# 4.1 创建等差矩阵(步长为整数)。使用arange创建时候，参数至少一个（此时默认为上限参数），默认步长为1，上限数字不在显示范围，
g = np.arange(1,20,3)
m = np.arange(20)   
n = np.arange(1,20)
print(g,m,n)
# 4.2 创建等差矩阵（步长为浮点数）。使用linspace创建时候,参数至少两个，第三个参数是代表元素个数，上限参数会显示，默认步长是50
h = np.linspace(1,20,5)
print(h)
# 可以使用endpoint函数来让上限数字不显示
h1 = np.linspace(1,20,5,endpoint=False)
print(h1)

# 5 创建随机数组
# 5.1 用random创建随机数组，输入参数为（行，列)，此时不能有多余的参数
x = np.random.random((3,4))
print(x)
# 5.2 用randint创建随机整数数组，输入参数必须包括：下限，上限，（行，列)
y = np.random.randint(1,8,(3,4))
print(y)
# 5.3 创建各种概率分布的给定形状随机数组,显示它的平均值，标准差，最大值，最小值，负数，正数，正数和
k = np.random.normal(0,3,(4,3))
print(k)
print(k.mean()) # 查看平均值
print(k.std())  # 查看方差
print(k.max())  # 查看最大值
print(k>0)		# 查看是否为正数
print((k>0).sum())

# 6 重置数组reshape
x = np.random.random((3,4))
w = x.reshape((2,6))
print(w)'''

# 创建数组实例，创建全为偶数的数组
import numpy as np
a = np.arange(2,34,2)
b = a.reshape((4,4))
print(b)


