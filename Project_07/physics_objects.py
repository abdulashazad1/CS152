'''Abdullah Shahzad
CS 152 B
11/1/2021
Lab & Project_07'''

import graphicsPlus as gr
import random

#making a global list so that I can randomly add colors to my objects
colors = ['Red', 'Blue', 'Yellow', 'Green']


class Ball(object):
    '''this class initializes a ball, it has the draw, get/set position, get/set velocity, get/set acceleration, get/set mass, get/set radius, and the update methods'''
    def __init__(self, win):
        #initializing attributes of a ball
        self.mass = 1
        self.radius = 1
        self.pos = [0, 0]
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.win = win
        self.Scale = 10
        self.Vis = [gr.Circle(gr.Point(self.pos[0]*self.Scale, win.getHeight()-(self.pos[1]*self.Scale)), self.radius*self.Scale )]
        self.color = self.Vis[0].setFill(colors[random.randint(0, 3)])

    def draw(self):
        '''this function draws a ball onto the window''' 
        for item in self.Vis:
            item.draw(self.win)
            
    def getPosition(self):
        '''this function returns a copy of the coordinates of the ball'''
        return self.pos[:]

    def setPosition(self, px, py):
        '''this function sets the coordinates of the position of the ball'''
        x_old = self.pos[0]
        y_old = self.pos[1]

        self.pos[0] = px
        self.pos[1] = py

        dx = (px-x_old)*self.Scale
        dy = (py-y_old)*self.Scale*-1

        for item in self.Vis:
            item.move(dx, dy)
    
    def getVelocity(self):
        '''this function returns a copy of the velocity values of a ball'''
        return self.velocity[:]

    def setVelocity(self, vx, vy):
        '''this function assigns the velocity values to a ball'''
        self.velocity[0] = vx
        self.velocity[1] = vy
    
    def getAcceleration(self):
        '''this function returns the acceleration values of a ball in the x and y dimension'''
        return self.acceleration[:]
    
    def setAcceleration(self, ax, ay):
        '''this function sets the acceleration values of a ball in the x and y dimension'''
        self.acceleration[0] = ax
        self.acceleration[1] = ay
    
    def getMass(self):
        '''this function returns the mass of the ball'''
        return self.mass*self.Scale

    def setMass(self, m):
        '''this function sets the mass of the ball'''
        self.mass = m
        
    def getRadius(self):
        '''this function returns a copy of the radius of the ball'''
        y = self.Vis[:]
        radius = self.radius*self.Scale
        return radius
    
    def setRadius(self, r):
        '''this function sets the radius of the ball'''
        self.undraw()
        self.Vis[1] = r
        for item in self.Vis:
            item.draw(win)

    def update(self, dt): #time step dt
        '''this function updates the position and velocity of the ball based on physics equations'''
        x_old = self.pos[0]
        y_old = self.pos[1]

        x_new = (x_old + self.velocity[0]*dt + 0.5*self.acceleration[0]*dt*dt)
        y_new = (y_old + self.velocity[1]*dt + 0.5*self.acceleration[1]*dt*dt)

        self.pos[0] = x_new
        self.pos[1] = y_new

        dx = (x_new - x_old)*self.Scale
        dy = -1*(y_new - y_old)*self.Scale

        for item in self.Vis:
            item.move(dx, dy)

        x_velocity = self.velocity[0] + (self.acceleration[0]*dt)
        y_velocity = self.velocity[1] + (self.acceleration[1]*dt)

        self.velocity[0] = x_velocity
        self.velocity[1] = y_velocity

class Block(object):
    '''this class initializes a block(rectangle), it has the draw/undraw, get/set position, get/set velocity, get/set acceleration, get/set mass, get width/height, and the update methods'''
    def __init__(self, win):
        '''this fucntion initializes a Block with its attributes'''
        self.mass = 1
        self.dx = 1
        self.dy = 1
        self.pos = [0, 0]
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.win = win
        self.Scale = 10
        self.Vis = [gr.Rectangle(gr.Point(self.pos[0]*self.Scale - 0.5*self.Scale, win.getHeight() - (self.pos[0]*self.Scale - 0.5*self.Scale)), gr.Point(self.pos[0]*self.Scale + 0.5*self.Scale, win.getHeight() - (self.pos[0]*self.Scale + 0.5*self.Scale)))]
        self.color = self.Vis[0].setFill(colors[random.randint(0, 3)])

    def draw(self):
        '''this function draws the block'''
        for item in self.Vis:
            item.draw(self.win)
    
    def undraw(self):
        '''and this function undraws the block'''
        for item in self.Vis:
            item.undraw()
    
    def getPosition(self):
        '''this function returns a copy of the coordinates of the block'''
        return self.pos[:]

    def setPosition(self, px, py):
        '''this function sets the position coordinates to px and py'''
        x_old = self.pos[0]
        y_old = self.pos[1]

        self.pos[0] = px
        self.pos[1] = py

        dx = (px - x_old)*self.Scale
        dy = (py - y_old)*self.Scale*-1

        for item in self.Vis:
            item.move(dx, dy)
        
    def getVelocity(self):
        '''this function returns a copy of the velocity value'''
        return self.velocity[:]

    def setVelocity(self, vx, vy):
        '''this function setss the velocity value to vx and vy'''
        self.velocity[0] = vx
        self.velocity[1] = vy

    def getAcceleration(self):
        '''this function returns a copy of the acceleration values'''
        return self.acceleration[:]

    def setAcceleration(self, ax, ay):
        '''this function sets the acceleration values to ax and ay'''
        self.acceleration[0] = ax
        self.acceleration[1] = ay

    def getWidth(self):
        '''this function returns the width of the rectangle'''
        return self.dx*self.Scale

    def getHeight(self):
        '''this function returns the height of the box'''
        return self.dy*self.Scale

    def update(self, dt):
        '''this function updates the box's coordinates and velocity using physics equations'''
        x_old = self.pos[0]
        y_old = self.pos[1]

        x_new = (x_old + self.velocity[0]*dt + 0.5*self.acceleration[0]*dt*dt)
        y_new = (y_old + self.velocity[1]*dt + 0.5*self.acceleration[1]*dt*dt)

        dx = (x_new - x_old)*self.Scale
        dy = -1*(y_new - y_old)*self.Scale

        for item in self.Vis:
            item.move(dx, dy)

        x_velocity = self.velocity[0] + (self.acceleration[0]*dt)
        y_velocity = self.velocity[1] + (self.acceleration[1]*dt)

        self.velocity[0] = x_velocity
        self.velocity[1] = y_velocity




        