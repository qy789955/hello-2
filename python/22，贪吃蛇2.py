import pygame,sys,random
pygame.init()
pygame.display.set_caption("贪吃蛇")  # 设置游戏名称
screen = pygame.display.set_mode([500,500])
screen.fill([127, 255, 212])

print(1231)
pygame.display.flip()

# 方向键对应的值
up = 273
Dowm = 274
Left = 276
Right = 275


while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == up:
                    print('上')
                    y_spead = -1
                    x_spead = 0
                elif event.key == Dowm:
                    print('下')
                    y_spead = 1
                    x_spead = 0
                elif event.key == Right:
                    print('右')
                    y_spead = 0
                    x_spead = 1
                elif event.key == Left:
                    print('左')
                    y_spead = 0
                    x_spead = -1