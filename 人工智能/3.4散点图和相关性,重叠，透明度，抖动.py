import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
import numpy as np
# pandas阅读数据
a = pd.read_csv("/Users/liudong/Desktop/工作簿2.csv")
# 创建散点图可以sb.regplot或者plt.scatter,其他相同,但是sb.regplot还带有数据的拟合回归线
# sb.regplot带有拟合回归线，此时默认fit_regplot=True,若取消，可以使用fit_reg=False
sb.regplot(data=a,x="displ",y="comb")
plt.scatter(data=a,x="displ",y="comb")
plt.xlabel("displacement")
plt.ylabel("combined fuel eff.(mpg)")
plt.show()
# 只有sb.regplot才可以设置抖动jitter,透明度设置alpha以字典形式scatter_kws={"alpha":1/10}
sb.regplot(data=a,x="displ",y="comb",fit_reg=False,x_jitter=0.3,scatter_kws={"alpha":1/5})
plt.show()
