class Computer:
	def prin(self):
		print("我可以打字")
	def install(self):
		print("我可以安装软件")
	def __init__ (self,brand,price,color,size):
		# python中定义变量，打印内容等不需要加；
		self.brand=brand  
		self.price=price
		self.color=color
		self.size=size
		print("我执行了")
	def __str__ (self): # python中加了__ __下划线的意思是已经封装好的函数，可以直接用，比如__str__ 和__init__
		# return多个内容时候，用+连接起来，但是注意+前后的数据类型需要相同
		return self.brand+str(self.price)+self.color+str(self.size)
# 在传参数时候，对于字符串要加引号，否则会认为是变量
c1 = Computer("thinkpad",10000,"red",15)
c1.prin()
c1.install()
# 创建的对象本质都是一个指针，是一个地址； 
print(c1)
# 若想打印出对象属性的内容，一个是可以打印c1.price，一个是可以在类中另外命名一个__str__,如上行
print(c1.price)
# 创建的类本质是指针，若想打出地址，使用id
print(id(Computer))
print(c1.brand)



