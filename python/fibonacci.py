import numpy as n

def fib(n):
    if n > 1:
        return n+fib(n-1)
    else:
        return 1


