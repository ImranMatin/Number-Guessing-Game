# Number guessing game in Python  
# Reference: Geeks4Geeks.org 

import random 

print("Hi welcome to the game. This is a number guessing game.\nYou got 7 chances to guess the number. Let's start the game")

number_to_guess = random.randrange(100)

chances = 7

guess_counter = 0

while guess_counter < chances:

    guess_counter += 1
    my_guess = int(input('Please Enter your Guess : '))

    if my_guess == number_to_guess:
        print(f'Congratulations!!. The number is {number_to_guess} and you got it right in the {guess_counter} attempt')
        break

    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f'Oops sorry, The number is {number_to_guess} better luck next time')

    elif my_guess > number_to_guess:
        print('Your guess is too big ')

    elif my_guess < number_to_guess:
        print('Your guess is too small')


# Time Complexity: 
# The time complexity of this code is O(log2n) where n is the difference between lower and upper bound of the range.

# Space Complexity: 
# The space complexity of this code is O(1) as all the variables used in this code are of the same size and no extra space is required to store the values.
