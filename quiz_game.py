print("Welcome to my computer quiz!")

playing = input('Do you want to play?')

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for?")
if answer.lower() == "Central Processing Unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("How many continents are in the world?")
if answer.lower() == "7":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("How do you insert Comments in Python code?")
if answer.lower() == "#":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What is the correct file extension for python files?")
if answer.lower() == ".py":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("How do you create a variable with the floating number 2.8?")
if answer.lower() == "x = 2.8":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What is the correct way to create a function in python?")
if answer.lower() == "def myFunction":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("Which collection is ordered, changeable, and allows duplicate members?")
if answer.lower() == "List":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score /7) * 100) + ":.2%.")
