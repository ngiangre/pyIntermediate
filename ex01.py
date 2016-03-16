'''
Exercise 1
Objective: create a function fibonacci(n) that will return the fibonacci sequence to the nth place
'''

#/usr/bin/python

#Objective: create a function fibonacci(n) that will return the fibonacci sequence to the nth place

import sys

n=int(sys.argv[1])+1

F0 = int(0)
F1 = int(1)

def fib(n):
	arr = [1]*n
	for i in range(0,n):
		if i == 0:
			arr[i]=F0
		if i == 1:
			arr[i]=F1
		if i >= 2:
			arr[i]=arr[i-1]+arr[i-2]
	print", ".join('%2d'%x for x in arr)

if __name__ == "__main__":
	fib(n)