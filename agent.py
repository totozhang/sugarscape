import operator
import random


class Agent():

    def __init__(self, identification, sugarscape, destiny):

        self.identification = identification
        self.sugarscape = sugarscape
        self.posx, self.posy = destiny.getBornPostion()
        self.energy = destiny.getBornSugar()
        self.vision = destiny.getBornVision()
        self.metabolism = destiny.getBornMetabolism()
        self.destiny = destiny

    def __str__(self):
        return "%s,(%s,%s),%s,%s,%s" % (
            self.identification, self.posx, self.posy, self.energy, self.vision, self.metabolism)

    # Search the best position on the sugarscape
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

        # 最后得到的bestposition就是自身的位置，则从searchlist中随机选择一个位置走一步
        if (operator.eq((self.posx, self.posy), bestposition)):
            bestposition = random.choice(positionsInVision)

        return bestposition

    # 糖人的可观测范围点的合法集合
    def getValidSearchPositions(self):
        list = []

        # 水平方向
        for x in range(self.posx - self.vision, self.posx + self.vision + 1):
            if self.sugarscape.isValidPosition((x, self.posy)):
                list.append((x, self.posy))
        # 垂直方向
        for y in range(self.posy - self.vision, self.posy + self.vision + 1):
            if self.sugarscape.isValidPosition((self.posx, y)):
                list.append((self.posx, y))
        return list

    # 糖人移动到参数给定点
    def moveTo(self, point):
        if self.isDead():
            return

        self.posx = point[0]
        self.posy = point[1]

    # 糖人吃糖
    def eatSugar(self):
        if self.isDead():
            return

        self.energy += self.sugarscape.getSugarValue((self.posx, self.posy))
        self.sugarscape.isEaten((self.posx, self.posy))

    # 判断糖人是否死亡
    def isDead(self):
        return self.energy < 0

    # 消耗体内的糖
    def digestSugar(self):
        if self.isDead():
            return

        self.energy -= self.metabolism
