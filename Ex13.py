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
