import numpy as np
# 1 数组的访问,一维和二维，倒序访问
a = np.array([1,2,3,4,5,6])
print(a[0])
print(a[-6])  # 访问时候的负值代表倒序数
b = a.reshape((2,3))
print(b[0,0])
print(b[-2,-2])

# 2 数组的修改
print(a)
a[0]=9
print(a)
print(b)
b[0,0]=10
print(b)

# 3 数组元素的删除，这里是外置数组，需要用np库调用delete函数
b = a.reshape((2,3))
print(a)
a = np.delete(a,[0,1])
print(a)
print(b)
b = np.delete(b,[0,1],axis=1) # 多个数字代表删除多个列
b = np.delete(b,0,axis=0) # axis=0 代表删除的是行，axis=1代表删除的是列
print(b)

# 4 数组元素的增加值，np.append
print(a)
a = np.append(a,[7,8])
print(a)
print(b)  
b = np.append(b,[[7],[9]],axis=1) # 增加元素时候涉及到元素格式，首先用【】写追加内容，行追加：【【1，2，3】】，列追加【【2】，【3】，【4】】
print(b)

# 5 数组元素的插入 ,np.insert  插入元素与增加元素形式类似时候涉及到元素格式，首先用【】写追加内容，行追加：【【1，2，3】】，列追加【【2】，【3】，【4】】
a = np.insert(a,2,[9,9])
print(a)
b = np.insert(b,0,[[9],[9]],axis=1)
print(b)

# 6 数组元素的堆叠,np.vstack np.hstack
a = np.array([1,2,3])
a1 = a.reshape((3,1))
b = np.array([4,5,6])
b1 = b.reshape((3,1))
c = np.hstack((a,b))
d = np.vstack((a1,b1))
print(d)