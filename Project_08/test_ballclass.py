# Bruce Maxwell
# Fall 2015
# CS 151S Project 9
#
# ball class test
#
# modified slightly by Eric Aaron for CS 152, Spring '19
# slightly updated by Bruce Maxwell for CS 152, Fall 2019
# simplified the constructor call to just the win variable
# update F2021 by Stacy Doore

import graphicsPlus as gr
import physics_objects as pho
import collision as coll
import time

# create two balls heading towards one another
def main():
    win = gr.GraphWin( 'balls colliding', 800, 700, False )

    ball1 = pho.Ball( win )
    ball2 = pho.Ball( win )
    ball1.set_position( 25, 25 )
    ball2.set_position( 70, 25 )
    print("set ball1 position = (25, 25)")
    print("set ball2 position = (70, 25)")
    ball1.draw()
    ball2.draw()
    # Block = pho.Block( win )
    # Block.setPosition( 30, 20 )
    # Block.draw()

##    Triangle = pho.Triangle( win )
##    Triangle.setPosition( 10, 20 )
##    Triangle.draw()
    # set up velocity and acceleration so they collide
    ball1.set_velocity( 20, 20 )
    ball2.set_velocity( -20, 20 )
    ball1.set_acceleration( 0, -20 )
    ball2.set_acceleration( 0, -20 )
    #ball1.draw()
    #ball2.draw()
    print("drawing ball1 and ball2")


    # loop for some time and check for collisions
    dt = 0.01
    for frame in range(120000000):
        if not coll.collision_ball_ball( ball1, ball2, dt ):
            ball1.update(dt)

        if not coll.collision_ball_ball( ball2, ball1, dt ):
            ball2.update(dt)
        
        if frame % 10 == 0:
            win.update()

        time.sleep(0.5*dt)
        if win.checkMouse() != None:
            break

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
