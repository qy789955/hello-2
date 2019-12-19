import pygame,sys # pygame相当于一个字典
pygame.init
pygame.display.set_mode([680,480])  # 创建了一个黑色的屏幕，无法关闭
while True:
    for event in pygame.event.get():  # 点鼠标发现关不了窗口，就可以将关这个事件显示出来
        if event.type == pygame.QUIT:  # quit是常量，常量用大写字母表示
            pygame.quit()
            sys.exit()




