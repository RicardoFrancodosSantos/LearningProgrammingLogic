#Project 2 – Guess the Number

'''Write a program that, when it starts, generates a random value from 1 to 10 and allows the user to guess numbers until they get the generated value right.

The program must inform whether the guess was higher than, lower than, or equal to the random value generated at the beginning.'''


import random

random_number = random.randint(1,10)
match = False

while match == False:
    guess = input('Guess a number: ')