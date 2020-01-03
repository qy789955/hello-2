#    file = open("/Users/liudong/Desktop/poetry.txt","r")
#    f = file.read()
#    print(f)
# file = open("/Users/liudong/Desktop/poetry.txt","a")
#a = file.write("\n这是缘分的句子")
#print(a)
#file.close()

m = "afjksdfjaskldjfsdf"   # 如果是字符串一定加引号，否则是变量
M = m.upper()
file = open("/Users/liudong/Desktop/Capital.txt","w")
a = file.write(M)    # write（）直接写内容
print(a)

