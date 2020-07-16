'''Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
My name is Michele

Then I would see the string:
Michele is name My'''

def reverse_words(input_text):
    words = input_text.split()
    rev_words = words[::-1]
    return " ".join(rev_words)

user_input_text = input("Type something: ")
print(f'Reversed output: {reverse_words(user_input_text)}')
