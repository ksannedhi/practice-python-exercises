'''Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)'''

input_string = input("Enter any word: ")

if input_string == input_string[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
