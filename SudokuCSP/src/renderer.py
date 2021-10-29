import turtle

from assignment import Assignment

class Renderer:
    __squareSize = 100

    def __init__(self, onClose):
        turtle.pencolor("")  # No color to avoid construction lines

        # add event listener when window is closed
        windows = turtle.Screen()
        canvas = windows.getcanvas()
        root = canvas.winfo_toplevel()
        root.protocol("WM_DELETE_WINDOW", onClose)

        turtle.speed(0)
        turtle.delay(0)
        # turtle.ht()
        turtle.tracer(0, 0)