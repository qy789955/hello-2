import pandas as pd 
a = pd.Series(data=["egg",30,8,3.2], index=["weight","height","word","abc"])
# 1 访问pandas的元素
# 1.1 关键字索引访问
print(a[["weight","height"]]) # 如果是一个索引访问，使用【】，多个索引访问，要使用双重【】
# 1.2 数字索引访问
print(a[[1,2,3]]) # 双或者多个数字索引访问也是双重【】
print(a[-1])
# 1.3 索引的指明,区分是数字访问还是关键字访问
print(a.loc[["weight","height"]])  # loc指明是关键字索引
print(a.iloc[[1,2,3]])

# 2 修改数据
a[[1,2,3]]=-1
print(a)

# 3 删除数据, drop是一个方法,对应用括号，drop只能用索引删除，同时drop删除元素不改动原来的数组
b = a.drop("weight")
print(a)
print(b)  