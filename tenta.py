''' 1
i=0
s=0
while i<50:
    if i%2 == 0:
        s+=i
    i+=1
print('s =', s)
'''
''' 2
returnerar hur många värden (a) som är större än x i ett lexikon
def value_biggerthan_x(dic,x):
    a = 0
    for e in d.items():
        if e[1] > x:
            a += 1
    return a
'''



def update(x, priceChange):
    global prices
    prices =[ i+i*priceChange/100 for i in x]
    
    return prices

prices = [2.5, 11.0, 9.5]
priceChange = 5.0  # Höj priset med 5%
print(update(prices, priceChange))


''' 4 
def distort(s):
    for i in s:
        if not s.islower():
            

s = 'AbCd'
print(distort(s))      # ger BcDe
s = 'Python'
print(distort(s))      # ger Qzuipo
'''
'''5
def mean(x):
    x=[float(i) for i in x.split(',')]
    return sum(x)/len(x)
    
#sum(float(i.split(',')))/len(x)

print(mean('1.0,2.0,3.0,4.0'))
'''
'''6
def part2(x):
    return x[1]

def frek(s):
    freq={}
    s = [i.lower() for i in s.split()]
    for i in s:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    return sorted(freq.items(),key=part2, reverse=True)

s = 'ab dc DC be Dc Be xy z'
print(frek(s))
'''
'''
class MoneyMachine:
    
    def __init__(self, Namn, belopp):
        self.namn = Namn
        self.belopp = belopp
        
    def getBalance(self):
        return self.belopp
    
    def withdraw(self, belopp):
        self.belopp-=belopp
        return self.belopp


mm = MoneyMachine('PollaxAutomaten', 100)
print(mm)
while mm.getBalance() > 0:
    print('Automaten innehåller', mm.getBalance(), 'kr')
    belopp = int(input('Belopp att ta ut?'))
    if belopp <= mm.getBalance():
        mm.withdraw(belopp)
    else:
        print('Uttaget är för stort')

print('Automaten stänger')
print(mm)

'''






