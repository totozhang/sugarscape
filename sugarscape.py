import math


class SugarScape():

    # 50*50糖块组成地图
    def __init__(self, datafile, config):
        # sugarDictInitial用于存储初始含碳量用于自动恢复参照
        self.sugarDictInitial = self.initSugarDictAccordingToData(datafile)
        # sugarDictCurrent用于存储当前含糖量
        self.sugarDictCurrent = self.initSugarDictAccordingToData(datafile)
        # 每一个点的含糖量恢复速度
        self.sugarRecoveryRate = config.getint("sugarscape", "SugarRecoveryRate")

    # 给定位置的糖被吃
    def isEaten(self, point):
        self.sugarDictCurrent[point] = 0

    # 给定位置是否是有效位置
    def isValidPosition(self, point):
        return (point[0] >= 0 and point[0] <= 49 and point[1] >= 0 and point[1] <= 49)

    # 计算两点之间的距离
    def distance(self, p1, p2):
        return int(math.sqrt((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2))

    # 获取给定位置含糖量
    def getSugarValue(self, point):
        try:
            return self.sugarDictCurrent[point]
        except KeyError:
            return None

    # 地图含糖量自动恢复
    def recover(self):
        for point in self.sugarDictCurrent.keys():
            if self.sugarDictCurrent[point] == self.sugarDictInitial[point]:
                continue
            else:
                self.sugarDictCurrent[point] += self.sugarRecoveryRate

            if self.sugarDictCurrent[point] > self.sugarDictInitial[point]:
                self.sugarDictCurrent[point] = self.sugarDictInitial[point]

    # Key是点的坐标，Value是含糖量
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
