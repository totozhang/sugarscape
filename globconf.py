import random
from configparser import ConfigParser


class Globconf():

    def __init__(self):
        config = ConfigParser()
        config.read("conf/sugarscape.config")
        self.InitialEnergyMin = config.getint("agent", "InitialEnergyMin")
        self.InitialEnergyMax = config.getint("agent", "InitialEnergyMax")
        self.InitialVisionMin = config.getint("agent", "VisionMin")
        self.InitialVisionMax = config.getint("agent", "VisionMax")
        self.MetabolismMin = config.getint("agent", "MetabolismMin")
        self.MetabolismMax = config.getint("agent", "MetabolismMax")
        self.InitSugarRecoveryRate = config.getint("sugarscape", "SugarRecoveryRate")
        self.FPS = config.getint("refresh", "speed")
        self.MaxOfPopulation = config.getint("agent", "MaximumOfPopulation")

    def getBornPostion(self):
        return (random.randint(0, 49), random.randint(0, 49))

    def getBornSugar(self):
        return random.randint(self.InitialEnergyMin, self.InitialEnergyMax)

    def getBornVision(self):
        return random.randint(self.InitialVisionMin, self.InitialVisionMax)

    def getBornMetabolism(self):
        return random.randint(self.MetabolismMin, self.MetabolismMax)

    def getRandomPoint(self, p1, p2):
        return random.choice([p1, p2])
