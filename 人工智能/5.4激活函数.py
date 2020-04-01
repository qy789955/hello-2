# 四种激活函数sigmoid softmax relu tanh
'''model.add(Activation("sigmoid"))
model.add(Activation("softmax"))
model.add(Activation("relu"))
model.add(Activation("tanh"))
# 随机梯度下降
model.fit(X_train,Y_train,epochs=1000,batch_size=100,verbose=100)'''
from __future__ import print_function
import torch
x = torch.rand(5, 3)
print(x)