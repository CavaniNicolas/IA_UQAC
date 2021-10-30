import turtle

from assignment import Assignment

class Renderer:
    __squareSize = 64
    __colors = ["magenta", "red", "light green", "light sky blue", "brown", "yellow", "pink", "grey", "orange"]
    __width = 1400
    __height = 900

    def __init__(self, onClose):
        turtle.pencolor("")  # No color to avoid construction lines

        # add event listener when window is closed
        windows = turtle.Screen()
        canvas = windows.getcanvas()
        root = canvas.winfo_toplevel()
        root.protocol("WM_DELETE_WINDOW", onClose)

        # size of the actual window
        turtle.setup(self.__width, self.__height) 
        # set coordinates of lower left corner and upper right corner
        turtle.setworldcoordinates(0, self.__height, self.__width, 0)
        # careful not to call turtle.screensize() without arguments or it will reset window size

        # # to see turtle draw : comment next lines
        turtle.speed(0)
        turtle.delay(0)
        turtle.ht()
        turtle.tracer(0, 0)
        turtle.up()

    def drawState(self, assignment):

        startX = 0
        startY = self.__height / 6

        for i in range (9):
            for j in range (9):
                turtle.goto(startX + j * self.__squareSize, startY + i * self.__squareSize)
                color = "white"
                value = assignment.getValueAt(i, j)
                if (value is not None):
                    color = self.__colors[value - 1]
                    # print("value : {}, color : {}".format(value, color))
                self.__drawSquare(color)
                self.__drawNumber(value)

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

    def __drawNumber(self, value):
        turtle.pencolor("black")
        turtle.goto(turtle.position()[0] + self.__squareSize / 2, turtle.position()[1] + self.__squareSize * 3 / 4)
        turtle.write(value, False, align="center", font=('Arial', 14, 'normal'))
