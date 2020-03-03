# 用class主要是进行区分,将外在输入的针对格子行和列大小的数据存起来
class Point():
    row = 0
    col = 0
    def __init__ (self,row,col):
        self.row = row
        self.col = col



import pygame
pygame.init()
w = 600
h = 600

# 绘制格子的行和列,屏幕总共有100个格子
ROW = 6  # 整个屏幕被分成一些行高的格子
COL = 8


size = (w,h)
window = pygame.display.set_mode(size)
pygame.display.set_caption("贪吃蛇")

# 定义坐标
bg_color = (255,255,0)
head = Point(row = int(ROW/2),col=int(COL/2))
head_color = (0,128,128)
food = Point(row=2,col=3)
food_color = (255,255,0)

# 蛇头，蛇身，食物都是矩形，直接定义矩形的位置和颜色
def rect (point,color):
    cell_width = w/COL
    cell_height = h/ROW

    left = point.col * cell_width
    top = point.row * cell_height

    pygame.draw.rect(window,color,(left,top,cell_width,cell_height))

# 定义函数，可以将操作变成可以重用的操作


# 游戏循环
quit = True
clock = pygame.time.Clock()   # 返回一个时针
while quit:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False  # 循环结束

        # 渲染
        pygame.draw.rect(window,bg_color,(0,0,w,h)

        # 蛇头
        rect(head.head_color)

        # 等命令做完将系统交出去控制权
        pygame.display.flip()  # 渲染，把控制权交给系统

        # 设置帧
        clock.tick(60)  # 更新时针
