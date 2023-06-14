'''Abdullah Shahzad
9/22/2021
CS 152 B
LAB_03'''

def main():
    '''this function prints out elements of a list'''
    numbers = [5, 3, 6, 1, 2]
    #empty list: a list with no elements
    my_empty_list = [] 
    #Accessing one element of the list
    first_number = numbers[0] #index starts at zero. first_number is assigned to the number in position 0. 
    #printing out 5 and 1 from the list
    two_numbers = numbers[0], numbers[3] #This assigns the variable in the position 0 and 3 in the list to two_numbers
    print(two_numbers)
main()

#different function to practice appending to a list
def appender(r):
    'This function appends elements at the end of the list'
    numbers = [5, 3, 6, 1, 2] #I just copied the list into this function
    numbers.append(r) #this should add 7 to the end of the list, seperated by a comma when I call the function with argument 7
    print(numbers)
appender(7) #after running, it did add 7 to the end of the list so success!

#new function for replacing items in a list
def replacer(r):
    '''This function replaces the first item of the list'''
    numbers = [5, 3, 6, 1, 2] #copied the same list as above
    numbers[0] = r #Assigning a value to the first item in the list that should replace the original first element
    print(numbers)
replacer(4) #the list was automatically changed to have the first element be 4





