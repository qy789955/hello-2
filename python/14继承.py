# 继承是指多个类之间的父子关系，子进程继承了父进程中所有的实例变量和方法。父类也叫超类或者基类
class Cats:
	def __init__ (self,name,enjoy,height):
		self.name = name
		self.enjoy = enjoy
		self.height = height
	def run(self):
		print("蹦蹦跳跳")
# 想继承父类，就直接在定义类时候以父类为参数
class Bosi(Cats):
	# 定义属性不是非得用__init__?；如果都定义了属性怎么办？
	def newname(self,newname):
		self.newname = newname
	def run(self):
		print("跑")
# 当子类继续父类时候，创建对象时候也需要传参数（父类的init属性参数）
b = Bosi("tom","fish",12)
# 子类继承父类时候，调用两个类中相同的方法，执行的是子类的输出结果
b.run()


