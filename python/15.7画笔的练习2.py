import turtle
t = turtle.Turtle()
t.bk(60)        # 朝后走是t.bk()  朝后走时候箭头朝向还是前
t.setheading(180)
t.fillcolor("black")
t.begin_fill()
t.circle(30)
t.end_fill()
t.forward(80)
t.fillcolor("black")
t.begin_fill()
t.circle(30)
t.end_fill()
t.fillcolor("red")
t.begin_fill()
list = [80,40,80,80,80,40,40,40]
list2 = [90,0,30,0,270,0,270,180]
for i in list:
    t.forward(i)
    t.setheading(j)      # setheading永远指的是和x轴方向的夹角，负的为顺时针，正的为逆时针
t.forward(40)
t.end_fill()




