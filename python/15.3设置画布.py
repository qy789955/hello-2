# turtle也可以理解为一个画布,setup为画布（窗体）的函数(窗体的长度x，宽度y，位于电脑桌面的位置横向x，距离电脑左上角点的y轴距离),实际为设置了一个窗体样式
# turtle也可以设置窗体的大小screensize(画布的宽度，画布的高度，颜色属性)
import turtle
turtle.setup(400,600,100,100)
turtle.screensize(400,600,"#962121")  # 有关于背景颜色，python中用RGB表示，red,green,blue，三种组合可以组成任何一种颜色，三种颜色的取值都是0-255
                                  # 这里的"red"可以使用RGB色彩取色器，用"#色彩编号"，代替任何一种颜色
