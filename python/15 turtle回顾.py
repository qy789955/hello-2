'''
import turtle
amy = turtle.Turtle()
amy.color("yellow")
for m in ["a","b","c","d"]:  # 这里的side没有意义，只是代表一个计数器一样,用列表的方式可以让先后执行；列表内部的数字也没有意义，数字的个数有意义
    amy.forward(100)
    amy.left(90)

# for i in [1,"b","c","d"] for循环中的i代表计数器，没有意义；列表中的字符也没有意义，字符的个数是表达的意思
'''

import turtle
lucy = turtle.Turtle()
# list = "gray"
for i in (1,"a",3,4):    # for i in (1,"b","c","d") in后边的是列表还是括号没有区别
    lucy.color("gray")
    lucy.forward(100)
    lucy.left(90)






