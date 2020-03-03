import pandas as pd
import numpy as np
pd.set_option("precision",1)
dat={"books": pd.Series(data = ["Great Expectations", "Of Mice and Men", "Romeo and Juliet", "The Time Machine", "Alice in Wonderland"]),
     "authors": pd.Series(data = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ]),
"user_1": pd.Series(data=[3.2,np.nan,2.5]), "user_2":pd.Series(data=[5, 1.3, 4.0, 3.8,0]),
"user_3": pd.Series(data=[2.0, 2.3,np.nan, 4]), "user_4":pd.Series(data=[4, 3.5, 4, 5, 4.2]) }
book_ratings = pd.DataFrame(dat)
print(book_ratings)
c = book_ratings.interpolate(method="linear",axis=0)
print(c)
# 使用dataframe调用values结果是显示每行，只是不成表格
best_rated = book_ratings.values
print(best_rated)
# 若想选择性的只显示特定的数值，在调用values时候加上并列的条件
new_best_rated = book_ratings[(book_ratings==5).any(axis=1)]["books"].values
print(new_best_rated)
