from common import *

class State:
    def __init__(self, mansion):
        self.__mansion = mansion
        self.__robotPosition = mansion.getRobotPosition()

    def getMansionState(self):
        return self.__mansion.getRooms()

    def getRobotPosition(self):
        return self.__robotPosition

    def getMansion(self):
        return self.__mansion

    def __str__(self):
        str = ""
        mansionSize = self.__mansion.getMansionSize()
        for i in range(mansionSize):
            for j in range(mansionSize):
                if i == self.getRobotPosition()[0] and j == self.getRobotPosition()[1]:
                    str += "[{0}]".format(self.getMansionState()[i][j])
                else:
                    str += " {0} ".format(self.getMansionState()[i][j])
            if i < mansionSize - 1:
                str += "\n"
        return str

    def __eq__(self, other):
        return self.getMansionState() == other.getMansionState() and self.__robotPosition == other.getRobotPosition()