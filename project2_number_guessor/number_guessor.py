import random
top_range= input("Enter any number greater then 0: ")
if top_range.isdigit():
    top_range = int(top_range)
    if top_range == 0:
        print ("Please enter a number greater than 0")
else:
    print ("Please enter a number: ")
    quit()
random_number = random.randint(0,top_range)
guess_number = 0
while True:
    guess = input("Make your Guess: ")
    guess_number += 1
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Entered value is not a number!")
        continue
    if(guess == random_number):
        print("You got it!")
        break
    elif guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")
print ("You got it on ", guess_number," guess")

