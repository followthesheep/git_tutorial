import numpy as np

def fibonacci(nmax):
    fn = np.zeros(nmax,dtype="int")
    for i in range(0,nmax,1):
        if i < 1:
            fn[i] = 1
        else:
            fn[i] += fn[i-1] + fn[i-2]

    return fn


print fibonacci(10)
