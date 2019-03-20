import sys
import pygame
import random
import draw
from sugarscape import SugarScape
from agent import Agent


def main():
    # 初始化游戏屏幕
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Sugar Scape")

    # 屏幕刷新率
    clock = pygame.time.Clock()

    # 初始化地图
    sugarscape = SugarScape("SugarScapeMap.data")

    # 初始化糖人
    agents = []
    for index in range(200):
        id = "{:0>2d}".format(index)
        agents.append(Agent(id, sugarscape))

    # 开始游戏的主循环
    while True:
        # 事件处理
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()

        updateAgents(agents)
        updateSugarScape(sugarscape)
        draw.drawSugarScapeMap(screen, sugarscape)
        draw.drawAgents(screen, agents)

        # 刷新屏幕
        pygame.display.flip()
        clock.tick(3)


def updateAgents(agents):
    # 随机调度糖人
    random.shuffle(agents)

    for agent in agents:
        position = agent.findSugar()
        agent.moveTo(position)
        agent.eatSugar()
        agent.digestSugar()
        print(agent)


def updateSugarScape(sugarscape):
    sugarscape.recover()


if __name__ == "__main__":
    main()
