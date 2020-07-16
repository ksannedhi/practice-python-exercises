'''Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.'''

def using_lists(input_list):
    output_list1 = []
    for num in input_list:
        if num in output_list1:
            pass
        else:
            output_list1.append(num)
    return output_list1

def using_set(input_list):
    output_list2 = set(input_list)
    return output_list2

list1 = [2, 4, 6, 8, 10, 3, 4, 8]
print(f'Output with no duplicates using lists only {using_lists(list1)}')
print(f'Output with no duplicates using set {using_set(list1)}')
