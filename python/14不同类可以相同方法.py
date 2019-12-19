class Student:
	def __init__ (self,name,age):
		self.name = name 
		self.age = age
	def learn(self):
		# python是对缩进敏感的语言，一旦def了一个函数，下一行就一定需要缩进
		print("好好学习，天天向上")
	def run(self):
		print("跑")
class Man:
	# 定义类时候可以不定义属性？
	def learn(self):
		print("我是男人")
s1 = Student("tom",66)
s1.learn()
m = Man()
m.learn()
m.run()


