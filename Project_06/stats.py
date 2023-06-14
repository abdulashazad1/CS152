'''Abdullah Shahzad
9/24/2021
CS 152
Project_03'''

'''All values extracted from the .csv file have to, before calculations be converted to floats because they're saved as strings
hence the casting with float() throughout the code'''


def sum(numbers):
    '''This function returns the sum of the numbers in a list as a float'''
    total = 0.0 #variable to hold the sum. It also initializes sum to 0.0, a float.
    for number in numbers:
        total += float(number) #adds each number to 0.0, effectively making total hold the sum of all numbers

    return total #returns the sum (the final value of total after the  for loop)
#end of the function

def test():
    '''Tests my sum function'''
    list1 = [1, 2, 3, 4] #declaring the list to be summed in sum(numbers)
    caller = sum(list1) #variable to hold the sum of list1
    print('sum:', caller) #printing the sum of list1
if __name__ == "__main__": #prevents the test function from running when imported on another file
    test() #function call #the answer i got was 10.0 which is correct


def mean(numbers):
    '''This function calculates the mean of the values in the column and prints it out'''
    val_count = 0 #this variable stores the number of values in the list
    Sum = float(sum(numbers)) #calling the sum function above, reusing code. Used 'Sum' with a capital s to differentiate it from 'sum'

    for number in numbers: #for loop to loop through the list 'numbers'
        val_count += 1 #adds 1 to val_count every time a loop occurs, which is equal to the number of items in the list

    return float(Sum/val_count) #Neatly returns the mean value with a label "Mean:"
    #end of the function

def test():
    '''Testing my mean function'''
    list1 = [1, 2, 3, 4] #initializing the list to calculate the mean of
    print('mean:', mean(list1)) #calling the mean function inside a print statement with list1 as an argument
if __name__ == "__main__": #prevents the test function from running when imported on another file
    test() #test function call


def min(numbers):
    '''This function prints out the smallest value in the list'''
    low_val = 10000000.0 #Assigning a large value to low_val so that the smallest value in the list is definitely smaller than it
    for number in numbers: #For loop looping through the numbers in the list
        if low_val > float(number): #Conditional
            low_val = float(number) #When condition is met, the value of low_val is reassigned to the new newest number and this process keeps repeating
    return low_val #returns the value of low_val after assigning the lowest number of the list to it

def test():
    '''Testing my min function'''
    list3 = [1, 2, 3, 4] #Initializing a list to print the minimum value of
    print('min:', min(list3)) #calling the min function inside a print statement with the list as an argument
if __name__ == '__main__': #prevents the test function fron running when the code is imported somewhere
    test() #calling the test function


def max(numbers):
    '''This function prints out the largest value in the list'''
    high_val = -1000000.0 #Assigned a low value to high_val so that the highest number in the list will always be higher than this
    for number in numbers: #For loop looping througbh items in the list
        if high_val < float(number): #Conditional
            high_val = float(number) #If condition met, the highest number found in the list will be assigned to high_val
    return high_val #returns the value of high_val after assigning the highest value in the list to it

def test(): #copied and pasted the test for my min function, just called max() inside the test function
    '''Testing my max function'''
    list3 = [1, 2, 3, 4] 
    print('max:', max(list3)) 
if __name__ == '__main__': 
    test() 


def var(numbers):
    '''This function calculates the variance of the items in a list'''
    Mean = mean(numbers) #calls the mean function above to find the mean of a list and assigns the mean to a variable so that I can use it in calculations
    val_num = 0 #Variable holding the count of values in the list so I can use it in the calculation
    sum_of_diff = 0 #Holds the sum of all the squares of the differences between the items in the list and the mean

    for number in numbers: #loop to count the number of values in the list, adds 1 to val_num for every loop
        val_num += 1

    for number in numbers: #loop to calculate all the squares of the differences between an item in the list(number) and the mean 
        diff = (float(number) - Mean)**2
        sum_of_diff += (diff) #this adds all of the squares together

    denom = val_num - 1 #I assigned the denominator of the expression to the variable denom to make writing the equation easier
    var = (sum_of_diff/denom) #I took the underroot of the actual equation to get v and not sigma squared
    return var
    #end of function

def test(): #copied and pasted the test for my min function, just called var() inside the test function and edited the print statement to print neatly
    '''Testing my var function'''
    list3 = [1, 2, 3, 4] 
    print('var: %0.2f' % var(list3)) 
if __name__ == '__main__': 
    test()


def s_d(numbers):
    '''This function calculates the standard deviation of the items in a list'''
    Mean = mean(numbers) #calls the mean function above to find the mean of a list and assigns the mean to a variable so that I can use it in calculations
    val_num = 0 #Variable holding the count of values in the list so I can use it in the calculation
    sum_of_diff = 0 #Holds the sum of all the squares of the differences between the items in the list and the mean

    for number in numbers: #loop to count the number of values in the list, adds 1 to val_num for every loop
        val_num += 1

    for number in numbers: #loop to calculate all the squares of the differences between an item in the list(number) and the mean 
        diff = (float(number) - Mean)**2
        sum_of_diff += (diff) #this adds all of the squares together

    denom = val_num - 1 #I assigned the denominator of the expression to the variable denom to make writing the equation easier
    s_deviation = (sum_of_diff/denom) #I took the underroot of the actual equation to get v and not sigma squared
    return s_deviation**0.5

def test(): #copied and pasted the test for my min function, just called s_d() inside the test function and edited the print statement to print neatly
    '''Testing my standard deviation (s_d) function'''
    list3 = [1, 2, 3, 4] 
    print('standard deviation: %0.2f' % s_d(list3)) 
if __name__ == '__main__': 
    test()


#
def val_range(numbers):
    '''This is a function that calculates the range of the data being examined (lowest and highest values) and prints them out'''
    upper_bound = -1000 #upper bound is a small value so that the largest value in the list isn't smaller than this
    lower_bound = 1000 #lower bound is a large value so that the lowest value in the list isn't lower than this

    for number in numbers: #for loop looping through every item in the list
        if number > upper_bound: #conditional 1: checks if each item in the list is larger than upper_bound
            upper_bound = number #if conditional 1 is met, then that item in the list is assigned to upper_bound
        if number < lower_bound: #conditonal 2: checks if each item in the list is smaller than lower_bound
            lower_bound = number #if conditional 2 is met, then that item in the list is assigned to lower_bound

    return lower_bound, upper_bound 

def test(): #copied and pasted the test for my min function, just called val_range() inside the test function and edited the print statement to print neatly
    '''Testing my range (val_range) function'''
    list3 = [1, 2, 3, 4] 
    print('range: %0.2f - %0.2f' % val_range(list3)) 
if __name__ == '__main__': 
    test()