'''Abdullah Shahzad
11/3/2021
CS 152 B
Project 8'''

import random
import graphicsPlus as gr
import physics_objects as pho
import collision

def buildObstacles(win):
    '''this function sets up the obstacles in the course'''
    obstacles = [pho.Block(win), pho.Block(win), pho.Block(win), pho.Block(win), pho.Block(win), pho.Triangle(win), pho.Triangle(win), pho.Triangle(win), pho.Triangle(win), pho.Triangle(win), pho.Triangle(win)]

    #coding the walls of the program
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
    
    obstacles[3].set_width(10)
    obstacles[3].set_height(700)
    obstacles[3].set_position(65,35)
    obstacles[3].set_elasticity(0.8)
    obstacles[3].set_color((0,0,0))

    obstacles[4].set_width(10)
    obstacles[4].set_height(700)
    obstacles[4].set_position(5,35)
    obstacles[4].set_elasticity(0.8)
    obstacles[4].set_color((0,0,0))

    #coding the cones on the road into the program

    obstacles[5].set_radius(1.5)
    obstacles[5].set_color((255,140,0))
    obstacles[5].set_position(35, random.randint(10,65))

    obstacles[6].set_radius(1.5)
    obstacles[6].set_color((255,140,0))
    obstacles[6].set_position(15, random.randint(10,65))

    obstacles[7].set_radius(1.5)
    obstacles[7].set_color((255,140,0))
    obstacles[7].set_position(25, random.randint(10,65))

    obstacles[8].set_radius(1.5)
    obstacles[8].set_color((255,140,0))
    obstacles[8].set_position(45, random.randint(10,65))

    obstacles[9].set_radius(1.5)
    obstacles[9].set_color((255,140,0))
    obstacles[9].set_position(55, random.randint(10,65))

    obstacles[10].set_radius(1.5)
    obstacles[10].set_color((255,140,0))
    obstacles[10].set_position(30, random.randint(10,65))
    return obstacles


def main():
    '''this function is the main function of the project, it sets up the window, the obstacles, the car, and models the collisions'''
    win = gr.GraphWin('Traffic', 700, 700, False) #making a window

    win.setBackground('grey') #setting the bg color

    shapes = buildObstacles(win) #assigning the result of calling buildObstacles to shapes
    for shape in shapes: #looping over every obstacle
        shape.draw() #drawing the obstacle

    dt = 0.002
    frame = 0

    #drawing the car that we will be playing with
    ball = pho.Car(win)
    ball.set_color(1)
    ball.set_position(35, 5)
    ball.set_velocity(random.randint(-5,5), random.randint(4, 10))
    ball.set_acceleration(0, 5)
    ball.draw()

    #drawing all of the enemy cars
    ball1 = pho.Car(win)
    ball1.set_position(15, 65)
    ball1.set_velocity(random.randint(-5,5), -10)
    ball1.set_acceleration(0, -1)
    ball1.draw()

    ball2 = pho.Car(win)
    ball2.set_position(25, 65)
    ball2.set_velocity(random.randint(-5,5), -10)
    ball2.set_acceleration(0, -3)
    ball2.draw()

    ball3 = pho.Car(win)
    ball3.set_position(35, 65)
    ball3.set_velocity(random.randint(-5,5), -10)
    ball3.set_acceleration(0, -3)
    ball3.draw()

    ball4 = pho.Car(win)
    ball4.set_position(45, 65)
    ball4.set_velocity(random.randint(-5,5), -10)
    ball4.set_acceleration(0, -3)
    ball4.draw()

    ball5 = pho.Car(win)
    ball5.set_position(55, 65)
    ball5.set_velocity(random.randint(-5,5), -10)
    ball5.set_acceleration(0, -3)
    ball5.draw()
    
    new_obstacles = [ball1, ball2, ball3, ball4, ball5] #putting all of the enemy cars into a list
    
    while True: #infinite loop

        if win.checkKey() == 'w': #control for the game
            ball.set_velocity(random.randint(-10, 10), -10)
            ball.set_acceleration(0, 20)
        else:


            if frame%10 == 0:
                win.update()
            if win.checkKey() == 'q':
                break
            
            pos = ball.get_position()
            #checks if the ball has passed the top of the screen and indicates to a user that they won
            if pos[0]*ball.Scale > win.getWidth() or pos[1]*ball.Scale > win.getHeight():
                message = gr.Text(gr.Point(350, 350), 'You Won!')
                message.setFill('Yellow')
                message.setSize(30)
                message.draw(win)
                message2 = gr.Text(gr.Point(350, 400), "Press 'q' to quit game")
                message2.setFill('Black')
                message2.setSize(10)
                message2.draw(win)
                if win.checkKey() == 'q':
                    break

        
            if pos[0]*ball.Scale < 0 or pos[1]*ball.Scale < 0:
                message = gr.Text(gr.Point(350, 350), 'You Won!')
                message.setFill('Yellow')
                message.setSize(30)
                message.draw(win)
                message2 = gr.Text(gr.Point(350, 300), "Press 'q' to quit game")
                message2.setFill('Black')
                message2.setSize(10)
                message2.draw(win)
                if win.checkKey() == 'q':
                    break

            collided = False
            #mapping the collisions of every ball with the first list of obstacles
            for shape in shapes:
                if collision.collision(ball, shape, dt) == True:
                    collided = True
                
            if collided == False:
                ball.update(dt)

            for shape in shapes:
                if collision.collision(ball1, shape, dt) == True:
                    collided = True
                    
            if collided == False:
                ball1.update(dt)

            for shape in shapes:
                if collision.collision(ball2, shape, dt) == True:
                    collided = True
                    

            if collided == False:
                ball2.update(dt)

            for shape in shapes:
                if collision.collision(ball3, shape, dt) == True:
                    collided = True

            if collided == False:
                ball3.update(dt)
                    
            for shape in shapes:
                if collision.collision(ball4, shape, dt) == True:
                    collided = True
                    

            if collided == False:
                ball4.update(dt)

            for shape in shapes:
                if collision.collision(ball5, shape, dt) == True:
                    collided = True
                    

            if collided == False:
                ball5.update(dt)

            collided = False

            #mapping the collisions of all the enemy cars with our car
            for shape in new_obstacles:
                if collision.collision(ball, shape, dt) == True:
                    collided = True

            if collided == False:
                ball.update(dt)

            frame += 1
    win.close() #closing the window on our way out
if __name__ ==  '__main__':
    main()
    