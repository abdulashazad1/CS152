'''Abdullah Shahzad 
12/11/2021
CS 152 B
Project 10'''

#import statements and a color list for a particular set color function that I made in a previous project
import graphicsPlus as gr
import random
colors = ['Red', 'Blue', 'Yellow', 'Green']

'''this file is arranged in the following way: classes are seperated by double line gaps and methods of the same class are seperated by single line gaps
unless there's a # describing somethign abouth the code that follows.'''

class Thing:
    '''this is the parent class for all the simulated objects'''

    def __init__(self, win, the_type):
        '''this function creates an object (the_type) with relevant attributes'''
        '''the input is the GraphWin window for drawing and the_type, which is the name of the shape of the object'''
        self.type = the_type
        self.mass = 1
        self.position = [0, 0]
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.elasticity = 1 #the amount of energy retained after a collision
        self.Scale = 10
        self.win = win
        self.vis = [] #this empty list will hold Zelle graphics objects
        self.color = (0, 0, 0) #an rgb tuple defaulted to black
        self.drawn = False #a boolean indicating whether the shape has been drawn yet

    #creating get methods for Thing class   
    def get_type(self):
        '''this method returns a string with the type of object being drawn'''
        return self.type

    def get_mass(self):
        '''this method returns the mass of the object made'''
        return self.mass

    def get_position(self):
        '''this method returns a tuple with the position of the object'''
        return self.position[:]

    def get_velocity(self):
        '''this method returns a tuple with the velocity of the object'''
        return self.velocity[:]
    
    def get_acceleration(self):
        '''this method returns a tuple with the acceleration values of the object'''
        return self.acceleration[:]

    def get_elasticity(self):
        '''this method returns the elasticity value of an object'''
        return self.elasticity

    def get_scale(self):
        '''this method returns the scale value of the object'''
        return self.Scale

    def get_color(self):
        '''this method returns the rgb value of the color of the object'''
        color = gr.color_rgb(self.color[0], self.color[1], self.color[2])
        return color
        
    #creating draw and undraw methods
    def draw(self):
        '''this method draws the Zelle Graphics object imn self.vis'''
        for item in self.vis:
            item.draw(self.win)
            self.drawn = True
    
    def undraw(self):
        '''this method undraws the Zelle Graphics object in self.vis'''
        for item in self.vis:
            item.undraw()
            self.drawn = False

    #creating set methods for Thing class
    def set_mass(self, m):
        '''this method sets the mass of the object to m, returns nothing'''
        self.mass = m
    
    def set_velocity(self, vx, vy):
        '''this method sets the velocity of the object to vx and vy, returns nothing'''
        self.velocity[0] = vx
        self.velocity[1] = vy

    def set_acceleration(self, ax, ay):
        '''this method sets the acceleration of the object to ax and ay, returns nothing'''
        self.acceleration[0] = ax
        self.acceleration[1] = ay
    
    def set_elasticity(self, e):
        '''this method sets the elasticity of the object to e, returns nothing'''
        self.elasticity = e
    
    def set_position(self, px, py):
        '''this function sets the coordinates of the position of the ball, returns nothing'''
        x_old = self.position[0]
        y_old = self.position[1]
        
        self.position[0] = px
        self.position[1] = py

        dx = (px - x_old)*self.Scale
        dy = (py - y_old)*self.Scale*-1

        for item in self.vis:
            item.move(dx, dy)

    def set_color(self, c): #where c is an rgb tuple
        '''this method sets the color of the object to the rgb values c'''
        self.color = c
        if c != None:
            for item in self.vis:
                item.setFill(gr.color_rgb(c[0], c[1], c[2]))

    #coding the update method for the thing class
    def update(self, dt): 
        '''this function updates the position and velocity of the ball based on physics equations'''
        x_old = self.position[0]
        y_old = self.position[1]

        x_new = (x_old + self.velocity[0]*dt + 0.5*self.acceleration[0]*dt*dt)
        y_new = (y_old + self.velocity[1]*dt + 0.5*self.acceleration[1]*dt*dt)

        self.position[0] = x_new
        self.position[1] = y_new

        dx = (x_new-x_old)*self.Scale
        dy = -1*(y_new-y_old)*self.Scale

        for item in self.vis:
            item.move(dx, dy)

        x_velocity = self.velocity[0] + (self.acceleration[0]*dt)
        y_velocity = self.velocity[1] + (self.acceleration[1]*dt)

        self.velocity[0] = x_velocity
        self.velocity[1] = y_velocity
    
    
class Ball(Thing):
    '''this class interacts with the Thing class to create a ball'''

    def __init__(self, win, r=3, x=1, y=1, c=(100, 150, 200)):
        Thing.__init__(self, win, 'ball')
        self.set_position(x, y)
        self.radius = r
        self.refresh()
        self.set_color(c)

    #the refresh method defines self.vis which is the list that contains the Zelle Graphics Object
    def refresh(self):
        '''this method refreshes the object to its original position on the window'''
        drawn = self.drawn
        pos = self.position
        win = self.win
        if drawn:
            self.undraw()
        self.vis = [gr.Circle(gr.Point(pos[0], win.getHeight()-pos[1]), self.radius*self.Scale)]

        if drawn:
            self.draw()


    #coding methods that are exclusive to the Ball class
    def get_radius(self):
        '''this method returns the radius of the circle'''
        return self.radius

    def set_radius(self, r):
        '''this method sets the radius of the circle to r'''
        self.radius = r
        self.refresh()


class Block(Thing):
    '''this class interacts with the Thing class to create a block/box'''

    def __init__(self, win,x0=0,y0=0,width=20,height=10, color=(250, 250, 0)):
        Thing.__init__(self, win, 'block')
        self.position[0] = x0
        self.position[1] = y0
        self.width = width
        self.height = height
        self.reshape()
        self.set_color(color)
        
    def reshape(self):
        '''this method redraws the shape with the most local self.vis values'''
        win = self.win
        drawn = self.drawn
        pos = self.position
        
        if drawn:
            self.undraw()
        self.vis = [gr.Rectangle(gr.Point(pos[0]-(self.width*self.Scale)/2, win.getHeight()-pos[1]-(self.height*self.Scale)/2), gr.Point(pos[0]+(self.width*self.Scale)/2, win.getHeight()-pos[1]+(self.height*self.Scale)/2))]
        if drawn:
            self.draw()

    #get methods specific to the Block child class
    def get_width(self):
        '''this method returns the width of the rectangle to be/already drawn'''
        return self.width

    def get_height(self):
        '''this method returns the height of the rectangle to be/already drawn'''
        return self.height

    #set methods specific to the Block child class
    def set_width(self, new_width):
        '''this method sets the width of the block to new_width'''
        self.width = new_width
        self.reshape()

    def set_height(self, new_height):
        '''this method sets the heigh of the block to new_height'''
        self.height = new_height
        self.reshape()


class Triangle(Thing):
    '''this class interacts with the thing class to create a triangle'''

    def __init__(self,win,radius=1,c=(250,0,0)):
        Thing.__init__(self, win, 'ball')
        self.rad_from_center = radius
        self.redefine()
        self.set_color(c)

    #update method for the Triangle child class
    def redefine(self):
        '''this method redefines the vertices of the triangle with an updated self.vis value'''
        win = self.win
        drawn = self.drawn
        pos = self.position

        if drawn:
            self.undraw()
        self.vis = [gr.Polygon(gr.Point(pos[0]-(self.rad_from_center*self.Scale), win.getHeight()-(pos[1]-(self.rad_from_center*self.Scale))), gr.Point(pos[0]+(self.rad_from_center*self.Scale), win.getHeight()-(pos[1]-(self.rad_from_center*self.Scale))), gr.Point(pos[0], win.getHeight()-(pos[1]+(self.rad_from_center*self.Scale))))]
        if drawn:
            self.draw()
    
    #get and set methods specific to the Triangle child class, i treat it as a circle
    def get_radius(self):
        '''this method returns the current distance of the center of the tiangle from the vertices'''
        return self.rad_from_center
    
    def set_radius(self, r):
        '''this method redraws the shape with the new radius'''
        self.rad_from_center = r
        self.redefine()
    

class Snowman(Thing):
    '''this class interacts with the Thing class to make a Snowman (1 ball on top of another)'''
    def __init__(self,win,rad=1,c=(255,255,255)):
        Thing.__init__(self, win, 'ball')
        self.rad = rad
        self.recreate()
        self.set_color(c)

    #the update method for the Snowman child class
    def recreate(self):
        '''this method redefines the vertices of the triangle with an updated self.vis value'''
        win = self.win
        drawn = self.drawn
        pos = self.position

        if drawn:
            self.undraw()
        self.vis = [gr.Circle(gr.Point(pos[0], (win.getHeight()-pos[1]+(self.rad*self.Scale))), self.rad*self.Scale), gr.Circle(gr.Point(pos[0], (win.getHeight()-pos[1]-(self.rad*self.Scale))), self.rad*self.Scale)]
        if drawn:
            self.draw()

    #get and set methods specific to the Snowman child class
    def get_radius(self):
        '''this method returns the current distance of the center of the tiangle from the vertices'''
        return self.rad*2

    def set_radius(self, r):
        '''this method redraws the shape with the new radius'''
        self.rad = r
        self.recreate()


class Car(Thing):
    '''this class interacts with the Thing class to create a car'''
    def __init__(self, win, w1=3,h1=1.1,w2=2,h2=1,r=0.4,c=None):
        Thing.__init__(self, win, 'ball')
        self.h1=h1
        self.h2=h2
        self.w1=w1
        self.w2=w2
        self.r=r
        self.redraw()
        self.set_color(c)

    #the update method for the Car child class
    def redraw(self):
        '''this method redraws the car with an updated self.vis value'''
        win = self.win
        drawn = self.drawn
        pos = self.position

        if drawn:
            self.undraw()
        self.vis = [gr.Rectangle(gr.Point(pos[0]-(self.w1*self.Scale)/2, win.getHeight()-(pos[1]-(self.h1*self.Scale)/2)), gr.Point(pos[0]+(self.w1*self.Scale)/2, win.getHeight()-(pos[1]+(self.h1*self.Scale)/2))), gr.Rectangle(gr.Point(pos[0]-(self.w2*self.Scale)/2, win.getHeight()-pos[1]-(self.h1*self.Scale)/2), gr.Point(pos[0]+(self.w2*self.Scale)/2, win.getHeight()-pos[1]-((self.h2+self.h1)*self.Scale)/2)), gr.Circle(gr.Point(pos[0]-((self.w1*self.Scale)/2)*3/4, win.getHeight()-pos[1]+((self.h1*self.Scale)/2)*3/4), self.r*self.Scale), gr.Circle(gr.Point(pos[0]+((self.w1*self.Scale)/2)*3/4, win.getHeight()-pos[1]+((self.h1*self.Scale)/2)*3/4), self.r*self.Scale)]
        if drawn:
            self.draw()

    #coding a seperate set_color method for the car class because it has so many more shapes that need to be a different color
    def set_color(self,c):
        '''this method distinguishes between the friendly (green) and unfriendly (red) cars by giving them these respective colors'''
        self.color = c
        color_list = ['red', 'dark blue', 'pink', 'yellow', 'purple', 'orange']
        color_set = color_list[random.randint(0,5)]
        if c == 1:
            self.vis[0].setFill(color_list[random.randint(0, 5)])
        if c != random:
            self.vis[0].setFill(c)
        self.vis[1].setFill('light blue')
        self.vis[2].setFill('black')
        self.vis[3].setFill('black')
    
    #get and set methods specific to the Car child class
    def get_radius(self):
        '''this method returns the radius (actually the width of the roof of the car'''
        return self.w2-1
        
    def set_radius(self, r):
        '''this method sets the radius (actually the width of the roof of the car'''
        self.w2 = r
        self.redraw()


class Tree(Thing):
    '''this class interacts with the thing class to draw a tree as one of the obstacles for "bumpy ride"'''
    def __init__(self,win,x0=0,y0=0,width=1,height=4,r=1.5,color=None):
        Thing.__init__(self, win, 'block')
        self.position[0] = x0
        self.position[1] = y0
        self.width = width
        self.height = height
        self.radius = r 
        self.reinstantiate()
        self.set_color(color)
    
    #the update method for the Tree child class
    def reinstantiate(self):
        '''this method redraws the shape with the most local self.vis values'''
        win = self.win
        drawn = self.drawn
        pos = self.position
        
        if drawn:
            self.undraw()
        self.vis = [gr.Rectangle(gr.Point(pos[0]-(self.width*self.Scale)/2, win.getHeight()-pos[1]-(self.height*self.Scale)/2), gr.Point(pos[0]+(self.width*self.Scale)/2, win.getHeight()-pos[1]+(self.height*self.Scale)/2)), gr.Circle(gr.Point(pos[0], win.getHeight()-pos[1]-(self.height*self.Scale)/2), self.radius*self.Scale)]
        if drawn:
            self.draw()
     
    #get and set methods specific to the Tree object
    def get_radius(self):
        '''this method returns the current distance of the center of the tiangle from the vertices'''
        return self.radius
    
    def set_radius(self, r):
        '''this method redraws the shape with the new radius'''
        self.radius = r
        self.reinstantiate()

    #a seperate set_color function too because there are two objects that need to be a different color
    def set_color(self,c):
        '''this method colors the tree some very tree colors'''
        if c == None:
            self.vis[0].setFill('brown')
            self.vis[1].setFill('dark green')

    