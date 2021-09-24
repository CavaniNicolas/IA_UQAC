class Room:
    def __init__(self, i, j, hasDirt = False, hasJewel = False):
        self.__i = i
        self.__j = j
        self.__hasDirt = hasDirt
        self.__hasJewel = hasJewel

    def getHasDirt(self):
        return self.__hasDirt

    def setHasDirt(self, hasDirt):
        self.__hasDirt = hasDirt

    def getHasJewel(self):
        return self.__hasJewel

    def setHasJewel(self, hasJewel):
        self.__hasJewel = hasJewel