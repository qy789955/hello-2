import torch
import numpy as np
import helper
import matplotlib.pyplot as plt
from torchvision import datasets,transforms
'''
    torchvision是pytorch的一个图形库，用来服务深度学习框架，构建计算机视觉模型
    torchvision.transforms用于常见的一些图形变化，
    transforms.normalize()---图像变幻，标准化（先减均值，再除以标准差）
    transforms.ToTensor 将像素值范围为【0，255】的PIL.image或者shape=（H*W*C)的np.ndarray转化为tensor，
        并且归一化至【0.0，1.0】的torch.FloatTensor,shape为（N*C*H*W）待确认
'''
# 定义一个图像变化并且归一化数据
transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))])
trainset = datasets.MNIST("MNIST_data/",download=True,train=True,transform=transform)
# dataloader是pytorch数据读取的一个接口，只要用pytorch训练模型都会用到，接口的目的是：将自定义的dataset按照batch——size大小以及是否shufle等封装成一个batch size大小的张量
trainloader = torch.utils.data.DataLoader(trainset,batch_size=64,shuffle=True)
# 使用iter将trainlodaer转化为迭代器，从而从中获取数据或者在for循环中使用它
dataiter = iter(trainloader)
print(trainloader)
