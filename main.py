from graphics import Window, Point, Line, Cell

def main():
    win = Window(800, 600)
    cell = Cell(Point(300,300), Point(150,150),win)
    cell.has_left_wall = False
    cell.draw()

    win.wait_for_close()



main()