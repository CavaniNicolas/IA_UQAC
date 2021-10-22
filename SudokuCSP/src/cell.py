
class Cell:
    def __init__(self, sudoku):
        # Value in the cell (int from 1 to 9)
        self.__value
        # List of possible values for this cell
        self.__possibleValues

    def addPossibleValue(self, value):
        pass

    def removePossibleValue(self, value):
        pass

    def hasValue(self):
        return True

    def getPossibleValues(self):
        return self.__possibleValues

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.__value = value

    def __str__(self):
        # return Cell value in a string
        return str(self.__value)
