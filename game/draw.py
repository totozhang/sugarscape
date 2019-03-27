import pygame

LVL4_AGENT_COLOR = (231, 41, 47)
LVL3_AGENT_COLOR = (24, 154, 26)
LVL2_AGENT_COLOR = (11, 7, 183)
LVL1_AGENT_COLOR = (32, 42, 47)
LVL0_AGENT_COLOR = (141, 193, 147)
DEAD_AGENT_COLOR = (98, 119, 143)
COLOR_SUGAR_LVL0 = (250, 226, 209)
COLOR_SUGAR_LVL1 = (248, 195, 163)
COLOR_SUGAR_LVL2 = (242, 167, 118)
COLOR_SUGAR_LVL3 = (239, 137, 75)
COLOR_SUGAR_LVL4 = (238, 107, 39)
COLOR_SCREEN = (240, 240, 240)


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
            continue

        if agent.bornLevel == 4:
            drawAgent(screen, (agent.posx, agent.posy), LVL4_AGENT_COLOR)
        elif agent.bornLevel == 3:
            drawAgent(screen, (agent.posx, agent.posy), LVL3_AGENT_COLOR)
        elif agent.bornLevel == 2:
            drawAgent(screen, (agent.posx, agent.posy), LVL2_AGENT_COLOR)
        elif agent.bornLevel == 1:
            drawAgent(screen, (agent.posx, agent.posy), LVL1_AGENT_COLOR)
        else:
            drawAgent(screen, (agent.posx, agent.posy), LVL0_AGENT_COLOR)


def drawScreenBackground(screen):
    screen.fill(COLOR_SCREEN)


def drawCopyright(screen):
    fontObj = pygame.font.SysFont("Arial", 22)
    textSurfaceObj = fontObj.render("© toto.zhang@gmail.com", True, (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (305, 503)
    screen.blit(textSurfaceObj, textRectObj)


def drawRoundNumber(screen, round):
    fontObj = pygame.font.SysFont("Arial", 22)
    textSurfaceObj = fontObj.render("Round: " + str(round), True, (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (10, 503)
    screen.blit(textSurfaceObj, textRectObj)
