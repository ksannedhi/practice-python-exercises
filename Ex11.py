def find_prime_or_not(num):
    divisors = list(range(1,num+1))
    div_list = [div for div in divisors if num%div == 0]
    if len(div_list) == 2:
        result = "Prime"
    else:
        result = "Not prime"

    return result

user_input = int(input("Please enter a number: "))
print(find_prime_or_not(user_input))
