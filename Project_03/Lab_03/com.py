'''Abdullah Shahzad
9/24/2021
CS 152
LAB_03'''

import sys
print(sys.argv) #shows me ['com.py']

'''When I enter other words after "py com.py", the words are added to the list'''
#sys allows me to see what I typed in the command line

print('Running program', sys.argv[0])
print("I'm going to open the file", sys.argv[1])
print("I'm going to extract the column", int(sys.argv[2]))

'''Indexing to different inputs in the command line allows them to interact with the code
The input I give to the command line can also be used to name files and number columns'''




