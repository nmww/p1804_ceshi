#-*- coding=utf-8 -*-
import pygame
import time

def main():
    #1.窗口
    screen = pygame.display.set_mode((480,600),0,32)
    #2.背景
    background = pygame.image.load('./images/background.png')
    #3.英雄
    hero = pygame.image.load('./images/hero1.png')

    # 4. 定义英雄的初始位置
    hero_rect = pygame.Rect(150, 500, 102, 126)
    # 4.1. 创建游戏时钟对象
    clock = pygame.time.Clock()
    while True:
        screen.blit(background,(0,0))
        screen.blit(hero,hero_rect)
        pygame.display.update()
        #time.sleep(0.01)
        # 设置屏幕刷新帧率
        clock.tick(60)
        hero_rect.y -= 1 #move hero y
        if hero_rect.y <= 0:
            hero_rect.y = 500

if __name__ == '__main__':
    main()
