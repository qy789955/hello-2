# 文件的读
file = open("/Users/liudong/Desktop/ceshi.py","r") # 返回的是一个特殊的文件
a = file.read()
print(a)
file.close()  # 文件读写完需要进行关闭

# 文件的写：只覆盖，生成新的内容
file = open("/Users/liudong/Desktop/ceshi.py","w") # 如果这里的文件路径是新的，就会生成一个新的文件放置写的内容
file2 = open("/Users/liudong/Desktop/ceshi.py2","w")
b = file.write("新写的内容")
b2 = file2.write("新写的内容")
print(b,b2)
file.close()
file2.close()

# 文件的写：只添加，不覆盖
file = open("/Users/liudong/Desktop/ceshi.py","a") # 如果这里的文件路径是新的，就会生成一个新的文件放置写的内容
b = file.write("\n 添加的内容")
print(b)
file.close()

# 文件的复制，实际是读取文件，写入新文件
file = open("/Users/liudong/Desktop/ceshi.py","r") # 如果这里的文件路径是新的，就会生成一个新的文件放置写的内容
data = file.read()
file.close()

file_copy = open("/Users/liudong/Desktop/copyceshi.py","w")
c = file_copy.write(data)
file_copy.close()


# 总体，文件的读写复制，区别在于"mode"处的值不同，有的是"a"--添加新内容，不覆盖；"w"写入新内容，覆盖； "r"读取文件内容
# file = ("文件的路径","mode","encoding=utf-8可以省略")
# file.read()  file.write()
# file.close()  读写完文件后需要关闭

