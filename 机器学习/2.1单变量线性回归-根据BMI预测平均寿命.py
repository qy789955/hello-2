import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
data = pd.read_csv("/Users/liudong/python/hello-2/机器学习/2线性回归-根据BMI预测平均寿命.csv")
# 设置显示多列
#pd.set_option("display.max_rows",None)
#pd.set_option("display.max_columns",None)
print(data.head())
print(data.shape)
x_values = data[["BMI"]] # x和y的取值都是双重【】，表示可以容纳多个变量
y_values = data[["Life expectancy"]]
model = LinearRegression()
model.fit(x_values,y_values)
print(model.predict([[21.07931]]))






