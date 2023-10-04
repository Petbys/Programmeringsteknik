'''
def fahrenheit_to_kelvin(f):  
    c=(5/9) * (f - 32)
    return c+273

print('temperaturen i kelvin', fahrenheit_to_kelvin(float(input('temperatur i faherenheit'))))

'''

'''Skriv en funktion som tar en temperatur uttryckt i grader Celsius (som parameter) och returnerar temperaturen i grader Fahrenheit.'''
'''

t = float(input('temperatur i celsius'))

def celcius_to_faherenheit(c):
    f=(9/5)*c+32
    return f
print('temperaturen i fahrenheit',celcius_to_faherenheit(t))
'''
'''

#Kör programmet och undersök vad variablerna f och c har för värde efter print-satsen!

def fahrenheit_to_celsius(f):
    c = (5/9) * (f - 32)
    return c

print(fahrenheit_to_celsius(77))
'''
'''

#Skriv en funktion howmany(sum) som beräknar och returnerar antalet termer som behövs i den harmoniska serien för att summan ska bli större än sum.


def howmany(sum):
    s = 0
    n = 0
    while s < sum:
        n += 1
        s += 1/n
    return n
print(howmany(sum))
'''
'''
    
#Skriv en funktion digits(x) som returnerar antalet (decimala) siffror som finns i heltalet x. Låt digits(0) vara 0.

#Float -> int, float-int, float*10, repetera
x=230
def digits(x):
    n=0
    while x!=0:
        n+=1
        x= x//10
    return n
print('antal siffror', digits(x))
    
'''
'''
#Skriv en funktion digitsum(x) som siffersumman i heltalet x.
x=

def digitsum(x):
    s=0
    
    while x!=0:
        s += x%10
        x=x//10

    return s
print('siffersumma', digitsum(x))
    
'''
'''

import math
# # Herons formel: Beräknar arean av 
# # en triangel med sidorna a, b, c
# def triangle_area(a, b, c):        
#     s = (a + b + c)/2
#     t = s*(s-a)*(s-b)*(s-c)
#     if t < 0:
#         print("Can't form a triangle of: ", a, b, c)
#         return None
#     r = math.sqrt(t)
#     return r

def triangle_area(a, b, c):
    s = (a + b + c)/2
    t = s*(s-a)*(s-b)*(s-c)
    if t < 0:
        print("Can't form a triangle of: ", a, b, c)
        return None
    r = math.sqrt(t)
    return r

'''
'''
def square_sum(a_list):  
    result = 0
    for x in a_list:
        result += x*x
    return result
'''
'''

def is_prime(n):
    limit = int(n**0.5)
    i = 2
    for i in range(2, limit+1):
        if n%i == 0:
            return False
    return True

def is_twin_prime(n):
    return is_prime(n) and is_prime(n+2)


is_twin_prime(7)

'''
import math

p=float(input('ange p'))
q=float(input('ange q'))
def quad_equation(p, q):
    disc = p*p - 4*q
    if disc >= 0:
        d = math.sqrt(disc)
        x1 = (-p + d)/2.0
        x2 = (-p - d)/2.0
        return x1, x2
    else:
        return None
while True:
        print(quad_equation(p, q))
        p=float(input('ange p'))
        q=float(input('ange q'))
        try:
            print(quad_equation(p, q))
            break
        except ValueError:
            print('Dåliga argument forsok igen')
        return None
        
    
'''
r = quad_equation(-3, 2) 
if r == None:
    print('Komplexa rötter')
else:
    print('x1: ', r[0])
    print('x2: ', r[1])

if (p/2)*(p/2) =< q:
    raise value

'''

