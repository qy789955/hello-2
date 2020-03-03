# 用单变量图表描述多个变量的方法，1，分面；2，调整单变量图像
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
# 1，分面描述
# 针对任何图表，都可以进行分面，可以解决定性变量太多的问题 sb.FacetGird(),指明分的数据来自哪里，分的对象是谁
bins = np.arange(0,1,0.1)
a = pd.read_csv("/Users/liudong/Desktop/工作簿2.csv")
# 确定一行有2个分面，col_wrap=2
b = sb.FacetGrid(data=a,col="car",col_wrap=2)
# 指明每个分面要绘制的图表b.map()
# 为了使得每个分面的数组间距相同，使用bins参数
b.map(plt.hist,"type",bins=bins)
plt.show()

# 2，调整单变量图形，使用有关于第二个变量的中值或者平均值等代替原来的频率，就可以表示双变量了，sb.barplot()
# errwidth=0表示不显示误差线
sb.barplot(data=a,x="car",y="comb",errwidth=0)
plt.ylabel("mean(mpg)")
plt.show()


