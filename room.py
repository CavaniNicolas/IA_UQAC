
class Room:
    def __init__(self, i, j, hasDirt = False, hasJewel = False):
        # position
        self.__i = i
        self.__j = j

        # booleans
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

    def clean(self):
        self.__hasDirt = False
        self.__hasJewel = False

    def pickupJewel(self):
        self.__hasJewel = False

    # 0 : empty
    # 1 : dirt
    # 2 : jewel
    # 3 : dirt + jewel
    def getState(self):
        if (self.__hasDirt == True):
            hasDirt = 1
        else:
            hasDirt = 0
        if (self.__hasJewel == True):
            hasJewel = 2
        else:
            hasJewel = 0
        return hasDirt + hasJewel

    def __str__(self):
        str = "{0}".format(self.getState())
        return str