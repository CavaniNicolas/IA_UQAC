import copy
import random

from node import Node
from state import State

class Robot:
    def __init__(self, i, j, mansion=None):
        self.__i = i
        self.__j = j
        self.__energyUsed = 0
        self.__performanceMeasure = 0
        self.__mansionView = mansion # a verifier par rapport a la copie / reference
        # remember the number of times the robot went through those rooms
        self.__visitedRooms = [[0 for j in range(mansion.getMansionSize())] for i in range(mansion.getMansionSize())]
        self.__maxVisitsPerRoom = 1

    def getEnergyUsed(self):
        return self.__energyUsed

    def setEnergyUsed(self, energy):
        self.__energyUsed = energy

    def getI(self):
        return self.__i

    def setI(self, i):
        self.__i = i

    def getJ(self):
        return self.__j

    def setJ(self, j):
        self.__j = j

    def getPosition(self):
        return [self.__i,  self.__j]

    def setPosition(self, i, j):
        self.__i = i
        self.__j = j

    def hasRoomBeenVisited(self, i, j):
        return self.__visitedRooms[i][j]

    def getMaxVisitsPerRoom(self):
        return self.__maxVisitsPerRoom

    def visitRoom(self, i, j):
        self.__visitedRooms[i][j] += 1

    def getPerformanceMeasure(self):
        return self.__performanceMeasure

    def setPerformanceMeasure(self, measure):
        self.__performanceMeasure = measure

    def getMansionView(self):
        return self.__mansionView

    def percept(self, mansion):
        self.__mansionView = copy.deepcopy(mansion)

    def chooseActionBFS(self, problem):
        mansionInitialState = State(self.__mansionView, self)
        initialNode = Node(mansionInitialState, None, None, 0, 0)
        fringe = [initialNode]
        visitedStates = []

        while len(fringe) > 0:
            node = fringe.pop(0)
            visitedStates.append(node.getState())
            if problem.goalTest(node.getState()):
                return node

            successors = problem.expand(node)
            for s in successors:
                if s.getState() not in visitedStates:
                    fringe.append(s)
        return None

    def chooseActionDFS(self, problem):
        mansionInitialState = State(self.__mansionView, self)
        initialNode = Node(mansionInitialState, None, None, 0, 0)
        fringe = [initialNode]
        visitedStates = []

        while len(fringe) > 0:
            node = fringe.pop(0)
            visitedStates.append(node.getState())
            if problem.goalTest(node.getState()):
                return node

            successors = problem.expand(node)
            for s in successors:
                if s.getState() not in visitedStates:
                    fringe.insert(0, s)
        return None

    def makeAction(self):
        print("make action")

    def goToRoom(self, i, j):
        if (self.__i == i and self.__j == j):
            return True
        else:
            if (self.__i != i):
                self.setI(self.__i + (i - self.__i) / abs(i - self.__i))
            else:
                self.setJ(self.__j + (j - self.__j) / abs(j - self.__j))