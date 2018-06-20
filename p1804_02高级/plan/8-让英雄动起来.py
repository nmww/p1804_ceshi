import pygame

pygame.init()

#创建窗口
screen = pygame.display.set_mode((480,700))
#创建图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
#pygame.display.update()

#创建英雄图像
hero = pygame.image.load("./images/hero.gif")
screen.blit(hero,(180,500))

clock = pygame.time.Clock()

#创建英雄的rect
hero_rect = pygame.Rect(180,500,200,200)




while True:
	clock.tick(60)
	hero_rect.y -=10
	#覆盖背景
	screen.blit(bg,(0,0))
	screen.blit(hero,hero_rect)

	pygame.display.update()



pygame.quit()
