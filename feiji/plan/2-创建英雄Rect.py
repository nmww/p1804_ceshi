import pygame

pygame.init()

hero_rect =  pygame.Rect(100,500,120,120)
print("hero.x=%d,hero.y=%d"%(hero_rect.x,hero_rect.y))
print("width=%d,height=%d"%(hero_rect.width,hero_rect.height))
print(hero_rect.size)