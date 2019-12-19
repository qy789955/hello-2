import turtle
t = turtle.Turtle()
turtle.bgcolor("black")   # 设置背景颜色  turtle.bgcolor   后退是t.bk()
t.speed(0)
color=["red","yellow","blue","white","green","purple"]
for i in range(0,300,1):   # for循环使用range，0为起点，300为终点，1为增量（步长），就是不同数字之间间隔为3
    t.pencolor(color[i%4])
    t.fd(i*0.8)
    t.lt(46)