import pygame,sys,random
pygame.init()
pygame.display.set_caption("贪吃蛇")  # 设置游戏名称
screen = pygame.display.set_mode([500,500])
food = pygame.draw.rect(screen, [160, 32, 240],(random.randint(20, 400), random.randint(20, 400), random.randint(5, 10), 4))


x = 250   # 若想x，y的值不一直控制snake，需要放在snake所在的循环外
y = 250
speed = 10
up = 273
Dowm = 274
Left = 276
Right = 275

# 用键盘控制蛇的移动
while True:
    pygame.time.delay(20)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



screen.fill([127, 255, 212])


            a = random.randint(20, 400)
            b = random.randint(20, 400)
            len = random.randint(10, 100)
            food = pygame.draw.rect(screen, [160, 32, 240], (a, b, len, 4))

pygame.display.flip()


