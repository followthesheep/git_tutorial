import numpy as np

def getNthFib(n):
    """ Print the Nth entry in the Fibonacci Sequence """
    seq = [1,1]
    for ii in range(2,n):
        seq.append(seq[ii-1] + seq[ii-2])
    return seq[-1]

def getClosestFib(x):
    """ Print the closest Fibonacci number to a given input """
    seq = [1,1]
    stop = int(2*x)
    for ii in range(2,stop):
        seq.append(seq[ii-1] + seq[ii-2])
    seq    = np.array(seq)
    deltas = np.abs(seq - x)
    return seq[np.argmin(deltas)]

