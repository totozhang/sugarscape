import pygame

LIVE_AGENT_COLOR = (0, 0, 128)
DEAD_AGENT_COLOR = (66, 204, 133)
COLOR_SUGAR_LVL0 = (250, 226, 209)
COLOR_SUGAR_LVL1 = (248, 195, 163)
COLOR_SUGAR_LVL2 = (242, 167, 118)
COLOR_SUGAR_LVL3 = (239, 137, 75)
COLOR_SUGAR_LVL4 = (238, 107, 39)


def drawSugar(screen, position, color):
    rectangular = pygame.Rect(10 * position[0], 10 * position[1], 10, 10)
    pygame.draw.rect(screen, color, rectangular)


def drawAgent(screen, position, color):
    rectangular = pygame.Rect(10 * position[0] + 3, 10 * position[1] + 3, 4, 4)
    pygame.draw.rect(screen, color, rectangular)


def drawSugarScapeMap(screen, sugarscape):
    for position in sugarscape.sugarDictCurrent.keys():
        if (sugarscape.sugarDictCurrent[position] == 0):
            color = COLOR_SUGAR_LVL0
        elif (sugarscape.sugarDictCurrent[position] == 1):
            color = COLOR_SUGAR_LVL1
        elif (sugarscape.sugarDictCurrent[position] == 2):
            color = COLOR_SUGAR_LVL2
        elif (sugarscape.sugarDictCurrent[position] == 3):
            color = COLOR_SUGAR_LVL3
        else:
            color = COLOR_SUGAR_LVL4

        drawSugar(screen, position, color)


def drawAgents(screen, agents):
    for agent in agents:
        if agent.isDead():
            drawAgent(screen, (agent.posx, agent.posy), DEAD_AGENT_COLOR)
        else:
            drawAgent(screen, (agent.posx, agent.posy), LIVE_AGENT_COLOR)
