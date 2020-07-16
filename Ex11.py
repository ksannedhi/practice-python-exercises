'''Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer from Exercise 4 to help you. Take this opportunity to practice using functions.'''

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
