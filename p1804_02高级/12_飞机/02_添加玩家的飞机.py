#-*- coding=utf-8 -*-
import time
import pygame

def main():
    # 创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)

    # 把本地文件夹的图片，获取到 代码中
    background = pygame.image.load('./images/background.png')
    hero_plane = pygame.image.load("./images/hero1.png")#飞机图片

    # 定义好的位置，和尺寸
    rect = pygame.Rect((400-100)/2,350, 100,124)

    while True:
        # 把图片 加载 到 游戏窗口上
        screen.blit(background, (0,0))
        screen.blit(hero_plane, rect)#设置飞机

        # 移动
        rect.x += 1

        # 刷新显示
        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()


