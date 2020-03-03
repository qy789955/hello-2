# 小提琴图使用sb.violinplot进行绘制,定性变量和定量变量适合
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
a = pd.read_csv("/Users/liudong/Desktop/工作簿2.csv")
sb.violinplot(data=a,x="displ",y="comb")
# 可以改变颜色设置为统一以及不显示内部的箱线图
base_color=sb.color_palette()[0]  # [0]代表颜色列表中位置为0的颜色
sb.violinplot(data=a,x="displ",y="comb",color=base_color,inner=None)
plt.show()

