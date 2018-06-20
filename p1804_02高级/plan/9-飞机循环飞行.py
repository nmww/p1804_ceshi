
import pygame
from PlanSprite import *

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


#创建时钟对象
clock = pygame.time.Clock()

#创建英雄的rect
hero_rect = pygame.Rect(180,500,200,200)

#创建敌机精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png",3)
enemy1.rect.x = 100
#创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)

while True:
	clock.tick(60)
	hero_rect.y -=3
	#覆盖背景
	screen.blit(bg,(0,0))
	screen.blit(hero,hero_rect)

	# if hero_rect.y + hero_rect.height <= 0:
	# 	hero_rect.y = 700

	if hero_rect.bottom <= 0:
		hero_rect.y = 700

	#监听退出
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	#更新		
	enemy_group.update()
	enemy_group.draw(screen)			

	pygame.display.update()



pygame.quit()
