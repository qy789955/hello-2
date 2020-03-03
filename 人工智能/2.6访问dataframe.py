import pandas as pd
# 创建dataframe时候，两种方法
# 方法一：建立两个并列的字典,创建datagrame时候再加入行名称
a = [{"bikes":20, "pants":30, "watches":35 },{"watches":10,"glasses":50,"bikes":15,"pants":5}]
store_items = pd.DataFrame(a,index=["store1","store2"])
print(store_items)
# 方法二：建立一个字典，键值对应的内容使用series的格式
b = {"bikes":pd.Series(data=[20,15],index=["store1","store2"]),"glasses":pd.Series(data=[50],index=["store2"]),"pants":pd.Series(data=[30,5],index=["store1","store2"]),"watches":pd.Series(data=[35,10],index=["store1","store2"])}
c = pd.DataFrame(b)
print(c)

# 访问dataframe的列，行和单个元素
print(store_items[["bikes"]]) # 访问列，直接利用索引访问（键值）
print(store_items[["bikes","watches"]])
print(store_items.loc[["store2","store1"]]) # 访问行，使用loc定位
print(store_items["glasses"]["store1"])   # 访问单个元素，先列，再行

# 添加列，行
# 添加列到末端两种方法
store_items["newwatches"] = [1,2]  # 直接将新值付给新列，访问时候是双重【】，赋值时候是单程【】
print(store_items)
store_items["new pants"] = store_items["pants"] + 5 # 通过原来的列运算关系添加新列
print(store_items)
# 用已有的列进行运算和仿照添加新的列
store_items["new ones"] = store_items["watches"][0:] # 仿照watches的列中行索引值为0和0以后的
print(store_items)
# 添加列到某一个位置，用insert(loc,index,data)
store_items.insert(5,"shoes",[10,20])
print(store_items)
# 添加行,需要先设置一个新的dataframe，使用append进行
new = {"bikes":11, "pants":22, "watches":33,"glasses":44,"new watches":55,"new pants":66 }
add = pd.DataFrame(new,index=["store3"])
new_store = store_items.append(add)
print(new_store)

# 删除列，".pop()"; 删除行,".drop()",drop需要指明axis=0，代表为行，axis=1，代表为列
new_store.pop("pants") # pop是个方法，是在原来的基础上进行修改
print(new_store)
new_store = new_store.drop(["store1"],axis=0) # drop是先复制原来的，再进行修改
print(new_store)







