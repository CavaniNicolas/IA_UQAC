
class Cell:
    def __init__(self, value = None, domain = []):
        # Value in the cell (int from 1 to 9)
        self.__value = value
        # List of possible values for this cell
        self.__domain = domain

    def addValueToDomain(self, value):
        pass

    def removeValueToDomain(self, value):
        pass

    def hasValue(self):
        return self.__value != None

    def getDomain(self):
        return self.__domain

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.__value = value

    def __str__(self):
        # return Cell value in a string
        if self.__value:
            return str(self.__value)
        else:
            return "."
