import turtle
t = turtle.Turtle()
t.pensize(5)
t.pencolor("red")
t.penup()        # 抬笔的意思，此时笔前进不会在画板上留痕迹 t.penup()
t.forward(100)
t.pendown()      # 落笔，会在画板上留下痕迹，t.pendown()
t.forward(100)
t.setheading(180)   # 设置旋转角度，设置龟头的指向
t.fillcolor("green")    # 设定填充的颜色
t.begin_fill()     # 开始填充颜色
t.circle(180)      # 指定绘制一个圆，圆的直径为180
t.end_fill()        # 结束填充颜色

# 总体而言，关于笔，可以设置本身属性，设置移动到某个点 设置移动方式和方向  设置落不落笔在画板上 可以画圆 可以设置填充颜色
# t.pensize() t.pencolor("") t.speed()  t.setpos(1,2) t.setposition(1,2) t.goto(1,2) t.fd t.bd t.lt t.rt t.setheading(角度) t.penup() t.pendown() t.corcle(直径) t.fillcolor("") t.begin_fill() t.end_fill()
