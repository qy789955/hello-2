import pandas as pd
import numpy as np
'''from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
data = load_boston()
x = data['data']
y = data['target']
model = LinearRegression()
model.fit(x,y)
sample_house =[[2.29690000e-01, 0.00000000e+00, 1.05900000e+01, 0.00000000e+00, 4.89000000e-01,
                6.32600000e+00, 5.25000000e+01, 4.35490000e+00, 4.00000000e+00, 2.77000000e+02,
                1.86000000e+01, 3.94870000e+02, 1.09700000e+01]]
print(type(sample_house))
print(model.predict(sample_house)'''
bias = -0.5
weight1 = 0.7
weight2 = 1
test_inputs = [(1,1),(1,0),(0,1),(0,0)]
correct_outputs = [1,1,1,0]
outputs = []
for input,output in zip(test_inputs,correct_outputs):
    pre_outputs=weight1*input[0]+weight2*input[1]+bias
    out=int(pre_outputs)
    is_correct="yes" if out == output else "No"
    outputs.append([input[0],input[1],output,out,is_correct])
a=pd.DataFrame(outputs,columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output', '  Is Correct'])
print(a)

