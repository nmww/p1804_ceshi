import pygame

pygame.init()

#创建窗口
screen = pygame.display.set_mode((480,700))
#创建图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
pygame.display.update()



while True:
	pass

pygame.quit()
