class State:
    def __init__(self, roomsState, robotPosition):
        self.__roomsState = roomsState
        self.__robotPosition = robotPosition

    def getRoomsState(self):
        return self.__roomsState

    def getRobotPosition(self):
        return self.__robotPosition

    def __str__(self):
        str = ""
        for i in range(5):
            for j in range(5):
                if i == self.getRobotPosition()[0] and j == self.getRobotPosition()[1]:
                    str += "[{0}]".format(self.getRoomsState()[i][j])
                else:
                    str += " {0} ".format(self.getRoomsState()[i][j])
            if i < 4:
                str += "\n"
        return str

    def __eq__(self, other):
        return self.__roomsState == other.getRoomsState() and self.__robotPosition == other.getRobotPosition()