from sklearn.svm import SVC
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.model_selection import train_test_split

# 处理数据分为测试集和训练集
data = pd.read_csv("/Users/liudong/python/hello-2/机器学习/6支持向量机.csv")
data.columns = ["x1","x2","y"]
y_values = np.array(data["y"])
x_values = np.array(data[["x1","x2"]])
X_train, X_test, y_train, y_test = train_test_split(x_values, y_values, test_size=0.3, random_state=5)

svr = SVC()
# parameter_grid应该是一个列表，列表每部分元素是一个字典
parameter_grid = {'kernel': ['rbf'], 'gamma': [1,10,50,100,500,1000],"C": [0.01,0.1,1,10,50,100],}
cross_validation = StratifiedKFold(n_splits=5,shuffle=False,random_state=None)
clf = GridSearchCV(svr,param_grid=parameter_grid,scoring=None,cv=cross_validation)
# 此时gridsearch fit的x_values是一个数组，因为svm处理的是线性关系，而朴素贝叶斯处理的是条件概率关系，所以fit的应该是概率矩阵，类似于dataframe
clf.fit(X_train,y_train)
print(clf.best_params_)
# GridSearchCV得出的分数并不是我们的准确率分数，具体准确率分数还需要另外计算
print(clf.best_score_)
predictions = clf.predict(X_test)
a = accuracy_score(y_test,predictions)
print(a)


