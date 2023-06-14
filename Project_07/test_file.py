'''Abdullah Shahzad
CS 152 B
11/1/2021
Lab & Project_07'''

'''on running this file, users will be prompted in the command prompt to pick which direction to throw the ball to with the keys 'wasd', they can also enter r and get a random direction'''

import graphicsPlus as gr
import physics_objects as pho
import random
import time

def main():
    '''main function for implementing the test code'''
    
    win = gr.GraphWin("Falling Objects", 500, 500, False)
    
    #assigning variables to the ccenter placement so if someone decides to change the dimensions of the window, they don't have to change all that code.
    x_center = (win.getWidth()/20)
    y_center = (win.getHeight()/20)
    ball = pho.Ball(win)
    ball.setPosition(x_center, y_center)
    ball.draw()

    a = input('Pick a direction:')
    if a == 'w':
        ball.setVelocity(0, 30)
    if a == 's':
        ball.setVelocity(0, 0)
    if a == 'd':
        ball.setVelocity(5, 15)
    if a == 'a':
        ball.setVelocity(-5, 15)
    if a =='r':
        ball.setVelocity(random.randint(-30,30), random.randint(-30, 30))
    ball.setAcceleration(0, -20)

    

    #making a ball in the center of the window
    
    #making box 1
    box = pho.Block(win)
    box.setPosition(19, 6)
    box.draw()
    #making box 2
    box2 = pho.Block(win)
    box2.setPosition(25, 6)
    box2.draw()
    #making box 3
    box3 = pho.Block(win)
    box3.setPosition(31,6)
    box3.draw()
    #making box 4
    box4 = pho.Block(win)
    box4.setPosition(37,6)
    box4.draw()
    #making box 5
    box5 = pho.Block(win)
    box5.setPosition(13,6)
    box5.draw()
    #making box 6
    box6 = pho.Block(win)
    box6.setPosition(7,6)
    box6.draw()
    #making box 7
    box7 = pho.Block(win)
    box7.setPosition(43, 6)
    box7.draw()


    #need to fix falling effect and recenter call
    dt = 0.033
    while True:
        #updating all boxes and the ball
        box.update(dt)
        box2.update(dt)
        box3.update(dt)
        box4.update(dt)
        box5.update(dt)
        box6.update(dt)     
        box7.update(dt)   
        ball.update(dt)
        time.sleep(dt)

        if win.checkKey() == 'q':
            break
        elif win.checkMouse():
            break
        
        #retrieving the positions of all the boxes and the ball
        box_pos = box.getPosition()
        ball_pos = ball.getPosition()
        box2_pos = box2.getPosition()
        box3_pos = box3.getPosition()
        box4_pos = box4.getPosition()
        box5_pos = box5.getPosition()
        box6_pos = box6.getPosition()
        box7_pos = box7.getPosition()

        #seeing if the ball intersects with any of the boxes
        dx = box_pos[0] - ball_pos[0]
        dy = box_pos[1] - ball_pos[1]

        dx2 = box2_pos[0] - ball_pos[0]
        dy2 = box2_pos[1] - ball_pos[1]

        dx3 = box3_pos[0] - ball_pos[0]
        dy3 = box3_pos[1] - ball_pos[1]

        dx4 = box4_pos[0] - ball_pos[0]
        dy4 = box4_pos[1] - ball_pos[1]

        dx5 = box5_pos[0] - ball_pos[0]
        dy5 = box5_pos[1] - ball_pos[1]

        dx6 = box6_pos[0] - ball_pos[0]
        dy6 = box6_pos[1] - ball_pos[1]

        dx7 = box7_pos[0] - ball_pos[0]
        dy7 = box7_pos[1] - ball_pos[1]

        #if they do intersect, these conditionals work to delete the box the ball intersects with
        if abs(dx) <= (ball.getRadius()/10 + box.getHeight()/20) and abs(dy) <= (ball.getRadius()/10 + box.getHeight()/20):
            box.undraw()
            #extension commented out
            ball.setVelocity(random.randint(-10, 10), 20)
            ball.setAcceleration(0, -20)
       
        elif abs(dx2) <= (ball.getRadius()/10 + box2.getHeight()/20) and abs(dy2) <= (ball.getRadius()/10 + box2.getHeight()/20):
            box2.undraw()
            ball.setVelocity(random.randint(-10, 10), 20)
            ball.setAcceleration(0, -20)
        elif abs(dx3) <= (ball.getRadius()/10 + box3.getHeight()/20) and abs(dy3) <= (ball.getRadius()/10 + box3.getHeight()/20):
            box3.undraw()
            ball.setVelocity(random.randint(-10, 10), 20)
            ball.setAcceleration(0, -20)
        elif abs(dx4) <= (ball.getRadius()/10 + box4.getHeight()/20) and abs(dy4) <= (ball.getRadius()/10 + box4.getHeight()/20):
            box4.undraw()
            ball.setVelocity(random.randint(-10, 10), 20)
            ball.setAcceleration(0, -20)
        elif abs(dx5) <= (ball.getRadius()/10 + box5.getHeight()/20) and abs(dy5) <= (ball.getRadius()/10 + box5.getHeight()/20):
            box5.undraw()
            ball.setVelocity(random.randint(-10, 10), 20)
            ball.setAcceleration(0, -20)
        elif abs(dx6) <= (ball.getRadius()/10 + box6.getHeight()/20) and abs(dy6) <= (ball.getRadius()/10 + box6.getHeight()/20):
            box6.undraw()
            ball.setVelocity(random.randint(-10, 10), 20)
            ball.setAcceleration(0, -20)
        elif abs(dx7) <= (ball.getRadius()/10 + box7.getHeight()/20) and abs(dy7) <= (ball.getRadius()/10 + box7.getHeight()/20):
            box7.undraw()
            ball.setVelocity(random.randint(-10, 10), 20)
            ball.setAcceleration(0, -20)
        
        pos = ball.getPosition()
        
        #checking to see if the ball is out of the window, if it is, these conditionals replace the ball at the center
        if pos[0]*ball.Scale > win.getWidth() or (ball.getPosition()[1]*ball.Scale) > win.getHeight():
            ball.setPosition(x_center, y_center)
            ball.setVelocity(random.randint(-30, 30), random.randint(-30, 30))
            ball.setAcceleration(0, -20)

        if pos[0]*ball.Scale < 0 or (ball.getPosition()[1]*ball.Scale) < 0:
            ball.setPosition(x_center, y_center)
            ball.setVelocity(random.randint(-30, 30), random.randint(-30, 30))
            ball.setAcceleration(0, -20) 
            

    win.close() #closing the window on my way out

if __name__ == "__main__":
    main()
