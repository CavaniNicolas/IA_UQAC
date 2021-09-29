
import turtle
from state import State

class Renderer:
    __squareSize = 75

    def __init__(self, onClose):
        turtle.tracer(20)
        turtle.pencolor("")  #Pas de couleur pour éviter les traits de construction
        # turtle.speed(0)  #Vitesse de crayon rapide, no need if there is turtle.tracer(5)

        # add event listener when window is closed
        windows = turtle.Screen()
        canvas = windows.getcanvas()
        root = canvas.winfo_toplevel()
        root.protocol("WM_DELETE_WINDOW", onClose)

    def drawState(self, state):
        turtle.clearscreen()
        turtle.pencolor("")
        turtle.tracer(16)
        mansionSize = state.getMansion().getMansionSize()

        startX = int(mansionSize / 2) * self.__squareSize
        startY = -int(mansionSize / 2) * self.__squareSize

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

        # __drawRobot(state.getRobot())

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