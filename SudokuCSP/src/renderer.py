import turtle

from assignment import Assignment

class Renderer:
    __squareSize = 64
    __colors = []
    __width = 1400
    __height = 900

    def __init__(self, onClose, gridSize = 9):
        turtle.pencolor("")  # No color to avoid construction lines

        self.__gridSize = gridSize

        # initialize turtle
        self.__initTurtle(onClose)

        # initialize dimensions needed to draw on screen
        self.__initDimensions()

        # if (self.__gridSize == 9):
        if (False):
            # nice colors if we only use 9
            self.__colors = ["#fff200", "#ff7f25", "#00a2e9", "#eb1c23", "#23b14d", "#ffacc8", "#b9795b", "#c8bfe6", "#eee4ae"]
        else:
            # nice colors if we use more
            self.__initColors()

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

    ##############################
    ### INITIALIZATION METHODS ###
    ##############################

    def __initTurtle(self, onClose):
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

        # to see turtle draw : comment next lines
        turtle.speed(0)
        turtle.delay(2)
        turtle.ht()
        turtle.tracer(0, 0)
        turtle.up()

    def __initDimensions(self):
        self.__margin = 16
        self.__gridWidth = (self.__width - 4 * self.__margin) / 2
        self.__squareSize = self.__gridWidth / self.__gridSize

    def __initColors(self):
        hueStep = 360 / self.__gridSize

        hue = 0 # teinte
        sat = 0.7 # saturation %
        light = 0.6 # luminosite %

        for i in range (self.__gridSize):

            # see https://www.rapidtables.com/convert/color/hsl-to-rgb.html
            c = (1 - abs(2 * light - 1)) * sat
            x = c * abs((hue / 60) % 2 - 1)
            m = light - c / 2

            # round() : valeur entiere la plus proche
            c = round((c + m) * 255) 
            x = round((x + m) * 255)
 
            if (0 <= hue < 60):
                red = c
                green = x
                blue = 0

            elif (60 <= hue < 120):
                red = x
                green = c
                blue = 0

            elif (120 <= hue < 180):
                red = 0
                green = c
                blue = x

            elif (180 <= hue < 240):
                red = 0
                green = x
                blue = c

            elif (240 <= hue < 300):
                red = x
                green = 0
                blue = c

            elif (300 <= hue < 360):
                red = c
                green = 0
                blue = x

            hexa = self.getHexa(red, green, blue)
            self.__colors.append(hexa)

            hue += hueStep

    def getHexa(self, red, green, blue):
        if (red == 0):
            hexRed = "00"
        elif (red > 0 and red < 16):
            hexRed = "0" + hex(red).lstrip("0x")
        else:
            hexRed = hex(red).lstrip("0x")

        if (green == 0):
            hexGreen = "00"
        elif (green > 0 and green < 16):
            hexGreen = "0" + hex(green).lstrip("0x")
        else:
            hexGreen = hex(green).lstrip("0x")

        if (blue == 0):
            hexBlue = "00"
        elif (blue > 0 and blue < 16):
            hexBlue = "0" + hex(blue).lstrip("0x")
        else:
            hexBlue = hex(blue).lstrip("0x")

        hexNum = "#" + hexRed + hexGreen + hexBlue
        return hexNum
