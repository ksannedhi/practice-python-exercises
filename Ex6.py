input_string = input("Enter any word: ")

if input_string == input_string[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
