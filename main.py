from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    line1 = Line(Point(1,1), Point(100,100))
    line2 = Line(Point(10,10), Point(232,123))
    line3 = Line(Point(30,30), Point(687,130))

    win.draw_line(line1, 'red')
    win.draw_line(line2, 'black')
    win.draw_line(line3, 'yellow')

    win.wait_for_close()



main()