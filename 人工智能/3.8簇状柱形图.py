import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
# 绘制两个定性变量之间的关系，用热图和簇状柱形图都可以
# 1，使用绘制分类变量的热图sb.heatmap,参数需要进行数据处理
a = pd.read_csv("/Users/liudong/Desktop/工作簿2.csv")
ct_counts = a.groupby(["type","car"]).size() # groupby([]).size()提取数据
ct_counts = ct_counts.reset_index(name="count") # reset_index()将序列转化为dataframe
ct_counts = ct_counts.pivot(index="type",columns="car",values="count")   # pivot可以重新安排数据的行或者列
sb.heatmap(ct_counts,annot=True,fmt="d")
''' heatmap以二维数组或者dataframe为参数
    annot = True表示显示数据
    fmt="d"确保所有数量统计都是十进制的'''
plt.show()

# 2，簇状柱形图sb.countplot()
sb.countplot(data=a,x="type",hue="car") # countplot是单柱状图，hue参数可以添加柱数量
plt.xticks(rotation=100) #rotation显示的是label的旋转角度
plt.show()

