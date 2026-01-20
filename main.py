"1. Which are all necessary data inputs?"
"2. What i need to do with this data?"
"3. Which are all restrictions of this problem?"
"4. Which is the expected result?"
"5. Which are the step sequence to achieve the expected result?"

"Conditionals if elif else"

"I’m late for class. Can I still come in?"

"If this were your first or second time, yes, you could. But if this were your third time, you would be suspended."

lates = int(input('How many absences do you have?'))
if lates >= 3:
    print("you`re suspended")
elif lates == 1:
    print("you have just two more chances")
elif lates == 2:
    print("you have just one more chance")
else:
    print ("you didn`t late yet")



