#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #printing the word "greetings"
colors = ['red','orange','yellow','green','blue','violet','purple'] #creates a list of colors
play_again = ''
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): #will play again if not correct
    match_color = random.choice(colors) #program runs a random color within
    count = 0 #creating count
    color = '' #allowing user to input a color 
    while (color != match_color): #color equals match_color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() #color is lower case and strip eliminates space issues before and after word
        count += 1 # each time the game is played it will ad one to the count prior to getting it correct
        if (color == match_color): #if color is correct
            print('Correct!')#will print correct
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))#otherwise it will print try again and tell you how many times you guessed
    print('\nYou guessed it in {0} tries!'.format(count))
    if (count < best_count): #if it was the best guess
        print('This was your best guess so far!') #will print this if it is your best and closest guess
        best_count = count
    play_again = input("\nWould you like to play again? ").lower().strip()#typing play_again will allow you to restart game
print('Thanks for playing!')#ends by saying "thanks for playing"