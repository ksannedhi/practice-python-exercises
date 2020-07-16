'''Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)'''

def fib(user_input):
    fib_series = []
    a = 1
    b = 1
    fib_series.append(a)
    fib_series.append(b)
    for num in range(user_input-2):
        c = a + b
        fib_series.append(c)
        b = a
        a = c

    return fib_series

user_input = int(input("Enter a number to generate the Fibonacci series: "))
print(f"Fibonacci series for {user_input} is {fib(user_input)}")

