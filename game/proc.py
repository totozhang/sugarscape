import random


def updateAgents(agents):
    random.shuffle(agents)

    for agent in agents:
        print(agent)
        position = agent.searchSugar()
        agent.moveTo(position)
        agent.eatSugar()
        agent.digestSugar()
        # if agent.isDead():
        #    agents.remove(agent)


def updateSugarScape(sugarscape):
    sugarscape.recover()
