import turtle

from assignment import Assignment

class Renderer:
    __squareSize = 64
    __colors = ["magenta", "red", "light green", "light sky blue", "brown", "yellow", "pink", "grey", "orange"]
    __width = 1400
    __height = 900

    __gridSize = 9


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
        turtle.delay(2)
        turtle.ht()
        turtle.tracer(0, 0)
        turtle.up()

        self.__initDimensions()

    def __initDimensions(self):
        self.__margin = 16
        self.__gridWidth = (self.__width - 4 * self.__margin) / 2
        self.__squareSize = self.__gridWidth / self.__gridSize


    def drawGame(self, assignments):

        startX = 0
        startY = self.__height / 6

        self.__fillGrid(assignments[0], startX, startY)

        startX = self.__width / 2 + self.__margin
        startY = self.__height / 6

        self.__fillGrid(assignments[1], startX, startY)
    
        turtle.update()

    def __fillGrid(self, assignment, startX, startY):
        for i in range (self.__gridSize):
            for j in range (self.__gridSize):
                turtle.goto(startX + j * self.__squareSize, startY + i * self.__squareSize)
                color = "white"
                value = assignment.getValueAt(i, j)
                if (value is not None):
                    color = self.__colors[value - 1]
                    # print("value : {}, color : {}".format(value, color))
                self.__drawSquare(color)
                if (value is None):
                    value = ""
                self.__drawNumber(value)

        self.__drawGrid(startX, startY)

    def __drawGrid(self, startX, startY):
        turtle.pencolor("black")
        turtle.pensize(5)

        # draw external lines
        turtle.goto(startX - 2, startY - 2)
        turtle.down()
        for i in range(4):
            turtle.forward(self.__gridSize * self.__squareSize + 4)
            turtle.left(90)
        turtle.up()

        # # draw vertical in lines
        # turtle.pensize(3)
        # turtle.left(90)

        # turtle.goto(startX + 3 * self.__squareSize, startY)
        # turtle.down()
        # turtle.forward(self.__gridSize * self.__squareSize + 2)
        # turtle.up()

        # turtle.goto(startX + 6 * self.__squareSize, startY)
        # turtle.down()
        # turtle.forward(self.__gridSize * self.__squareSize + 2)
        # turtle.up()

        # # draw horizontal in lines
        # turtle.right(90)

        # turtle.goto(startX, startY + 3 * self.__squareSize)
        # turtle.down()
        # turtle.forward(self.__gridSize * self.__squareSize + 2)
        # turtle.up()

        # turtle.goto(startX, startY + 6 * self.__squareSize)
        # turtle.down()
        # turtle.forward(self.__gridSize * self.__squareSize + 2)
        # turtle.up()

        # reset pen
        turtle.pensize(0)

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
