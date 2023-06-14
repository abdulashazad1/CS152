'''Abdullah Shahzad
11/1/2021
CS 152 B
Lab & Project_07'''

import graphicsPlus as gr
import time
import random  

def main():
    '''this function makes a window and a circle, it then waits for the user to click.
    When the user clicks, it closes the window and prints the coordinates of the click to the terminal'''

    win = gr.GraphWin("My First Window!", 500, 500, False) #making a new window and assigning it to the variable win
    point = gr.Point(100, 200) #assigning coordinates to a variable 'point' on the window
    circle = gr.Circle(point, 10) #making a circle with the center 'point' and radius 10
    circle.draw(win) #drawing the circle in the window
    win.update() #updating the window to make a circle while in the middle of the function

    pos = win.getMouse() #gets the coordinates of the mouse cursor from the user's click
    print('X = '+str(pos.getX())) #uses dot operator and get X to get the x coordinate of the cursor
    print('Y = '+str(pos.getY())) #the same as above but for y coordinates
    win.close() #closes the window
#main()


def test2():
    win = gr.GraphWin('My Second Window!', 500, 500, False) #making a new window
    shapes = [] #assigning an empty list to shapes

    while True: #loops while condition is True which means that the loop doesn't stop
        pos = win.checkMouse() #this is different from the getmouse() function because it doesn't wait for the user, if the user doesn't click, it returns 'None'
        if pos != None: #conditional making sure that pos has a value since checkmMouse() returns 'None' instances
            circle = gr.Circle(pos, 10) #makes a circle, the center is where the user clicks and the radius is 10

            #colors extension
            colors = ['Red', 'Blue', 'Yellow', 'Green']            
            circle.setFill(colors[random.randint(0, 3)]) #colors the circle Blue
            shapes.append(circle) #appends each circle made in the loop to shapes
            circle.draw(win) #draws a circle to the window
        #this code would let us break out of the function by pressing q
        user_key = win.checkKey() 
        if user_key == 'q':
            break

        win.update() #updates the window
        time.sleep(0.033) #delay of 0.033 seconds before a circle is drawn
        for shape in shapes: #looping over every circle
            shape.move(random.randint(-3, 3), random.randint(-3, 3)) #making the shape move +-3 units
    win.close() #closes the window
if __name__ == '__main__': 
    test2() #function call
