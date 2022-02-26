cache = {}

def fibonacci(n):
    if n < 3:
        return 1
    if n in cache:
        return cache[n] 
    cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]


fib_30 = fibonacci(30)
print(f'the 30th Fibonacci number is {fib_30}')
fib_50 = fibonacci(50)
print(f'the 30th Fibonacci number is {fib_50}')

