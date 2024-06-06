from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title = "Maze Solver"
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.window_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()
    
    def close(self):
        self.window_running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.start_point = point1
        self.end_point = point2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.start_point.x, self.start_point.y, self.end_point.x, self.end_point.y, 
            fill = fill_color, width = 2
            )
        
