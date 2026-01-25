# While

'''
syntax
while condition:
    # code to be executed
'''

# Create a program that allows 3 attempts before closing
attempts = 0

while attempts < 3:
    print('try again')
    attempts = attempts + 1

# When we want an action to keep happening
# until a condition is satisfied

# User can only log in if the correct password is entered
password = ''

while password != '123456':
    password = input('Enter the correct password: ')