import pandas as pd
# 读取数据
Google_stock = pd.read_csv("/Users/liudong/Desktop/abc.csv")
print(Google_stock)
# 查看数据类型
print(Google_stock.shape)
print(type(Google_stock))
# 查看数据的前后几行，head() tail()
print(Google_stock.head(3))
print(Google_stock.tail(3))
# describe()查看每列数据的平均值，最大值，最小值等
print(Google_stock.describe())
print(Google_stock["A"].describe()) # 查看某一列的具体数据
print(Google_stock.mean()) # 注意这里的mean会计算出每列对应的平均值
print(Google_stock.max())
print(Google_stock.min())
# 检查数据是否具有NaN值, .isnull().any() 查看是否有任何含有NaN值的列
print(Google_stock.isnull().any())
# 查看不同列之间的相关性.corr()
print(Google_stock.corr())
# 用不同的方式对数据分组.groupby()
fake = pd.read_csv("/Users/liudong/Desktop/fake_company.csv")
print(fake)
print(fake.groupby(["Year"])["Salary"].sum())
print(fake.groupby(["Year"])["Salary"].mean())
print(fake.groupby(["Name"])["Salary"].sum())
print(fake.groupby(["Year","Department"])["Salary"].sum())