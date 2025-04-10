# Modules
import random

# Variables
sgw = {
    1 : "snake",
    2 : "water",
    3 : "gun"
}
rule = '''
Winning Rules:
Snake vs. Water → Snake drinks water and Snake wins
Water vs. Gun → Water douses gun and Water wins
Gun vs. Snake → Gun shoots snake and Gun wins
'''
print(rule)
usr_choice = input("Enter your Choice: ").strip().lower()

# Random
rand = random.randint(1,3)
com = sgw.get(rand)

# Printing
print(f"Computer chose: {com}")
print(f"You chose: {usr_choice}")

# Conditional Statements
if usr_choice not in sgw.values():
    print("Invalid Choice!!!")
elif com==usr_choice:
    print("Oh That's a Draw")
else:
    if com=="snake" and usr_choice=="water":
        print("So sorry, You lose")
    elif com=="water" and usr_choice=="snake":
        print("Congrats, You won")
    elif com=="water" and usr_choice=="gun":
        print("So sorry, You lose")
    elif com=="gun" and usr_choice=="water":
        print("Congrats, You won")
    elif com=="snake" and usr_choice=="gun":
        print("Congrats, You won")
    elif com=="gun" and usr_choice=="snake":
        print("So sorry, You lose")
    else:
        print("Something went wrong!!")
        