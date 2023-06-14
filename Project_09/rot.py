'''Abdullah Shahzad
CS 152 B
11/17/2021
Lab 9'''

import graphicsPlus as gr 
import math
import time

#the goal of this lab is to create a line and have it rotate 360 degrees around the screen
#the scale factor will be 10

class RotatingLine():
    def __init__(self, win, x0, y0, length, Ax = None, Ay = None):
        self.pos = [x0, y0]
        self.length = length

        if Ax == None and Ay == None:
            self.anchor = [x0, y0]
        else:
            self.anchor = [Ax, Ay]

        self.points = [[-length/2.0, 0.0], [length/2.0, 0.0]]
        self.angle = 0.0 #the current orientation of the line
        self.rvel = 0.0 #the current rotational velocity
        self.win = win 
        self.scale = 10
        self.vis = []
        self.drawn = False
        self.refresh()

    def render(self):
        theta = self.angle*math.pi/180.0
        cth = math.cos(theta)
        sth = math.sin(theta)
        pts = []
        for point in self.points:
            x = self.pos[0]+point[0] - self.anchor[0]
            y = self.pos[1]+point[1] - self.anchor[1]

            xt = x*cth - y*sth
            yt = x*sth + y*cth

            x = xt + self.anchor[0]
            y = yt + self.anchor[1]

            pts.append(gr.Point(self.scale*x, (self.win.getHeight()-self.scale*y)))
            

        self.vis = [gr.Line(pts[0], pts[1])]
    
    def draw(self):
        for item in self.vis:
            item.draw(self.win)
        self.drawn = True

    def undraw(self):
        for item in self.vis:
            item.undraw()
        self.drawn = False

    def refresh(self):
        drawn = self.drawn
        if drawn:
            self.undraw()
        self.render()
        if drawn:
            self.draw()

    def getAngle(self):
        return self.angle

    def setAngle(self, angle):
        self.angle = angle
        self.refresh()

    def rotate(self, incr):
        self.angle += incr
        self.refresh()

    def setAnchor(self, Ax, Ay):
        self.anchor = [Ax, Ay]

def test1():
    win = gr.GraphWin('line thingy', 500, 500, False)

    line = RotatingLine(win, 25, 25, 10)
    line.draw()

    while win.checkMouse() == None:
        line.rotate(3)
        time.sleep(0.08)
        win.update()

    win.getMouse()
    win.close()

if __name__ == "__main__":
    test1()
