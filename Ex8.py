import random

while True:
    choice_list = ["Rock", "Paper", "Scissors"]
    my_selection = random.choice(choice_list)

    user_selection = input("What is your pick out of Rock, Paper, Scissors? ")

    if user_selection == "Rock" and my_selection == "Rock":
        print("You have selected", user_selection)
        print("I have selected", my_selection)
        print("We are tied!")
        break
    if user_selection == "Rock" and my_selection == "Paper":
        print("You have selected", user_selection)
        print("I have selected", my_selection)
        print("You have lost!")
        break
    if user_selection == "Rock" and my_selection == "Scissors":
        print("You have selected", user_selection)
        print("I have selected", my_selection)
        print("You have won!")
        break
    if user_selection == "Paper" and my_selection == "Rock":
        print("You have selected", user_selection)
        print("I have selected", my_selection)
        print("You have won!")
        break
    if user_selection == "Paper" and my_selection == "Paper":
        print("You have selected", user_selection)
        print("I have selected", my_selection)
        print("We are tied!")
        break
    if user_selection == "Paper" and my_selection == "Scissors":
        print("You have selected", user_selection)
        print("I have selected", my_selection)
        print("You have lost!")
        break
    if user_selection == "Scissors" and my_selection == "Rock":
        print("You have selected", user_selection)
        print("I have selected", my_selection)
        print("You have lost!")
        break
    if user_selection == "Scissors" and my_selection == "Paper":
        print("You have selected", user_selection)
        print("I have selected", my_selection)
        print("You have won!")
        break
    if user_selection == "Scissors" and my_selection == "Scissors":
        print("You have selected", user_selection)
        print("I have selected", my_selection)
        print("We are tied!")
        break
