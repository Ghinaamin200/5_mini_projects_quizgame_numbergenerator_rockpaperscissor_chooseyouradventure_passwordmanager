import random
user = 0
computer = 0
options = ["rock","paper","scissor"]
user_win = 0
computer_win  =0
total  = 0
draw = 0
while True:
    user = input("Enter Rock/Paper/Scissor or Q to Quit: ").lower()
    if user == "q":
        break
    elif user not in options:
        print("Invalid Input!")
        continue
    total += 1
    random_number = random.randint(0,2)
    computer = options[random_number]
    print("Computer picked: ",computer)
    if computer != user:
        if user == 'scissor' and computer == 'paper':
            print ("You win!")
            user_win += 1
            continue
        elif user == 'paper' and computer == 'rock':
            print ("You win!")
            user_win += 1
            continue
        elif user == 'rock' and computer == 'scissor':
            print ("You win!")
            user_win += 1
            continue
        else:
            print("You lose!")
            computer_win += 1
    else:
        print("Draw!")
        draw += 1
print ("You wins",user_win,"times out of",total,"games")
print ("Percentage = "+str(round((user_win/total)*100,2))+"%")
print ("Computer wins",computer_win,"times out of",total,"games")
print ("Percentage = "+str(round((computer_win/total)*100,2))+"%")
print ("Number of Draws =",draw)
print ("Percentage = "+str(round((draw/total)*100,2))+"%")
print ("GoodBye!")