'''Abdullah Shahzad
CS 152B
12/4/21
Project 9 Extension'''



import graphicsPlus as gr
import new_physics_objects as pho
import new_collision as coll
import math
import time
import rot
            
def test():
    # Create a window, rotating block, and ball
    win = gr.GraphWin('rotator', 500, 500, False)

    block = pho.RotatingPlus(win, 25, 25, 2, 10)
    block.draw()
    block.setRotVelocity(140)

    

    ball = pho.Ball(win)
    ball.setPosition(25, 45)
    ball.setAcceleration(0, -10)
    ball.draw()

    time.sleep(0.08)
        
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