import pandas as pd
import numpy as np
import string
import collections
import pprint
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

df = pd.read_table("/Users/liudong/python/hello-2/机器学习/5,朴素贝叶斯dataset",
                  sep="\t",
                  header=None,
                  names=["label","sms_message"])

# 行，列的数值处理 .map  .apply   .applymap
df["label"] = df["label"].map({"ham":0,"spam":1})
documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']
# # 字符串的操作：小写 str.lower()  数据类型仍然为列表
# lower_case_documents = []
# for i in documents:
#     lower_case_documents.append(i.lower())
# print(lower_case_documents)
#
# # 字符串的操作：去标点符号str.translate(trantab) trantab=str.maketrans("","",str.punctuation)，数据类型仍然为列表
# sans_punctuation_documents = []
# trantab = str.maketrans("","",string.punctuation)
# for i in lower_case_documents:
#     sans_punctuation_documents.append(i.translate(trantab))
# print(sans_punctuation_documents)
#
# # 字符串的操作：划分单词串。数据类型为列表中嵌套列表
# preprocessed_documents = []
# for i in sans_punctuation_documents:
#     preprocessed_documents.append(i.split())
# print(preprocessed_documents)
#
# # 形成单词频率列表   collections.Counter(str)。 数据类型仍然为列表中嵌套collections.Counter（字典）
# frequency_list = []
# for i in preprocessed_documents:
#     a = collections.Counter(i)
#     frequency_list.append(a)
# pprint.pprint(frequency_list)
#
# # CountVectorizer实现特征值提取和计数，形成关键词频率矩阵。 可以用CountVectorizer(stop_words=["a","b","s"])来忽略掉一些单词如a,b,s
# count_vector = CountVectorizer()
# count_vector.fit(documents)
# a = count_vector.get_feature_names()
# doc_array = count_vector.transform(documents).toarray()
# print(a)
# print(doc_array)
# frequency_matrix = pd.DataFrame(doc_array,columns=a)
# print(frequency_matrix)

# 处理分析数据
X_train, X_test, y_train, y_test = train_test_split(df["sms_message"],df["label"],random_state=1)
# sklearn中的CountVectorizer()函数是文本特征提取器，
count_vector = CountVectorizer()
# 注意count_vector.fit_transform(X_train) 与 count_vector.transform(X_test)
training_data = count_vector.fit_transform(X_train)  # 输入的X-train是一个series，此时training_data是一个单词频率矩阵，也就是dataframe的形式
testing_data = count_vector.transform(X_test)

# 贝叶斯算法
naive_bayes = MultinomialNB()
# 贝叶斯分类器拟合的参数（x，y），y是label，x是关于特征文本出现的频率矩阵，数据格式可以是列表嵌套的字典格式，或者dataframe等
naive_bayes.fit(training_data,y_train)
predictions = naive_bayes.predict(testing_data)
print('Accuracy score: ', format(accuracy_score(y_test, predictions)))
print('Precision score: ', format(precision_score(y_test, predictions)))
print('Recall score: ', format(recall_score(y_test, predictions)))
print('F1 score: ', format(f1_score(y_test, predictions)))







