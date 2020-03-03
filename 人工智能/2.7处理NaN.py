import pandas as pd
items = [{"bikes":20,"pants":30,"shirts":15,"shoes":8,"suits":45},{"watches":10,"glasses":50,"bikes":15,"pants":5,"shirts":2,"shoes":5,"suits":7},{"bikes":20,"pants":30,"watches":35,"glasses":4,"shoes":10}]
store_items=pd.DataFrame(items)
print(store_items)

# 查找NaN值 .isnull显示NaN值为布尔型，布尔型dataframe调用 .sum（）加和计算NaN值数量
x = store_items.isnull() # true代表NaN值，显示为1
print(x)
y = x.sum()  # 用一个sum()可以显示NaN值的pandas series
print(y)
z = y.sum() # 用两个sum()可以显示整个NaN值的数量
print(z)
# 查找非NaN值的数量  用dataframe调用.count（）方法
t = store_items.count()
print(t)

# 删除NaN值 dataframe调用 .dropna(axis)
a = store_items.dropna(axis=0) # 删除含有nan的行
print(a)
b = store_items.dropna(axis=1) # 删除含有nan的列
print(b)


# 替换NaN值
# .fillna()替换
c = store_items.fillna(0) # 把所有nan值替换为0
print(c)
d = store_items.fillna(method="ffill",axis=0) # 用前边的行或者列的值替换nan值
print(d)
e = store_items.fillna(method="ffill",axis=1)
print(e)
f = store_items.fillna(method="backfill",axis=1) # 用后边的行或者列的值替换nan值
print(f)
# .interpolate(method="linear",axis)
g = store_items.interpolate(method="linear",axis=1) # 线性代替，nan值前后的值的平均值
print(g)