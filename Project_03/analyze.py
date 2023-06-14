'''Abdullah Shahzad
9/22/2021
CS 152 B
Project_03'''

'''turning the pseudocode into actual code'''
#importing sys to allow for arguments to be given through command line
import sys
import stats #imports the stats.py file that I created

#giving the function 'main' parameters that will be filled in through command line
def main(filename, column_id):
    '''This function extracts the header and 1 column from a .csv file depending on the arguments given, appends them to a list and prints the list out'''
    '''By the end of Lab 03, it also sums the numbers in the list and gives us the total as a float'''

# assign to fp the result of opening the file hurricanes.csv for reading
    fp = open( filename, 'r')

# assign to line the first line of the data file
    line = fp.readline()

# assign to headers the result of splitting the line using commas
    headers = line.split(',')

# print headers
    #print(headers)

# assign to data an empty list
    data = []
    
# for all of the lines in the file
    for line in fp:

  # assign to words the result of splitting the line using commas
        words = line.split(',')

  # append second item to data (which index?) in words cast as a float
        data.append(words[column_id]) #column number can now be assigned via arguments

    l_total = stats.sum(data) #ALL these assignments call functions from stats.py and compute data to get the sum, mean, min, max, and var of items in data
    l_mean = stats.mean(data)
    l_min = stats.min(data)
    l_max = stats.max(data)
    l_var = stats.var(data)

  # close the data file
    fp.close()
  # print data
    return print('sum: %0.2f' % l_total), print('mean: %0.2f'% l_mean), print('min: %0.2f' % l_min), print('max: %0.2f ' % l_max), print('var: %0.2f' % l_var) 
    #with a comma, I can return both values in one line of code and I used formatting from lab 02 to format my output
if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2])) 

#when i substitute out 1 for 2 in the terminal, the terminal dumps out the 3rd column

