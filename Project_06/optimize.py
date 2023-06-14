'''Abdullah Shahzad 
10/26/2021
CS 152 B
Project_06'''

'''this python file contains function to find the percentage of elephants that need to be darted to control the elephant population at the carrying capacity. 
this file does not require terminal input besides the standard 'py optimize.py' call to run the program'''

import sys
import elephant
import random
import matplotlib.pyplot as plt
import stats


def optimize( min, max, optfunc, parameters = None, tolerance = 0.001, maxIterations = 20, verbose=False ):
    '''this function executes a search to bring the result of the function optfunc to zero.'''
    done = False
    # while loop for the optimize function that keeps looping
    while done == False:
        testValue = (max + min)/2 # not integer division
        if verbose:
            print("test value is " + str(testValue))
        # optimizes the function using testValue
        result1 = optfunc(testValue, parameters)
        result = result1[0]
        averagePopulation = result1[1]
        if verbose:
            print("optfunc result is " + str(result))
        # search conditionals 
        if result > 0:
            max = testValue
        elif result < 0:
            min = testValue
        else:
            done = True
        # checks if the optimized value is correct to enough sigfigs by comparing it to the tolerance
        if (max - min) < tolerance:
            done = True
        maxIterations-=1
        # checks to see if > maxiterations have been allowed
        if maxIterations <= 0:
            done = True
    return (testValue, averagePopulation)

def target(x, pars):
    "A funciton that was used to test the optimize function. Takes the a target value and a list of parameters. Returns a float of x - target"
    return x - 0.73542618


def testTarget():
    '''this function tests the binary search using a simple target function and prints the resulting optimal value'''
    #runs the optimize function and prints it
    res = optimize( 0.0, 1.0, target, tolerance = 0.01, verbose=True)
    print(res)
    return

def testESim():
    '''this functin tests the optimize function using the elephantSim function imported from elephant.py'''
    res = optimize(0.0, 0.5, elephant.elephantSim, tolerance = 0.0001, verbose = True)
    print (res)
    return

def evalParameterEffect(whichParameter, testmin, testmax, teststep, defaults = None, verbose = False):
    '''this function evaluates the effect of the selected parameter on the dart percentage'''
    # if a parameter list isn't give, default parameters are used 
    if defaults == None:
        simParameters = elephant.defaultParameters()
    else:
        simParameters = defaults[:]
    results = []
    # checks if the user wants a printout of the function's function
    if verbose:
        print ("Evaluating parameter %d from %.3f to %.3f with step %.3f" % (whichParameter, testmin, testmax, teststep))
    # executes a binary search using the optimize function and elephantSim
    t = testmin
    averagePopulation = []
    while t < testmax:
        simParameters[whichParameter] = t
        percDart1 = optimize(0.0, 0.5, elephant.elephantSim, simParameters, tolerance = 0.0001, verbose = verbose)
        percDart = percDart1[0]
        results.append((t,percDart))
        averagePopulation.append(percDart1[1])
        if verbose:
            print ("%8.3f \t%8.3f" % (t, percDart))
        t+=teststep
    # again, checks to see if the user wants a printout of the function's function
    print('Average Population For Each Simulation: ' + str(averagePopulation))
    sD = stats.s_d(averagePopulation)
    if verbose:
        print("terminating")
    return [results, sD] 

def main():
    '''the main function that runs the evalParameterEffect function and graphs them using MatPlotLib'''
    # assigns the return of calling evalParameterEffect to results
    results1 = evalParameterEffect(elephant.IDXMaxAge, 56, 66, 2, verbose=False)
    results = results1[0]
    percDart = []
    changedParameter = [] 
    print('Standard Deviation: ' + str(results1[1]))
    # loops over objects in results and assigns each index to x and y axis lists
    for i in range(len(results)):
        changedParameter.append(results[i][0])
        percDart.append(results[i][1])
    # matplotlib calls to graph the results
    plt.plot(changedParameter, percDart, "o")
    plt.title("Effect of Changing the Max Age on the Optimal Percent Darted")
    plt.xlabel("Survival Probability")
    plt.ylabel("Optimal Percent Darted")
    plt.show()
    print(results)

if __name__ == "__main__":
    main()