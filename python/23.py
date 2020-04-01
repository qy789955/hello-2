import pygame,sys,random
from pygame.locals import *  # 导入pygame的local，可以调用其中的任何目录
pygame.init()
pygame.display.set_caption("贪吃蛇")  # 设置游戏名称
screen = pygame.display.set_mode([500,500])


direction = "right"
changedDrection = direction
x = 250  # 变量定义在循环前，才能在循环过程中不限制变量的值
y = 250
speed = 10
up = 273
Dowm = 274
Left = 276
Right = 275
length = 10
pygame.time.delay(20)


while True:
    for event in pygame.event.get():  # 从队列当中去获取事件
        print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                changeDirection = "right"
            if event.key == K_LEFT:
                changeDirection = "left"
            if event.key == K_UP:
                changeDirection = "up"
            if event.key == K_DOWN:
                changeDirection = "down"
                # 对应键盘上的esc键
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))


            # 碰撞检测
        if x >= 200 and x <= 210 or y >= 300 and y <= 304:
            length = length + 10
        screen.fill([127, 255, 212])
        snake = pygame.draw.rect(screen, [255,255,0], (x, y, length, 4))  # 蛇是与if循环平齐的内容

        # 生成食物
        for i in range(0,2):
            a = [200, 400]
            b = [300, 100]
            len = [10, 100]
            food = pygame.draw.rect(screen, [160, 32, 240], (a[i], b[i], len[i], 4))


        pygame.display.flip()

