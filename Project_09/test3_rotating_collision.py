# Bruce A. Maxwell
# Fall 2015
# CS 151S Project 10
#
# third test function for RotatingBlock, testing collisions
#
# Updated for Python3 by Caitrin Eaton
# 15 November 2017
#
# Modified by Eric Aaron, Fall 2018, Spring 2019
# Modified by Bruce Maxwell, Fall 2019

import graphicsPlus as gr
import new_physics_objects as pho
import new_collision as coll
import math
import time

            
def test():
    # Create a window, rotating block, and ball
    win = gr.GraphWin('rotator', 500, 500, False)

    block = pho.RotatingBlock(win, 25, 25, 20, 10)
    block.draw()
    block.setRotVelocity(108)

    ball = pho.Ball(win)
    ball.setPosition(30, 45)
    ball.setAcceleration(0, -10)
    ball.draw()

    # execute an update loop, checking for collisions
    dt = 0.02
    for i in range(400):
        block.update(dt)
        
        if coll.collision(ball, block, dt):
            print('collision')
        else:
            ball.update(dt)

        if i % 10:
            win.update()
            time.sleep(0.01)
            
        if win.checkMouse() != None:
            break

    # wait for a mouse click to quit
    win.getMouse()
    win.close()

if __name__ == "__main__":
    test()
    
