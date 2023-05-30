import pygame
from pygame.locals import *

# 初始化游戏
pygame.init()

# 创建窗口
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Phigros")

# 定义角色初始位置
x = 400
y = 300

# 游戏主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                y -= 10
            elif event.key == K_DOWN:
                y += 10
            elif event.key == K_LEFT:
                x -= 10
            elif event.key == K_RIGHT:
                x += 10

    # 更新画面
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 20)
    pygame.display.flip()

# 退出游戏
pygame.quit()
