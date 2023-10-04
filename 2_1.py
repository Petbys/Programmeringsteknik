#mpg = float(input('Ange miles per gallon: '))
#lpm = 10./(mpg*1.609/3.785)
#lpm=round(lpm,1)
#print(f'Detta svarar mot {lpm} liter per mil')

#f=float(input('grader fahrenheit: '))
#c=(f-32)/1.8
#c=round(c,2)
#print(f'temperaturen motsvarar {c} grader celcius')
        
#kr=float(input('kronor: '))
#R=float(input('ränta: '))
#ar=int(input('år: '))
#sek=kr*R**ar
#
# import math
# p=float(input('p-värde'))
# q=float(input('p-värde'))
# rot1=-p/2+math.sqrt((p/2)**2-q)
# rot2= -p/2-math.sqrt((p/2)**2-q)       
# print(f'rötterna är {rot1} och {rot2}')

# import math
# p = float(input('p: '))
# q = float(input('q: '))
# disc = p*p - 4*q
# if disc < 0:
#     print('Komplexa rötter')
# else:
#     d = math.sqrt(disc)
#     print('x1 = ', (-p + d) /2.0)
#     print('x2 = ', (-p - d) /2.0)
# 
# numbers = []   # En tom lista
# print('Mata in positiva tal. Avbryt med 0')
# x = int(input('Första: '))
# while x > 0:
#     x = int(input('Nästa: '))
#     if x<=0:
#         print('negativt')
#         break
#     numbers.append(x)
# print('Inmatad lista: ', numbers)
# 
# j=0
# i=0
# while i<len(numbers):
#     
#     if numbers[i]%2 ==0:
#         j +=1
#         i +=1
#     else:
#         i +=1
#     
# print('antal jämna tal', j)

# x=int(input('x= '))
# n=int(input('n= '))
# j=1
# for i in range(n):
#     j*=x
# print(j)

values = [10, 15, 24, 17, 9, 8, 3]
for v in values:
    for i in range(v):
        print('ä',end='')
    print()

