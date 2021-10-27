
from cell import Cell

class Assignment:
    def __init__(self, sudoku):
        # Sudoku is a matrix of Cells
        self.__sudoku = sudoku

    def checkIsConsistant(self, i, j, value):
        # Check if the given value for the cell [i, j] respects the constraints

        # Check the entire column
        for row in range(9):
            if row != i:
                if self.__sudoku[row][j].getValue() == value:
                    return False

        # Check the entire row
        for column in range(9):
            if column != j:
                if self.__sudoku[i][column].getValue() == value:
                    return False

        # Check the entire 3x3 square
        squareStartI = i - i % 3
        squareStartJ = j - j % 3
        for row in range(3):
            currentI = squareStartI + row
            for column in range(3):
                currentJ = squareStartJ + column
                if currentI != i and currentJ != j:
                    if self.__sudoku[currentI][currentJ].getValue() == value:
                        return False

        return True

    def isComplete(self):
        # Check if each cell has a value
        for i in range(9):
            for j in range(9):
                if not self.__sudoku[i][j].hasValue():
                    return False
        return True

    def selectUnassignedCell(self):
        # Simple implementation : select the first unassigned cell
        for i in range(9):
            for j in range(9):
                if not self.__sudoku[i][j].hasValue():
                    return (i, j)

    def __str__(self):
        # return sudoku in a string
        res = ""
        for i in range(9):
            for j in range(9):
                res += str(self.__sudoku[i][j])
                if j != 8 and (j + 1) % 3 == 0:
                    res += " "

            if i != 8 :
                if (i + 1) % 3 == 0:
                    res += "\n"
                res += "\n"

        return res

    def orderedDomainValues(self, i, j):
        return self.__sudoku[i][j].getDomain()

    def backtracking(self):
        if self.isComplete():
            return True

        cellI, cellJ = self.selectUnassignedCell()

        orderedDomainValuesCell = self.orderedDomainValues(cellI, cellJ)

        for value in orderedDomainValuesCell:
            if self.checkIsConsistant(cellI, cellJ, value):
                self.__sudoku[cellI][cellJ].setValue(value)
                result = self.backtracking()
                if result:
                    return result
                self.__sudoku[cellI][cellJ].setValue(None)
        return False