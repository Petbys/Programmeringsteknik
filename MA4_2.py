#!/usr/bin/env python3

from integer import Integer
import matplotlib.pyplot as plt
from time import perf_counter as pc

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))



def main():
	
	tidpy = []
	fibpy = []
	tidc = []
	fibc = []
	startpy = pc()
	f = Integer(1)
	for i in range(10 ,30):
		fibpy.append(fib_py(i))
		tid = pc()
		tidpy.append(round(tid-startpy,2))
	startc = pc()
	for i in range(10,30):
		f.set(i)
		fibc.append(f.fib())
		tid = pc()
		tidc.append(round(tid-startc,2))
		
	end = pc()
	#print(f'tid = {end-start}')
	plt.plot(fibpy,tidpy,'r',fibc,tidc,'b')
	plt.savefig('fib.png')
if __name__ == '__main__':
	main()