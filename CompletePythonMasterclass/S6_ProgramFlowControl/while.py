# i = 0
# while i < 10:
#     print('i is now {}'.format(i))
#     i += 1
# available_exits = ['east', 'north east', 'south']
#
# chosen_exit = ''
# while chosen_exit not in available_exits:
#     chosen_exit = input('Please choose a direction: ')
#     if chosen_exit == 'quit':
#         print('Game over.')
#         break
#
# print("aren't you glad you got out of there!")

import random

highest = 10
answer = random.randint(1, highest)

print('Please guess a number between 1 and {}: '.format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print('Please guess higher')
    else:
        print('Print guess lower')
    guess = int(input())
    if guess == answer:
        print('Well done! You guessed it.')
    else:
        print('Sorry, not this time.')
else:
    print('Wow! You nailed it on the first try.')
