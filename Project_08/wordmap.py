'''Abdullah Shahzad
11/3/2021
CS 152 B
Lab & Project 8'''

def main():
    #this function asks the user for some input and outputs the input with a relevant question keyword in a dictionary
    #user provides input as strings or integers and the output is a dictionary printed to the terminal

    #asking the user for input
    print("You're about to be asked some biographical details.")
    words = ['name', 'age', 'hometown', 'school', 'graduation year', 'courses', 'class', 'grade', 'date', 'time', ]
    mapping = {} #empty dictionary called mapping

    for word in words: #loops over the word list to ask the user for input and then puts the questions key word as a key into the dictionary along with the answer
        answer = input('Enter ' + word + ':')
        mapping[word] = answer

    for key in mapping.keys(): #loops over the keys so that I can print out the question's keyword and the corresponding answer in the dictionary
        print('Your entries:')
        print(key + ': ' + mapping.get(key))
main()

