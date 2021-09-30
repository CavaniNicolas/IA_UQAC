
import turtle
from state import State

class Renderer:
    __squareSize = 75

    def __init__(self, onClose):
        turtle.pencolor("")  # No color to avoid construction lines

        # add event listener when window is closed
        windows = turtle.Screen()
        canvas = windows.getcanvas()
        root = canvas.winfo_toplevel()
        root.protocol("WM_DELETE_WINDOW", onClose)

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
                if k == 0:
                    self.__drawSquare("white")
                elif k == 1:
                    self.__drawSquare("red")
                elif k == 2:
                    self.__drawSquare("blue")
                else:
                    self.__drawSquare("purple")
                turtle.forward(self.__squareSize)

        self.__drawRobot(startX, startY, state.getRobot())

        self.__drawColorsCaptions(mansionSize)

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

    def __drawRobot(self, startX, startY, robot):
        robotI, robotJ = robot.getPosition()
        turtle.goto(startY + robotJ * self.__squareSize + self.__squareSize / 2, startX - robotI * self.__squareSize + self.__squareSize / 4)
        turtle.pencolor("black")
        if robot.getIsChoosingAction():
            turtle.fillcolor("green")
        else:
            turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.down()
        turtle.circle(self.__squareSize / 4)
        turtle.up()
        turtle.end_fill()

    def __drawColorsCaptions(self, mansionSize):
        textOffsetX = 20 # offset to write text a little bit below each square
        textOffsetY = 0 # offset to center text with each square
        startX = int(mansionSize / 2) * self.__squareSize - self.__squareSize * 6
        startY = -int(mansionSize / 2) * self.__squareSize

        turtle.pencolor("black")

        # 'Empty' caption
        textOffsetY = self.__squareSize - 7 * 8 # squareSize - (3 * textLength / 2) * fontSize
        turtle.goto(startY, startX)
        self.__drawSquare("white")
        turtle.goto(startY + textOffsetY, startX - textOffsetX)
        turtle.write("Empty")

        # 'Dirt' caption
        textOffsetY = self.__squareSize - 6 * 8 # squareSize - (3 * textLength / 2) * fontSize
        startY += 4 * self.__squareSize / 3
        turtle.goto(startY, startX)
        self.__drawSquare("red")
        turtle.goto(startY + textOffsetY, startX - textOffsetX)
        turtle.write("Dirt")

        # 'Jewel' caption
        textOffsetY = self.__squareSize - 7 * 8 # squareSize - (3 * textLength / 2) * fontSize
        startY += 4 * self.__squareSize / 3
        turtle.goto(startY, startX)
        self.__drawSquare("blue")
        turtle.goto(startY + textOffsetY, startX - textOffsetX)
        turtle.write("Jewel")

        # 'Dirt + Jewel' caption
        textOffsetY = self.__squareSize - 9 * 8 # squareSize - (3 * textLength / 2) * fontSize
        startY += 4 * self.__squareSize / 3
        turtle.goto(startY, startX)
        self.__drawSquare("purple")
        turtle.goto(startY + textOffsetY, startX - textOffsetX)
        turtle.write("Dirt + Jewel")