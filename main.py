import sys

import pygame

import draw
from agent import Agent
from sugarscape import SugarScape
from util import Util
from util import updateAgents
from util import updateSugarScape


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Sugarscape")

    util = Util()
    fpsclock = pygame.time.Clock()
    pause = True

    sugarscape = SugarScape("map/map.data", util.InitSugarRecoveryRate)
    agents = []
    for index in range(util.InitMaxOfPopulation):
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
            print("Round:" + str(util.Round))
            updateAgents(agents)
            updateSugarScape(sugarscape)
            draw.drawSugarScapeMap(screen, sugarscape)
            draw.drawAgents(screen, agents)
            fpsclock.tick(util.FPS)
            util.Round += 1
            pygame.display.flip()


if __name__ == "__main__":
    main()
