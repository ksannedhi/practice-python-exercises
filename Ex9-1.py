'''Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.'''

import random
computer_guess = random.randint(1, 9)
your_num = int(input("Guess a number: "))

while True:
    if your_num > computer_guess:
        print("Guess a lower number.")
        your_num = int(input("Enter your guess again: "))
        pass
    elif your_num < computer_guess:
        print("Guess a bigger number.")
        your_num = int(input("Enter your guess again: "))
        pass
    else:
        print("You guessed it correctly. Good job!")
        break
