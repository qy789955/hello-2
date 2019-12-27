import pygame,sys,random   # 调用random时候需要首先导入
pygame.init   # 初始化surface
screen = pygame.display.set_mode([1000,1000])


# 设置一个名为Dogs的动画精灵类
class Dogs (pygame.sprite.Sprite):  # pygame.sprite.Sprite为动画精灵的父类，基类
    def __init__(self, file_name, location,speed):   # 属性内的参数可以自己随意设置
        pygame.sprite.Sprite.__init__(self)    # 父类的参数
        self.img = pygame.image.load(file_name)
        self.r = self.img.get_rect()
        self.r.left, self.r.top = location
        self.speed = speed

    # 定义动画精灵移动的方法
    def move(self):
        self.r = self.r.move(self.speed)
        if self.r.top < 0 or self.r.bottom > screen.get_height():
            self.speed[1] = -self.speed[1]
        if self.r.left > 0 or self.r.right > screen.get_width():
            self.speed[0] = -self.speed[0]



#  设置循环，创建多个位置不同的对象
sprits = pygame.sprite.Group()  # 动画精灵中用于显示所有对象的包袋，返回一个group
for i in range(0,3):
    for j in range(0,3):
        dog = Dogs("kuankuan_gaitubao_75x100.png", [100+i*100 , 100+j*100], [random.randint(-8,9),random.randint(-2,8)]) # 添加一个新位置的对象,生成关于速度的随机数，让每个小球随机移动
        sprits.add(dog)  # 新的对象加入sprits包中

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 设置循环，显示出每次创建对象的情况
    screen.fill([22, 55, 88])  # 每次运行前将屏幕重新显示一次，是运动的原理
    for dog in sprits:
        dog.move()
        screen.blit(dog.img, dog.r)

    pygame.display.flip() # 对于surface的更新要放在最后，才能将所有改动显示出来

