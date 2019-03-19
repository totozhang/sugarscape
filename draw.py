import pygame
from sugarscape import SugarScape
from agent import Agent


def drawRect(screen, position, type, color=(60, 60, 60)):
    if (type == "sugar"):
        rectangular = pygame.Rect(10 * position[0], 10 * position[1], 10, 10)
        pygame.draw.rect(screen, color, rectangular)
    if (type == "agent"):
        rectangular = pygame.Rect(10 * position[0] + 3, 10 * position[1] + 3, 4, 4)
        pygame.draw.rect(screen, color, rectangular)


def drawSugarScapeMap(screen, sugarscape):
    for position in sugarscape.sugarDictCurrent.keys():
        if (sugarscape.sugarDictCurrent[position] == 0):
            color = (250, 226, 209)
        elif (sugarscape.sugarDictCurrent[position] == 1):
            color = (248, 195, 163)
        elif (sugarscape.sugarDictCurrent[position] == 2):
            color = (242, 167, 118)
        elif (sugarscape.sugarDictCurrent[position] == 3):
            color = (239, 137, 75)
        else:
            color = (238, 107, 39)

        drawRect(screen, position, "sugar", color)


def drawAgents(screen, agents):
    for agent in agents:
        drawRect(screen, (agent.posx, agent.posy), "agent")
