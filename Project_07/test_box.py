'''Abdullah Shahzad
CS 152 B
11/1/2021
Lab & Project_07'''

import physics_objects as pho
import graphicsPlus as gr
import random
import time

def main():
    '''main function for this test code that tests if my box maker works'''
    win = gr.GraphWin( "Ball test", 500, 500, False)

    #making a block
    block = pho.Block(win)
    block.setPosition(25, 25)
    block.setVelocity(10, 10)

    block.draw()

    dt = 0.1
    #looing until someone clicks
    while win.checkMouse() == None:
	    block.update(dt) 
	    time.sleep(dt)
	    block.setVelocity( random.randint(-10,10), random.randint(-10,10) )
	    win.update()

    win.getMouse()
    win.close()
if __name__ == "__main__":
    main()