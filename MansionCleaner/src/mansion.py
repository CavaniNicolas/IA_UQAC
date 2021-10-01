
import random

from room import Room

class Mansion:
    def __init__(self, mansionSize, rooms = None, probaDirt = 2, probaJewel = 1):
        self.__mansionSize = mansionSize
        self.__nbOfDirt = 0
        self.__nbOfJewels = 0

        if (rooms == None):
            self.__rooms = [[Room(i, j, False, False) for j in range(self.__mansionSize)] for i in range(self.__mansionSize)]
            self.generateRandomDirt(probaDirt)
            self.generateRandomJewel(probaJewel)
        else:
            self.__rooms = rooms

    def getRooms(self):
        return self.__rooms

    def getRoom(self, i, j):
        return self.__rooms[i][j]

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

    def generateRandomDirt(self, n=2):
        for i in range(self.__mansionSize):
            for j in range(self.__mansionSize):
                proba = random.randint(0, 100)  # Random value between 0 and 100
                roomState = self.getRoomState(i, j)
                if roomState != 1 and roomState != 3 and proba < n:
                    # There is no dirt in this room
                    self.__rooms[i][j].setHasDirt(True)
                    self.__nbOfDirt += 1

    def generateRandomJewel(self, n=1):
        for i in range(self.__mansionSize):
            for j in range(self.__mansionSize):
                proba = random.randint(0, 100) # Random value between 0 and 100
                roomState = self.getRoomState(i, j)
                if roomState != 2 and roomState != 3 and proba < n:
                    # There is no jewel in this room
                    self.__rooms[i][j].setHasJewel(True)
                    self.__nbOfJewels += 1

    def __str__(self):
        str = ""
        for i in range(self.__mansionSize):
            for j in range(self.__mansionSize):
                str += " {0} ".format(self.__rooms[i][j])
            if i < self.__mansionSize - 1:
                str += "\n"
        return str