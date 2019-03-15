import random


class Agent():

    def __init__(self, sugarscape):
        # 糖人出生点位即使重合也不影响后续的处理
        self.posx = random.randint(0, 49)
        self.posy = random.randint(0, 49)

        # 糖人出生的生命值
        self.energy = 10

        # 糖人的视力1-5
        self.vision = random.randint(1, 5)

        # 糖人的代谢速度，每次移动所需要的能量1-3
        self.metabolism = random.randint(1, 3)
        self.sugarscape = sugarscape

    def searchPath(self):

