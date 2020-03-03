# dataframe可以将数据排成列表的形式
import pandas as pd
# 创建字典，字典作为item导入dataframe
a = {"Bob": pd.Series(data=[12,13,14],index=["bike","pants","watch"]),"Alice":pd.Series([40,110,500,45],index=["book","glasses","bike","pants"])}
b = pd.DataFrame(a)   # 键值是列标签，索引是行标签，同时按照字母排序；NaNd代表非数字，这里表示没有索引值
print(b)

# 没有索引标签会默认0,1，2，3，4等作为标签
e = {"Bob": pd.Series(data=[12,13,14],index=["pants","books","email"]),"Alice":pd.Series([40,110,500,45])}
f = pd.DataFrame(e)
print(f)

# 可以用columns和index来决定放入dataframe的数据
g = pd.DataFrame(e,columns=["Bob","Alice"])
h = pd.DataFrame(e,index=["pants","email"])
print(g)
print(h)
# 从DataFrame中使用属性提取数据
print(b.shape)
print(b.ndim)
print(b.size)
print(b.values)  # values查看数值
print(b.index)   # index查看索引
print(b.columns) # columns查看列标签