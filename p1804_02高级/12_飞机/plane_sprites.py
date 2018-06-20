#-*-coding:utf-8-*-
import pygame, time
class GameSprite(pygame.sprite.Sprite):
    """游戏精灵基类"""
    def __init__(self,image_name,speed=1):
        # 调用父类的初始化方法
        super().__init__()
        # 加载图像
        self.image = pygame.image.load(image_name)
        # 设置尺寸
        self.rect = self.image.get_rect()
        # 记录速度
        self.speed = speed
    def update(self, *args):
       # 默认在垂直方向移动
        self.rect.y += self.speed
