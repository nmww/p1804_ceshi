#-*- coding=utf-8 -*-
import pygame
# 3. 创建游戏时钟对象
clock = pygame.time.Clock()
i = 0
# 游戏循环
while True:
    # 设置屏幕刷新帧率
    clock.tick(60)
    print(i)
    i += 1
 