import random
computer_guess = random.randint(1, 11)
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
