import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
a = pd.read_csv("/Users/liudong/Desktop/工作簿2.csv")
# 箱线图使用sb.boxplot(),箱线图可以直观表示数据的中位线，最大值，最小值，四分之一线和四分之三线
base_color=sb.color_palette()[0]
plt.subplot(1,2,1)
ax1 = sb.boxplot(data=a,x="displ",y="comb",color=base_color)

# 使用小提琴图也可以体现中位数，四分之一线和四分之三线,设置innner="quartile"
plt.subplot(1,2,2)
sb.violinplot(data=a,x="displ",y="comb",color=base_color,inner="quartile")
# 设置两个图的左边y轴对齐
plt.ylim(ax1.get_ylim())
plt.show()
