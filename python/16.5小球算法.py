import pygame,sys
screen = pygame.display.set_mode([1000,600])
x = 100
y = 100
x_bujin = 2
y_bujin = 1
a = 22
b = 55
c = 88
def fantan():
    global x,y,x_bujin,y_bujin,a,b,c
    if x >= screen.get_width()-75 or x <= 0:
        x_bujin = - y_bujin
    if y >= screen.get_height()-100 or y <= 0:
        y_bujin = - y_bujin
    x += x_bujin
    y += y_bujin
    screen.fill([a,b,c])
    img = pygame.image.load("kuankuan_gaitubao_75x100.png")
    screen.blit(img, [x, y])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    fantan()
    pygame.display.flip()

