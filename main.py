import sys
import pygame
import random
import draw
from sugarscape import SugarScape
from agent import Agent
from configparser import ConfigParser


def main():
    config = ConfigParser()
    config.read("conf/sugarscape.config")

    # 初始化游戏屏幕
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Sugar Scape")

    # 屏幕刷新率和暂停开关
    round = 0
    clock = pygame.time.Clock()
    pause = True

    # 初始化地图
    sugarscape = SugarScape("map/map.data", config)

    # 初始化糖人
    agents = []
    for index in range(config.getint("agent", "MaximumOfPopulation")):
        id = "{:0>3d}".format(index)
        agents.append(Agent(id, sugarscape, config))

    # 开始游戏的主循环
    while True:
        # 事件处理
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()
            if ev.type == pygame.KEYDOWN:
                pause = not pause

        # 开始处理
        if not pause:
            print("Round:" + str(round))
            updateAgents(agents)
            updateSugarScape(sugarscape)
            draw.drawSugarScapeMap(screen, sugarscape)
            draw.drawAgents(screen, agents)

            pygame.display.flip()
            clock.tick(config.getint("refresh", "speed"))
            round += 1


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
