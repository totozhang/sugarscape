import random
import operator


class Agent():

    def __init__(self, identification, sugarscape):
        self.identification = identification
        self.posx = random.randint(0, 49)
        self.posy = random.randint(0, 49)
        self.energy = random.randint(15, 30)
        self.vision = random.randint(1, 6)
        self.metabolism = random.randint(1, 2)
        self.sugarscape = sugarscape

    def __str__(self):
        return "%s, (%s, %s), %s, %s, %s" % (
            self.identification, self.posx, self.posy, self.energy, self.vision, self.metabolism)

    # 获取自身可视范围内最优位置(含糖量最高且距离最近)
    def findSugar(self):
        if self.isDead():
            return

        bestposition = (0, 0)
        maxvalue = 0

        # 需要检索的位置列表
        searchlist = self.getSearchlist()

        for pos in searchlist:
            value = self.sugarscape.getSugarValue(pos)
            if value > maxvalue:
                maxvalue = value
                bestposition = pos
            if value == maxvalue:
                bestposition = self.nearWhichPosition(pos, bestposition)

        # 最后得到的bestposition就是自身的位置，则从searchlist中随机选择一个位置走一步
        if (operator.eq((self.posx, self.posy), bestposition)):
            bestposition = random.choice(searchlist)

        return bestposition

    # 从两点中获取距离自己位置距离近的点
    def nearWhichPosition(self, position1, position2):
        distance1 = self.sugarscape.distance((self.posx, self.posy), position1)
        distance2 = self.sugarscape.distance((self.posx, self.posy), position2)

        if distance1 < distance2:
            return position1
        elif distance1 > distance2:
            return position2
        else:
            return random.choice([position1, position2])

    # 糖人的可观测范围点的合法集合
    def getSearchlist(self):
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
