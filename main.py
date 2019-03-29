import sys
import pygame
import draw
import proc
from agent import Agent
from setting import Setting
from sugarscape import SugarScape


def main():
    setting = Setting()
    pygame.init()
    screen = pygame.display.set_mode((setting.ScreenWidth, setting.ScreenHeigth))
    pygame.display.set_caption(setting.Application)

    fpsclock = pygame.time.Clock()
    pause = True

    sugarscape = SugarScape("map/map.data", setting.InitSugarRecoveryRate)
    agents = []
    for index in range(setting.InitMaxOfPopulation):
        id = "{:0>3d}".format(index)
        agents.append(Agent(id, sugarscape, setting))

    draw.drawScreenBackground(screen)
    draw.drawCopyright(screen)
    draw.drawRoundNumber(screen, setting.Round)
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
            print("Round:" + str(setting.Round))
            draw.drawScreenBackground(screen)
            draw.drawCopyright(screen)
            draw.drawRoundNumber(screen, setting.Round)
            proc.updateAgents(agents)
            proc.updateSugarScape(sugarscape)
            draw.drawSugarScapeMap(screen, sugarscape)
            draw.drawAgents(screen, agents)
            fpsclock.tick(setting.FPS)
            setting.Round += 1
            pygame.display.flip()

        if (setting.Round % 10 == 0 and setting.Round >= 10) or (setting.Round == 1):
            proc.plotWeath(agents, setting.Application)


if __name__ == "__main__":
    main()
