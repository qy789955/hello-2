class Student:
	gender = "male" # 类变量，类中的变量
	heigth = 12
	def __init__ (self,name,age):
		self.name = name # 实例变量
		self.age = age
	def learn(self):
		print("好好学习，天天向上")
		print(self.name)
		print(self.gender)
	def run(self):
		# print的内容如果有多个，可以直接用，隔开
		print(self.gender,self.heigth,self.name)

stu1 =  Student("tony",12)
# 修改类变量，直接在调用时候赋新值就可以; 方法如果不调用是不会执行的，只有属性函数会在创建对象时候就执行
stu1.gender = "tom"
print(stu1.gender)
# 修改实例变量，直接在调用时候赋新值就可以;
stu1.name = "tom"
print(stu1.name)