'''Abdullah Shahzad
9/26/2021
CS 152 B
Project 3'''

import sys
import thermocline
#a general function which clears the file given in the argument when calling it
def clearfile(fileToClear):
    fp = open(fileToClear, 'w')    
    fp.close()
clearfile('JulyThermocline2.csv')

#name function
fp = open('JulyThermocline2.csv', 'a') #opens the file 'JulyThermocline.csv' to append (write) to it
fp.write('Day' + ',' + 'Thermodepth 12:00 AM' + '\n') #Write the header in that file
fp.close() #closes the file

def main(time):
    #these are the fields corresponding to the temperatures in order by depth
    #uses 0 indexing
    fields = [10, 11, 16, 17, 15, 14, 13, 12]
    #these are the depth values for each temperature measurement\
    depths = [1, 3, 5, 7, 9, 11, 13, 15]

    fp = open('GoldieJuly2019.csv', 'r') #opens the file 'GoldieJuly2019.csv' to read it
    line = fp.readline() #Reads the first line(header) of GoldieJuly2019.csv
    day = 0 #days assigned to the number 0
    day2 = 0
    for line in fp: #for loop for that loops through every line in fp
        words = line.split(',') #seperates the columns in the line with a comma, making them indexable

        if time in words[0]: #conditional checking for the time at which the data was taken
            day += 1 #adds 1 to the variable 'day'
            temps = [] #empty list assigned to temps

            for i in range(len(depths)): #for loop with variable i for range the length of depths
                temps.append(float(words[fields[i]])) #appends the value in words[fields[i]] to temps after casting it into a float

            thermo_depth = thermocline.thermocline_depth(temps, depths) #calls the function thermocline_depth with the arguments temps and depths
            print(day, ',', thermo_depth) #prints day and corresponding thermodepth into the terminal
            fp = open('JulyThermocline2.csv', 'a') #opens the file JulyThermocline.csv' to append to it
            fp.write(str(day) + ',' + str(thermo_depth) + '\n') #writes the day number and the corresponding thermodepth value into the data file

    fp.close() #closes a previously openned data file
    return 
if __name__ == '__main__': #doesn't automatically call the function if it is imported and the entire program is run
    main(sys.argv[1])