# 通过学习曲线检测过拟合和欠拟合
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import logistic_regression_path
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import learning_curve

data = pd.read_csv("/Users/liudong/Desktop/1.2验证过拟合和欠拟合.csv")
X = np.array(data[["x1","x2"]]) # X 为100行2列的数字

'''np.array()作用将输入转化为矩阵形式
    输入为[1,2,3,4,5]，转化为5行1列，输入为[[1,2,3],[4,5,6]]，转化为2行3列
    若输入为[1,2,3,4,5]，转化为5行1列，此时使用a.shape[0],输出5，但是a.shape[1]输出会报错
'''
y = np.array(data["y"])
np.random.seed(55)

# 在画学习曲线前，需要先随机化数据
def randomize(X,y):
    # np.random.permutation（a）是随机排序函数，随机化排序小于a,从0开始的数据
    permutation = np.random.permutation(y.shape[0]) # 取到所有小于100的数字
    x2 = X[permutation,:]  # X[permutation,:]可以将所有的X的数据经过随机排序后都取到
    y2 = y[permutation]
    return x2,y2
x2,y2 = randomize(X,y)

'''数组取值的表示
    m = np.array([[1,2,3],[4,5,6]])
    print(m[1]),第一行
    print(m[1,2],第一行第二列
    print(m[1,:],第一行所有列
    '''

classifier1 = DecisionTreeClassifier()
classifier2 = SVC(kernel="rbf",gamma=2)
classifier1.fit(X,y)
classifier2.fit(X,y)

''' 函数learning_curve(estimator,X,y,cv=None,n_jobs=1,train_sizes=np.linspace(.1,1.0,num_trainings)
    estimator分类器
    cv:int 交叉验证生成器或可迭代的可选项，cv=None，使用默认的3倍交叉验证;cv=2，指定折叠数为2
    n_jobs可选并行的作业数，默认为1
    train_sizes曲线上每个点的数据大小
    train_scores针对每组数据训练后的算法训练得分
    test_scores针对每组数据训练后的算法测试得分
'''
def draw_learning_curves(X, y, estimator, num_trainings):
    train_sizes,train_scores,test_scores = learning_curve(DecisionTreeClassifier,x2,y2,cv=None,n_jobs=1,train_sizes=np.linspace(.1,1.0,num_trainings))
    # 训练数据的平均值np,mean  标准差np.std     np.mean(train_scores,axis=1)计算每一行的平均值
    train_scores_mean = np.mean(train_scores,axis=1)
    train_scores_std = np.std(train_scores,axis=1)
    test_scores_mean = np.mean(test_scores,axis=1)
    test_scores_std = np.std(test_scores,axis=1)

    # plt.grid(linestyle=":",color="r") 绘制带刻度线的网格线，linestyle线条风格 color线条颜色
    plt.grid()

    plt.tytle("learning curve")
    plt.xlabe("Training examples")
    plt.ylabel("Score")

    plt.plot(train_scores_mean, 'o-', color="g",
             label="Training score")
    plt.plot(test_scores_mean, 'o-', color="y",
             label="Cross-validation score")

    plt.legend(loc="best")

    plt.show()






