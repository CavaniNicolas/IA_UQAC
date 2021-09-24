import random

from node import Node
from robot import Robot
from problem import Problem
from state import State


def treeSearch(problem, initialNode):
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


def tp1GoalTest(state):
    for i in range(5):
        for j in range(5):
            if state.getRoomsState()[i][j] != 0:
                return False
    return True


def tp1SuccessorFn(state):
    successors = []

    robotPosition = state.getRobotPosition()
    roomsState = state.getRoomsState()

    # successors with cleaning action (exclude "do nothing" action when room is clean)
    if roomsState[robotPosition[0]][robotPosition[1]] != 0:
        tmpRoomsState = [roomsState[i][:] for i in range(5)]
        tmpRoomsState[robotPosition[0]][robotPosition[1]] = 0
        successors.append(State(tmpRoomsState, robotPosition))
    else :
        # successors with movement action
        if robotPosition[0] > 0:
            successors.append(State(state.getRoomsState(), [robotPosition[0] - 1, robotPosition[1]]))
        if robotPosition[0] < 4:
            successors.append(State(state.getRoomsState(), [robotPosition[0] + 1, robotPosition[1]]))
        if robotPosition[1] > 0:
            successors.append(State(state.getRoomsState(), [robotPosition[0], robotPosition[1] - 1]))
        if robotPosition[1] < 4:
            successors.append(State(state.getRoomsState(), [robotPosition[0], robotPosition[1] + 1]))

    return successors

if __name__ == "__main__":
    vacuumCleaner = Robot(random.randint(0, 4), random.randint(0, 4))

    # while(1):
    #     vacuumCleaner.printWorld()
    #     time.sleep(0.7)
    #     if (vacuumCleaner.goToRoom(0, 0)):
    #         break

    problem = Problem(tp1GoalTest, tp1SuccessorFn)
    randomRoomState = [[random.randint(0, 3) for j in range(5)] for i in range(5)]
    initialState = State(randomRoomState, [0, 0])

    initialNode = Node(initialState, None, None, 0, 0)

    print()

    print("Initial node = ")
    print(initialNode)

    print()

    print("Goal test :", problem.goalTest(initialNode.getState()))

    print()

    # print("Successors of Random state = ")
    # successors = problem.expand(initialNode)
    # for n in successors:
    #     print(n)
    #     print()
    #
    # print()

    endNode = treeSearch(problem, initialNode)
    nodePath = []
    while endNode != None:
        nodePath.insert(0, endNode)
        endNode = endNode.getParentNode()

    print("Tree search = ")
    for n in nodePath:
        print(n)
        print()