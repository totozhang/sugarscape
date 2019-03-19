import random
from sugarscape import SugarScape


class Agent():

    def __init__(self, sugarscape):

        # 出生点位, 即使重合也不影响后续的处理
        self.posx = random.randint(0, 49)
        self.posy = random.randint(0, 49)
        # 出生生命值
        self.energy = random.randint(10, 25)
        # 视力
        self.vision = random.randint(1, 6)
        # 代谢速度
        self.metabolism = random.randint(1, 3)
        # 所在地图
        self.sugarscape = sugarscape

    def findSugar(self):
        bestposition = (0, 0)
        maxvalue = 0
        # 需要检索的位置列表
        searchlist = self.getSearchlist()

        for pos in searchlist:
            value = self.sugarscape.getSugarValue(pos[0], pos[1])
            if value > maxvalue:
                maxvalue = value
                bestposition = (pos[0], pos[1])
            if value == maxvalue:
                bestposition = self.getNearPosition((pos[0], pos[1]), bestposition)

        return bestposition

    # 从两点中获取距离自己位置距离近的点
    def getNearPosition(self, pos1, pos2):
        distance1 = self.sugarscape.distance((self.posx, self.posy), pos1)
        distance2 = self.sugarscape.distance((self.posx, self.posy), pos2)

        if distance1 < distance2:
            ret = pos1
        elif distance1 > distance2:
            ret = pos2
        else:
            ret = random.choice([pos1, pos2])

        return ret

    def getSearchlist(self):
        list = []
        # Horizontal
        for x in [self.posx - self.vision, self.posx + self.vision]:
            if self.sugarscape.isValidPosition(x, self.posy):
                list.append((x, self.posy))
        # Vertical
        for y in [self.posy - self.vision, self.posy + self.vision]:
            if self.sugarscape.isValidPosition(self.posx, y):
                list.append((self.posx, y))
        return list

    def moveTo(self, point):
        self.posx = point[0]
        self.posy = point[1]

    def eatSugar(self):
        self.energy += self.sugarscape.getSugarValue(self.posx, self.posy)
        self.sugarscape.isEaten(self.posx, self.posy)

    def isDead(self):
        return self.energy < 0

    def digestSugar(self):
        self.energy -= self.metabolism

    def __str__(self):
        return "(%s, %s), %s" % (self.posx, self.posy, self.energy)
