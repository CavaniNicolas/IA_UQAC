
from cell import Cell

class Assignment:
    def __init__(self, sudoku):
        # Sudoku is a matrix of Cells
        self.__sudoku = sudoku
        self.initialDomainAdjustment()

    def checkIsConsistant(self, i, j, value):
        # Check if the given value for the cell [i, j] respects the constraints

        cellConstraints = self.getCellConstraints(i, j)
        for (row, column) in cellConstraints:
            if self.__sudoku[row][column].getValue() == value:
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

    def selectUnassignedCellMRV(self):
        # MRV implementation : select the cell with the least legal values remaining
        sudokuSize = 9

        nextCell = (0, 0) # cell with mrv
        mrv = sudokuSize # minimum remaining values
        for i in range(sudokuSize):
            for j in range(sudokuSize):
                mrv_tmp = self.__sudoku[i][j].getDomainSize()
                # if this cell is unassigned and it has less remaining values, keep this cell's coordinates and mrv
                if (not self.__sudoku[i][j].hasValue() and mrv_tmp < mrv):
                    mrv = mrv_tmp
                    nextCell = (i, j)
        return nextCell


        pass

    # To be done
    def selectUnassignedCellDegreeHeuristic(self):
        pass

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
        return self.leastConstrainingValue(i, j)

    def backtracking(self):
        if self.isComplete():
            return True

        cellI, cellJ = self.selectUnassignedCellMRV()

        orderedDomainValuesCell = self.orderedDomainValues(cellI, cellJ)

        for value in orderedDomainValuesCell:
            if self.forwardChecking(cellI, cellJ, value):
                self.__sudoku[cellI][cellJ].setValue(value)

                cellConstraints = self.getCellConstraints(cellI, cellJ)
                trulyRemoved = list()   # Position of the cells where the value has been truly removed from the domain
                for (row, column) in cellConstraints:
                    if self.__sudoku[row][column].removeValueFromDomain(value):
                        trulyRemoved.append((row, column))

                result = self.backtracking()

                if result:
                    return result

                self.__sudoku[cellI][cellJ].setValue(None)

                # Put the value back only in the domain of the cells where the value had been truly removed
                for (row, column) in trulyRemoved:
                    self.__sudoku[row][column].addValueToDomain(value)
        return False

    def leastConstrainingValue(self, i, j):
        cellDomain = self.__sudoku[i][j].getDomain()

        orderedDomainValues = []

        numConstrainedCells = dict()

        for value in cellDomain:
            numConstrainedCells[value] = 0

            if self.checkIsConsistant(i, j, value):
                cellConstraints = self.getCellConstraints(i, j)
                for (row, column) in cellConstraints:
                    if not self.__sudoku[row][column].hasValue() and self.checkIsConsistant(row, column, value):
                        numConstrainedCells[value] += 1
            else:
                numConstrainedCells[value] = 1000

        # Order values
        for n in range(len(cellDomain)):
            currentMin = float('inf')
            currentValue = 0
            for value in cellDomain:
                if numConstrainedCells[value] < currentMin:
                    currentMin = numConstrainedCells[value]
                    currentValue = value

            orderedDomainValues.append(currentValue)
            numConstrainedCells[currentValue] = float('inf')

        return orderedDomainValues

    def getCellConstraints(self, i, j):
        # Return a list containing all the coordinates of the cells applying a constraint on the cell [i, j]
        cellConstraint = []

        # Entire column
        for row in range(9):
            if row != i:
                cellConstraint.append((row, j))

        # Entire row
        for column in range(9):
            if column != j:
                cellConstraint.append((i, column))

        # Entire 3x3 square
        squareStartI = i - i % 3
        squareStartJ = j - j % 3
        for row in range(3):
            currentI = squareStartI + row
            for column in range(3):
                currentJ = squareStartJ + column
                if currentI != i and currentJ != j:
                    cellConstraint.append((currentI, currentJ))

        return cellConstraint

    def forwardChecking(self, i, j, value):
        cellConstraints = self.getCellConstraints(i, j)

        for (row, column) in cellConstraints:
            cellDomain = self.__sudoku[row][column].getDomain()

            if value in cellDomain:
                cellDomain.remove(value)

            if len(cellDomain) == 0 and not self.__sudoku[row][column].hasValue():
                # The cell has no more legal values
                return False

        return True

    def initialDomainAdjustment(self):
        # Adjust the domain of each cells at the beginning (after reading the sudoku)
        for i in range(9):
            for j in range(9):
                if not self.__sudoku[i][j].hasValue():
                    cellConstraints = self.getCellConstraints(i, j)

                    for (row, column) in cellConstraints:
                        if self.__sudoku[row][column].hasValue():
                            self.__sudoku[i][j].removeValueFromDomain(self.__sudoku[row][column].getValue())