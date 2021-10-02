
from node import Node

class Problem:
    def __init__(self, goalTestFn, successorFn):
        self.__goalTestFn = goalTestFn
        self.__successorFn = successorFn

    def goalTest(self, state):
        return self.__goalTestFn(state)

    def successorFn(self, state):
        return self.__successorFn(state)
