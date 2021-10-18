#!/usr/bin/env python3

from integer import Integer
import matplotlib as plt
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
	for i in range(30 ,45):
		fibpy.append(fib_py(i))
		tidpy.append(pc()-startpy)
	startc = pc
	for i in range(30,45):
		f.set(i)
		fibc.append(f.fib())
		tidc.append(pc()-startc)
		
	end = pc()
	#print(f'tid = {end-start}')
	plt.plot(tidpy,fibpy,tidc,fibc)
	plt.show()
if __name__ == '__main__':
	main()