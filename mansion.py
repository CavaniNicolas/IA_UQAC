
import random

class Mansion:
    __rooms = list(list())


    def __init__(self, mansionSize, robotPosition = [0, 0], rooms = None):
        self.__mansionSize = mansionSize
        if (rooms == None):
            self.__rooms = [[random.randint(0, 3) for j in range(self.__mansionSize)] for i in range(self.__mansionSize)]
        else:
            self.__rooms = rooms
        self.__robotPosition = robotPosition
        # self.generateRandomDirt(5)
        # self.generateRandomJewel(2)

    def getRooms(self):
        return self.__rooms

    def getRobotPosition(self):
        return self.__robotPosition

    def getMansionSize(self):
        return self.__mansionSize


    def getRoomState(self, x=None, y=None):
        return self.__rooms  # [x][y]

    def generateRandomDirt(self, n):
        for i in range(n):
            x = random.randint(0, self.__mansionSize)
            y = random.randint(0, self.__mansionSize)
            if self.__rooms[x][y] != 1 and self.__rooms[x][y] != 3:
                self.__rooms[x][y] += 1

    def generateRandomJewel(self, n):
        for i in range(n):
            x = random.randint(0, self.__mansionSize)
            y = random.randint(0, self.__mansionSize)
            if self.__rooms[x][y] != 2 and self.__rooms[x][y] != 3:
                self.__rooms[random.randint(0, self.__mansionSize)][random.randint(0, self.__mansionSize)] += 2

    def __str__(self):
        str = ""
        for i in range(self.__mansionSize):
            for j in range(self.__mansionSize):
                str += " {0} ".format(self.__rooms[i][j])
            if i < self.__mansionSize - 1:
                str += "\n"
        return str