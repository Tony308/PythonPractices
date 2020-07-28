def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
        
def fibonacci(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) + factorial(n)
    
