#-*- coding=utf-8 -*-
import pygame

def main():
    # 创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)

    # 把本地文件夹的图片，获取到 代码中
    background = pygame.image.load('./images/background.png')
    hero_plane = pygame.image.load("./images/hero1.png")#飞机图片

    # 定义好的位置，和尺寸
    rect = pygame.Rect((400-100)/2,350, 100,124)
    clock = pygame.time.Clock() #获得游戏时钟 控制器

    while True:
        # 把图片 加载 到 游戏窗口上
        screen.blit(background, (0,0))
        screen.blit(hero_plane, rect)#设置飞机

        # 移动
        rect.x += 1
        if rect.x > 400:
            rect.x = 0

        # 游戏事件的监听 控制
        for event in pygame.event.get():
            print('event.type = ', event.type)
            print('event = ', event)
            if event.type == pygame.QUIT:#退出游戏
                print('游戏退出')
                pygame.quit()
                exit() #退出程序

        # 刷新显示
        pygame.display.update()
        clock.tick(60) # 让游戏时钟，1/60秒运行一次


if __name__ == '__main__':
    main()


