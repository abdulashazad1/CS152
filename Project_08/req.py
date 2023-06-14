'''Abdullah Shahzad
11/3/2021
CS 152 B
Project 8'''

'''this file contains code for required element 2'''

#importing all the necessary libraries
import random
import graphicsPlus as gr
import physics_objects as pho
import collision


def buildObstacles(win):
    '''this function returns a list of all the obstacles'''
    #in this file I'll just be using it to code the walls of the window
    obstacles = [pho.Block(win), pho.Block(win), pho.Block(win), pho.Block(win)]

    obstacles[0].set_width(50)
    obstacles[0].set_height(700)
    obstacles[0].set_position(-25,35)
    obstacles[0].set_elasticity(0.8)
    
    obstacles[1].set_width(700)
    obstacles[1].set_height(50)
    obstacles[1].set_position(35,-25)
    obstacles[1].set_elasticity(0.8)
    
    obstacles[2].set_width(50)
    obstacles[2].set_height(700)
    obstacles[2].set_position(95.5,35)
    obstacles[2].set_elasticity(0.8)
    
    obstacles[3].set_width(700)
    obstacles[3].set_height(50)
    obstacles[3].set_position(35,95)
    obstacles[3].set_elasticity(0.8)

    return obstacles

def main():
    '''this function is the main function of the project, it sets up the window, the obstacles, the snowwman, and models the collisions'''
    win = gr.GraphWin('Pinball', 700, 700, False)
    shapes = buildObstacles(win)
    for shape in shapes: #looping over shapes to draw every obstacle
        shape.draw()
    dt = 0.001
    frame = 0

    #drawing the snowman 
    ball = pho.Snowman(win)
    ball.set_radius(1.25)
    ball.set_position(35, 70)
    ball.set_velocity(random.randint(-5,5), random.randint(-5,5))
    ball.set_acceleration(0, 0.1)
    ball.set_color((255, 0, 255))
    ball.draw()

    while True:
        if frame%10 == 0:
            win.update()
        if win.checkKey() == 'q':
            break
        
        collided = False

        for shape in shapes:
            if collision.collision(ball, shape, dt) == True:
                collided = True

        if collided == False:
            ball.update(dt)
        frame += 100
    win.close()
if __name__ ==  '__main__':
    main()