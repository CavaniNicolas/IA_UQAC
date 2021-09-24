from node import Node

class Problem:
    def __init__(self, goalTestFn, successorFn):
        self.__goalTestFn = goalTestFn
        self.__successorFn = successorFn

    def goalTest(self, state):
        return self.__goalTestFn(state)

    def successorFn(self, state):
        return self.__successorFn(state)

    def expand(self, node):
        successors = []
        # TODO: add actions
        result = self.successorFn(node.getState())
        for r in result:
            successors.append(Node(r, node, None, node.getDepth() + 1, node.getPathCost() + 1))
        return successors
