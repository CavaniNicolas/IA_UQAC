
from assignment import Assignment
from cell import Cell
from time import time
from copy import deepcopy

def readSudoku(filepath):
    sudoku = [[None for j in range(9)] for i in range(9)]
    with open(filepath, 'r') as file:
        currentI = 0
        for line in file:
            line = line.rstrip()

            currentJ = 0
            for i in range(len(line)):
                if line[i] == '.':
                    sudoku[currentI][currentJ] = Cell(None, [1, 2, 3, 4, 5, 6, 7, 8, 9])
                else:
                    sudoku[currentI][currentJ] = Cell(int(line[i]), [int(line[i])])
                currentJ += 1

            currentI += 1
    return sudoku

if __name__ == "__main__":
    sudoku = readSudoku("../resources/hardSudoku.txt")
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