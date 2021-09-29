import random
import copy
import time

from node import Node
from robot import Robot
from problem import Problem
from state import State
from mansion import Mansion
from renderer import Renderer

def treeSearchBFS(problem, initialNode):
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

def treeSearchDFS(problem, initialNode):
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

# returns True if the mansion is clean
def tp1GoalTest(state):
    return [0, 0] == state.getMansion().getDirtAndJewelsLeft()


# returns the successor states of "state" from the tree
def tp1SuccessorFn(state):
    successors = []

    mansionSize = state.getMansion().getMansionSize()
    mansionCpy = copy.deepcopy(state.getMansion())

    # print(copy.deepcopy(state.getMansionState()))
    roomsCpy = copy.deepcopy(state.getMansionState())
    robotCpy = copy.deepcopy(state.getRobot())
    robot_I = robotCpy.getI()
    robot_J = robotCpy.getJ()

    # pickup jewel
    if roomsCpy[robot_I][robot_J].getState() >= 2:
        mansionCpy.pickupJewelInRoom(robot_I, robot_J)
        successors.append(State(mansionCpy, robotCpy))

    # clean dirt
    elif roomsCpy[robot_I][robot_J].getState() == 1:
        mansionCpy.cleanRoom(robot_I, robot_J)
        successors.append(State(mansionCpy, robotCpy))

    # successors with movement action
    else :
        # go up
        if robot_I > 0 and robotCpy.hasRoomBeenVisited(robot_I - 1, robot_J) < robotCpy.getMaxVisitsPerRoom():
            robotCpy = copy.deepcopy(state.getRobot())
            robotCpy.visitRoom(robot_I, robot_J)
            robotCpy.setPosition(robot_I - 1, robot_J)
            successors.append(State(state.getMansion(), robotCpy))

        # go down
        if robot_I < mansionSize - 1 and robotCpy.hasRoomBeenVisited(robot_I + 1, robot_J) < robotCpy.getMaxVisitsPerRoom():
            robotCpy = copy.deepcopy(state.getRobot())
            robotCpy.visitRoom(robot_I, robot_J)
            robotCpy.setPosition(robot_I + 1, robot_J)
            successors.append(State(state.getMansion(), robotCpy))

        # go left
        if robot_J > 0 and robotCpy.hasRoomBeenVisited(robot_I, robot_J - 1) < robotCpy.getMaxVisitsPerRoom():
            robotCpy = copy.deepcopy(state.getRobot())
            robotCpy.visitRoom(robot_I, robot_J)
            robotCpy.setPosition(robot_I, robot_J - 1)
            successors.append(State(state.getMansion(), robotCpy))

        # go right
        if robot_J < mansionSize - 1 and robotCpy.hasRoomBeenVisited(robot_I, robot_J + 1) < robotCpy.getMaxVisitsPerRoom():
            robotCpy = copy.deepcopy(state.getRobot())
            robotCpy.visitRoom(robot_I, robot_J)
            robotCpy.setPosition(robot_I, robot_J + 1)
            successors.append(State(state.getMansion(), robotCpy))

    return successors


if __name__ == "__main__":

    # rooms_1 = [[0,1,0], [0,0,0], [0,0,0]]

    problem = Problem(tp1GoalTest, tp1SuccessorFn)
    mansion = Mansion(5)
    robot = Robot(0, 0, mansion)
    mansionInitialState = State(mansion, robot)

    # print(mansionInitialState)

    renderer = Renderer()

    initialNode = Node(mansionInitialState, None, None, 0, 0)

    print()

    print("Initial node = ")
    print(initialNode)

    print()

    print("Goal test :", problem.goalTest(initialNode.getState()))

    print()

    endNode = treeSearchDFS(problem, initialNode)
    nodePath = []
    while endNode != None:
        nodePath.insert(0, endNode)
        endNode = endNode.getParentNode()


    prevTime = time.time()
    currTime = 0

    i = 0

    print("Tree search = ")
    while (i < len(nodePath)):
        currTime = time.time()
        if (currTime - prevTime > 0.4):
            n = nodePath[i]

            renderer.drawState(n.getState())
            print(n)
            print()

            prevTime = currTime
            i += 1
