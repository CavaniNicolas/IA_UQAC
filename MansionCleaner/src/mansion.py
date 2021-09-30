
import random

from room import Room

class Mansion:
    def __init__(self, mansionSize, rooms = None):
        self.__mansionSize = mansionSize
        if (rooms == None):
            self.__rooms = [[Room(i, j, random.randint(0, 1), random.randint(0, 1)) for j in range(self.__mansionSize)] for i in range(self.__mansionSize)]
        else:
            self.__rooms = rooms
        # self.generateRandomDirt(5)
        # self.generateRandomJewel(2)
        self.__nbOfDirt = 0
        self.__nbOfJewels = 0

        for i in range(mansionSize):
            for j in range(mansionSize):
                if self.__rooms[i][j].getHasDirt():
                    self.__nbOfDirt += 1
                if self.__rooms[i][j].getHasJewel():
                    self.__nbOfJewels += 1

    def getRooms(self):
        return self.__rooms

    def getMansionSize(self):
        return self.__mansionSize

    def getRoomState(self, i, j):
        return self.__rooms[i][j].getState()

    def getDirtAndJewelsLeft(self):
        return [self.__nbOfDirt, self.__nbOfJewels]

    def cleanRoom(self, i, j):
        jewelSucked = False

        if (self.__rooms[i][j].getState() == 1):
            self.__nbOfDirt -= 1

        elif (self.__rooms[i][j].getState() == 2):
            self.__nbOfJewels -= 1
            jewelSucked = True

        elif (self.__rooms[i][j].getState() == 3):
            self.__nbOfDirt -= 1
            self.__nbOfJewels -= 1
            jewelSucked = True

        self.__rooms[i][j].clean()
        return jewelSucked

    def pickupJewelInRoom(self, i, j):
        if (self.__rooms[i][j].getState() >= 2):
            self.__nbOfJewels -= 1

        self.__rooms[i][j].pickupJewel()

    # def generateRandomDirt(self, n):
    #     for i in range(n):
    #         x = random.randint(0, self.__mansionSize)
    #         y = random.randint(0, self.__mansionSize)
    #         if self.__rooms[x][y] != 1 and self.__rooms[x][y] != 3:
    #             self.__rooms[x][y] += 1

    # def generateRandomJewel(self, n):
    #     for i in range(n):
    #         x = random.randint(0, self.__mansionSize)
    #         y = random.randint(0, self.__mansionSize)
    #         if self.__rooms[x][y] != 2 and self.__rooms[x][y] != 3:
    #             self.__rooms[random.randint(0, self.__mansionSize)][random.randint(0, self.__mansionSize)] += 2

    def __str__(self):
        str = ""
        for i in range(self.__mansionSize):
            for j in range(self.__mansionSize):
                str += " {0} ".format(self.__rooms[i][j])
            if i < self.__mansionSize - 1:
                str += "\n"
        return str