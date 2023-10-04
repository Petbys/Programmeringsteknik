"""
Solutions to module 1
Student: 
Mail:
Reviewed by:
Reviewed date:
"""

import random
import time
from unittest.main import TestProgram


def power(x, n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)


def multiply(m, n):
        if m <= 0 or n <= 0:
            return 0
        else:
            return m+multiply(m,n-1)

def divide(t, n):
    if t-n==0:
        return 1
    else:
        return 1+divide(t-n,n)

def harmonic(n):
    if n==1:
        return 1
    else:
        return 1/n+harmonic(n-1)

def digit_sum(x):
    if x<10:
        return 1
    else:
        return x%10 + digit_sum(x//10)

def get_binary(x):
    if x < 2:
        print(x,end='')
    else:
        get_binary(x//2)
        get_binary(x%2)

def reverse(s):
    if len(s) == 1:
        return s
    else:    
        return s[-1] + reverse(s[:(len(s)-1)])


def largest(a):
    if len(a) == 1:
        return int(a[0])
    if a[0] < a[1]:
        return largest(a[1:])
    else:
        if len(a) >= 2:
            return largest([a[0]]+a[2:])
        else:
            return a[0]
#a = [5, 3, 7, 11, 4]
#print(largest(a),a)
def count(x, s):
    if len(s) < 1:
        return 0
    else:
        if type(s[0]) == list:
            return count(x, s[1:])
        else:
            if s[0] == x:
                return 1 + count(x,s[1:])
            else:
                return count(x,s[1:])
#print(count(4, [1, 4, 2, ['a', [ [ 4 ] , 3, 4] ] ] ))


def count2(x, s):        
    if len(s) < 1:
        return 0
    else:
    
        if type(s[0]) == list:
            if s[0] == x:
                return 1 + count2(x, s[1:]) 
            else:
                return count2(x, s[0]) + count2(x,s[1:])
        else:
            if s[0] == x:
                return 1 + count2(x, s[1:]) 
            else: 
                return count2(x, s[1:])
#print(count2([4,3], [1, 4, 2, ['a', [[4,3 ] , 4,3, 4] ] ] ))  

def zippa(l1, l2):
    if l1 != [] or len(l1) > 1:
        return [l1[0]] + zippa(l2,l1[1:])
    else:
        if len(l1) < 1 and len(l2) < 1:
            return []
        else:
            return zippa(l2,l1)
    

#print(zippa([1, 3, 5], [ 2, 4, 6, 8, 10]))



def bricklek(f, t, h, n): # Compulsory
    if n>1:
        return bricklek(f,h,t,n-1)+[f+'->'+t]+bricklek(h,t,f,n-1)

    else:
        return [f+'->'+t]

def power(x, n):
    i = 0
    s = 1
    if n % 2 == 1:
        n -= 1
        s = x
    while n % 2 == 0:
        n *= 1/2
        i +=1
    for _ in range(0,i+1):
        for _ in range (0, int(n)):
            s*= x
    return s

#print(power(2,16))
            
            
        

print(bricklek('f','t','h',4))
def main():
    """ Demonstates my implementations """
    # Write your demonstration code here
    print('Bye!')

def time():
    return 

if __name__ == "__main__":
    main()
    
####################################################    
    
"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 15: Time for bricklek with 50 bricks:
"""
def tidbricklek(l): # Compulsory
    return str(len(l)) + ' sekunder'

#print(tidbricklek(bricklek('a','b','c',30)))

"""
  Exercise 17: Time for Fibonacci:
"""
#(a)
"""
t(n) = 1.618^n * c
c = t(n)/1.618^n
c = 1.818*10^-7
fib 50 = 5 113,3912841387 sek
fib 100 = 143 758 949 531 346,56 sek
"""
#(b)


""" 
  Exercise 19: Comparison sorting methods:
  
  m(10^6) = 2000 s
  m(10^9) = 3*10^6 s
  i(10^6)= 10^6 s
  i(10^9) = 10^12 s

  
  
  
  Exercise 20: Comparison Theta(n) and Theta(n log n)
  
B -  c*n*logn
vid n = 10 => 1 sek
1 sek = c*n*logn
1/(10*1) = c
c = 1/10
vilket ger:
B - n*logn/10
A - n
n  < n*logn/10
1  < logn/10
10 < logn
10^10 < n
  
"""