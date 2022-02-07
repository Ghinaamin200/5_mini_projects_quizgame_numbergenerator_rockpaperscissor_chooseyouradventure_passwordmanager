print("Welcome to My computer code")

playing = input("Do you want to play: ")

if (playing.lower() != "yes"):
    quit()

print("Okay let's play!")
score = 0
answer = input("What does CPU stands for? ")
correct = "central processing unit"
if (answer.lower() == correct):
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print('Correct Answer = ' + correct)
answer = input("What does GUI stands for? ")
correct = "graphical user interface"
if (answer.lower() == correct):
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    print('Correct Answer = ' + correct)
answer = input("What does HTML stands for? ")
correct = "hypertext markup language"
if (answer.lower() == correct):
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    print('Correct Answer = ' + correct)
print ("You got "+ str(score)+ " questions correctly.")
answer = input("What does CSS stands for? ")
correct = "cascading style sheets"
if (answer.lower() == correct):
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    print('Correct Answer = ' + correct)
print ("You got "+ str(score)+ " questions correctly.")
print( "Percentage = "+ str((score/4)*100)+ " %")