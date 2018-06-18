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

    move_x, move_y = 0, 0
    while True:
        screen.blit(background,(0,0))
        screen.blit(hero,hero_rect)
        
        #time.sleep(0.01)
        # 设置屏幕刷新帧率
        clock.tick(60)
        # hero_rect.y -= 1 #move hero y
        if hero_rect.y <= 0:
            hero_rect.y = 500

        # =====事件监听
        for event in pygame.event.get():
            # 判断用户是否点击了关闭按钮
            if event.type == pygame.QUIT:
                print("退出游戏...")
                pygame.quit()
                # 直接退出系统
                exit()
            elif event.type == pygame.KEYDOWN:
                #键盘有按下？
                if event.key == pygame.K_LEFT:
                    #按下的是左方向键的话，把x坐标减一
                    move_x = -2
                elif event.key == pygame.K_RIGHT:
                    #右方向键则加一
                    move_x = 2
                elif event.key == pygame.K_UP:
                    #类似了
                    move_y = -2
                elif event.key == pygame.K_DOWN:
                    move_y = 2
            elif event.type == pygame.KEYUP:
                #如果用户放开了键盘，图就不要动了
                move_x = 0
                move_y = 0

            #计算出新的坐标
            hero_rect.x += move_x
            hero_rect.y += move_y
        pygame.display.update()
   
if __name__ == '__main__':
    main()
