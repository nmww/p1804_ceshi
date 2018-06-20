import pygame

pygame.init()

#创建窗口
screen = pygame.display.set_mode((480,700))
#创建图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
#pygame.display.update()

#创建飞机图像
bg = pygame.image.load("./images/hero.gif")
screen.blit(bg,(180,500))

clock = pygame.time.Clock()

pygame.display.update()

i = 0
while True:
	clock.tick(60)
	i+=1
	print(i)

pygame.quit()
