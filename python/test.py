import math

fibs = {1:1,2:1}
def fib(n):
	if n in fibs.keys(): return fibs[n]
	else: val = n if n<2 else fib(n-1) + fib(n-2)
	fibs.update({n:val})
	return val

def closest_fib(x):
	assert(x>0)
	prevdist,currdist=-1,0
	prevfib,currfib = 0,0
	i=0
	while True:
		i+=1
		currfib = fib(i)
		currdist=abs(currfib-x)
		if prevdist<currdist and prevdist!=-1:
			return prevfib
		else:
			prevdist=currdist
			prevfib=currfib

print 'closest_fib(11) ',closest_fib(354224848179261915076)
