
import time
from copy import deepcopy

from renderer import Renderer
from assignment import Assignment
from cell import Cell
import time
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

    return sudoku, sudokuLength

def onRenderClose():
    global isRunning
    isRunning = False

isRunning = True

if __name__ == "__main__":
    sudoku, sudokuLength = readSudoku("../resources/sudoku.txt")

    renderer = Renderer(onRenderClose, sudokuLength)

    assignment = Assignment(sudoku)
    finalAssignment = None

    print("========= Sudoku initial =========")
    print(assignment)
    print("==================================")

    print()

    totalTime = 0
    nbRun = 1

    for i in range(nbRun):
        tmpAssignment = deepcopy(assignment)
        startTime = time.time()
        tmpAssignment.backtracking()
        totalTime += time.time() - startTime

        if i == (nbRun - 1):
            finalAssignment = deepcopy(tmpAssignment)

    if finalAssignment.isComplete():
        print("========= Solution =========")
        print(finalAssignment)
        print("==================================")
    else:
        print("Ce sudoku n'a pas de solution !")

    print("Consistant : " + str(finalAssignment.isConsistent()))

    print("Temps d'exécution moyen ({} runs) : {}".format(nbRun, totalTime / float(nbRun)))

    while isRunning:
        renderer.drawGame((assignment, finalAssignment))
        time.sleep(0.2)
