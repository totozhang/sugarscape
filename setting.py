import random
from configparser import ConfigParser


class Setting():

    def __init__(self):
        config = ConfigParser()
        config.read("conf/sugarscape.config")
        self.InitialEnergyMin = config.getint("agent", "InitialEnergyMin")
        self.InitialEnergyMax = config.getint("agent", "InitialEnergyMax")
        self.InitialVisionMin = config.getint("agent", "VisionMin")
        self.InitialVisionMax = config.getint("agent", "VisionMax")
        self.InitMetabolismMin = config.getint("agent", "MetabolismMin")
        self.InitMetabolismMax = config.getint("agent", "MetabolismMax")
        self.InitSugarRecoveryRate = config.getint("sugarscape", "SugarRecoveryRate")
        self.InitMaxOfPopulation = config.getint("agent", "MaximumOfPopulation")
        self.FPS = config.getint("refresh", "speed")
        self.ScreenWidth = config.getint("screen", "width")
        self.ScreenHeigth = config.getint("screen", "height")
        self.Application = config.get("application", "name")
        self.Round = 0

    def getBornPostion(self):
        return (random.randint(0, 49), random.randint(0, 49))

    def getBornSugar(self):
        return random.randint(self.InitialEnergyMin, self.InitialEnergyMax)

    def getBornVision(self):
        return random.randint(self.InitialVisionMin, self.InitialVisionMax)

    def getBornMetabolism(self):
        return random.randint(self.InitMetabolismMin, self.InitMetabolismMax)

    def getRandomPoint(self, p1, p2):
        return random.choice([p1, p2])
