'''Abdullah Shahzad
10/02/2021
CS 152 B
Project_04'''

import random as rand #imports the random function with the nickname rand
import sys #imports the sys function
import matplotlib.pyplot as plt #imports matplot library for me to plot with
import stats

def initPopulation(num, probFemale): 
    '''This function initializes a penguin population to compute with'''
    population = [] #assigns population to an empty list
    #start of for loop
    for x in range(num):
        random = rand.random() #generates a random number
        if random < probFemale: #conditional1 checking if the generated number is greater than the probability of a penguin being female
            population.append('f') #adds 'f' to the list if conditional1 is true
        if random > probFemale: #conditional2 checking if the generated number is smaller than the probability of a penguin being female
            population.append('m') #adds 'm to the list if conditional2 is true
    return population #returns the population list

#test1
'''def test():
    popsize = 10
    probFemale = 0.5
    pop = initPopulation(popsize, probFemale)
    print( pop )
    return
if __name__ == "__main__":
    test()'''


def simYear(pop, elNinoProb, stdRho, elNinoRho, probFemale, maxCapacity): 
    '''Runs a simulation of 1 year with penguins'''
    #determining if the year is an el nino year:
    enYear = False #default value for el nino year is false
    if elNinoProb > rand.random(): #if the probability of enYear is higher than a randomly generated number, then the year is an enYear
        enYear = True

    newpop = [] #initializes newpop to an empty list
    for penguin in pop: #for each loop going through each item in the list
        if len(newpop) > maxCapacity: #conditional1 checking if the number of items in newpop is greater than maxCapacity
            break #if conditional1 is true, the function breaks out of the loop and executes the next line of code after the loop.
        if enYear == True: #conditional2 checking if it is an enYear
            if rand.random() < elNinoRho: #conditonal inside conditional checking if elNinoRho is greater than a random number
                newpop.append(penguin) #appends the penguin being processed to newpop
        else:
            newpop.append(penguin) #appends penguin being processed to newpop
            if rand.random() < (stdRho - 1.0): #checks if a randomly generated number is less than the growth factor during a standard year - 1.0
                if rand.random() < probFemale: #conditional3 checking if a randomly generated number is smaller than the probability of a penguin being female
                    newpop.append('f') #appends 'f' to newpop if conditional3 is true
                else:
                    newpop.append('m') #if conditional3 isn't true, appends 'm' to the list
    return newpop #returns the new list

#test 2 
'''def test():
    popsize = 10
    probFemale = 0.5
    pop = initPopulation(popsize, probFemale)
    print( pop )

    newpop = simYear(pop, 1.0, 1.188, 0.4, 0.5, 2000)
    print( "El Nino year" )
    print( newpop )

    newpop = simYear(pop, 0.0, 1.188, 0.4, 0.5, 2000)
    print( "Standard year" )
    print( newpop )

    return
if __name__ == "__main__":
    test()'''


def runSimulation(N, initPopSize, probFemale, elNinoProb, stdRho, elNinoRho, maxCapacity, minViable):
    '''Loops over the simYear function to run a simulation for N years'''
    #assigning variables
    population = initPopulation(N, probFemale) 
    endDate = N
    newPop = []
    #FUNCTION WILL RETURN ENDDATE
    for x in range(N):
        newPop = simYear(population, elNinoProb, stdRho, elNinoRho, probFemale, maxCapacity) #calls the simYear function N number of times
        if (newPop.count('m') + newPop.count('f')) < minViable: #if the number of penguins was less than the minimum viable number, the function returns the enddate and breaks out of the loop
            endDate = x
            break
        
        if newPop.count('f') == 0: #if the number of female pengiuns = 0, the function returns the enddate and breaks out of the loop
            endDate = x
            break

        if newPop.count('m') == 0: #if the number of male penguins = 0, the function returns the enddate and breaks out of the loop
            endDate = x
            break

        if (newPop.count('m') + newPop.count('f')) and newPop.count('m') > 0 and newPop.count('f') > 0: #if the number of penguins was more than the minimum viable number and the number of females and males != 0, the function assigns population to newpop
            population = newPop
            
    return endDate #returns endDate

'''def test():
    popsize = 10
    probFemale = 0.5
    pop = initPopulation(popsize, probFemale)
    print( pop )

    newpop = simYear(pop, 1.0, 1.188, 0.4, 0.5, 2000)
    print( "El Nino year" )
    print( newpop )

    newpop = simYear(pop, 0.0, 1.188, 0.4, 0.5, 2000)
    print( "Standard year" )
    print( newpop )

    runSimulation(201, 500, 0.5, 1.0/7.0, 1.188, 0.41, 2000, 10)
    runSimulation(201, 500, 0.5, 1.0/6.0, 1.188, 0.41, 2000, 10)
    runSimulation(201, 500, 0.5, 1.0/5.0, 1.188, 0.41, 2000, 10)
    return
if __name__ == "__main__":
    test()'''


def computeCEPD(result, N):
    '''This function processes the results of the simulation to make a CEPD list'''
    #creating a list w/ n zeroes
    list0 = [] #assigns list0 to empty list
    for x in range(N): #loops from 0 to N-1
        list0.append(0) #appends zeroes to list0
    for year in result: #for each loop for every value in the result list
        if year < N:
            for i in range(year, N): #nested for loop looping from the year of extinction to N
                list0[i] = int(list0[i] + 1) #fixing indexes
    for i in range(len(list0)): #loops for the length of list0
        list0[i] = int(list0[i])/len(result) #calculates the probability of extinction
    
    #te following loop is jsut to make it easier for me to make graphs 
    list1 = [] 
    for i in range(0, 201):
        list1.append(i)
    #plt.plot(list1, list0, 'o' )
    #plt.show()
    return list0
#computeCEPD(main(sys.argv), 201)


def main(argv):
    '''Calls the runSim function, CEPD, and is the function that takes the arguments from the command line'''
    if len(argv) < 3: #checking for arguments in the command line
        print('You need at least 3 arguments in the command line')
        exit()
    else: #if the command line has three arguments, the following code is executed
        #assignments
        numSim = int(argv[1])
        elNinoDiff = int(argv[2])
    #more assignments
    N = 201
    initPopSize = 500
    probFemale = 0.5
    elNinoProb = 1/elNinoDiff
    stdRho = 1.188
    elNinoRho = 0.41
    maxCapacity = 2000
    minViable = 10
    result = []
    #for loop for with range = value of numSim
    for i in range(numSim):
        y = runSimulation(N, initPopSize, probFemale, elNinoProb, stdRho, elNinoRho, maxCapacity, minViable) #assigning the result of calling runSim to y
        int(y) #casting y to int
        result.append(y) #appending y to result
    '''REMOVE THE FOLLOWING COMMEND IF YOU WANT TO PRINT RESULT'''
    #print(result) 
    #calculating the probability of extinction
    extinctions = 0
    for outcome in result:
        if outcome < N:
            extinctions += 1
    probExtinction = extinctions/numSim
    #return result, print('Probability of extinction:', probExtinction)
    cepd = computeCEPD(result, 201) #calling cepd as cepd
    #empty lists to help with plots
    plot = [] 
    horiz = []
    #for loop for every 10 cepd's
    for i in range(0, len(cepd), 10):
        plot.append(cepd[i])
        horiz.append(i)
    #plot instructions
    plt.plot(horiz, plot, 'o-')
    plt.title("Probability of Extinction for 1000 Years & 1/5 El Nino Years")
    plt.xlabel('Years')
    plt.ylabel('CEPD')
    plt.show()
    return
main(sys.argv) #calling main accepting arguments from the commandline



