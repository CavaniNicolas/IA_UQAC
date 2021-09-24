import turtle
import random


class world:
    __roomState = list()
    __firstCaseAttribute=0

    def __init__(self):
        for i in range(5):
            self.__roomState.append(list())
            for j in range(5):
                self.__roomState[i].append(0)
        self.generateRandomDirt(5)
        self.generateRandomJewel(2)

    def getRoomState(self, x=None, y=None):
        if not x and not y:
            return self.__roomState
        else:
            return self.__roomState[x][y]

    def generateRandomDirt(self, n):
        for i in range(n):
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            if self.__roomState[x][y] != 1 and self.__roomState[x][y] != 3:
                self.__roomState[x][y] += 1

    def generateRandomJewel(self, n):
        for i in range(n):
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            if self.__roomState[x][y] != 2 and self.__roomState[x][y] != 3:
                self.__roomState[x][y] += 2

    def __drawSquare(self):
        turtle.pencolor("black")
        turtle.begin_fill()
        turtle.down()
        for i in range(4):
            turtle.forward(75)
            turtle.left(90)
        turtle.up()
        turtle.end_fill()

    def drawRoom(self):
        # turtle.tracer(2)
        turtle.speed(0)
        startX=int(5/2)*75
        startY=-int(5/2)*75
        for i in range(5):
            for j in range(5):
                turtle.goto(startY+j*75,startX-i*75)
                k=self.__roomState[i][j]
                if k==0:
                    turtle.fillcolor("white")
                    self.__drawSquare()
                elif k==1:
                    turtle.fillcolor("red")
                    self.__drawSquare()
                elif k==2:
                    turtle.fillcolor("blue")
                    self.__drawSquare()
                else:
                    turtle.fillcolor("purple")
                    self.__drawSquare()
                turtle.forward(75)
