
import random

class Robot:
    def __init__(self, i, j):
        self.__energyUsed = 0
        self.__i = i
        self.__j = j
        self.__performanceMeasure = 0

    def getEnergyUsed(self):
        return self.__energyUsed

    def setEnergyUsed(self, energy):
        self.__energyUsed = energy

    def getI(self):
        return self.__i

    def setI(self, i):
        self.__i = i

    def getJ(self):
        return self.__j

    def setJ(self, j):
        self.__j = j

    def getPerformanceMeasure(self):
        return self.__performanceMeasure

    def setPerformanceMeasure(self, measure):
        self.__performanceMeasure = measure

    def chooseAction(self):
        print("choose action")

    def makeAction(self):
        print("make action")

    def goToRoom(self, i, j):
        if (self.__i == i and self.__j == j):
            return True
        else:
            if (self.__i != i):
                self.setI(self.__i + (i - self.__i) / abs(i - self.__i))
            else:
                self.setJ(self.__j + (j - self.__j) / abs(j - self.__j))