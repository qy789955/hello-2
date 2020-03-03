import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
# seaborn的barplot函数是条形图，适合已经经过整理归纳的数据，如果数据没有归纳，则使用countplot函数
# plt的pie函数可以绘制饼状图
size = [20,320,440]
colors = ['red','yellowgreen','lightskyblue']
# startangle=90意思是垂直上方开始第一个扇形区域，counterclock=False是指按着顺时针方向进行
m = plt.pie(size,labels=["a","b","c"],colors=colors,startangle=90,counterclock=False)
# axis函数使得x和y轴的刻度相等
plt.axis("square")
plt.show()

# 用plt的pie函数绘制环形图，只需要加一个参数wedgeprops,扇形图wedgeprops=1，饼状图<1,wedgeprops={"width":0.4}
n = plt.pie(size,labels=["a","b","c"],colors=colors,startangle=90,counterclock=False,wedgeprops={'width' : 0.4})
plt.show() # plt.show()用来绘图，show出现几次，绘制几个图
