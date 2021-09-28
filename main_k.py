import random
import copy

from node import Node
from robot import Robot
from problem import Problem
from state import State
from mansion import Mansion

import threading
import time


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
        successors.append(State(mansionCpy, robotCpy))

    # clean dirt
    elif roomsCpy[robotI][robotJ].getState() == 1:
        mansionCpy.cleanRoom(robotI, robotJ)
        successors.append(State(mansionCpy, robotCpy))

    # successors with movement action
    else:
        # go up
        if robotI > 0 and robotCpy.hasRoomBeenVisited(robotI - 1, robotJ) < robotCpy.getMaxVisitsPerRoom():
            robotCpy = copy.deepcopy(state.getRobot())
            robotCpy.visitRoom(robotI, robotJ)
            robotCpy.setPosition(robotI - 1, robotJ)
            successors.append(State(state.getMansion(), robotCpy))

        # go down
        if robotI < mansionSize - 1 and robotCpy.hasRoomBeenVisited(robotI + 1, robotJ) < robotCpy.getMaxVisitsPerRoom():
            robotCpy = copy.deepcopy(state.getRobot())
            robotCpy.visitRoom(robotI, robotJ)
            robotCpy.setPosition(robotI + 1, robotJ)
            successors.append(State(state.getMansion(), robotCpy))

        # go left
        if robotJ > 0 and robotCpy.hasRoomBeenVisited(robotI, robotJ - 1) < robotCpy.getMaxVisitsPerRoom():
            robotCpy = copy.deepcopy(state.getRobot())
            robotCpy.visitRoom(robotI, robotJ)
            robotCpy.setPosition(robotI, robotJ - 1)
            successors.append(State(state.getMansion(), robotCpy))

        # go right
        if robotJ < mansionSize - 1 and robotCpy.hasRoomBeenVisited(robotI, robotJ + 1) < robotCpy.getMaxVisitsPerRoom():
            robotCpy = copy.deepcopy(state.getRobot())
            robotCpy.visitRoom(robotI, robotJ)
            robotCpy.setPosition(robotI, robotJ + 1)
            successors.append(State(state.getMansion(), robotCpy))

    return successors


robotIsAlive = True


def robotThreadFn(robot, mansion, problem):
    while robotIsAlive:
        robot.percept(mansion)
        robot.chooseActionDFS(problem)
        robot.makeAction()
        time.sleep(1)


if __name__ == "__main__":

    # variables initialization
    problem = Problem(tp1GoalTest, tp1SuccessorFn)
    mansion = Mansion(5)
    robot = Robot(0, 0, mansion)

    # start the robot thread
    robotThread = threading.Thread(target=robotThreadFn, args=[robot, mansion, problem])
    robotThread.start()

    # start the mansion thread
    # TODO

    # wait for user input to exit the application
    input()
    robotIsAlive = False
