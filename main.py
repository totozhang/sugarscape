import random
import sys
from configparser import ConfigParser

import pygame

import draw
from agent import Agent
from sugarscape import SugarScape


def main():
    config = ConfigParser()
    config.read("conf/sugarscape.config")

    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Sugar Scape")

    round = 0
    clock = pygame.time.Clock()
    pause = True

    sugarscape = SugarScape("map/map.data", config)

    agents = []
    for index in range(config.getint("agent", "MaximumOfPopulation")):
        id = "{:0>3d}".format(index)
        agents.append(Agent(id, sugarscape, config))

    while True:

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()
            if ev.type == pygame.KEYDOWN:
                pause = not pause

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
    random.shuffle(agents)

    for agent in agents:
        print(agent)
        position = agent.findSugar()
        agent.moveTo(position)
        agent.eatSugar()
        agent.digestSugar()


def updateSugarScape(sugarscape):
    sugarscape.recover()


if __name__ == "__main__":
    main()
