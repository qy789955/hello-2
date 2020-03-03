# 热图是在网格中，将散点图的密度，用不同单元格的颜色深度体现出来，并且可以显示数量
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
plt.subplot(1,2,1)
a = pd.read_csv("/Users/liudong/Desktop/工作簿2.csv")
sb.regplot(data=a,x="displ",y="comb",fit_reg=False,x_jitter=0.2,y_jitter=0.2,scatter_kws={"alpha":1/3})
plt.subplot(1,2,2)
# 使用plt.hist2d绘制热图，与hist形式相同，只是可以使用cmap设置显示颜色板和cmin设置最小显示限度
bins_x=np.arange(0,5,1)
bins_y=np.arange(0,30,1)
plt.hist2d(data=a,x="displ",y="comb",bins=[bins_x,bins_y],cmap="viridis_r",cmin=0.5) # cmap="viridis_r"代表与默认的颜色反转
plt.colorbar()
plt.show()


