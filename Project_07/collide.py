'''Abdullah Shahzad
CS 152 B
11.2.2021
Project_07'''

#compute dx and dy between object centers
#h/2 is d bw edge and center, rad is dist between edge and center
#assume circle as square
#condition at touch = collision
#dy between object centers is <= radius + h/2
#dx between object centers is <= radius + w/2
#collisions from both directions so abs val needed abs(dx) and abs(dy)

import physics_objects as pho
import graphicsPlus as gr
import random
import time

def collider():
    '''this is a simple collision function that collides a ball with a stationary box to demonstrate the principle of collisions'''
    #making a window & a block
    win = gr.GraphWin("Collider", 500, 500, False)
    box = pho.Block(win)
    ball = pho.Ball(win)
    #setting up a block above a ball, giving the ball the initial velocity it needs to collide with that stationary block
    box.setPosition(25, 25)
    ball.setPosition(25, 20)
    ball.setVelocity(0, 1)
    box.draw()
    ball.draw()    
    #distance between centers calculater
    dt = 0.033
    while win.checkMouse() == None:
        ball.update(dt)
        box.update(dt)
        time.sleep(dt)
        win.update()
        box_pos = box.getPosition()
        ball_pos = ball.getPosition()
        
        dx = box_pos[0] - ball_pos[0]
        dy = box_pos[1] - ball_pos[1]

        #if the distance between centers is not enough, the block will undraw itself
        if abs(dx) <= (ball.getRadius()/10 + box.getHeight()/20) and abs(dy) <= (ball.getRadius()/10 + box.getHeight()/20):
            box.undraw()
    
    win.getMouse()
    win.close()
collider()
    
    
        