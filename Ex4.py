user_input = int(input("Enter a number: "))

list_divisors = []

for num in range(2, user_input):
    if user_input % num == 0:
        list_divisors.append(num)

print(f"List of divisors = {list_divisors}")
