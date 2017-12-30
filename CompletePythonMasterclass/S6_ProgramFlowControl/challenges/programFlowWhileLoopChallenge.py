# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

import random

highest = 1000
answer = random.randint(1, highest)

print('Please guess a number between 1 and {}: '.format(highest))
guess = 0  # initialize
while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print('Please guess higher')
    elif guess > answer:
        print('Print guess lower')
    else:
        print('Well done! You guessed it.')
