# -*- coding: utf-8 -*-
"""
制作游戏窗口
窗口绘图
加载图像
"""
import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')
    # 窗口背景色
    screen.fill((242, 242, 242))
    # 绘制圆（参数：屏幕，颜色，圆心位置，半径，0表示填充圆）
    pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
