import torch
def activation(x):
    return 1/(1+torch.exp(-x))
torch.manual_seed(7)
features = torch.randn((1,3))
n_hidden = 2
n_output = 1
w1 = torch.randn((features.shape[1],n_hidden))
w2 = torch.randn((n_hidden,n_output))
B1 = torch.randn((1,n_hidden))
B2 = torch.randn((1,n_output))
h = activation(torch.mm(features,w1) + B1)
output = activation(torch.mm(h,w2) + B2)
print(output)
