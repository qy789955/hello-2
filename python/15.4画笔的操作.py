import turtle
t = turtle.Turtle()
t.pensize(5)  # python中所有表示长度的单位都是像素，pensize是设置画笔的粗细程度 pensize
t.pencolor("red")     # 设置画笔的颜色 pencolor
t.speed(10)          # 设置画笔的速度 speed 范围是0-10，数字越小移动越快
t.setpos(100,100)    # 设置画笔移动到某个点，三种函数一样的意思t.setpos   t.goto  t.setposition
t.goto(100,100)
t.setposition(100,100)

for i in range(0,100):
    t.forward(i)       # t.forward向前走，可缩写为t.fd; t.backward向后走，可缩写为t.bd; t.left向左转，可缩写为t.lt; t.right向右转，可缩写为t.rt
    t.lt(60)           # t.bd  t.fd 他们两个都是箭头朝前，但是t.lt t.rt是转，转了方向
#  总体而言，关于turtle,可以理解为画布，导入turtle：import turtle     设置画布的参数turtle.setup(画布x值，y值，距离电脑屏幕左上角的x值，y值)   设置画布的尺寸turtle.screensize(画布的宽度，画布的高度，"画布的颜色（使用RGB颜色码）")
#  t=turtle.Turtle()就是实例化对象，实际为创建了一个画笔，画笔的很多参数可以设置 t.pensize  t.pencolor  t.speed t.setpos  t.setposition t.goto  t.fd t.bd t.lt t.rt
#  画笔向前走走多少可以用t.fd(66)，其中66代表走的长阿杜，实际为像素的位置；t.lt（88）代表向左转的角度为88度
