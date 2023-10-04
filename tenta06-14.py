'''
def euro_sek(pengar, euro):
    sek = pengar * euro
    return sek

pengar = int(input('Hur många euro vill du omvandla till SEK? '))

euro_i_sek = euro_sek(pengar, 10)
print(f'{pengar} euro är {euro_i_sek} sek')
'''
'''
ort  = ['Uppsala', 'Borås', 'Sundsvall', 'Luleå', 'Säffle']
boende = [177000, 113000, 99000, 78000, 9000]
stad={}
for i in range(len(ort)):
    stad[ort[i]] = boende[i]
print(stad['Borås'])
'''
'''
friends = ['Cia', 'Pia', 'Mia', 'Fia', 'Kurt']
enemy = input('Vem är inte längre din vän? ')
newfriends = [ind for ind in friends if ind != enemy]
for i in newfriends:
    print(f' Hi {i}')
'''
'''
ålder = int(input('Hur gammal är du? '))
if (ålder > 100):
    print('GRATTIS från Kungen')
elif (ålder >= 65):
    print('GRATTIS till pensionen')
elif (ålder >= 18):
    print('GRATTIS du är myndig')
else:
    print('GRATTIS lek medans du kan!')
'''
'''
def is_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def print_all_primes(n):
    for i in range(n):
        if is_prime_number(i) == True:
            print(i)
        
print_all_primes(17)
'''
'''
def delbart_3_5(n):
    for i in range(1,n+1):
        if i%3 ==0 and i%5 == 0:
            print(f'{i} ABCDEF')
        elif i%3 ==0:
            print(f'{i} ABC')
        elif i%5 ==0:
            print(f'{i} ABC')
        else:
            print(i)
delbart_3_5(100)
'''

import random
password_length = random.randint(8,12)
password = []
for _ in range(password_length):
    password.append(chr(random.randint(33,126)))
print(password)
print(random.randint(33,34))

'''
import math
def f(p,x):
    sum = 0
    for i, e in enumerate(p, 0):
        sum += math.pow(x, 0)*p[i]
    return sum

print(f([4,3,2],2))
'''
