import numpy as np
import torch
# numpy和torch之间转换时候，内存会共享，一个更改，另一个也会更改
a = np.random.rand(3,4)
# torch.from_numpy将numpy转换为torch，可以用到torch的方法
b = torch.from_numpy(a)
print(b)
# torch元组转换为numpy
c = b.numpy()
print(c)