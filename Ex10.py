a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

if len(b) > len(a):
    c = [num for num in b if num in a]
else:
    c= [num for num in a if num in b]

print(f"Unique elements between both the lists {c}")
