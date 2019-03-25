import math


class SugarScape():

    # Sugarscapte 50 * 50 Map
    def __init__(self, datafile, recovery_rate):
        self.sugarDictInitial = self.initSugarDictAccordingToData(datafile)
        self.sugarDictCurrent = self.initSugarDictAccordingToData(datafile)
        self.sugarRecoveryRate = recovery_rate

    # The sugar at the given postion is eaten.
    def isEaten(self, point):
        self.sugarDictCurrent[point] = 0

    # If given position on the map
    def isValidPosition(self, point):
        return (point[0] >= 0 and point[0] <= 49 and point[1] >= 0 and point[1] <= 49)

    # Distance between p1 and p2
    def distance(self, p1, p2):
        return int(math.sqrt((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2))

    # Get the sugar amount at given position
    def getSugarValue(self, point):
        try:
            return self.sugarDictCurrent[point]
        except KeyError:
            return None

    # Get a nearer postion from p1 and p2 to pcurrent
    def getNearerPostion(self, destiny, pcurrent, p1, p2):
        distance1 = self.distance(pcurrent, p1)
        distance2 = self.distance(pcurrent, p2)

        if distance1 < distance2:
            return p1
        elif distance1 > distance2:
            return p2
        else:
            return destiny.getRandomPoint(p1, p2)

    # The sugar recovery of the SugarScape
    def recover(self):
        for point in self.sugarDictCurrent.keys():
            if self.sugarDictCurrent[point] == self.sugarDictInitial[point]:
                continue
            else:
                self.sugarDictCurrent[point] += self.sugarRecoveryRate

            if self.sugarDictCurrent[point] > self.sugarDictInitial[point]:
                self.sugarDictCurrent[point] = self.sugarDictInitial[point]

    # sugar dictionary, key is the postion x,y, value is the sugar
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

    # get the sugar level district
    def getSugarLevelArea(self, position):
        return self.sugarDictInitial[position]
