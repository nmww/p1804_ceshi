#-*- coding=utf-8 -*-
import pygame
import time

class HeroPlane(object):
    """英雄的创建和展示类"""
    def __init__(self, arg):
        super(HeroPlane, self).__init__()
        self.screen = arg
        self.x = 150
        self.y = 500
         #3.英雄
        self.image = pygame.image.load('./images/hero1.png')
        # 4. 定义英雄的初始位置
        self.hero_rect = pygame.Rect(self.x, self.y, 102, 126)
        self.bullet_list = [] #保持子弹引用
    def display(self):
        self.screen.blit(self.image,self.hero_rect)
        if len(self.bullet_list) > 0:
           for bullet in self.bullet_list:
                bullet.display()
                bullet.move()
    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.hero_rect.x, self.hero_rect.y))
        
class EnemyPlane(object):
    """敌人飞机 创建和展示类"""
    def __init__(self, arg):
        super(EnemyPlane, self).__init__()
        self.screen = arg
        self.x = 0
        self.y = 0 
         #3.英雄
        self.image = pygame.image.load('./images/enemy0.png')
        # 4. 定义英雄的初始位置
        self.enemy_rect = pygame.Rect(self.x, self.y, 102, 126)
        # self.bullet_list = [] #保持子弹引用
    def display(self):
        self.screen.blit(self.image,self.enemy_rect)
        # if len(self.bullet_list) > 0:
        #    for bullet in self.bullet_list:
        #         bullet.display()
        #         bullet.move()
    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.enemy_rect.x, self.enemy_rect.y))
        

class Bullet(object):
    """docstring for Bullet"""
    def __init__(self, arg ,x ,y):
        super(Bullet, self).__init__()
        self.screen = arg
        self.x = x+40
        self.y = y+20
         #3.英雄
        self.image = pygame.image.load('./images/bullet.png')
    def display(self):
        self.screen.blit(self.image,(self.x, self.y))
    def move(self):
        self.y -= 4
        
def key_control(hero):
    '''键盘的监听控制方法'''
    move_x, move_y = 0, 0
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
            elif event.key == pygame.K_SPACE:
                hero.fire()
        elif event.type == pygame.KEYUP:
            #如果用户放开了键盘，图就不要动了
            move_x = 0
            move_y = 0

        #计算出新的坐标
        hero.hero_rect.x += move_x
        hero.hero_rect.y += move_y

def main():# 主方法 调用 类和方法
    #1.窗口
    screen = pygame.display.set_mode((480,600),0,32)
    #2.背景
    background = pygame.image.load('./images/background.png')
    #3.英雄
    hero = HeroPlane(screen)
    # 4.1. 创建游戏时钟对象
    clock = pygame.time.Clock()

    # 5创建一个敌人飞机
    enemy = EnemyPlane(screen)

    while True:
        screen.blit(background,(0,0))
        hero.display()
        enemy.display()
        # 设置屏幕刷新帧率
        clock.tick(60)
        if hero.hero_rect.y <= 0:
            hero.hero_rect.y = 500
        key_control(hero)
        pygame.display.update()
   
if __name__ == '__main__':
    main()
