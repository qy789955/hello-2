import turtle # 可以不设置窗口，不设置画笔的形状等，直接设置画笔的走向
t = turtle.Turtle()
t.fillcolor("red")
t.begin_fill()
t.speed(10)
# 对于不变循环执行的内容，用for循环简化过程
for i in range(0,2):
    t.lt(120)
    t.forward(88)
t.end_fill()
t.forward(20)
# 对于变动的值，可以传入一个列表，用for循环依次执行列表中的数值
list = [120,120,240]
for i in list:
    t.lt(i)
    t.fd(88)
# for  循环两种for i in range(a,d)，下边不用i时候，代表执行次数     for i in list，i代表list中的从左到右的元素

