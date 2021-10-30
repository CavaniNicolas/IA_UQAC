
from assignment import Assignment
from cell import Cell
from time import time
from copy import copy, deepcopy

def readSudoku(filepath):
    with open(filepath, 'r') as file:

        firstLine = file.readline()
        sudokuLength = int(firstLine.rstrip())

        cellDomain = list(range(sudokuLength))
        for i in range(sudokuLength):
            cellDomain[i] += 1 # range(sudokuLength) goes from 0 to sudokuLength - 1

        sudoku = [[None for j in range(sudokuLength)] for i in range(sudokuLength)]

        currentI = 0
        for line in file:
            line = line.rstrip()

            if len(line) == 0:
                continue

            line = line.split(" ")

            currentJ = 0
            for value in line:
                if value == '.':
                    sudoku[currentI][currentJ] = Cell(None, copy(cellDomain))
                else:
                    sudoku[currentI][currentJ] = Cell(int(value), [int(value)])
                currentJ += 1
            currentI += 1

    return sudoku

if __name__ == "__main__":
    sudoku = readSudoku("../resources/hard16x16.txt")

    assignment = Assignment(sudoku)
    finalAssignment = None

    print("========= Sudoku initial =========")
    print(assignment)
    print("==================================")

    print()

    totalTime = 0
    nbRun = 20

    for i in range(nbRun):
        tmpAssignment = deepcopy(assignment)
        startTime = time()
        tmpAssignment.backtracking()
        totalTime += time() - startTime

        if i == (nbRun - 1):
            finalAssignment = deepcopy(tmpAssignment)

    if finalAssignment.isComplete():
        print("========= Solution =========")
        print(finalAssignment)
        print("==================================")
    else:
        print("Ce sudoku n'a pas de solution !")

    print("Consistant : " + str(finalAssignment.isConsistant()))

    print("Temps d'exécution moyen ({} runs) : {}".format(nbRun, totalTime / float(nbRun)))