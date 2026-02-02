#Problem - total expenses wit salary payments
#Given a list of salaries, calculate the total paid to all employees

##1. What are the required input data?
# the salaries list
#2. What should I do with these data?
# sum all given salaries
#3. What are the constraints of this problem?
#sum only the given salaries, at least 2 salaries
#4. What is the expected result?
# the sum of the given salaries
#5. What is the sequence of steps to reach the expected result? (pseudocode)
#5.1.receive the salaries list
#5.2.sum the salaries list until receive the total
#5.3 print the value of the sum

salaries = [2500, 900, 500, 7500]
total = 0
for salary in salaries:
    total = total + salary
    print(total)
