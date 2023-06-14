'''Abdullah Shahzad 
12/11/2021
CS 152 B
Project 10'''

#import statements go here:
import phy_obs_final as pho
import graphicsPlus as gr
import random
import time
import game_functs as gg

def collider(win, ball, coin):
    '''this function checks if the car collided with the coin and deletes the coin off the screen if it did'''
    dt = 0.015
    #while looping for it to check continuously
    while win.checkMouse() == None:
        #updating positions continuously
        ball.update(dt)
        coin.update(dt)
        time.sleep(dt)
        win.update()
        #getting the position of the car and the coin object
        coin_pos = coin.get_position()
        ball_pos = ball.get_position()
        #checking the distance between the x and y coordinates of the coin and car
        dx = coin_pos[0] - ball_pos[0]
        dy = coin_pos[1] - ball_pos[1]

        #if the distance between centers is not enough, the coin will undraw itself
        #i added numbers to the radius values to make the collision look more natural
        if abs(dx) <= (ball.get_radius()+1 + coin.get_radius()+0.2) and abs(dy) <= (ball.get_radius()+1 + coin.get_radius()+0.2):
            coin.undraw()
            break
        else:
            break


def collider2(win, ball, obs, lives, coin_counter):
    '''this function checks if the car collided with the obstacles, it resets the car and deletes a life if it did'''
    dt = 0.015
    #this function is inside a while loop already so i don't need a while loop here
    #checking for each obstacle in the obstacle list returned by perm_obstacles
    for obstacle in obs:
        #updating the positions of the object continuously
        ball.update(dt)
        obstacle.update(dt)
        time.sleep(dt)
        win.update()
        #getting the position of each obstacle and the car
        obs_pos = obstacle.get_position()
        ball_pos = ball.get_position()
        #checking the distance, on both axis, between the car and the obstacles
        dx = obs_pos[0] - ball_pos[0]
        dy = obs_pos[1] - ball_pos[1]

        #if the distance between centers is not enough, the bcar is reset at the start, and a life is deleted
        if abs(dx) <= (ball.get_radius()+1 + obstacle.get_radius()-0.5) and abs(dy) <= (ball.get_radius()+1 + obstacle.get_radius()-0.5):
                ball.set_position(-5, 22.5)
                ball.set_velocity(30, -5)
                if lives[0].drawn == True and lives[1].drawn == True and lives[2].drawn == True:
                    lives[0].undraw()
                elif lives[1].drawn == True and lives[2].drawn == True:
                    lives[1].undraw()
                elif lives[2].drawn == True:
                    lives[2].undraw()
                    #when the lives run out, the game over function is called and the game ends.
                    gg.game_over(win, ball, coin_counter)
