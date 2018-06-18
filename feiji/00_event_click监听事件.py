#-*- coding=utf-8 -*-
import pygame

clock = pygame.time.Clock()
# 游戏循环
while True:
    # 设置屏幕刷新帧率
    clock.tick(60)
    # 事件监听
    for event in pygame.event.get():
        # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏...")
            pygame.quit()
            # 直接退出系统
            exit()