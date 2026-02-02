# Project 1 – Factorial of a number
# Create a program that receives a number and prints its factorial.

'''
# 5Q Method to build an algorithm:

Critically analyze the problem and find out:
(Try to explain this problem to yourself out loud and ask for more information / investigate
until you fully understand the problem.)

1. What are the required input data?
#a positive and integer number
2. What should I do with this data?
#calculate the factorial of the received number
3. What are the constraints of this problem?
a positive and integer number
4. What is the expected result?
#factorial print in the screen
5. What is the sequence of steps to reach the expected result?
(pseudocode)
#1. receive the user value
#2.verify if the number is integer and positive
#3. identify the factorial value and multiply (initializing with 1 until the factorial value, executing sum the previous output until reach in the last calculus (trough the factorial value))
#4. Print the output in the screen
'''

number = int(input ('Type desired factorial that you want to calculate: '))
if number > 0 and type(number) == int:
   factorial = 1
   for item in range (1, number + 1): 
    print(f'{factorial} * {item}')
    factorial = factorial * item
    print(f'{factorial}')
   print(f' the factorial of the {number} is {factorial}') 
else:
  print ('please, only inform positive and integer numbers')
