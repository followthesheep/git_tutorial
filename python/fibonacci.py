#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = int(raw_input('Give the number of the element in fib: '))

def fib(n):
    a, b = 0, 1
    for _ in xrange(n):
        yield a
        a, b = b, a + b

fiblist = list(fib(100))
fiblist.pop(0)

print 'the element is ', fiblist[int(a-1)]

