import random
import copy
import time

from action import Action
from robot import Robot
from problem import Problem
from state import State
from mansion import Mansion
from renderer import Renderer

import threading
import time


# heuristic value : sum of remaining number of dirt and jewels
def heuristicRemainingDirtAndJewels(state):

    nbDirt, nbJewels = state.getNbDirtAndJewels()

    return nbDirt + nbJewels


# returns True if the mansion is clean
def tp1GoalTest(state):
    return [0, 0] == state.getMansion().getDirtAndJewelsLeft()

# returns the successor states of "state" from the tree
def tp1SuccessorFn(state):
    successors = []

    mansionCpy = copy.deepcopy(state.getMansion())
    roomsCpy = copy.deepcopy(state.getMansionState())
    robotCpy = copy.deepcopy(state.getRobot())

    mansionSize = mansionCpy.getMansionSize()
    robotI = robotCpy.getI()
    robotJ = robotCpy.getJ()

    # pickup jewel
    if roomsCpy[robotI][robotJ].getState() >= 2:
        mansionCpy.pickupJewelInRoom(robotI, robotJ)
        successors.append([State(mansionCpy, robotCpy), Action.PICKUP])

    # clean dirt
    elif roomsCpy[robotI][robotJ].getState() == 1:
        mansionCpy.cleanRoom(robotI, robotJ)
        successors.append([State(mansionCpy, robotCpy), Action.CLEAN])

    # successors with movement action
    else:
        # go up
        if robotI > 0 and robotCpy.hasRoomBeenVisited(robotI - 1, robotJ) < robotCpy.getMaxVisitsPerRoom():
            robotCpy = copy.deepcopy(state.getRobot())
            robotCpy.visitRoom(robotI, robotJ)
            robotCpy.setPosition(robotI - 1, robotJ)
            successors.append([State(state.getMansion(), robotCpy), Action.MOVE_UP])

        # go down
        if robotI < mansionSize - 1 and robotCpy.hasRoomBeenVisited(robotI + 1, robotJ) < robotCpy.getMaxVisitsPerRoom():
            robotCpy = copy.deepcopy(state.getRobot())
            robotCpy.visitRoom(robotI, robotJ)
            robotCpy.setPosition(robotI + 1, robotJ)
            successors.append([State(state.getMansion(), robotCpy), Action.MOVE_DOWN])

        # go left
        if robotJ > 0 and robotCpy.hasRoomBeenVisited(robotI, robotJ - 1) < robotCpy.getMaxVisitsPerRoom():
            robotCpy = copy.deepcopy(state.getRobot())
            robotCpy.visitRoom(robotI, robotJ)
            robotCpy.setPosition(robotI, robotJ - 1)
            successors.append([State(state.getMansion(), robotCpy), Action.MOVE_LEFT])

        # go right
        if robotJ < mansionSize - 1 and robotCpy.hasRoomBeenVisited(robotI, robotJ + 1) < robotCpy.getMaxVisitsPerRoom():
            robotCpy = copy.deepcopy(state.getRobot())
            robotCpy.visitRoom(robotI, robotJ)
            robotCpy.setPosition(robotI, robotJ + 1)
            successors.append([State(state.getMansion(), robotCpy), Action.MOVE_RIGHT])

    return successors


isRunning = True


def robotThreadFn(robot, mansion, problem):
    global isRunning
    while isRunning:
        robot.percept(mansion)
        robot.chooseActionGreedySearch(problem, heuristicRemainingDirtAndJewels)
        robot.makeAction(mansion)
        time.sleep(1)


def mansionThreadFn(mansion, robot):
    global isRunning
    while isRunning:
        # TODO: generate dirt and jewel
        rooms = mansion.getRooms()
        for i in range(len(rooms)):
            for j in range(len(rooms)):
                if robot.getI() == i and robot.getJ() == j:
                    print("[{0}]".format(rooms[i][j]), end="")
                else:
                    print(" {0} ".format(rooms[i][j]), end="")
            print()
        print()
        time.sleep(1)


def onRenderClose():
    global isRunning
    isRunning = False


if __name__ == "__main__":

    # variables initialization
    problem = Problem(tp1GoalTest, tp1SuccessorFn)
    mansion = Mansion(5)
    robot = Robot(0, 0, mansion)
    renderer = Renderer(onRenderClose)

    # start the mansion thread
    mansionThread = threading.Thread(target=mansionThreadFn, args=[mansion, robot])
    mansionThread.daemon = True
    mansionThread.start()

    # start the robot thread
    robotThread = threading.Thread(target=robotThreadFn, args=[robot, mansion, problem])
    robotThread.daemon = True
    robotThread.start()

    while isRunning:
        currentState = State(mansion, robot)
        renderer.drawState(currentState)
        time.sleep(0.2)