
'''
def todict(lst):
    result = {}
    for word in lst:
        key = word[0].upper()
        if key not in result:
            result[key] = []
        result[key].append(word)   
    return result
lst=['arm','varm','harm','larm','srm','rrm','aaaarm','fffarm']
print(todict(lst))
'''
'''
def reciprocal(lst):
    nylst = []
    for i in lst:
        nylst.append(1/i)
    return nylst

lst = [5,10,15,14]
print(reciprocal(lst))
'''
'''
class student:
    
    
    __init__(self,first,last):
        self.name = f'{first + last}'
        self.grade = 'None'
        
        
    setGrade(self,grade=3):
        if grade not in [0,3,4,5]:
            return
        self.grade = grade
'''
'''
class Square:
    def __init__(self, side):
        """Initialize a list of lists with spaces in all position, representing
        an empty side * side square."""
        self.map = [[’ ’] * side for _ in range(side)]
    def plot(self, x, y, c):
        """Plot character c at the appropriate integer location within
        the current map, for x and y coordinates in the range
        0 <= x, y < 1."""
        side = len(self.map)
        # ingen avrundning, utan trunkering, f ̈or att alltid ge giltiga index
        self.map[int(y * side)][int(x * side)] = c  # To be implemented by you
    def __str__(self):
        """Present the map as a single string."""
        return ’\n’.join([’’.join(row) for row in self.map])
s = Square(5)
    # We can plot something manually
s.map[3][3] = ’x’
    # We should be able to do so using the plot method as well
s.plot(0.45, 0.73, ’y’)
print(s)

'''
'''
def cube(lst):
    q = [ i*i*i for i in lst]
    return q

def capitalize(word):
    return word[0].upper() + word[1:]


def countQ(word):
    count = 0
        for c in line:
            if c == ’Q’:
                count += 1
return count


def longestWord(data):
     with open(data, 'r') as file:
        word=[i.split() for i in file]
        sofar =' '
        for i in word:
            if len(word)>len(sofar)
                sofar = word
    return sofar 
'''
'''
def double(x):
    x=x*2
    return x
x=2
y = increment(x)
print(x, y)
'''
'''
def add_two_lists(a,b):
    nylista=[]
    if len(a)>=len(b):
        for n in range(len(b)):
            nylista.append(a[n]+b[n])
    else:
        for n in range(len(a)):
            nylista.append(a+b)
    return nylista

print (add_two_lists([1,2,4,5,3],[2,1,3,4,5]))
'''
'''
def fibonacci(n):
    a0=0
    a1=1
    for i in range(1,n):
        fib=a0+a1
        a0=a1
        a1=fib
        print(a0,a1,fib)
    return a1
        
        
print(fibonacci(6))


'''
'''
def median(lst):
    a = len(lst)
    mid = (lst[int(a/2)]+lst[int((a-1)/2)])/2
    return mid

print(median([1,1,1,1,1,2,4,5,6,7,8,9]))
'''
'''
def word_freq(s):
    s.isalpha()
    text = s.split()
    print(s)
    freq = {}
    for word in text:
        if freq.get(word) == None:
            freq[word] =1
        else:
            freq[word] +=1
    return freq

print(word_freq('hej hej monica hej på dig monica'))
'''
'''
import random

class PokerDice:
    
    def __init__(self):
        self.values = [random.randint(0,12) for _ in range(5)]
        
    def __str__(self):
        self.assvalues1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, Kn, D, K, E]
        for i in self.values():
            self.assvalues2 = self.assvalues1[i]
        return self.assvalues2()
        
        strs = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             'Kn', 'D', 'K', 'E']
        inner = ', '.join([strs[i] for i in self.values])
        return f'[{inner}]'
    def roll(self):
        
        
'''
'''        
def bubblesort(lst):
    for i in range(len(lst)):
        if lst[i] < lst[i+1]:
            temp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = temp
'''
'''
def reverse_list(lst):
    for i in range(int(len(lst)/2)):
        temp = lst[i]
        lst[i] = lst[-i-1]
        lst[-i-1] = temp
    return lst


    
    
lst = [1,2,3,4,5,6,7,4,2]
print(reverse_list(lst))

'''
'''
def factorial(m):
    n = m-1
    while n >0:
        m*=n
        n-=1
    return m
print (factorial(4))
        
'''
'''
def maximum_with_index(lst):
    maxindex=0
    for i, val in enumerate(lst):
        if val>lst[maxindex]:
            maxindex=i
    return (lst[maxindex],maxindex)
lst = [1,2,3,4,5,6,7,4,2]
print(maximum_with_index(lst))
'''
'''
def letter_freq(s):
    freq={}
    
    for i in s:
        if i.isalpha():
            if i in freq:
                freq[i]+= 1
            else:
                freq[i] = 1
        else:
            continue
    return freq
print(letter_freq('hej hej monica hej på dig monica'))
'''
'''
def split(s,c):
    nylst = []
    paus = 0
    for i in s:
        if i != c:
            if nylst[paus] == None:
               nylst.append(i)
            else:
                nylst[paus] += i
             
        else:
            paus +=1
   
    return nylst
            
print(split('hej hej monica hej på dig monica',' '))
'''
'''
class Vector2D:
    
    def __init__(self,x,y):
        self.xcord = x
        self.ycord = y
        
    def __str__(self):
        return f'<{self.xcord},{self.ycord}>'
        
        
    def add(self,v):
        return Vector2D( self.xcord + v.xcord,self.ycord + v.ycord)
        
        
        
    def scalar_product(self,v):
        return  self.xcord * v.xcord +self.ycord * v.ycord
        
'''
'''
def f(x):
    return (x[0]+x[1])
    


a = [(1, 2), (5, -7), (9, 3), (0, 1)]
b = sorted(a, key=f, reverse=True)
x1 = f((3, 4))
print(x1)
print(b)




'''
'''
def pow(x, y):
    xy=x
    for _ in range(y-1):
        xy*=x
    return xy
print(pow(3,3))
'''
'''
def less(lst,a):
    result = []
    for i, x in enumerate(lst):
        if x<a:
            result.append(i)
    return result
print(less([1, 2, 6, 4, 0, 7, 9, 3, 2], 3))
def less(lst,a):
    return [i for i,x in enumerate(lst) if x<a]
    
print(less([1, 2, 6, 4, 0, 7, 9, 3, 2], 3))    

'''
'''
class Person:
    
    def __init__(self, namn, epost):
        self.namn = namn
        self.epost = epost
        
    def print_person(self):
        print( f' Namn:  {self.namn}  Epost: {self.epost}')
p = Person('Jan Karlsson', 'jan.karlsson@gmail.com')
p.print_person()
        
'''
'''
import math

def e_distance(a,b):
    distance = math.sqrt(((a[0]-b[0])**2 +(a[1]-b[1])**2 ))
    return distance
print (e_distance((2,2),(3,3)))
'''

