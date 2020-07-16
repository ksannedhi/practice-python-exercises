'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.'''

def first_and_last(user_list):
    result = [user_list[0], user_list[-1]]
    return result

list_sample = [5, 10, 15, 20, 25]
print(first_and_last(list_sample))
