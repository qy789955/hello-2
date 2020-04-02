# 为慈善机构寻找捐助者 1，数据预处理，拆分为y和x，x中的数据文本数字化，异常值处理，归一化等等。  2，数据集划分，测试集，验证集，训练集
# 3，定义天真模型和评估指标，定义预设的预测评估方法 带入不同预设模型比较效果 4，选择合适的模型进行优化处理：参数调整和摘取重要特征
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import time
from sklearn.metrics import accuracy_score,fbeta_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import GridSearchCV,KFold
from sklearn.metrics import make_scorer


# 一，数据处理
# 1，读取数据，浏览数据
data = pd.read_csv("./census.csv")
# 显示所有的行列，pd.set_option("display.max_columns",None) pd.set_option("display.max_rows",None) None表示全部，可以用数字代替
pd.set_option("display.max_columns",None)
at_most_50k = []
greater_50k = []
for i in data["income"]:
    if i == "<=50K":
        at_most_50k.append(i)
    else:
        greater_50k.append(i)
n_at_most_50k = int(len(at_most_50k))
n_greater_50k = int(len(greater_50k))
print(data.columns.values)
print(data.head)
print("Total number of records:{}",format(len(data)))
print("Individuals making more than 50k:{}",format(n_greater_50k))
print("Individuals making at most 50k:{}",format(n_at_most_50k))
print("Percentage of individuals making more than 50k:{}",format(n_greater_50k/(n_at_most_50k + n_greater_50k)))
# 2,拆分为labels和features
label_data = data["income"]
labels = label_data.map({"<=50K":0,">50K":1})
print(labels)
features_raws = data.drop(["income"],axis=1)
print(features_raws.head)
# 3,使用对数函数处理异常偏差值features np.log(x+1)防止x=0时候对应的无穷大的值
features_raws[["capital-gain","capital-loss"]]= features_raws[["capital-gain","capital-loss"]].apply(lambda x:np.log(x+1))
print(features_raws[["capital-gain","capital-loss"]])
# 4,归一化数字特征，进行特征缩放
scaler = MinMaxScaler()
numerical = ['age', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
features_raws[numerical] = scaler.fit_transform(features_raws[numerical])
# 5,使用pandas的独热编码处理文本特征 使用独热编码，适合于处理离散型数据特征(表示类别的那些特征),好处是让特征之间的距离更加合理
features = pd.get_dummies(features_raws)
print(len(list(features.columns)))
# 6,数据拆分 straify=labels是按照labels的数据比例进行拆分
x_train,x_test,y_train,y_test = train_test_split(features,labels,test_size=0.2,random_state=0,stratify=labels)
x_tra,x_val,y_tra,y_val = train_test_split(x_train,y_train,test_size=0.2,random_state=0,stratify=y_train)
print("the number of train samples was :{}".format(len(x_tra)))
print("the number of validation samples was :{}".format(len(x_val)))
print("the number of test samples was :{}".format(len(x_test)))


# 二：天真模型，以及其他模型的构建
# 1，构建天真模型：设定无论什么情况下都预测调查者都是年收入超过50的人,进行评估天真模型
accuracy = n_greater_50k/(n_greater_50k + n_at_most_50k)
precision = n_greater_50k/(n_greater_50k + n_at_most_50k)
recall = n_greater_50k/n_greater_50k
beta = 0.5
fscore = (1 + beta**2) * precision * recall / (recall + precision * beta**2)
print("accuracy score was:{}".format(accuracy))
print("fscore score was:{}".format(fscore))

# 2,利用sklearn构建模型
# 先定义一个模型检测方法
def train_predict(learner,sample_size,x_train,y_train,x_val,y_val):
    # return results就可以直接将字典中的所有新值全部加入
    results = {}
    learner = learner.fit(x_train[0:sample_size],y_train[0:sample_size])
    predictions_train = learner.predict(x_train[0:300])
    predictions_val = learner.predict(x_val)
    results["acc_train"] = accuracy_score(y_train[0:300],predictions_train)
    results["acc_val"] = accuracy_score(y_val,predictions_val)
    results["f_train"] = fbeta_score(y_train[0:300],predictions_train,beta=0.5)
    results["f_val"] = fbeta_score(y_val,predictions_val,beta=0.5)
    # learner.__class__.__name__   表示显示learner的类名
    print("{} trained on {} samples.".format(learner.__class__.__name__,sample_size))
    return results

# 导入模型进行预测 比较不同的模型：决策树，支持向量机，朴素贝叶斯，集成方法对应的预测效果
clf_C = MultinomialNB()
clf_D = AdaBoostClassifier()
clf_A = DecisionTreeClassifier(random_state=0)
clf_B = SVC()
clfs = [clf_A,clf_B,clf_C,clf_D]
# 计算1%，10%，100%的训练数据分别对应多少点
sample_1 = int(len(x_tra)*0.01)
sample_10 = int(len(x_tra)*0.1)
sample_100 = int(len(x_tra))
sample_sizes = [sample_1,sample_10,sample_100]
# for循环使得每个模型都经历不同的数据样本量
results = {}
#  将结果写入results.csv中
csv = open("project3_results.csv","w")
for clf in clfs:
    clf_name = clf.__class__.__name__
    results[clf_name] = {}
    # for i,samples in enumerate(sample_sizes) enumerate遍历元素以及下标，如果遍历的是字典，返回的是下标是字典的索引值
    for i,samples in enumerate(sample_sizes):
        result = train_predict(clf, samples, x_tra, y_tra, x_val, y_val)
        # 若写入列表或者字典等，需要写的时候用str（data）先转化格式再写入
        csv.write(str(clf_name) + "\n")
        csv.write(str(result) + "\n")


# 三，模型优化：选定AdaBoostClassifier作为最佳模型，同时利用网格搜索和k折交叉验证优化参数

clf = AdaBoostClassifier(random_state=6)
scorer = make_scorer(fbeta_score,beta=2)
# 通常用步长（学习率）和迭代次数一起调整进行参数优化
parameters = {"n_estimators":[25,50,100],
             "learning_rate":[1,5,10]}
grid_obj = GridSearchCV(estimator=clf,param_grid=parameters,scoring=scorer,cv=KFold(n_splits=12))
# 一定不用测试数据，知道所有模型完全好以后，再用测试数据进行拟合
grid_obj_fit = grid_obj.fit(x_tra,y_tra)
best_clf = grid_obj_fit.best_estimator_
predictions = clf.fit(x_tra,y_tra).predict(x_val)
best_predictions = best_clf.predict(x_val)
# 汇报调参前后的参数
print("Unoptimized model\n------")
print("Accuracy score on validation data:{}".format(accuracy_score(y_val,predictions)))
print("F-score on validation data:{}".format(fbeta_score(y_val,predictions,beta=0.5)))
print("\nOptimized Model\n------")
print("Accuracy score on validation data:{}".format(accuracy_score(y_val,best_predictions)))
print("F-score on validation data:{}".format(fbeta_score(y_val,best_predictions,beta=0.5)))
# 结果证实：模型的默认参数："n_estimators":50，"learning_rate":1 与调优后的参数，相距不大，可以使得模型的fbeta score提高0.01


# 四：进一步优化模型的预测时间：减少特征数量，尝试一下如果只使用几个重要特征（权重加和超过百分之50），对于模型的预测能力会影响多少
from sklearn.base import clone
# 使用模型中的"feature_importances_"提取模型的特征权重，注意要求模型必须有"feature_importances_"
# x_tra.columns.values对于特征的列表，
model = DecisionTreeClassifier(random_state=0)
model.fit(x_tra,y_tra)
# model.feature_importances_结果是各个feature的权重，并没有排序
importances = model.feature_importances_
'''
a = [5,6,7,8,9,10]  np.argsort() 参数为列表，排序列表，打印出对应的索引
print(np.argsort(a))        >>>>>[0 1 2 3 4 5] 是将a列表中的数字从小到大排序，再打出来对应的索引
print(np.argsort(a)[::1])   >>>>>[0 1 2 3 4 5] 从小到大排
print(np.argsort(a)[::2])   >>>>>[0 2 4]       从小到大，隔二取一
print(np.argsort(a)[::-1])  >>>>>[5 4 3 2 1 0] 从大到小排
print(np.argsort(a)[::-2])  >>>>>[5 3 1]       从大到小排，对应的索引，隔两个取一个
print(np.argsort(a)[::-3])  >>>>>[5 2]         从大到小排，对应的索引，隔3个取一个
'''
# 减少特征
x_tra_reduced = x_tra[x_tra.columns.values[(np.argsort(importances)[::-1])[:5]]]
x_val_reduced = x_val[x_val.columns.values[(np.argsort(importances)[::-1])[:5]]]
# 在网格搜索的基础上训练一个"最好的模型"
clf_on_reduced = (clone(best_clf)).fit(x_tra_reduced,y_tra)
reduced_predicitions = clf_on_reduced.predict(x_val_reduced)
# 对于每一个版本汇报分数
print("Final Model trained on full data\n------")
print("Accuracy on validation data: {:.4f}".format(accuracy_score(y_val, best_predictions)))
print("F-score on validation data: {:.4f}".format(fbeta_score(y_val, best_predictions, beta = 0.5)))
print("\nFinal Model trained on reduced data\n------")
print("Accuracy on validation data: {:.4f}".format(accuracy_score(y_val, reduced_predicitions)))
print("F-score on validation data: {:.4f}".format(fbeta_score(y_val, reduced_predicitions, beta = 0.5)))
'''
Final Model trained on full data
------
Accuracy on validation data: 0.8684
F-score on validation data: 0.7517

Final Model trained on reduced data
------
Accuracy on validation data: 0.8577
F-score on validation data: 0.7337

Process finished with exit code 0'''

# 五，测试集上测试模型，计算准确率和fscore
y_predictions = best_clf.predict(x_test)
print("Accuracy score of the best model was:{}".format(accuracy_score(y_test,y_predictions)))
print("Fbeta score of the best model was:{}".format(fbeta_score(y_test,y_predictions,beta=0.5)))











