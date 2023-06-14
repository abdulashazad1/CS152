'''Abdullah Shahzad
11/3/2021
CS 152 B
Project 8'''

import physics_objects as pho
import graphicsPlus as gr
import random
import collision

def buildObstacles(win):
    obstacles = [pho.Block(win), pho.Block(win), pho.Block(win), pho.Block(win), pho.Ball(win), pho.Ball(win), pho.Block(win), pho.Block(win), pho.Ball(win), pho.Ball(win), pho.Ball(win), pho.Ball(win), pho.Triangle(win), pho.Triangle(win), pho.Triangle(win), pho.Block(win), pho.Block(win)]
    #wall positions from left, bottom, right, top

    #obstacles[0].set_width(20)

    obstacles[0].set_width(50)
    obstacles[0].set_height(700)
    obstacles[0].set_position(-25,35)
    obstacles[0].set_elasticity(0.4)
    
    obstacles[1].set_width(700)
    obstacles[1].set_height(50)
    obstacles[1].set_position(35,-25)
    obstacles[1].set_elasticity(0.4)
    
    obstacles[2].set_width(50)
    obstacles[2].set_height(700)
    obstacles[2].set_position(95.5,35)
    obstacles[2].set_elasticity(0.4)
    
    obstacles[3].set_width(700)
    obstacles[3].set_height(50)
    obstacles[3].set_position(35,95)
    obstacles[3].set_elasticity(0.4)

    #coding 2 balls intp the center of the screen
    obstacles[4].set_position(20, 15)
    obstacles[4].set_elasticity(2.0)
    obstacles[5].set_position(50, 15)
    obstacles[5].set_elasticity(2.0)

    #coding two boxes to hang from the sides of the screen
    obstacles[6].set_width(50)
    obstacles[6].set_height(5)
    obstacles[6].set_position(0,50 )
    obstacles[6].set_color((250, 250, 0))

    obstacles[7].set_width(50)
    obstacles[7].set_height(5)
    obstacles[7].set_position(70,50 )
    obstacles[7].set_color((250, 250, 0))

    #coding another 4 smaller balls
    obstacles[8].set_radius(1)
    obstacles[8].set_color((0, 250, 250))
    obstacles[8].set_position(5, 5)
    obstacles[8].set_elasticity(1.5)

    obstacles[9].set_radius(1)
    obstacles[9].set_color((0, 250, 250))
    obstacles[9].set_position(65, 5)
    obstacles[9].set_elasticity(1.5)

    obstacles[10].set_radius(1)
    obstacles[10].set_color((0, 250, 250))
    obstacles[10].set_position(5, 65)
    obstacles[10].set_elasticity(1.5)

    obstacles[11].set_radius(1)
    obstacles[11].set_color((0, 250, 250))
    obstacles[11].set_position(65, 65)
    obstacles[11].set_elasticity(1.5)

    #coding a trianlge
    obstacles[12].set_radius(2)
    obstacles[12].set_color((200,0,0))
    obstacles[12].set_position(35,35)
    obstacles[12].set_elasticity(1)

    obstacles[13].set_color((0,255,255))
    obstacles[13].set_position(30, 5)
    obstacles[13].set_elasticity(1)

    obstacles[14].set_color((0,255,255))
    obstacles[14].set_position(40, 5)
    obstacles[14].set_elasticity(1)

    obstacles[15].set_width(10)
    obstacles[15].set_height(10)
    obstacles[15].set_position(10,35)
    obstacles[15].set_elasticity(0.6)
    obstacles[15].set_color((0,250,50))

    obstacles[16].set_width(10)
    obstacles[16].set_height(10)
    obstacles[16].set_position(60,35)
    obstacles[16].set_elasticity(0.6)
    obstacles[16].set_color((0,250,50))

    return obstacles

def main():
    '''this function is the main function of the project, it sets up the window, the obstacles, the ball, and models the collisions'''
    win = gr.GraphWin('Pinball', 700, 700, False) #making the window for all our graphics
    shapes = buildObstacles(win) #assigning the result of calling buildObstacles to shapes
    for shape in shapes: #looping over shapes and drawing each one
        shape.draw() 
    dt = 0.002
    frame = 0

    #coding the pinball and putting it at the top, in the center
    ball = pho.Ball(win)
    ball.set_radius(1.25)
    ball.set_position(35, 70)
    ball.set_velocity(random.randint(-5,5), random.randint(-5,5))
    ball.set_acceleration(0, -2)
    ball.set_color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    ball.draw()

    while True:
        if win.checkKey() == 'w': #this is part of my extensions, where you cna whack the pinball
            ball.set_velocity(random.randint(-5, 5), 10)
            ball.set_acceleration(0, -3)
        if frame%10 == 0:
            win.update()
        if win.checkKey() == 'q': #lets the user quit by pressing q
            break
        pos = ball.get_position()
        
        #checking to see if the ball is out of the window, if it is, these conditionals replace the ball at the center
        if pos[0]*ball.Scale > win.getWidth() or pos[1]*ball.Scale> win.getHeight():
            ball.set_position(35, 35)
            ball.set_velocity(random.randint(-5,5),random.randint(-5, 5))
            ball.set_acceleration(0, -2)
        #i need to figure out how to color my square, i think 
        if pos[0]*ball.Scale < 0 or pos[1]*ball.Scale < 0:
            ball.set_position(35, 35)
            ball.set_velocity(random.randint(-10,10), random.randint(-5, 5))
            ball.set_acceleration(0, -2)
        
        collided = False
        #modelling the collisions of the ball with any of the obstacles
        for shape in shapes:
            if collision.collision(ball, shape, dt) == True:
                collided = True

        if collided == False:
            ball.update(dt)
        frame += 1
    win.close() #closing the window on our way out
if __name__ ==  '__main__':
    main()


