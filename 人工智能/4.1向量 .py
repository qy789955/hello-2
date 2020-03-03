import matplotlib.pyplot as plt
import numpy as np
# 利用向量绘图
'''v = np.array([1,2])
a = 3
av = a*v
# 参照ax创建图的坐标轴
ax = plt.axes()
ax.plot(0,0,"or")
# 向量v作为蓝色的线从原点开始绘制,arrow是箭头
ax.arrow(0,0,*v,color="b",linewidth=2.5,head_width=0.30,head_length=0.35)
ax.arrow(0,0,*av,color="c",linestyle="dotted",linewidth=2.5,head_width=0.30,head_length=0.35)
plt.show()'''
# 设置v向量的显示np.array([1,2])
v = np.array([1,1])
w = np.array([-2,2])
vw = v+w
# 定义坐标图，参照 plt.axes（）绘制坐标
ax = plt.axes()
# 坐标上进行绘图操作ax.plot(0,0,"or")
ax.plot(0,0,"or")
ax.arrow(0,0,*v,color="b",linewidth=2.5,head_width=0.30,head_length=0.1)
ax.arrow(0,0,*vw,color="k",linewidth=3.5,head_width=0.2,head_length=0.2)
plt.show()
