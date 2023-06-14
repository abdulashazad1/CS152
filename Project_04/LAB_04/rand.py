'''Abdullah Shahzad
9/29/2021
CS 152 B
LAB_04'''

import random as rand #imports the random library with the nickname "rand"
import matplotlib.pyplot as plt

def genNrandom(N):
    ''''''
    numbers = []
    for loop in range(N):
        caller = rand.random()
        numbers.append(caller)
    return numbers

def test1():
    fetch = genNrandom(10)
    for number in fetch:
        print(number)
if __name__ == '__main__':
    test1()


def genNintegers(N, lowBound, upBound):
    ''''''
    numbers = []
    for i in range(N):
        caller = rand.randint(lowBound, upBound)
        numbers.append(caller)
    return numbers

def test2():
    fetch = genNintegers(10, -10, 10)
    print(fetch)
if __name__ == '__main__':
    test2()

def genNnormal(N, mean, std):
    numbers = []
    for i in range(N):
        caller = rand.gauss(mean, std)
        numbers.append(caller)
    return numbers

def test3():
    fetch = genNnormal(10, 0, 0.2)
    print(fetch)
if __name__ == '__main__':
    test3()

#Installing and creating plots with matplotlib
#Plotting some of the numbers i generated with the rand function

def test4():
    x = genNrandom(10)
    print(x)
    z = genNnormal(10, 0, 0.2)
    plt.plot(x, z, 'o')
    plt.show()
if __name__ == '__main__':   
    test4()