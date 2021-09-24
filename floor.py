import turtle
import random

from common import *

class world:
    __roomState = list(list())

    def __init__(self):
        for i in range(mansionSize):
            for j in range(mansionSize):
                self.__roomState[i][j] = 0
        self.generateRandomDirt(5)
        self.generateRandomJewel(2)

    def getRoomState(self, x=None, y=None):
        return self.__roomState  # [x][y]

    def generateRandomDirt(self, n):
        for i in range(n):
            x = random.randint(0, mansionSize)
            y = random.randint(0, mansionSize)
            if self.__roomState[x][y] != 1 and self.__roomState != 3:
                self.__roomState[x][y] += 1

    def generateRandomJewel(self, n):
        for i in range(n):
            x = random.randint(0, mansionSize)
            y = random.randint(0, mansionSize)
            if self.__roomState[x][y] != 2 and self.__roomState != 3:
                self.__roomState[random.randint(0, mansionSize)][random.randint(0, mansionSize)] += 2
