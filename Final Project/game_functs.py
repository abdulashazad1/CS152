'''Abdullah Shahzad 
12/11/2021
CS 152 B
Project 10'''

#import statements below:
import random as rand
import graphicsPlus as gr
import phy_obs_final as pho
import collision
import random as rand
import time


def game_over(win, ball, coin_counter):
    '''this function prints appropriate messages when the game ends'''
    #stopping the ball to end the game
    ball.set_velocity(0, 0) 
    ball.set_acceleration(0, 0)
    #messages to print when the game ends
    message = gr.Text(gr.Point(450, 350), 'Game Over')
    message.setFill('Red')
    message.setSize(30)
    message.draw(win)
    message2 = gr.Text(gr.Point(450, 400), "Your Score:"+ str(coin_counter))
    message2.setFill('Black')
    message2.setSize(15)
    message2.draw(win)


def perm_obstacles(win):
    '''this function initializes the obstacles that'll be showing up in the game. all the obstacles made in this function don't need to be reset'''
    #list of all the obstacles to help arrange them
    obstacles = [pho.Block(win), pho.Ball(win), pho.Ball(win), pho.Ball(win), pho.Ball(win), pho.Ball(win), pho.Ball(win), pho.Ball(win), pho.Ball(win), pho.Ball(win), pho.Ball(win), pho.Ball(win), pho.Ball(win), pho.Ball(win), pho.Ball(win)]
    #assignign attributes to the obstacles like sizes and positions and drawing them onto the screen
    obstacles[0].set_width(750)
    obstacles[0].set_height(20)
    obstacles[0].set_position(350, 10)
    obstacles[0].set_elasticity(0.001)
    obstacles[0].set_color((34,139,34))
    
    obstacles[1].set_radius(1)
    obstacles[1].set_position(3, 69)
    obstacles[1].set_color((255,215,0))

    #for loop to loop over the snowflakes and draw them randomly onto the screen, this is convenient because they're so small and so many
    for i in range(2, 15):
        obstacles[i].set_radius(0.2) #life 3
        obstacles[i].set_position(rand.randint(0,89), rand.randint(24, 89))
        obstacles[i].set_color((255,255,255))

    return obstacles #coded in this return to undraw things if i wanted to while developing the game


def coin_generator(win):
    '''this function generates coins in every iteration of the game level, it also positions them randomly in one of 5 preset positions that I designed''' 
    #lists of lists of presset positions 
    pos_list1 = [[38,25], [41,28], [44,25], [69,22], [71,22]] 
    pos_list2 = [[10,22], [12,22], [14,22], [61,26], [61,28]] 
    pos_list3 = [[10,22], [15,22], [25,22], [35,22], [70,22]] 
    pos_list4 = [[12,22], [14,22], [16,22], [54,22], [56,22]] 
    pos_list5 = [[10,22], [12,22], [59,25], [61,27], [63,25]] 
    #list of all the presets to access them randomly with random.randint
    pos_list_list = [pos_list1, pos_list2, pos_list3, pos_list4, pos_list5]
    list_randomizer = pos_list_list[rand.randint(0,4)]
    #all the coins designed with indexes to my list of preset positions, i guess i could've put them in a for loop but i was wired when i typed this out
    coin = pho.Ball(win)
    coin.set_radius(0.7)
    coin.set_color((255, 215,0))
    coin.set_position(list_randomizer[0][0], list_randomizer[0][1])
    coin.draw()

    coin_2 = pho.Ball(win)
    coin_2.set_radius(0.7)
    coin_2.set_color((255, 215,0))
    coin_2.set_position(list_randomizer[1][0], list_randomizer[1][1])
    coin_2.draw()

    coin_3 = pho.Ball(win)
    coin_3.set_radius(0.7)
    coin_3.set_color((255, 215,0))
    coin_3.set_position(list_randomizer[2][0], list_randomizer[2][1])
    coin_3.draw()

    coin_4 = pho.Ball(win)
    coin_4.set_radius(0.7)
    coin_4.set_color((255, 215,0))
    coin_4.set_position(list_randomizer[3][0], list_randomizer[3][1])
    coin_4.draw()

    coin_5 = pho.Ball(win)
    coin_5.set_radius(0.7)
    coin_5.set_color((255, 215,0))
    coin_5.set_position(list_randomizer[4][0], list_randomizer[4][1])
    coin_5.draw()

    return [coin, coin_2, coin_3, coin_4, coin_5] #returning the list of coins because i want to undraw them at the end of every level


def coin_counter(win, coin_counter, message = None):
    '''this function updates the users score at the top left of the screen after they finish every game level'''
    #seeing if there is already a score on the top left of the screen, if there is one, it undraws it
    if message != None:
        message.undraw()
    #writing the new score in the same position according to the player's latest score
    message = gr.Text(gr.Point(50, win.getHeight()-680), coin_counter)
    message.setFill('White')
    message.setSize(10)
    message.draw(win)

    return message #returning the message so that i can use it in the parameter of this same function


def lives(win):
    '''this function draws the three traffic light like circles at the top right, these are the player's lives'''
    obstacles = [pho.Ball(win), pho.Ball(win), pho.Ball(win)]

    obstacles[0].set_radius(1) #life 1
    obstacles[0].set_position(87, 69)
    obstacles[0].set_color((0,200,0))
    obstacles[0].draw()

    obstacles[1].set_radius(1) #life 2
    obstacles[1].set_position(84, 69)
    obstacles[1].set_color((255,165,0))
    obstacles[1].draw()

    obstacles[2].set_radius(1) #life 3
    obstacles[2].set_position(81, 69)
    obstacles[2].set_color((255,0,0))
    obstacles[2].draw()

    return obstacles #returning the list of obstacles because i want to undraw the lives when the user bumps into an obstacle

def temp_obstacles(win):
    '''this function generates the obstacles in the course that can affect the number of lives of the player'''

    obstacles = [pho.Tree(win), pho.Tree(win), pho.Triangle(win), pho.Triangle(win)] #a list of the obstacles

    obs_pos1 = [[20,22], [40,22], [60,21.5], [80,21.5]] 

    obstacles[0].set_position(obs_pos1[0][0], obs_pos1[0][1])

    obstacles[1].set_position(obs_pos1[1][0], obs_pos1[1][1])
    
    obstacles[2].set_radius(1.2)
    obstacles[2].set_color((255,140,0))
    obstacles[2].set_position(obs_pos1[2][0], obs_pos1[2][1])

    obstacles[3].set_radius(1.2)
    obstacles[3].set_color((255,140,0))
    obstacles[3].set_position(obs_pos1[3][0], obs_pos1[3][1])

    for o in range(4): #iterating over the obstacles to draw them
        if obstacles[o].drawn == False:
            obstacles[o].draw()
        else:
            break
    
    return obstacles





    










    
