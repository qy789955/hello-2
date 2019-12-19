# 模块：具有一定功能的函数放在一个python文件中，这个文件就是模块
# 将一个功能定义进去函数
def mp(number):
	for j in range(0,len(number)):
		for i in range(j+1,len(number)):
			if number[i]>number[j]:
				number[j],number[i]=number[i],number[j]
	return number


print(4)