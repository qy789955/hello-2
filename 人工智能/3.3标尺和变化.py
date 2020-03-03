import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=[10,5])
plt.subplot(1,2,1)
data=np.random.randn(1000)
bin_edges=np.arange(0,100,10)
plt.hist(x=data,bins=bin_edges)
plt.show()
plt.subplot(1,2,2)
data2=np.random.randn(1000)
bin_edges2=np.arange(0,100,10)
plt.hist(x=data2,bins=bin_edges2)
# plt.xscale("log"),xscale包含几个常见的内置变化，通过它可以将标尺换为对数标尺
plt.xscale("log")
plt.show()

