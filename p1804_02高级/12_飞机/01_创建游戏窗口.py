#-*- coding=utf-8 -*-
import pygame

def main():

    # 创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)

    # 把本地文件夹的图片，获取到 代码中
    background = pygame.image.load('./images/background.png')

    # 把图片 加载 到 游戏窗口上
    screen.blit(background, (0,0))

    # 刷新显示
    pygame.display.update()
    while True:
        pass
if __name__ == '__main__':
    main()

    '''
    # 1.x 2.y 3.宽度 4.高度
    feiji = pygame.Rect(100,500,50,50)
    print('x = ',feiji.x)
    print('y = ',feiji.y)
    print('width = ', feiji.width)
    print('height = ', feiji.height)
    screen = pygame.display.set_mode((480, 700))
    '''



