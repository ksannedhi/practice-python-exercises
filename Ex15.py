def reverse_words(input_text):
    words = input_text.split()
    rev_words = words[::-1]
    return " ".join(rev_words)

user_input_text = input("Type something: ")
print(f'Reversed output: {reverse_words(user_input_text)}')
