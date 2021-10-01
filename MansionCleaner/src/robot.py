import copy
import random
import time

from node import Node
from state import State
from action import Action
from robotPerformance import RobotPerformance

class Robot:
    def __init__(self, i, j, mansion=None):
        self.__i = i
        self.__j = j

        self.__performance = RobotPerformance()

        self.__energyUsed = 0 # a mettre dans __performance

        self.__mansionView = mansion # a verifier par rapport a la copie / reference
        # remember the number of times the robot went through those rooms
        self.__visitedRooms = [[0 for j in range(mansion.getMansionSize())] for i in range(mansion.getMansionSize())]
        self.__maxVisitsPerRoom = 1
        self.__isChoosingAction = False
        self.__actionSequence = []
        self.__maxNbOfActions = 20

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

    def getIsChoosingAction(self):
        return self.__isChoosingAction

    def createActionSequence(self, endNode):
        # create the sequence of actions by browsing the nodes of the solution
        self.__actionSequence = []
        while endNode is not None:
            self.__actionSequence.insert(0, endNode.getOperator())
            endNode = endNode.getParentNode()

    # Sensor : Observe the "true" world and update internal state
    def percept(self, mansion):
        self.__energyUsed += 1
        self.__mansionView = copy.deepcopy(mansion)

    def chooseActionBFS(self, problem):
        self.__isChoosingAction = True
        mansionInitialState = State(self.__mansionView, self)
        initialNode = Node(mansionInitialState, None, None, 0, 0)
        fringe = [initialNode]
        visitedStates = []

        while len(fringe) > 0:
            node = fringe.pop(0)
            visitedStates.append(node.getState())
            if problem.goalTest(node.getState()):
                self.__isChoosingAction = False
                self.createActionSequence(node)
                return node

            successors = node.expand(problem)
            for s in successors:
                if s.getState() not in visitedStates:
                    fringe.append(s)
        self.__isChoosingAction = False
        return None

    def chooseActionDFS(self, problem):
        self.__isChoosingAction = True
        mansionInitialState = State(self.__mansionView, self)
        initialNode = Node(mansionInitialState, None, None, 0, 0)
        fringe = [initialNode]
        visitedStates = []

        while len(fringe) > 0:
            node = fringe.pop(0)
            visitedStates.append(node.getState())
            if problem.goalTest(node.getState()):
                self.__isChoosingAction = False
                self.createActionSequence(node)
                return node

            successors = node.expand(problem)
            for s in successors:
                if s.getState() not in visitedStates:
                    fringe.insert(0, s)
        self.__isChoosingAction = False
        return None

    def chooseActionGreedySearch(self, problem, heuristicFn):
        self.__isChoosingAction = True
        mansionInitialState = State(self.__mansionView, self)
        initialNode = Node(mansionInitialState, None, None, 0, 0)
        fringe = [initialNode]
        visitedStates = []

        while len(fringe) > 0:
            # select the node with the lowest heuristic value
            minValue = 100000000000
            indexMinValue = 0
            for i in range(len(fringe)):
                tmpValue = heuristicFn(fringe[i].getState())
                if tmpValue < minValue:
                    minValue = tmpValue
                    indexMinValue = i
            node = fringe.pop(indexMinValue)

            visitedStates.append(node.getState())
            if problem.goalTest(node.getState()):
                self.__isChoosingAction = False
                self.createActionSequence(node)
                self.__performance.createStatesHeuristicValues(heuristicFn, node)
                return node

            successors = node.expand(problem)
            for s in successors:
                if s.getState() not in visitedStates:
                    fringe.append(s)
        self.__isChoosingAction = False
        return None

    def chooseActionAStar(self, problem, heuristicFn):
        self.__isChoosingAction = True
        mansionInitialState = State(self.__mansionView, self)
        initialNode = Node(mansionInitialState, None, None, 0, 0)
        fringe = [initialNode]
        visitedStates = []

        while len(fringe) > 0:
            # select the node with the lowest heuristic value
            minValue = 100000000000
            indexMinValue = 0
            for i in range(len(fringe)):
                tmpValue = heuristicFn(fringe[i].getState()) + fringe[i].getPathCost()
                if tmpValue < minValue:
                    minValue = tmpValue
                    indexMinValue = i
            node = fringe.pop(indexMinValue)

            visitedStates.append(node.getState())
            if problem.goalTest(node.getState()):
                self.__isChoosingAction = False
                self.createActionSequence(node)
                self.__performance.createStatesHeuristicValues(heuristicFn, node)
                return node

            successors = node.expand(problem)
            for s in successors:
                if s.getState() not in visitedStates:
                    fringe.append(s)
        self.__isChoosingAction = False
        return None

    # Effector : make actions on the "true" world
    def makeAction(self, mansion, heuristicFn = None):
        countAction = 0

        for action in self.__actionSequence:

            if action == Action.CLEAN:
                jewelSucked = mansion.cleanRoom(self.__i, self.__j)
                self.__performance.addNbDirtCleaned()
                if jewelSucked:
                    self.__performance.addPenalty(8)

            elif action == Action.PICKUP:
                mansion.pickupJewelInRoom(self.__i, self.__j)
                self.__performance.addNbJewelPickedUp()

            elif action == Action.MOVE_UP:
                self.__i -= 1

            elif action == Action.MOVE_LEFT:
                self.__j -= 1

            elif action == Action.MOVE_DOWN:
                self.__i += 1

            elif action == Action.MOVE_RIGHT:
                self.__j += 1

            self.__energyUsed += 1
            countAction += 1

            if heuristicFn is not None:
                self.determinePerformance(heuristicFn, State(mansion, self), countAction - 1)
                if countAction >= self.__maxNbOfActions:
                    return

            time.sleep(1)

    def determinePerformance(self, heuristicFn, realState, indexAction):
        # get the real heuristic value
        realHeuristicValue = heuristicFn(realState)
        estimatedHeuristicValue = self.__performance.getStateHeuristicValue(indexAction)

        # add the difference between the estimated and the real heuristic values
        self.__performance.addDifferenceSumHeuristicValues(realHeuristicValue - estimatedHeuristicValue)

        # get some state values after the action
        nbDirtCleaned = self.__performance.getNbDirtCleaned()
        nbJewelPickedUp = self.__performance.getNbJewelPickedUp()
        penalty = self.__performance.getPenalty()

        # determine the cleaningEfficiencyRatio (good when small)
        if nbDirtCleaned + nbJewelPickedUp == 0:
            cleaningEfficiencyRatio = (self.__energyUsed / 1) + penalty
        else:
            cleaningEfficiencyRatio = (self.__energyUsed / (nbDirtCleaned + nbJewelPickedUp)) + penalty

        # counts number of action the robot does (final performance gets updated for every action)
        self.__performance.incrementCountPerformanceUpdates()

        # update performance
        meanDifferenceHeuristicValues = self.__performance.getMeanDifferenceHeuristicValues()
        if meanDifferenceHeuristicValues + cleaningEfficiencyRatio == 0:
            self.__performance.setCurrentPerformance(100 / 1)
        else:
            self.__performance.setCurrentPerformance(100 / (5 * meanDifferenceHeuristicValues + cleaningEfficiencyRatio))

    def getFinalPerformance(self):
        return self.__performance.getFinalPerformance()

    def getCurrentPerformance(self):
        return self.__performance.getCurrentPerformance()

    def resetPerformance(self):
        self.__energyUsed = 0
        self.__performance.reset()

    def adaptMaxNbOfActions(self):
        currentPerformance = self.__performance.getCurrentPerformance()

        # if currentPerformance <= 50:
