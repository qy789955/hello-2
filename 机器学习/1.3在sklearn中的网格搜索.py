'''
 支持向量机为对象徐训练网格搜索
 1，导入gridsearchcv
 from sklearn.model_selection import GridSearchCV
 2,挑选参数,用字典形式展示
  parameters={"kernel":["ploy","rbf"],"c":[0.1,1,10]}
 3,创建评分机智
 from sklearn.metrics import make_scorer
 from sklearn.metrics import f1_score
 scorer=make_scorer(f1_score)
 4，创建参数和评分机制的gridsearch对象，对象与数据保持一致
 grid_obj=GridSearchCV(clf,parameters,scoring=scorer)
 grid_fit=grid_obj.fit(X,y)
 5,获得最佳估算器
 best_clf=grid_fit.best_estimator_
'''