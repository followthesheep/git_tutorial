#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

a = int(raw_input('Give the number of the element in fib (within 1000): '))

def fib(n):
    a, b = 0, 1
    for _ in xrange(n):
        yield a
        a, b = b, a + b

fiblist = list(fib(1000))
fiblist.pop(0)

print 'the element is ', fiblist[int(a-1)]


b = float(raw_input('Give me the number: '))

fibarray = np.asarray(fiblist)
c = fibarray - b
ind = np.argmin(np.abs(c))

print 'the closest element is ', fiblist[ind]
