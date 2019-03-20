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

    # 初始化Sugar Scape地图
    sugarscape = SugarScape("SugarScapeMap.data")

    # 初始化200个糖人
    agents = []
    for index in range(200):
        agents.append(Agent(sugarscape))

    # 开始游戏的主循环
    while True:
        # 事件处理
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()
            if ev.type == pygame.KEYDOWN:
                updateAgents(agents)
                updateSugarScape(sugarscape)

        # 画地图
        draw.drawSugarScapeMap(screen, sugarscape)

        # 画糖人
        draw.drawAgents(screen, agents)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


def updateAgents(agents):
    random.shuffle(agents)

    for agent in agents:
        position = agent.findSugar()
        agent.moveTo(position)
        agent.eatSugar()
        agent.digestSugar()

        if agent.isDead():
            agents.remove(agent)


def updateSugarScape(sugarscape):
    sugarscape.recover()


if __name__ == "__main__":
    main()
