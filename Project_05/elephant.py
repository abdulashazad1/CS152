'''Abdullah Shahzad
10/6/2021
CS 152 B
Project_05 & Lab_05'''

# nested lists = a list inside a list
# no lab folder this week

import sys
import random 

# assigning variables    
calveInt = 3.1
#dartPercent = 0.0
juvAge = 12
maxAge = 60
calveMort = 0.85
adultMort = 0.996
seniorMort = 0.20    
maxCapacity = 8000
years = 200
    
# top level assignment of indexes for parameters
IDXCalveInt = 0
IDXDartPercent = 1
IDXJuvAge = 2
IDXMaxAge = 3
IDXCalveMort = 4
IDXAdultMort = 5
IDXSeniorMort = 6
IDXMaxCapacity = 7
IDXYears = 8

# top level assignment of indexes for elephants
IDXGender = 0
IDXAge = 1
IDXMonthsPregnant = 2
IDXMonthsContraceptiveRemaining = 3



def newElephant(paraList, age):
    '''This function creates a signle new elephant when called'''
    elephant = [0, 0, 0, 0] # initializing a list for an elephant with 0 values
    elephant[IDXGender] = random.choice('m' 'f') # assigning a gender to the elephant in index value 1
    elephant[IDXAge] = age # assigning an age to the elephant with an argument
    # checking if the elephant is female and then checking if she's pregnant
    if elephant[IDXGender] == 'f': 
        if elephant[IDXAge] > juvAge and elephant[IDXAge] <= maxAge: # checking to see if female elephant is of appropriate age
            if random.random() < 1/calveInt:
                elephant[IDXMonthsPregnant] = random.randrange(1, 22)
    return elephant


def initPopulation(paraList):
    '''This function creates a list of elephants equal to the maximum capacity of Kruger park'''
    pop = [] # initializing the population list to an empty list
    for i in range(maxCapacity): # looping 7k times
        pop.append(newElephant(paraList, random.randrange(1, 60))) # creating an elephant each time
    return pop # returning the population list


def incrementAge(population):
    '''Takes in a population list and returns a population list after incrementing the age of every elephant by 1 year'''
    for elephant in population:
        elephant[IDXAge] += 1
    return population


'''def test():
    # making parameter list
    paraList = [calveInt, dartPercent, juvAge, maxAge, calveMort, adultMort, seniorMort,maxCapacity, years]
    # printing parameter list
    print(paraList)
    # testing if indexes in the top level function are correctly assigned
    #print(paraList[IDXAdultMort])
    pop = []
    for i in range(15):
        pop.append( newElephant( paraList, random.randint(1, paraList[IDXMaxAge]) ))

    for e in pop:
        print(e)
    
    testPop = initPopulation(paraList)
    print(incrementAge(testPop))
    print(incrementAge(testPop))

if __name__ == '__main__':
    test()'''

#END OF LAB EXERCISE
def calcSurvival(paraList, population):
    '''This function determines if each indicidual elephant survives to the next year'''
    new_population = []
    for elephant in population:
        # conditional checking if the calve will die
        if elephant[IDXAge] == 1:  #
            if random.random() < calveMort:
                new_population.append(elephant)
        # conditional checking if the adult will die
        if elephant[IDXAge] > 1 and elephant[IDXAge] <= 60:
            if random.random() < adultMort:
                new_population.append(elephant)
        # conditional checking if the senior elephant will die
        if elephant[IDXAge] > 60:
            if random.random() < seniorMort:
                new_population.append(elephant)
    # output of the function is a list of elephants that survived the year        
    return new_population


def dartElephants(paraList, population):
    '''This function randomly decides which female elephants to dart based on the darting probability (dartPercent)'''
    for elephant in population: # loops over every elephant in the population
        if elephant[IDXGender] == 'f': # conditional that checks if the elephant is a female
            if elephant[IDXAge] > juvAge and elephant[IDXAge] < maxAge: # conditional that checks if the elephant is of appropriate age
                if random.random() < paraList[IDXDartPercent]: # probability of the female elephant getting darted
                    elephant[IDXMonthsPregnant] = 0 
                    elephant[IDXMonthsContraceptiveRemaining] = 22
    return population # returns the new list after darting females


def cullElephants(paraList, population):
    '''If the number of elephants exceeds the carrying capacity, this function culls an appropriate amount of randomly chosen elephamts to fit them in Kruger Park'''
    cullAmount = (int(len(population)) - paraList[IDXMaxCapacity]) # determines the amount of elephants to cull
    if cullAmount > 0: # checks if there are any elephants to cull
        random.shuffle(population) # shuffles the population list
        del population[paraList[IDXMaxCapacity]:] # deletes excess elephants, effectively culling them
    return (population, cullAmount)


def controlPopulation(paraList, population):
    ''''This function determines what method of population control should be used'''
    if paraList[IDXDartPercent] == 0: # checks if the percentage of population we're darting is null
        newpop, cullAmount = cullElephants(paraList, population) # culls elephants with the previous function
    else: # checks if the darting percentqage is > 0
        newpop = dartElephants(paraList, population) # darts elephants with the dartElephants function
        cullAmount = 0 # since culling hasn't been opted for the amount of elephants culled = 0
    return (newpop, cullAmount)


def simulateMonth(paraList, population):
    '''This function simulates a month in elephant land'''
    for e in population: # loops over every elephant in the population
        # assigning variables to indexes in the elephant list
        gender = e[IDXGender]
        age = e[IDXAge]
        monthsPregnant = e[IDXMonthsPregnant]
        monthsContraceptive = e[IDXMonthsContraceptiveRemaining]

        if gender == 'f' and age >= 12 and age < 60 : # checking to see if the elphant is female and an adult
            if monthsContraceptive > 0:
                e[IDXMonthsContraceptiveRemaining] = (monthsContraceptive-1) # if the elephant is darted, this removes a month from the contraqceptive remaining index of the list after a month has passed in elephant land
            elif monthsPregnant > 0:
                if monthsPregnant >= 22: # gives birth to a new elephant of age 1
                    population.append(newElephant(paraList, 1))
                    e[IDXMonthsPregnant] = 0 
                else: # or adds a month to the months pregnant index if the elephant is not 22 months pregnant
                    e[IDXMonthsPregnant] += 1
            else: # makes female elephants pregnant according to the probability below
                if random.random() < (1.0/(3.1*12 - 22)):
                    e[IDXMonthsPregnant] = 1
    return population


def simulateYear(paraList, population):
    '''This function simulates a full year in elephant land'''
    population = calcSurvival(paraList, population) # calls the calcSurvival function and assigns it to population
    population = incrementAge(population) # increases the age of the elephants by 1 year

    for i in range(12):
        simulateMonth(paraList, population) # runs the simulate month function 12 times to simulate a full year
    return population


def calcResults(paraList, population, culledAmount):
    '''This function tells us the total population, the amount of elephants culled, and the number of each type of elephant'''
    # initializing variables to hold the number of each type of elephant
    calveNum = 0
    juvNum = 0
    adultMaleNum = 0
    adultFemaleNum = 0
    seniorNum = 0
    for e in population: # loops over every elephant in the population, checks their age and assigns a type to them, it then adds a number to the appropriate variable to keep count
        if e[IDXAge] == 1:
            calveNum += 1
        if e[IDXAge] > 1 and e[IDXAge] <= 12:
            juvNum += 1
        if e[IDXAge] > 12 and e[IDXAge] < 60:
            if e[IDXGender] == 'm':
                adultMaleNum += 1
            if e[IDXGender] == 'f':
                adultFemaleNum += 1
        if e[IDXAge] > 60:
            seniorNum += 1
    total = calveNum + juvNum + adultMaleNum + adultFemaleNum + seniorNum # summing all elephants
    final_list = [total, calveNum, juvNum, adultMaleNum, adultFemaleNum, seniorNum, culledAmount]  # the final list with the number of each type of elephant
    return final_list


def runSimulation(paraList, N):
    popsize = paraList[IDXMaxCapacity]

    # init the population
    population = initPopulation(paraList)
    [population,numCulled] = controlPopulation( paraList, 
    population )

    # run the simulation for N years, storing the results
    results = []
    for i in range(paraList[IDXYears]):
        population = simulateYear( paraList, population )
        [population, numCulled] = controlPopulation( paraList, 
         population )
        results.append( calcResults( paraList, population, 
        numCulled) )
        print('Year', i+1, 'population: %0.1f' % len(population))
        if results[i][0] > 2 * popsize or results[i][0] == 0 : 
            # cancel early, out of control
            print('The elephant population was feasible uptill year', i+1)
            print( 'Terminating early' )
            break
    return results


def main(argv):
    if len(argv) == 2:
        if float(argv[1]) >= 0.0 and float(argv[1]) <= 1.0: # usage statement
            dartPercent = float(argv[1]) # assigning dartPercent using a command line argument entered by the user
            years = 200 # having this variable here let's me change it easily if i have to
            # making a parameters list
            paraList = [calveInt, dartPercent, juvAge, maxAge, calveMort, adultMort, seniorMort,maxCapacity, years]
            paraList[IDXDartPercent] = dartPercent
            # run simulation
            results = runSimulation(paraList, years)
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