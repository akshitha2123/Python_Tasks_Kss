#  Create a Number Guessing Game where: 
# The program generates a random number between 1 and 50 using random. 
# The user has 5 attempts to guess the number. 
# After each guess, calculate the absolute difference using math.fabs() and 
# display how far the guess is from the correct number. 

import random
import math
number = random.randint(1, 50)
print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 50.")
print("You have 5 attempts.")
for i in range(5):
    guess = int(input("Enter your guess: "))
    difference = math.fabs(number - guess)

    print("Difference:", difference)

    if guess == number:
        print("Congratulations! You guessed correctly.")
        break
    else:
        print("Wrong guess!")

else:
    print("Sorry! You used all 5 attempts.")
    print("The correct number was:", number)
