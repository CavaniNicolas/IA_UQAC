
from cell import Cell
from copy import copy

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

        initialDomainIJ = self.__sudoku[cellI][cellJ].getDomain()
        cellConstraints = self.getCellConstraints(cellI, cellJ)

        AC3Queue = []
        for (tmpI, tmpJ) in cellConstraints:
            AC3Queue.append(((tmpI, tmpJ), (cellI, cellJ)))

        for value in orderedDomainValuesCell:
            self.__sudoku[cellI][cellJ].setDomain([value])
            allRemovals = []
            if self.AC3(copy(AC3Queue), allRemovals):
                self.__sudoku[cellI][cellJ].setValue(value)

                result = self.backtracking()

                if result:
                    return result

                self.__sudoku[cellI][cellJ].setValue(None)

            for (tmpI, tmpJ, tmpValue) in allRemovals:
                self.__sudoku[tmpI][tmpJ].addValueToDomain(tmpValue)

            self.__sudoku[cellI][cellJ].setDomain(initialDomainIJ)
        return False

    def leastConstrainingValue(self, i, j):
        cellDomain = self.__sudoku[i][j].getDomain()

        orderedDomainValues = []

        numConstrainedCells = dict()

        for value in cellDomain:
            cellConstraints = self.getCellConstraints(i, j)
            nConstrained = 0

            for (tmpI, tmpJ) in cellConstraints:
                if not self.__sudoku[tmpI][tmpJ].hasValue():
                    if value in self.__sudoku[tmpI][tmpJ].getDomain():
                        nConstrained += 1

            numConstrainedCells[value] = nConstrained

        # Order values
        numConstrainedCells = dict(sorted(numConstrainedCells.items(), key=lambda item: item[1]))
        return list(numConstrainedCells.keys())

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
        AC3Queue = []
        for i in range(9):
            for j in range(9):
                cellConstraints = self.getCellConstraints(i, j)
                for (tmpI, tmpJ) in cellConstraints:
                    AC3Queue.append(((tmpI, tmpJ), (i, j)))
        self.AC3(AC3Queue, [])

    def AC3(self, queue, allRemovals):
        while len(queue) > 0:
            (i1, j1), (i2, j2) = queue.pop(0)
            if self.removeInconsistentValues(i1, j1, i2, j2, allRemovals):
                if self.__sudoku[i1][j1].getDomainSize() == 0:
                    return False
                cellConstraints = self.getCellConstraints(i1, j1)
                for tmpI2, tmpJ2 in cellConstraints:
                    queue.append(((tmpI2, tmpJ2), (i1, j1)))
        return True

    def removeInconsistentValues(self, i1, j1, i2, j2, allRemovals):
        removed = False
        domain1 = self.__sudoku[i1][j1].getDomain()
        domain2 = self.__sudoku[i2][j2].getDomain()
        for value1 in domain1:
            if len(domain2) == 1 and domain2[0] == value1:
                self.__sudoku[i1][j1].removeValueFromDomain(value1)
                allRemovals.append((i1, j1, value1))
                removed = True
        return removed
