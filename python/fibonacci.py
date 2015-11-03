import numpy as np

nmax0 = sys.argv[1]
nmax0 = int(nmax0)

def fibonacci(nmax):
    fn = np.zeros(nmax,dtype="int")
    for i in range(0,nmax,1):
        if i < 1:
            fn[i] = 1
        else:
            fn[i] += fn[i-1] + fn[i-2]

    return fn

print fibonacci(nmax0)
