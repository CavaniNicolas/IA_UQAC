import copy
import random
import time

from node import Node
from state import State
from action import Action

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

            successors = node.expand(problem)
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

            successors = node.expand(problem)
            for s in successors:
                if s.getState() not in visitedStates:
                    fringe.insert(0, s)
        return None

    def chooseActionGreedySearch(self, problem, heuristic):
        mansionInitialState = State(self.__mansionView, self)
        initialNode = Node(mansionInitialState, None, None, 0, 0)
        fringe = [initialNode]
        visitedStates = []

        while len(fringe) > 0:
            # select the node with the lowest heuristic value
            minValue = 100000000000
            indexMinValue = 0
            for i in range(len(fringe)):
                tmpValue = heuristic(fringe[i].getState())
                if tmpValue < minValue:
                    minValue = tmpValue
                    indexMinValue = i
            node = fringe.pop(indexMinValue)

            visitedStates.append(node.getState())
            if problem.goalTest(node.getState()):
                return node

            successors = node.expand(problem)
            for s in successors:
                if s.getState() not in visitedStates:
                    fringe.append(s)
        return None

    def makeAction(self, seq, mansion):
        for action in seq:
            if action == Action.CLEAN:
                mansion.cleanRoom(self.__i, self.__j)
            elif action == Action.PICKUP:
                mansion.pickupJewelInRoom(self.__i, self.__j)
            elif action == Action.MOVE_UP:
                self.__i -= 1
            elif action == Action.MOVE_LEFT:
                self.__j -= 1
            elif action == Action.MOVE_DOWN:
                self.__i += 1
            elif action == Action.MOVE_RIGHT:
                self.__j += 1

            time.sleep(1)

    def goToRoom(self, i, j):
        if (self.__i == i and self.__j == j):
            return True
        else:
            if (self.__i != i):
                self.setI(self.__i + (i - self.__i) / abs(i - self.__i))
            else:
                self.setJ(self.__j + (j - self.__j) / abs(j - self.__j))