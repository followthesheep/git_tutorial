def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n = int(raw_input("This program computes the nth number in the fibonnaci sequence.\nEnter a value for n: "))

print fibonacci(n)
