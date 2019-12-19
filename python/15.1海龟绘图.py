# turtle海龟，python中就有这个模块，可以直接导入应用
import turtle
t = turtle.Turtle()  # 创建的新的变量t可以理解为一只钢笔，也可以通过改变名字将它换成一个乌龟
for i in range(0,15):
    t.forward(i)     # 用实例化对象调用前进的方法，括号中的代表像素.   类中实例化对象要传参数，但是调用函数不需要，直接".函数（）"
    t.right(90)      # 向左转90度的意思
import turtle
t = turtle.Turtle()