#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #Prints "Greetings!"
colors = ['red','orange','yellow','green','blue','violet','purple'] #Lists all of the possible color variables
play_again = '' #Recognizes an input
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): #Begins a while loop that depends on the users willingness to play again or not.
    match_color = random.choice(colors) #Randomizes the "correct" color from the list of colors above
    count = 0 #Sets the count at 0 
    color = '' #Recognizes a user input
    while (color != match_color): #"While color doesn not match the specefied color"
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() #accepts a user input 
        count += 1 #Add one to the count of 0
        if (color == match_color): #An if statement that evaluates if the user input is correct and then prints a statement
            print('Correct!') #Prints correct if the correct color is guessed
        else: #An else statement that prompts another set of commands if the correct color is not guessed
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #Prints "incorrect" and the number of guesses so far
    print('\nYou guessed it in {0} tries!'.format(count)) #Prints how many tries it took to guess the correct color
    if (count < best_count): # compares all of the recorded guess counts that it took to get the correct color.
        print('This was your best guess so far!') #Prints this if the guess count is the lowest in comparison to all the others
        best_count = count #Sets the variable to 0 again
    play_again = input("\nWould you like to play again? ").lower().strip() #Prompts the user to play again or not
print('Thanks for playing!') #This is printed if the user input is no and the while loop does not start over again.