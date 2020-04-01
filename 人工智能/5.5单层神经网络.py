import torch
def activation(x):
    # 定义sigmoid激活函数 s型曲线，将输入值压缩到了0-1之间，适合提供概率值
    return 1/(1+torch.exp(-x))

torch.manual_seed(7)
# 创建网络的输入特征，输入数据,randn生成正太分布的随机数,randn((1,5))指定元组，生成1行5列的二维张量
features = torch.randn((1,5)) # ()个数不影响
# randn_like()传入一个参数，查看参数的形状并且生成与之相似形状的新的随机数
weights = torch.randn_like(features)
# 创建随机偏差
bias = torch.randn((1,1))
# 进行求和，每个元素相乘相加再加偏差值,两类方法
# 第一类方法：直接求和，.sum()
y = activation((weights*features).sum()+bias)
y2 = activation(torch.sum(weights*features)+bias)
# 第二类方法：矩阵内积。torch.mm()或者torch.matmul(),  torch.mm()对矩阵形状要求严格，需要改变矩阵形状
# 更改矩阵形状的方法reshape()  resize_() view()
'''weights = weights.reshape(5,1)  # .reshape()返回一个新的矩阵，原来的矩阵数据没有变
a = torch.mm(features,weights)
print(a+bias)
weights.resize_(5,1)      # .resize_()是在原来数据上进行操作，返回一个经过更改的矩阵，但是如果请求的数据太多，可能会导致虚假数据
b = torch.mm(features,weights)
print(b+bias)
weights = weights.view(5,1)  # .view() 返回一个新的矩阵，原来的矩阵数据没有改变，并且如果数据不够，会报错，不会导致信息虚假
'''
y = activation(torch.mm(features,weights.view(5,1))+bias)
print(y)










