
from cell import Cell

class Assignment:
    def __init__(self, sudoku):
		# Sudoku Matrix of Cells
        self.__sudoku

    def isConsistant(self):
        return True

    def isComplete(self):
        return True

	def getNextUnassignedCell(self):
        return Cell

    def getSudoku(self):
        return self.__sudoku

    def __str__(self):
		# return sudoku in a string
        return "__sudoku :\n"
