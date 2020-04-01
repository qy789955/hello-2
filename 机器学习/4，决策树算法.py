from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
# DecisionTreeClassifier(max_depth,max_features,min_samples_leaf,min_samples_split)
# 1，建模型  -----参数调整
max_depths = [5,6,7,8,9,10,11,12,13,14]
min_samples_leafs = [5,6,7,8,9,10,11,12,13,14,15]

# # 2，划分数据为训练集和测试集，训练集训练模型
# data = pd.read_csv("/Users/liudong/python/hello-2/机器学习/4.csv")
# data.columns = ["x1","x2","y"]
# x_values = np.array(data[["x1","x2"]])
# y_values = np.array(data["y"])
# # train_test_split(train_data,train_target,test_size=0.1,random_state=5)
# train_X,test_X,train_y,test_y = train_test_split(x_values,y_values,test_size=0.05,random_state=5)

# # 4，基础for循环调整参数，找到最大score的参数值
# argus = []
# for i in range(len(max_depths)):
#     for j in range(len(min_samples_leafs)):
#         model = DecisionTreeClassifier(max_depth=max_depths[i],min_samples_leaf=min_samples_leafs[j])
#         model.fit(train_X,train_y)
#
#         # 3，定义准确率评估函数，测试集测试模型
#         y_true = test_y
#         y_pred = model.predict(test_X)
#         score = metrics.accuracy_score(y_true, y_pred, normalize=True, sample_weight=None)
#
#         new_argus = [max_depths[i], min_samples_leafs[j],score]
#         argus.extend(new_argus)
# print(argus)
#
# # 比较score找到最大score对应的参数
# argues = np.array(argus)
# new_argues = argues.reshape(110,3)
# a = 0
# for i in range(len(new_argues)):
#     if new_argues[i,2] > a:
#         a = new_argues[i,2]
#         print(i,a)
# print(new_argues[0,:])

# 优化参数方案：使用k折交叉验证划分数据，网格搜索穷尽最优化的参数组合
# sklearn.model_selection.StratifiedKFold(n_splits=3,shuffle=False,random_state=None)与kfold参数类似，只是StratifiedKFold按照标签比例取值
data = pd.read_csv("/Users/liudong/python/hello-2/机器学习/4.csv")
data.columns = ["x1","x2","y"]
x_values = np.array(data[["x1","x2"]])
y_values = np.array(data["y"])
decision_tree_classifier = DecisionTreeClassifier()
cross_validation = StratifiedKFold(n_splits=3,shuffle=False,random_state=None)
#  网格搜索，cv用k折交叉验证
parameter_grid = {"max_depth":[5,6,7,8,9,10,11,12,13,14],
                  "min_samples_leaf":[5,6,7,8,9,10,11,12,13,14,15]}
gridsearch = GridSearchCV(decision_tree_classifier,
             scoring="accuracy",
             param_grid=parameter_grid,
             cv=cross_validation)
gridsearch.fit(x_values,y_values)
best_param = gridsearch.best_params_
print(best_param)
print(gridsearch.best_score_)
best_decision_tree_classifier = DecisionTreeClassifier(max_depth=best_param["max_depth"],min_samples_leaf=best_param["min_samples_leaf"])
best_decision_tree_classifier.fit(x_values,y_values)
y_true = y_values
y_pred = best_decision_tree_classifier.predict(x_values)
score = metrics.accuracy_score(y_true, y_pred, normalize=True, sample_weight=None)
print(score)









