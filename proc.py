import random
from matplotlib import pyplot


def updateAgents(agents):
    random.shuffle(agents)

    for agent in agents:
        print(agent)
        position = agent.searchSugar()
        agent.moveTo(position)
        agent.eatSugar()
        agent.digestSugar()

        if agent.isDead():
            agents.remove(agent)


def updateSugarScape(sugarscape):
    sugarscape.recover()


def plotWeath(agents, figureName):
    wealths = []
    for agent in agents:
        wealths.append(agent.energy)

    pyplot.figure("Sugarscape")
    pyplot.ion()
    pyplot.cla()
    pyplot.hist(wealths, 10)
    pyplot.xlabel('Interval')
    pyplot.ylabel('Population')
    pyplot.title('Wealth distribution')
    pyplot.grid(True)
    pyplot.pause(0.3)
