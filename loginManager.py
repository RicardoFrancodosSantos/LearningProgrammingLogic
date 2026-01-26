'''
Real-world scenario for a simple login manager. 
Build an authentication functionality in Python 
with a maximum of three login attempts. 
There is only one allowed user with fixed credentials. 
The valid username is **“jhonatan”** and the valid password 
is **“senha123”**. On each attempt, 
the system must validate whether the provided username and password 
exactly match the allowed credentials. 
If the user enters incorrect credentials three consecutive times, 
the system must block further attempts and display the message: 
**“Wait 30 minutes before trying again!”**. 
If the user enters the correct username and password 
before reaching the three-attempt limit, 
the system must stop the attempt process and display the message: **“Login successful”**.

'''
'''
1. What input data is required?

user and password

2. What should I do with this data?

validate whether the provided username and password 
exactly match the allowed credentials.

If the user enters incorrect credentials three consecutive times, 
the system must block further attempts and display the message: 
**“Wait 30 minutes before trying again!”**. 
If the user enters the correct username and password 
before reaching the three-attempt limit, 
the system must stop the attempt process and 
display the message: **“Login successful”**.


3. What are the constraints of this problem?

only allow specifc user and password 

4. What is the expected result?
If the user enters incorrect credentials three consecutive times, 
the system must block further attempts and display the message: 
**“Wait 30 minutes before trying again!”**. 
If the user enters the correct username and password 
before reaching the three-attempt limit, 
the system must stop the attempt process and 
display the message: **“Login successful”**.

5. What is the sequence of steps to reach the expected result? (pseudocode)

1. Declare the variables
2. Validate if the variables are the correct in each execution (user jhonathan and password is password123)
3. If the variables isn`t correct from the fourth execution, print the message "**“Wait 30 minutes before trying again!”**.
If the user enters the correct username and password 
before reaching the three-attempt limit, 
the system must stop the attempt process and 
display the message: **“Login successful”**.
4. "

What is the sequence of steps to reach the expected result? (pseudocode)
1. receive an user name;
2.receive a password
3.verify if the user name is jhonathan
4. verify if the password is password123
5. allow 3 attempts of login. If from the fourth attempt onward the user fails authentication,print the message "**“Wait 30 minutes before trying again!”
6. if meanwhile the attempts , the user input correct login and password,print the message If the user enters the correct username and password 
before reaching the three-attempt limit, 
the system must stop the attempt process and 
display the message: **“Login successful”**. '''

user = ''
password = ''
attempts = 0

