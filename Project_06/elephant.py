'''Abdullah Shahzad
10/25/2021
CS152 B
Project_06'''

'''This file is run using the terminal. It will give you a usage statement if the terminal input is inappropriate, however, you run it by typing 'py elephant.py dartingPercentage' in the terminal
where dartingPercentage is a number between 0.0 and 1.0 that represents what percentage of adult female elephants should be darted and this program run with'''

from hashlib import new
import random
import sys
import stats


# top level assignment of all the index values of variables in the lists
IDXCalveInt = 0
IDXDartPercent = 1
IDXJuvAge = 2
IDXMaxAge = 3
IDXCalveMort = 4
IDXAdultMort = 5
IDXSeniorMort = 6
IDXMaxCapacity = 7
IDXYears= 8
IDXGender = 0
IDXAge = 1
IDXMonthsPregnant = 2
IDXMonthsContraceptiveRemaining = 3

def newElephant(parameters, age):
    '''this function gives birth to a new elephant'''
    # initializes the elephant as a list with all zeroes
    elephant = [0,0,0,0]
    # assigns a gender to elephant
    elephant[IDXGender] = random.choice(['m', 'f'])
    # assigns an age to the elphant that is equal to the argument
    elephant[IDXAge] = age
    # checks if the elephant is a female
    if elephant[IDXGender] == 'f':
        # if the elephant is an adult, according to a probability, the elephant is assigned a pregnancy and the amount of time that it has been pregnant
        if (elephant[IDXAge] > parameters[IDXJuvAge]) and (elephant[IDXAge] <= parameters[IDXMaxAge]):
            if (random.random() < 1.0/parameters[IDXCalveInt]):
                elephant[IDXMonthsPregnant] = random.randint(1,22)
    return elephant

def initPopulation(paraList):
    '''this function initializes a list of elephants for us to work with'''
    population = [] # assigning population to an empty list
    # calls the new elephant function as many times as it needs to to fill up the carrying capacity and appends all those elephants to the population list
    for i in range(paraList[IDXMaxCapacity]):
        population.append(newElephant(paraList, random.randint(1, paraList[IDXMaxAge])))
    return population 

def incrementAge(population):
    '''this function increases the age of all the elephants in the list by 1 year'''
    for e in population: # loops over the elphants in the population
        e[IDXAge] += 1 # adding 1 to the age of the elephant
    return population 

def calcSurvival(paraList, population):
    '''this function uses probabilities to determine whether an elephant of a particular age will survive the year'''
    newPop = [] # new list to append the undead elephants to
    
    for elephant in population: # loops through the population list
        age = elephant[IDXAge]

        if age == 1: # checks if the elephant is a calf 
            if random.random() < paraList[IDXCalveMort]:
                newPop.append(elephant)
        
        elif age > paraList[IDXMaxAge]: #checks if the elephant is a senior
            if random.random() < paraList[IDXSeniorMort]:
                newPop.append(elephant)
        # checks if the elphant will survive based on the mortality rate of adult elephants
        else:
            if random.random() < paraList[IDXAdultMort]:
                newPop.append(elephant)
    return newPop

def dartElephants(paraList, population):
    '''this function, according to the darting probability, decides on random which female elephants of appropriate age to dart'''
    dartPercent = paraList[IDXDartPercent]
    juvAge = paraList[IDXJuvAge]
    maxAge = paraList[IDXMaxAge]
    #loops through the population
    for i in range(len(population)):
        # checks tto see if the elephant is a female of appropriate age
        if (population[i][IDXAge] > juvAge) and (population[i][IDXAge] < maxAge) and (population[i][IDXGender == "f"]):
            # darts or doesn't dart the appropriate female elephant based on the darting probabilty 
            if random.random() < dartPercent:
                population[i][IDXMonthsPregnant] = 0
                population[i][IDXMonthsContraceptiveRemaining] = 22
    return population

def cullElephants(paraList, population):
    '''if the number of elephants exceeds the carrying capacity, this function randomly removes the excess elephants and returns a new, shorter list'''
    maxCapacity = paraList[IDXMaxCapacity]
    cullNum = len(population) - maxCapacity
    newPop = [] # new list for the population of elephants after the culling
    # checking to see if the number of elephants > max capacity. If true, the elephant population list is shuffled randomly and the excess elephants removed.
    if cullNum > 0:
        random.shuffle(population)
        newPop = population[:maxCapacity]
        result = (newPop, cullNum)
    # if no elephant needs to be culled, returns the population list and sets cullNum = 0
    else: 
        newPop = population
        result = (newPop, 0)
    return result

def controlPopulation(paraList, population):
    '''this function determines whether the method of population control should be culling or darting depending on whether or not darting probability is available'''
    if paraList[IDXDartPercent] == 0: # if we aren't darting, we're culling
        (newPop, cullNum) = cullElephants(paraList, population)
    
    else:
        newPop = dartElephants(paraList, population)
        cullNum = 0
    return(newPop, cullNum)

def simulateMonth(paraList, population):
    '''this function imulates one month in elephant land'''
    calvingInterval = paraList[IDXCalveInt]
    juvAge = paraList[IDXJuvAge]
    maxAge = paraList[IDXMaxAge]
    
    for elephant in population: # loops over the elephant population
        gender = elephant[IDXGender] 
        age = elephant[IDXAge]
        monthsPregnant = elephant[IDXMonthsPregnant]
        monthsContraceptive = elephant[IDXMonthsContraceptiveRemaining]
        
        if (gender == "f") and (age > juvAge) and (age < maxAge): # checks if the elephant is a female adult
            if monthsContraceptive > 0:
                elephant[IDXMonthsContraceptiveRemaining]-=1 # reduces one month from the contraceptive's duration
            elif monthsPregnant > 0:
                if monthsPregnant >= 22: # checks if the female elephant is more than 22 months pregnant and if it is, then makes a new elephant
                    population.append(newElephant(paraList, 1))
                    elephant[IDXMonthsPregnant] = 0
                else:
                    elephant[IDXMonthsPregnant] +=1
            else:
                if random.random() < (1.0/(calvingInterval * 12 - 22)): # if the elephant is not darted, then this checks if the elephant will become pregnant
                    elephant[IDXMonthsPregnant] = 1
    return population

def simulateYear(paraList, population):
    '''this function simulates one whole year in elephant land'''
    # determines what elephants survive and increases their age by a year
    population = calcSurvival(paraList, population)
    population = incrementAge(population)
    # loops 12 times, calling the simulate month function
    for i in range(12):
        population = simulateMonth(paraList, population)
    return population

def calcResults(paraList, population, cullNum):
    '''this function calculates statistics for the elephant population and puts them in a list, the statistics are about the total number of elephants
    and the number of elephants in each age group'''
    juvAge = paraList[IDXJuvAge]
    maxAge = paraList[IDXMaxAge]
    numCalves = 0
    numJuv = 0
    numAdultMale = 0
    numAdultFemale = 0
    numSenior = 0 
    total = 0
    # looping over every elephant in the list and adding 1 to each category that elephant belongs to
    for e in population:
        if e[IDXAge] == 1:
            numCalves +=1
        elif e[IDXAge] <= juvAge:
            numJuv+=1
        elif e[IDXAge] > maxAge:
            numSenior += 1
        # adds 1 to the number of adult females or adult males depending on the gender of the elephant
        else:
            if e[IDXGender] == 'f':
                numAdultFemale += 1
            else:
                numAdultMale +=1
        total += 1
    return [total, numCalves, numJuv, numAdultFemale, numAdultMale, numSenior, cullNum]

def runSimulation(paraList):
    '''code provided as part of the project that simulates the number of years specified'''
    popsize = paraList[IDXMaxCapacity]
    population = initPopulation(paraList)
    [population, cullNum] = controlPopulation(paraList, population)
    results = []
    for i in range(paraList[IDXYears]):
        population = simulateYear( paraList, population )
        [population,cullNum] = controlPopulation(paraList, population)
        results.append(calcResults(paraList, population, cullNum))
        if results[i][0] > 2 * popsize or results[i][0] == 0 :
            
            break
        
    return results

def defaultParameters():
    '''this function returns a list of default parameters for the elephant population'''
    # default assignments for every parameter
    calveInt = 3.1
    dartPercent = 0.0
    juvAge = 12
    maxAge = 60
    calveMort = 0.85
    adultMort = 0.996
    seniorMort = 0.2
    maxCapacity = 100
    years = 200
    # putting the assignments in a list and then returning i
    result = [calveInt, dartPercent, juvAge, maxAge, calveMort, adultMort, seniorMort, maxCapacity, years]
    return result 

def elephantSim(percDart, inputParameters = None):
    '''this function tells us if too many or too few elephants are being darted depending on the difference between the average population size and the carrying capacity'''
    # if a parameter list isn't provided, default parameters are assigned for the simulation
    if inputParameters == None:
        parameters = defaultParameters()
    else:
        parameters = inputParameters
    parameters[IDXDartPercent] = percDart
    # runs a simulation, initializes results
    results = runSimulation(parameters)
    # loops 4 times, calling the runSimulation function
    for i in range(4):
        results += runSimulation(parameters)
    totalPop = 0
    # loops over the results to calculate the average total population for 5 years
    for i in range(len(results)):
        totalPop += results[i][0]
    avgTotalPop = totalPop/len(results)
    return (int(parameters[IDXMaxCapacity] - avgTotalPop), avgTotalPop)



def test():
    """Test function to test the basic functions that were written in the Lab portion of this project"""
    # making a parameter list within the function to call elephantSim 
    calvingInterval = 3.1
    percentDarted = 0.0
    juvenileAge = 12
    maxAge = 60
    probCalfSurvival = 0.85
    probAdultSurvival = 0.996
    probSeniorSurvival = 0.20
    carryingCapacity = 20
    numYears = 200
    parameters = [calvingInterval, percentDarted, juvenileAge, maxAge, probCalfSurvival, probAdultSurvival, probSeniorSurvival, carryingCapacity, numYears]
    # printing the parameter list
    print(parameters)
    # create a test population list with 20 elephants
    pop = []
    for i in range(20):
        pop.append(newElephant(parameters, random.randint(1,parameters[IDXMaxAge])))
    for e in pop:
        print(e)
    #initialize the population and print the test population created
    testPop = (initPopulation(parameters))
    print(testPop)
    testPop = incrementAge(testPop)
    print(testPop) 

    

    #assign each relevant elephant probability/statistic to variables. 
    calvingInterval = 3.1
    juvenileAge = 12
    maxAge = 60
    probCalfSurvival = 0.85
    probAdultSurvival = 0.996
    probSeniorSurvival = 0.20
    carryingCapacity = 500
    numYears = 200

def main(argv):
    '''this is the main function for the project, it assigns the darting probability based on an argument entered by the user in the terminal and prints the average statistics
    for the elephant population'''

    # making local assignments for the parameter list inside the  main function
    calveInt = 3.1
    juvAge = 12
    maxAge = 60
    calveMort = 0.85
    adultMort = 0.996
    seniorMort = 0.20
    maxCapacity = 500

    if len(argv) == 2:
        if float(argv[1]) >= 0.0 and float(argv[1]) <= 1.0: # usage statement
            dartPercent = float(argv[1]) # assigning dartPercent using a command line argument entered by the user
            years = 200 # having this variable here let's me change it easily if i have to
            # making a parameters list
            paraList = [calveInt, dartPercent, juvAge, maxAge, calveMort, adultMort, seniorMort,maxCapacity, years]
            paraList[IDXDartPercent] = dartPercent
            # run simulation
            results = runSimulation(paraList)
            # assigning variables to hold averages
            avgTotalPop = 0
            avgCalveNum = 0
            avgAdultMaleNum = 0
            avgAdultFemaleNum = 0
            avgSeniorNum = 0
            avgCulledAmount = 0
            
            for i in range(len(results)):
                avgTotalPop += results[i][0]
                avgCalveNum += results[i][1]
                avgAdultMaleNum += results[i][2]
                avgAdultFemaleNum += results[i][3]
                avgSeniorNum += results[i][4]
                avgCulledAmount += results[i][5]
            # print statements to get the final output
            print('The average total population for each year in this simulation: %0.2f' % (avgTotalPop/years))
            print('The average number of calves in each year in this simulation: %0.2f' % (avgCalveNum/years))
            print('The average number of adult males in each year of this simulation: %0.2f' % (avgAdultMaleNum/years))
            print('The average number of adult females in each year of this simulation: %0.2f' % (avgAdultFemaleNum/years))
            print('The average number of seniors in each year of this simulation: %0.2f' % (avgSeniorNum/years))
            print('The average amount of elephants culled every year for each year in this simulation: %0.2f' % (avgCulledAmount/years))

    if len(argv) == 1 or float(argv[1]) > 1.0:
        print('To run this function, you must either put 0 or a number between 0.0 and 1.0 in the command line.')
        print('If you put in 0, the simulation will run and use culling as the population control method.')
        print('If you put in a number between 0.0 and 1.0, then the simulation will run while using darting as a population control method')

if __name__ == '__main__':
    main(sys.argv) # calling the main function with a command line argument
  