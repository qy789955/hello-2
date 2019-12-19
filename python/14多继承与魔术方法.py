# 一个类可以继承多个类，遵循哪个属性？父类有同样的方法时候，子类继承哪个方法？
class XiaoMing(object):
	def __init__ (self,height,age,money):
		self.height=183
		self.age=48
		self.money=100000000

	def health(self):
		print("小明身体非常健康")

class Xiaohong(object):
	def __init__ (self,height,age,money):
		self.height=165
		self.age=40
		self.money = 100


	def health(self):
		print("特别222好看！")

# 多继承就是在类名中加入多个父类名, 注意的是多个父类中命名:类名（object)
# 继承多个类时候,如果不同的父类有同一个方法，继承时候具有优先级别，按照子类书写的顺序
# 继承多个类时候,如果不同的父类有不同的方法，怎么全部继承下来？
class Xiaoqiang(Xiaohong,XiaoMing):
	def study(self):
		print("小强学习特别好")
c=Xiaoqiang(183,48,2)
c.health()
print(c.money) # 如果在init函数中已经固定了内容的变量，在调用时候，与传的参数没有关系


