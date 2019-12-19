# 命名py文件时候不可以有空格
# 对象：一切事物皆是对象。类=属性+方法，属性是信息，方法是功能，也就是动作，能做什么，对信息进行处理的函数，方法等
# 定义类,类名大写
class Students: # 说明要开启一个新的代码块了
# 先定义方法
	def learn(self):
		print("好好学习，天天向上")
#  类名加（）就是创建对象，也是是实例化对象 
stu1 = Students()
stu1.learn()
# 为对象属性赋值,调用方法用stu1.learn;为对象赋属性值，也用stu1.name
stu1.name = "tony"
stu1.age = 12
stu1.grand = 7


class Students():
	def run(self):
		print("我在跑步")
	# 定义属性,用__init__;每次用类创建对象时候属性函数也叫构造函数都要执行，要执行就必须给他传递参数；同时属性函数需要初始化参数
	def __init__ (self,name,age,grand): #定义了属性这个函数，有冒号意思是后续有内容，所以即使没有内容也得加个pass等	
		self.a = name		
		self.age = age
		self.grand = grand
		print("我执行了")
stu1=Students("小张",12,7) # 类中的self就是我们创建的对象
print(stu1,a)
