#!/usr/python/bin

import numpy as np

def sum_inverse_integers(n):
 if n <= 1: return 1
 else:
  tot = 0.
  for x in range(1,n+1): tot += 1./x
  return tot


def closest_sum(n):
 if n <= 1.: return 1.
 else:
  n = float(n)
  ind = 1
  diff = 1.
  while diff >= 0.:
   diff = n - sum_inverse_integers(ind)
   ind += 1
  argind = np.argmin([np.abs(diff), np.abs(n - sum_inverse_integers(ind-2))])
  return [sum_inverse_integers(ind-1), sum_inverse_integers(ind-2)][argind]

print "First 10 values in the sequence sum(1/x) where x is an integer > 0:"
for x in range(1,10): print sum_inverse_integers(x)

print "Closest value to 2.5:"
print closest_sum(2.5)
