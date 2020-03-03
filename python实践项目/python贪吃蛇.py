# pygame中的所有事件都是放在一个实时循环中完成的
import pygame,sys,random  # sys是python运行时候的环境
# locals这个模块包含各种pygame所使用的常量

from pygame.locals import *

# 1，定义颜色变量
redcolor = pygame.Color(255,0,0)
# 背景为黑色
blackcolor = pygame.Color(0,0,0)
# 贪吃蛇为白色
whitecolor = pygame.Color(255,255,255)

# 2，定义游戏结束时候的函数
def gameOver():
    pygame.quit()
    sys.exit()

# 3,定义main函数，定义我们的入口函数
def main():
    # 3.1 初始化pygame
    pygame.init()
    # 3.1 定义变量来控制游戏速度
    fpsClock = pygame.time.Clock()
    # 3.3 创建pygame的显示层
    playSurface = pygame.display.set_mode([640,480])
    pygame.display.set_caption("贪吃蛇")
    # 3.4 初始化变量
    # 3.4.1 初始化贪吃蛇的起始位置，以（100，100）为标准
    snakePosition = [100,100]
    # 3.4.2 初始化贪吃蛇的长度，列表中有几个元素代表有几段身体
    snakeBody = [[100,100],[80,100],[60,100]]
    # 3.4.3 初始化目标方块的位置
    targetPosition = [300,300]
    # 3.4.4 目标方块的标记，判断是否吃掉了目标方块，1就是没有吃掉，0就是吃掉了（随意定）
    targetflag = 1
    # 3.4.5 初始化方向
    direction = "right"
    # 定义一个方向变量（认为控制 按照按键）
    changeDirection = direction

    while True:
        for event in pygame.event.get(): # 从队列当中去获取事件
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
        # 3.6 确定方向
        if changeDirection == "left" and not direction == "right":
            direction = changeDirection
        if changeDirection == "right" and not direction == "left":
            direction = changeDirection
        if changeDirection == "up" and not direction == "dpwn":
            direction = changeDirection
        if changeDirection == "down" and not direction == "up":
            direction = changeDirection

        # 3.7 根据方向移动蛇头
        if direction == "right":
            snakePosition[0] += 20
        if direction == "left":
            snakePosition[0] -= 20
        if direction == "up":
            snakePosition[1] -= 20
        if direction == "down":
            snakePosition[1] += 20

        # 3.8 增加蛇的长度
        snakeBody.insert(0,list(snakePosition))

        # 如果贪吃蛇的位置和目标方块的位置重合，意味着蛇吃掉它了，目标方块为0
        if snakePosition[0] == targetPosition[0] and snakePosition[1] == targetPosition[1]:
            targetflag = 0
        else:
            snakeBody.pop()
        if targetflag == 0:
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)
            targetPosition = [int(x*20),int(y*20)]

        # 填充背景颜色
        playSurface.fill(blackcolor)

        # 画蛇
        for position in snakeBody:
            # 蛇
            pygame.draw.rect(playSurface,whitecolor,Rect(position[0],position[1],20,20))
            # 目标方块
            pygame.draw.rect(playSurface,redcolor,Rect(targetPosition[0],targetPosition[1],20,20))
        # 更新显示
        pygame.display.flip()
        # 判断是否游戏结束
        if snakePosition[0] > 620 or snakePosition[0] < 0:
            gameOver()
        elif snakePosition[1] > 460 or snakePosition[1] < 0:
            gameOver()
        # 控制游戏速度
        fpsClock.tick(5)

# 启动入口函数
if __name__ == "__main__":
    main()






















