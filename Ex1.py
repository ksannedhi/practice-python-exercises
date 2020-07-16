'''Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.'''

your_age = input("Enter your age: ")
your_name = input("Enter your name: ")

cur_year = 2020

birth_year = cur_year - int(your_age)

print(f'Hi {your_name}, you will turn 100 in the year {birth_year + 100}')
