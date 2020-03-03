import pandas as pd 
# 创建panda序列对象,查看对象的属性（元素数量，各个维度大小，几维）,以及它的数值和索引
a = pd.Series(data=["a",2,3,2.3],index=["word","bread","weight","height"]) # 注意这里的data和index不能替换,同时data类型可以是任意
print(a.size) # 查看元素个数
print(a.ndim) # 查看维度
print(a.shape) # 查看各个维度大小
print(a.index)
print(a.values) # 注意这里不是data查看，是用values

# 查找，某个索引是不是存在
print("word" in a)
