import operator
import random


class Agent():

    def __init__(self, identification, sugarscape, util):

        self.identification = identification
        self.sugarscape = sugarscape
        self.posx, self.posy = util.getBornPostion()
        self.energy = util.getBornSugar()
        self.vision = util.getBornVision()
        self.metabolism = util.getBornMetabolism()
        self.destiny = util

    def __str__(self):
        return "%s,(%s,%s),%s,%s,%s" % (
            self.identification, self.posx, self.posy, self.energy, self.vision, self.metabolism)

    def searchSugar(self):
        if self.isDead():
            return

        bestposition = (0, 0)
        maxvalue = 0

        # The positions in vision
        positionsInVision = self.getValidSearchPositions()

        for position in positionsInVision:
            value = self.sugarscape.getSugarValue(position)
            if value > maxvalue:
                maxvalue = value
                bestposition = position
            if value == maxvalue:
                bestposition = self.sugarscape.getNearerPostion(self.destiny, (self.posx, self.posy), position,
                                                                bestposition)

        # If the best position is the current position, select a random position in list positionsInVision
        if (operator.eq((self.posx, self.posy), bestposition)):
            bestposition = random.choice(positionsInVision)

        return bestposition

    def getValidSearchPositions(self):
        list = []

        for x in range(self.posx - self.vision, self.posx + self.vision + 1):
            if self.sugarscape.isValidPosition((x, self.posy)):
                list.append((x, self.posy))

        for y in range(self.posy - self.vision, self.posy + self.vision + 1):
            if self.sugarscape.isValidPosition((self.posx, y)):
                list.append((self.posx, y))
        return list

    def moveTo(self, position):
        if self.isDead():
            return

        self.posx = position[0]
        self.posy = position[1]

    def eatSugar(self):
        if self.isDead():
            return

        self.energy += self.sugarscape.getSugarValue((self.posx, self.posy))
        self.sugarscape.isEaten((self.posx, self.posy))

    def isDead(self):
        return self.energy < 0

    def digestSugar(self):
        if self.isDead():
            return

        self.energy -= self.metabolism
