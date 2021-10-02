
class RobotPerformance:

    def __init__(self):
        # performance goes from 0 to 100 (100 being good performance)
        self.__finalPerformance = 0
        self.__sumAllPerformances = 0
        self.__countPerformanceUpdates = 0

        self.__sumCurrentPerformances = 0
        self.__currentPerformance = 0
        self.__nbDirtCleaned = 0
        self.__nbJewelPickedUp = 0

        self.__statesHeuristicValues = []
        self.__penalty = 0

        self.__differenceSumHeuristicValues = 0


    def createStatesHeuristicValues(self, heuristicFn, endNode):
        self.__statesHeuristicValues = []
        while endNode is not None:
            value = heuristicFn(endNode.getState())
            self.__statesHeuristicValues.insert(0, value)
            endNode = endNode.getParentNode()

    def addPenalty(self, penalty):
        self.__penalty += penalty

    def getPenalty(self):
        return self.__penalty

    def resetDifferenceSumHeuristicValues(self):
        self.__differenceSumHeuristicValues = 0

    def addDifferenceSumHeuristicValues(self, difference):
        self.__differenceSumHeuristicValues += difference

    def getDifferenceSumHeuristicValues(self):
        return self.__differenceSumHeuristicValues

    def resetNbDirtCleaned(self):
        self.__nbDirtCleaned = 0

    def addNbDirtCleaned(self):
        self.__nbDirtCleaned += 1

    def resetNbJewelPickedUp(self):
        self.__nbJewelPickedUp = 0

    def addNbJewelPickedUp(self):
        self.__nbJewelPickedUp += 1

    def getNbDirtCleaned(self):
        return self.__nbDirtCleaned

    def getNbJewelPickedUp(self):
        return self.__nbJewelPickedUp

    def incrementCountPerformanceUpdates(self):
        self.__countPerformanceUpdates += 1

    def setCurrentPerformance(self, performance):
        self.__currentPerformance = performance
        self.__sumCurrentPerformances += performance
        self.__sumAllPerformances += performance
        self.__finalPerformance = self.__sumAllPerformances / self.__countPerformanceUpdates

    def getFinalPerformance(self):
        return self.__finalPerformance

    def getCurrentPerformance(self):
        return self.__currentPerformance

    def reset(self):
        self.__nbDirtCleaned = 0
        self.__nbJewelPickedUp = 0
        self.__penalty = 0
        self.__currentPerformance = 0
        self.__differenceSumHeuristicValues = 0
        self.__statesHeuristicValues = []
        self.__sumCurrentPerformances = 0

    def getStateHeuristicValue(self, index):
        return self.__statesHeuristicValues[index]

    def getDifferenceSumHeuristicValues(self):
        return self.__differenceSumHeuristicValues

    def getMeanDifferenceHeuristicValues(self):
        return self.__differenceSumHeuristicValues / self.__countPerformanceUpdates

    def getMeanCurrentPerformance(self, nbOfActions):
        return self.__sumCurrentPerformances / nbOfActions