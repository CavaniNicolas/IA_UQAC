
import turtle
from state import State

class Renderer:
    __squareSize = 100

    def __init__(self, onClose):
        turtle.pencolor("")  # No color to avoid construction lines

        # add event listener when window is closed
        windows = turtle.Screen()
        canvas = windows.getcanvas()
        root = canvas.winfo_toplevel()
        root.protocol("WM_DELETE_WINDOW", onClose)

        # import shape into turtle
        turtle.addshape('../resources/robot.gif')
        turtle.addshape('../resources/jewel.gif')
        turtle.addshape('../resources/dirt.gif')

    def drawState(self, state):
        turtle.pencolor("")
        mansionSize = state.getMansion().getMansionSize()

        startX = int(mansionSize / 2) * self.__squareSize
        startY = -int(mansionSize / 2) * self.__squareSize

        turtle.speed(0)
        turtle.delay(0)
        turtle.ht()
        turtle.tracer(0, 0)

        for i in range(mansionSize):
            for j in range(mansionSize):
                turtle.goto(startY + j * self.__squareSize, startX - i * self.__squareSize)
                k = state.getMansion().getRoomState(i, j)

                self.__drawSquare("white")
                if k == 1:
                    self.__drawDirt()
                elif k == 2:
                    self.__drawJewel()
                elif k == 3:
                    self.__drawDirt()
                    turtle.goto(startY + j * self.__squareSize, startX - i * self.__squareSize)
                    self.__drawJewel()
                turtle.forward(self.__squareSize)

        self.__drawRobot(mansionSize, state.getRobot())

        turtle.update()

    def __drawSquare(self, color):
        turtle.pencolor("black")
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.down()
        for i in range(4):
            turtle.forward(self.__squareSize)
            turtle.left(90)
        turtle.up()
        turtle.end_fill()

    def __drawRobot(self, mansionSize, robot):
        robotI, robotJ = robot.getPosition()
        startX = int(mansionSize / 2) * self.__squareSize
        startY = -int(mansionSize / 2) * self.__squareSize

        turtle.goto(startY + robotJ * self.__squareSize + self.__squareSize / 2, startX - robotI * self.__squareSize + self.__squareSize / 4)
        turtle.shape('../resources/robot.gif')
        turtle.stamp()

    def __drawDirt(self):
        offsetX = 3 * self.__squareSize / 4
        offsetY = 3 * self.__squareSize / 4
        turtle.goto( turtle.pos() + (offsetY, offsetX) )
        turtle.shape('../resources/dirt.gif')
        turtle.stamp()

    def __drawJewel(self):
        offsetX = 3 * self.__squareSize / 4
        offsetY = self.__squareSize / 4
        turtle.goto( turtle.pos() + (offsetY, offsetX) )
        turtle.shape('../resources/jewel.gif')
        turtle.stamp()
