import numpy as np
import math

nmax = 10
fn = np.zeros(nmax,dtype="int")
for i in range(1,nmax,1):
    if i < 2:
        fn[i] = 1
    else:
        fn[i] += fn[i-1] + fn[i-2]

print fn

