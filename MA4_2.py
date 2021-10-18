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
		tidpy.append(float(pc()-startpy))
	startc = pc()
	for i in range(10,30):
		f.set(i)
		fibc.append(f.fib())
		tid = pc()
		tidc.append(float(tid-startc))
		
	end = pc()
	#print(f'tid = {end-start}')
	plt.plot(tidpy,fibpy,tidc,fibc)
	plt.savefig('fib.png')
if __name__ == '__main__':
	main()