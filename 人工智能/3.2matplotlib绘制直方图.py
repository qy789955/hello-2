import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# 用hist绘制直方图
# numpy.random.randn(10)会随机生成一组具有正太分布的数组
x=np.random.randn(1000)
bins=np.arange(-3,4,1)

'''plt默认把图划分成10组,
bins代表长条形数目，默认为10,bins可以指定组边界，使用np.arange生成特定组距离的长条形,arange最大值取不到
alpha表示透明度
normed=1，代表归一化，显示频率
x代表数据集 '''
plt.hist(x,bins=bins,normed=0,facecolor="yellow",edgecolor="black",alpha=0.7)
plt.xlabel("区间")
plt.ylabel("频率/频数")
plt.show()
# seaborn的distplot也可以绘制直方图，sb.distplot(),同时可以绘制密度曲线

# 使用subplot绘制多个图的拼图，subplot（row,column,位置）
plt.subplot(221)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

plt.subplot(222)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])  # plot()折线图

plt.subplot(223)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

plt.subplot(224)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])


plt.show()
plt.figure(figsize = [10, 5]) # 规定了母图的整体大小

# histogram on left: full data
plt.subplot(1, 2, 1)
x=np.random.randn(1000)
bin_edges = np.arange(0, 800, 2.5) 
plt.hist(x, bins = bin_edges)
# histogram on right: focus in on bulk of data < 35
plt.subplot(1, 2, 2)
bin_edges = np.arange(0, 35+1, 1)
plt.hist(x, bins = bin_edges)
'''plt.xlim(a,b),可以调整子图的大小，其中a代表图片的宽度，h代表图片的高度
    写法这里不规定，可以xlim([0,10]),plt.xlim((0,10)),plt.xlim(0,10)'''
plt.xlim(0, 10)
plt.show() 












