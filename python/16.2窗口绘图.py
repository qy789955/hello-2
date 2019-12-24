import pygame,sys
pygame.init                     # 导入以后，先进行初始化，清除内存
screen = pygame.display.set_mode([280,280])   # 传参数时候不用加入参数名称，区别于介绍时候size=（0，0);调用方法后赋值变量，变量名不要是关键字名
                                     # 报错：2-item sequency not init. 此时需要变为数列
screen.fill([22,55,88])
pygame.draw.circle(screen,[200,1,2], [100,100], 100,0)   # RGB颜色对照表，要求颜色表示为【11，22，22】数组，三个元素

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()             # 写全称，只有在已经赋值变量时候才是新名称


