# Bruce A. Maxwell
# Fall 2015
# CS 151S Project 10
#
# First Test function for the RotatingBlock class
#
# Modified by Eric Aaron, Fall 2018
# Modified by Bruce Maxwell, Fall 2019

import graphicsPlus as gr
import new_physics_objects as pho
import math
import time

# Test function that rotates a block around its center a full rotation
def test():
    win = gr.GraphWin('rotator', 500, 500, False)

    block = pho.RotatingBlock(win,  25, 25, 20, 10)
    block.draw()
    block.setAngle(45)

    dt = 0.02
    for i in range(360):
        block.rotate(1)
        win.update()
        time.sleep(0.01)
            
        if win.checkMouse() != None:
            break

    win.getMouse()
    win.close()

if __name__ == "__main__":
    test()
    
