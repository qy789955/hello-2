# 层次聚类
from sklearn import datasets,cluster
X = datasets.load_iris().data[:10]
clust = cluster.AgglomerativeClustering(n_clusters=3,linkage="ward")  # linkage是指使用哪种聚类：全连接聚类，组平均聚类，离差平方和聚类
label = clust.fit_predict(X)  # 结果是输出每个数据点所在类的标签
#print(label)

# 画层次树，画系统树，使用scipy
from scipy.cluster.hierarchy import dendrogram,ward,single
from sklearn import datasets
import matplotlib.pyplot as plt
linkage_matrics = ward(X)
dendrogram(linkage_matrics)
plt.show()

# DBSCAN在sklearn中的实现
from sklearn import datasets,cluster
db = cluster.DBSCAN(eps=5,min_samples=5)
#print(db.fit(X))

# 高斯模型的实现
from sklearn import mixture
gmm = mixture.GaussianMixture(n_components=3)
print(gmm.fit_predict(X))
label1 = gmm.predict(X)
print(label1)

# 数据预处理，特征缩放，使得特征值权重相似，在sklearn中的实现
from sklearn.preprocessing import MinMaxScaler
import numpy as np
scaler = MinMaxScaler()
# 注意要求输入的是二维数组
weights = np.array([[115],[140],[175]])
rescaled_weights = scaler.fit_transform(weights)
print(rescaled_weights)

# sklearn中进行随机投影
from sklearn import random_projection
rp = random_projection.SparseRandomProjection()
new_x = rp.fit_transfrom(X)

# skleran中的ICA
from sklearn.decomposition import FastICA
ica = FastICA(n_components=3)
# X需要是列表
X = list(zip(signal_1,siagnal_2,signal3))
components = ica.fit_transform(X)



