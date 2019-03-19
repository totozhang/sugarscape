import math

class SugarScape():

    def __init__(self, datafile):

        # 50*50糖块组成地图(0-49)
        self.sugarDictInitial = self.initSugarDictAccordingToData(datafile)
        self.sugarDictCurrent = self.initSugarDictAccordingToData(datafile)
        self.sugarRecoveryRate = 4

    # 当前位置的糖被吃
    def isEaten(self, posx, posy):
        self.sugarDictCurrent[(posx, posy)] = 0

    # 当前给定坐标是否是有效的位置
    def isValidPosition(self, x, y):
        return (x >= 0 and x <= 49 and y >= 0 and y <= 49)

    # 计算两点之间的距离
    def distance(self, p1, p2):
        return math.sqrt((p2[1]-p1[1])**2+(p2[0]-p1[0])**2)

    # 根据给定坐标获取当前位置含糖量
    def getSugarValue(self, posx, posy):
        try:
            return self.sugarDictCurrent[(posx, posy)]
        except KeyError:
            return None

    # 地图含糖量自动恢复
    def recover(self):
        for coordinate in self.sugarDictCurrent.keys():
            if self.sugarDictCurrent[coordinate] == self.sugarDictInitial[coordinate]:
                continue
            else:
                self.sugarDictCurrent[coordinate] += self.sugarRecoveryRate
                if self.sugarDictCurrent[coordinate] > self.sugarDictInitial[coordinate]:
                    self.sugarDictCurrent[coordinate] = self.sugarDictInitial[coordinate]

    # Key是坐标，Value是糖量
    def initSugarDictAccordingToData(self, datafile):
        sugarDict = {}

        for line in open(datafile):

            str_sugars = line.split("\t")

            for str_sugar in str_sugars:
                x = int(str(str_sugar).split(",")[0])
                y = int(str(str_sugar).split(",")[1])
                s = int(str(str_sugar).split(",")[2])
                sugarDict[(x, y)] = s

        return sugarDict
