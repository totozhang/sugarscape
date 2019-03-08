import sys
import pygame


def main():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Sugar Scape")

    # 测试画一个矩形
    rectangular = pygame.Rect(0, 0, 10, 10)
    rectangular.x = 0
    rectangular.y = 0

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RIGHT:
                    rectangular.centerx += 10
                elif ev.key == pygame.K_LEFT:
                    rectangular.centerx -= 10
                if ev.key == pygame.K_UP:
                    rectangular.centery -= 10
                elif ev.key == pygame.K_DOWN:
                    rectangular.centery += 10

        # 绘制画面背景色，将上一次循环的画面刷新
        screen.fill((230, 230, 230))

        # 画矩形
        pygame.draw.rect(screen, (60, 60, 60), rectangular)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    main()
