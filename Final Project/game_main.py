'''Abdullah Shahzad 
12/11/2021
CS 152 B
Project 10'''

'''this file contains the main function for running the game'''

#import statements, all of them:
import random
import graphicsPlus as gr
import phy_obs_final as pho
import collision
import game_functs as gg 
import new_coll as coll

def main():
    '''this is the main function of the  car game'''

    color = input('Choose a color for your car:') #the user input statement that allows them to pick a color

    coin_counter = 0 #initializing the number of coins collected to zero

    #creating a window for the game and giving it the grey maine sky as a background
    win = gr.GraphWin('Bumpy Ride', 900, 700, False)
    win.setBackground('grey')
    
    #iterating through the shapes list to make the floor and any other objects
    shapes = gg.perm_obstacles(win)
    for shape in shapes:
        shape.draw()

    #down time and initial frame
    dt = 0.00075
    frame = 0

    #creating our car
    ball = pho.Car(win)
    ball.set_color(None)
    ball.set_position(-5, 22)
    ball.set_velocity(10,-5)
    ball.set_acceleration(0, 0)
    ball.set_color(color)
    ball.draw()

    #initializing our other functions as values of variables so that I can reference them later
    coin_label = gg.coin_generator(win)
    lives_label = gg.lives(win)
    coin_count_reset = gg.coin_counter(win, coin_counter)
     
    #looping infinitely
    while True:

        if frame%10 == 0:
            win.update()
        
        if win.checkKey() == 'w': #how the user controls if the car jumps
            ball.set_velocity(20, 70)
            ball.set_acceleration(5, -300)

        #intializing the obstacle course
        obs = gg.temp_obstacles(win)
        #checking if the car collides with any of the objects
        coll.collider2(win, ball, obs, lives_label, coin_counter)
        #just a check for the speed of the car when it lands
        if ball.get_position()[1] < 21:
            ball.set_acceleration(0, 0)
        #getting the position of the car to see if its leaving the screen in the following code
        pos = ball.get_position()

        #checking to see if the car is out of the window, if it is, these conditionals replace the ball at the left side to make it seem like you changed levels
        if pos[0]*ball.Scale > win.getWidth() or pos[1]*ball.Scale> win.getHeight():
            ball.set_position(-5, 22)
            ball.set_velocity(30, -5)
            #im undrawing the ibjects in every iteration of the level so that it'd be easy to add more orientations for the obstacles
            for k in range(4):
                obs[k].undraw()
            obs = gg.temp_obstacles(win)

            #this is how i keep count of the coins collected, if they're collected, they're undrawn and their drawn stats is == False
            for i in range(5):
                if coin_label[i].drawn==True:
                    continue
                else:
                    coin_counter+=1
            coin_count_reset = gg.coin_counter(win, coin_counter,coin_count_reset)
            
            #this undraws all the coins and then redraws them in a different, random orientation
            for i in range(5):
                coin_label[i].undraw()
            coin_label = gg.coin_generator(win)

        
        #this sees if the car has collided with the coins
        for m in range(5):
            coll.collider(win, ball, coin_label[m])
        
        #this code is important for the car-floor collision
        collided = False

        if collision.collision(ball, shapes[0], dt) == True:
            collided = True

        if collided == False:
            ball.update(dt)
        
        frame += 10
    win.close() #closing the window on our way out
    
if __name__ == '__main__': #only runs if its called from here
    main()

