import pandas as pd
import numpy as np
import random
np.random.seed(24)
data = pd.read_csv("/Users/liudong/python/hello-2/机器学习/3.csv")
data.columns=["x1","x2","y"]
data_x = data[["x1","x2"]]
X = np.array(data_x)
data_y = data[["y"]]
y = np.array(data_y)
w1 = random.randint(0,8)
w2 = random.randint(0,8)
W = np.array([w1,w2])
b = random.randint(0,8)

# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)

pre_y_hat = []
def prediction(X,W,b):
    for i in range(len(X)):
        y_values = np.matmul(X,W) + b
        if y_values[i] >= 0:
            y_values[i] = 1
            pre_y_hat.append(int(y_values[i]))
        else:
            y_values[i] = 0
            pre_y_hat.append(int(y_values[i]))
    return pre_y_hat

y_hat = np.array(prediction(X,W,b))
print(y_hat.shape)

# TODO: Fill in the code below to implement the perceptron trick.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.

def perceptronStep(X, y, W, b, learn_rate = 0.01):
    for i in range(len(X)):
        if y[i]-y_hat[i] == 1:
            W[0] = X[i,0]*learn_rate
            W[1] += X[i,1]*learn_rate
            b += learn_rate
        elif y[i]-y_hat[i] == -1:
            W[0] -= X[i,0]*learn_rate
            W[1] -= X[i,1]*learn_rate
            b -= learn_rate
    return W, b

m = perceptronStep(X, y, W, b, learn_rate = 0.01)
print(m)
# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainPerceptronAlgorithm(X, y, learn_rate=0.01, num_epochs=25):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2, 1))
    b = np.random.rand(1)[0] + x_max
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0] / W[1], -b / W[1]))
    return boundary_lines







