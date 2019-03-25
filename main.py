import random
import sys
import pygame
import draw
from agent import Agent
from util import Util
from sugarscape import SugarScape


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Sugarscape")

    util = Util()
    agents_moving_round = 0
    fpsclock = pygame.time.Clock()
    pause = True

    sugarscape = SugarScape("map/map.data", util.InitSugarRecoveryRate)
    agents = []
    for index in range(util.MaxOfPopulation):
        id = "{:0>3d}".format(index)
        agents.append(Agent(id, sugarscape, util))

    draw.drawSugarScapeMap(screen, sugarscape)
    draw.drawAgents(screen, agents)
    pygame.display.flip()

    while True:

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()
            if ev.type == pygame.KEYDOWN:
                pause = not pause

        if not pause:
            print("Round:" + str(agents_moving_round))
            updateAgents(agents)
            updateSugarScape(sugarscape)
            draw.drawSugarScapeMap(screen, sugarscape)
            draw.drawAgents(screen, agents)
            pygame.display.flip()
            fpsclock.tick(util.FPS)
            agents_moving_round += 1


def updateAgents(agents):
    random.shuffle(agents)

    for agent in agents:
        print(agent)
        position = agent.searchSugar()
        agent.moveTo(position)
        agent.eatSugar()
        agent.digestSugar()


def updateSugarScape(sugarscape):
    sugarscape.recover()


if __name__ == "__main__":
    main()
