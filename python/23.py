import pygame,sys,random
pygame.init()
pygame.display.set_caption("贪吃蛇")  # 设置游戏名称
screen = pygame.display.set_mode([500,500])



x = 250  # 变量定义在循环前，才能在循环过程中不限制变量的值
y = 250
speed = 10
up = 273
Dowm = 274
Left = 276
Right = 275
pygame.time.delay(20)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 用键盘控制蛇的移动
        if event.type == pygame.KEYDOWN:
            if event.key == up:
                if y > 0:
                    y -= speed
                elif y <= 0:
                    y += speed
            elif event.key == Dowm:
                if y < screen.get_height():
                    y += speed
                elif y >= screen.get_height()-4:
                    y -= speed
            elif event.key == Right:
                if x < screen.get_width()-10:
                    x += speed
                elif x >= screen.get_width()-10:
                    x -= speed
            elif event.key == Left:
                if x > 0:
                    x -= speed
                elif x <= 0:
                    x += speed
            screen.fill([127, 255, 212])
            snake = pygame.draw.rect(screen, [255,255,0], (x, y, 10, 4))

            # 生成食物
            for i in range ()
            a = [200,400,50]
            b = [300,100,500]
            len = random.randint(10, 100)
            food = pygame.draw.rect(screen, [160, 32, 240], (a[i], b[i], len, 4))

        pygame.display.flip()

