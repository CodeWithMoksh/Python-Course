# Random for choosing the random word from the list
import random

# List of Words
words = ["seperate", "moksh", "thanks", "python", "programmer", "counting"]

# Choosing Random word
word = random.choice(words)

guess_word = ['_'] * len(word)

# Count of attempts
attempts = 10

# Creating a while loop so that when the attempts are less than 0 it might stop
while attempts > 0:
    # Adding the space in the list of '_'
    print('Current word: ' + ' '.join(guess_word))

    # Taking input from the user
    user_word = input("Enter your guess: ").lower()

    if user_word in word:
        # Creating a for loop to check the letter and its index simultanously
        for index,letter in enumerate(word): 
            if(letter == user_word):
                guess_word[index] = user_word
                print("Good guess!!!")
    
    else:
        attempts -= 1
        print(f"Your guess is wrong. Now you have only {attempts} attempts left!!!")

    # Checking that the user has won the guess game or not
    if('_' not in guess_word):
        print(f"Congratulations!!! You guessed the word right. \n The word is {word}")
        break
    
# Ran out of attempts warning
else:
    print(f"Sorry, you ran out of attempts. The word was: {word}")