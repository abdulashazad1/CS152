'''Abdullah Shahzad
9/24/2021
CS 152
LAB_03'''

#Making a function that takes a list of numbers and returns their sum
def sum(numbers):
    total = 0.0 #variable to hold the sum. It also initializes sum to 0.0, a float.
    for number in numbers:
        total += float(number) #adds each number to 0.0, effectively making total hold the sum of all numbers

    return total #returns the sum (the final value of total after the  for loop)


#Testing my function
def test():
    list1 = [1, 2, 3, 4] #declaring the list to be summed in sum(numbers)
    caller = sum(list1) #variable to hold the sum of list1
    print(caller) #printing the sum of list1
if __name__ == "__main__": #prevents the function from running when imported on another file
    test() #function call

    #the answer i got was 10.0 which is correct

