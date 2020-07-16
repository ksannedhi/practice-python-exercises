'''Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.'''

import random

choice_range = list(range(1,10))
my_choice = random.choice(choice_range)
user_input = int(input("Enter a number between 0 and 10: "))

while True:
    if user_input == my_choice:
        print("You have typed:", user_input)
        print(f"Computer's guess: {my_choice}")
        print("You guessed it right")
        break
    elif user_input < my_choice:
        print("You have typed:", user_input)
        print("Your input is lower than computer's guess")
        user_input = int(input("Guess again: "))
        continue
    else:
        print("You have typed:", user_input)
        print("Your input is higher than computer's guess")
        user_input = int(input("Guess again: "))
        continue
