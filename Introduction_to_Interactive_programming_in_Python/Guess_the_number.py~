# template for "Guess the number" mini-project

import simplegui
import random
import math

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global allowed_guess
    print "Guess the Number!!!"
    print ""
    print "New Game. Range is from 0 to 100"
    secret_number = random.randrange(0,100)
    allowed_guess = 7
    print "Number of remaining guesses is",allowed_guess

# define event handlers for control panel
def range100():
    global secret_number
    global allowed_guess
    allowed_guess = 7
    secret_number = random.randrange(0,100)
    print ""
    print "New Game. Range is from 0 to 100"
    print "Number of remaining guesses is",allowed_guess
  
def range1000():
    global secret_number
    global allowed_guess
    allowed_guess = 10
    secret_number = random.randrange(0,1000)
    print ""
    print "New Game. Range is from 0 to 1000"
    print "Number of remaining guesses is",allowed_guess    
 
def input_guess(guess):
    global secret_number
    global allowed_guess
    global int_guess
    int_guess = int(guess)
    print ""
    print "Guess was",int_guess
    if allowed_guess > 1:
        allowed_guess -= 1
        print "Number of remaining guesses is", allowed_guess
        if secret_number > int_guess:
            print "Higher!"
        elif secret_number < int_guess:
            print "Lower!"
        else:
            print "Correct!"
            range100()
    else:
        print "Number of remaining guess is 0"
        print "You ran out of guesses. The number was",secret_number   
        new_game()
    
# create frame
f=simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()

