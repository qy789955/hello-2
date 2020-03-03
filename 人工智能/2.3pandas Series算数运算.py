import pandas as pd
import numpy as np
a = pd.Series(data=[1,2,3],index=["a","b","c"])
m = pd.Series(data=[1,"yes",3],index=["a","b","c"])


# pandas数组整体的加减乘除
print(a)
print(a*2)
print(a/2)
print(a+2)
# 引用numpy进行开方，幂运算(使用numpy自带的运算库)
b = np.sqrt(a) # sqrt和power是在numpy中的方法
c = np.power(a,2) # power是平方
print(c)

# pandas数组单个元素的运算
a["c"]+= 2
a.iloc[2] += 2 # iloc和loc是在pandas库中的方法
a.loc[["c","b"]] += 2
m = m*2 # 字符串相乘就是字符串出现两倍
print(a)
print(m)

