import sys
import pygame


def main():
    # 初始化游戏屏幕
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Sugar Scape")

    # 初始化Sugar Scape地图
    initSugarScapeMap()

    # 初始化200个糖人
    initAgents()

    # 开始游戏的主循环
    while True:

        # 监视定时器事件
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()
            if ev.type == pygame.KEYDOWN:
                processAgents()
                processSugarScapeMap()

        # 绘制画面背景色，将上一次循环的画面刷新
        screen.fill((230, 230, 230))

        # 画地图
        drawSugarScapeMap()

        # 画200个Agents的状态
        drawAgents()

        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    main()
