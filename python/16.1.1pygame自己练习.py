# pygame是一款可以用来开发电子游戏的，它可以跨多个平台，基于SDL基础（也是可以跨多个平台，只是由c语言编程），不受限于c语言和汇编语言，高级语言如python也可以提供它所有的资源结构
import pygame,sys
pygame.init                                 # 对导入的pygame模块进行初始化，清理一下之前的内存卡
screen = pygame.display.set_mode([680,480]) # 导入一个pygame模块
# argument 1 must be 2-item sequence, not int 此时可以将（）中内容改成列表
# 如果点击鼠标，屏幕没有响应，说明没有实时监测屏幕的事件，所以首先应该从列表中获取事件
while True:
    for event in pygame.event.get():            # 循环的意思是实时监测鼠标的事件。获取所有事件，所有事件应该是一个列表，用for循环打印出可以知道内容
        if event.type == pygame.QUIT:                   # 判断事件类型是我们想操作的内容，就实现关闭功能
            pygame.quit()                       # video system not initialized 意思是系统并没有被关闭，此时需要调用我们的sys包，用sys.exit完全退出系统
            sys.exit()

