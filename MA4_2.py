#!/usr/bin/env python3

from integer import Integer
import matplotlib
from time import perf_counter as pc



def main():
	start = pc()
	f = Integer(1)
	for i in range(10):
		print(f.fib(i))
		f.set(i)
		print(f.get())
	end = pc()
	print(f'tid = {end-start}')
if __name__ == '__main__':
	main()