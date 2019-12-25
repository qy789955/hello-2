import pygame,sys
pygame.init   # 初始化surface
screen = pygame.display.set_mode([1000,600])
img = pygame.image.load("kuankuan_gaitubao_75x100.png") # 只是把小球下载下来

# 图片步进
x = 100
y = 100
x_bujin = 2
y_bujin = 1

# surface步进
a = 22
b = 55
c = 88


# 定义反弹的算法
def fantan():
    global x,y,a,b,c,x_bujin,y_bujin
    if x >= screen.get_width()-75 or x <= 0:
        x_bujin = - (x_bujin)
    if y >= screen.get_height()-100 or y <= 0:
        y_bujin = - (y_bujin)
    x += x_bujin
    y += y_bujin
    screen.fill([a, b, c])
    screen.blit(img,[x,y])  # 小球显示到screen上

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    fantan()
    pygame.display.flip()



