import pandas as pd
import numpy as np
from IPython.display import display
# import visuals
''' 项目描述：对乘客的生还结果进行预测：一：真实的生还结果  二：定义方法预测生还结果并检测准确度  三：预测准确度的判断'''

# 1,数据处理。将生存结果"Survived"存贮在新的变量中
full_data = pd.read_csv("/Users/liudong/python/hello-2/项目集合/machine_learning projects1-titanic_survival_exploration/titanic_data.csv")
pd.set_option("display.max_columns",None)
print(full_data.shape)
outcomes = full_data["Survived"]
data = full_data.drop(["Survived"],axis=1)
print(data)


'''dataframe print显示不全的问题
1，显示所有的行和列 pd.set_option("display.max_columns",None)  pd.set_option("display.max_rows",None)
2,显示指定的行数 pd.set_option("max_colwidth",100)'''


# 2，定义预测准确度检测方法,并验证
def accuarcy_score(truth,pred):
    # truth和pred都是pd.series 的type
    if len(truth) == len(pred):
        # truth==pred type为dataframe，输出结果为每项判断后有关truth与false的列表， .mean()方法会显示其中truth所占的比例
        return "Predictions have an accuracy of {:.2f}%.".format((truth==pred).mean()*100)
    else:
        return "Number of predictions does not match number of outcomes!"
predictions=pd.Series(np.ones(5,dtype=int))
print(accuarcy_score(outcomes[:5],predictions))

# 3,定义预测生存率的方法，不断改进使得准确度提升
def predictions_0(data):
    predictions = []
    for _, passenger in data.iterrows():
        predictions.append(0)
    return pd.Series(predictions)
predictions = predictions_0(data)
print(accuarcy_score(outcomes,predictions))


def predictions_1(data):
    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex'] == "female":
            predictions.append(1)
        else:
            predictions.append(0)
    return pd.Series(predictions)
predictions = predictions_1(data)
print(accuarcy_score(outcomes,predictions))

def prediction_2(data):
    predictions=[]
    # dataframe.iterrows()是遍历dataframe中所有数据的方法。"_,"只是代表遍历数据的标号，可以被代替"a,"  "passengers"只是遍历数据后存储的一个变量，可以被代替
    for _, passengers in data.iterrows():
        if passengers["Sex"] == "female":
            predictions.append(1)
        elif passengers["Age"] <= 10:
            predictions.append(1)
        else:
            predictions.append(0)
    return pd.Series(predictions)
predictions = prediction_2(data)
print(accuarcy_score(outcomes,predictions))







