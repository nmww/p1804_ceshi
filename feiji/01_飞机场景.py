# -*- coding=utf-8 -*-
import pygame
import time

def main():
    #1.窗口
    screen = pygame.display.set_mode((480,600),0,32)
    #2.背景
    background = pygame.image.load('./images/background.png')
    #3.英雄
    hero = pygame.image.load('./images/hero1.png')

    while True:
        screen.blit(background,(0,0))
        screen.blit(hero,(210,500))
        pygame.display.update()
        time.sleep(0.01)

if __name__ == '__main__':
    main()
