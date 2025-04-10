# Modules
import random

#Variables
randnum = random.randint(1,100)
usernum = -1
guesses = 0

# If-elif-else Conditions
while(usernum!=randnum):
    usernum = int(input("Enter your Guess: "))
    guesses += 1
    if randnum > usernum:
        print("Guess a bigger number")
    elif randnum < usernum:
        print("Guess a shorter number")
    else:
        print(f"You Guessed the number right in {guesses} attempts. Congrats (: ")