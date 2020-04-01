import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
from sklearn import metrics

# 导入四种分类器
from sklearn.linear_model import logistic_regression_path
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

# pandas dataframe转变为numpy数组，1，取出数据 2，使用np.array()将取出的数据转化为列表
data = pd.read_csv("/Users/liudong/Desktop/训练模型.csv")
X = np.array(data[["x1","x2"]])
y = data["y"]

'''在scikit learn中训练模型 1，导入分类器 2，使用classifier.fit(X,y)将分类器和数据拟合。
classifier = logistic_regression_path()
classifier = MLPClassifier()
classifier = SVC()'''
classifier = DecisionTreeClassifier() # 这里的classifier是变量，名称只是为了容易辨认


# 使用散点图区分多个变量：画两个散点图，每个散点图限制取的点
plt.scatter(data["x1"][:50],data["x2"][:50],y, c='r',label='afDDf2')
plt.scatter(data["x1"][50:],data["x2"][50:],y, c='y',label='afDDf2')
plt.xlabel('Time')
plt.ylabel('Number')
plt.title('JFJF')
plt.show()

'''手动调整支持向量机参数调整
classifier = SVC(kernel="poly",degree=2)
kernel:  poly(多项式),linear(线性),rbf(高斯核）
degree: 多项式内核的次数，在选择了poly后需要加
c: c参数
gamma： y参数
'''

#测试模型train-test-split函数 test——size是指用来测试的数据占比
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.25)
print(len(X_train))
print(len(X_test))





