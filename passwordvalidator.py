"Problem: you work in a system that need to check if all typed passwords are valid. To a password be valid, it needs to have at least six characters"

"1. Which are all necessary data inputs?"
"the password"





"2. What i need to do with this data?"
"validate if the password have at least 6 characters"

"3. Which are all restrictions of this problem?"

"devo receber a senha do usuario e possuir 6 caracteres"

"4. Which is the expected result?"
"validate that the password have at least 6 chracters. if don`t have, print the warning to the user in the screen 'your password must have at least 6 chracters"""




"5. Which are the step sequence to achieve the expected result?"
"1 - receive the password / 2 - verify if the password have at least 6 chracters"


passwords = ["abc","abcde","abcdefgh","abcdefghijkl"]
for password in passwords:
  if len(password) >= 6:
    print(f'The password {password} is valid')
  else:
    print(f'The password {password} must have at least 6 characters')
   

