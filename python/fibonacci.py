#!/usr/bin/env python

from numpy import *

def fibonacci(wantedElement):
	fibSequence = []
	fibSequence.append(1)
	fibSequence.append(1)
	
	curElementIndex = 2
	
	while curElementIndex < wantedElement:
		fibSequence.append(fibSequence[curElementIndex - 1] + fibSequence[curElementIndex - 2])
		
		curElementIndex = curElementIndex + 1
	
	return fibSequence[wantedElement - 1]

def closest_fibonacci(wantedClosestNumber):
	curFibIndex = 1
	prevFibNum = 0
	curFibNum = fibonacci(curFibIndex)
	
	diff = wantedClosestNumber - curFibNum
	
	while diff > 0:
		curFibIndex = curFibIndex + 1
		prevFibNum = curFibNum
		curFibNum = fibonacci(curFibIndex)
	
		diff = wantedClosestNumber - curFibNum
	
	if abs(wantedClosestNumber - curFibNum) < abs(wantedClosestNumber - prevFibNum):
		return curFibNum
	else:
		return prevFibNum

def testerFunc():
	print fibonacci(3)
	
	print closest_fibonacci(12)

if __name__ == "__main__":
	testerFunc()