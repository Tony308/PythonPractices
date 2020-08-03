def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
        
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)