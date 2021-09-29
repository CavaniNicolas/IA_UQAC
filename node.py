class Node:
    def __init__(self, state, parentNode, operator, depth, pathCost):
        self.__state = state
        self.__parentNode = parentNode
        self.__operator = operator
        self.__depth = depth
        self.__pathCost = pathCost

    def __str__(self):
        return "- State :\n" + str(self.__state) + "\n- Operator : " + str(
            self.__operator) + "\n- Depth : " + str(
            self.__depth) + "\n- Cost : " + str(self.__pathCost)

    def getState(self):
        return self.__state

    def getParentNode(self):
        return self.__parentNode

    def getOperator(self):
        return self.__operator

    def getDepth(self):
        return self.__depth

    def getPathCost(self):
        return self.__pathCost

    def expand(self, problem):
        successors = []

        results = problem.successorFn(self.__state)
        for resultState, resultAction in results:
            successors.append(Node(resultState, self, resultAction, self.__depth + 1, self.__pathCost + 1))

        return successors
