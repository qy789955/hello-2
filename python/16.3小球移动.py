import pygame,sys
pygame.init
screen = pygame.display.set_mode([1000,1000])
screen.fill([22,55,88])    # surface颜色填充
img = pygame.image.load("kuankuan_gaitubao_75x100.png")  # 上传图片

# 图片位置步进
x = 100
y = 100
x_bujin = 2
y_bujin = 1

# surface步进
a = 22
b = 55
c = 88
bujin = 30

# 定义移动函数，surface移动和图片同步移动
def move():
    global x,y,a,b,c  # 申明x，y为全局变量，才可以应用上面的赋值
    x += x_bujin
    y += x_bujin
    a += bujin  # RGB参数范围限制
    b += bujin
    c += bujin
    if a > 255:
        a = 0
    if b > 255:
        b = 0
    if c > 255:
        c = 0
    screen.fill([a, b, c])  # surface，视觉上认为在移动
    screen.blit(img,[x,y])  # 上传后的图片传送到surface上

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    move()
    pygame.display.flip()  # 写全称，只有在已经赋值变量时候才是新名称
