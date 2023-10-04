def cube(lst):
    [3*3 for el in lst]
    return lst

[1,2,3,4,5,6,7]

def capitalize(word):
    return word[0].upper() + word[1:]



def countQ(line):
    count = 0
    for c in line:
        if c == 'Q':
            count += 1
    return count

print(countQ('QDFSFFSQQQFSFD'))

def longestword(data):
    sofar = ' '
    for word in data.split():
        if len(word)>len(sofar):
            sofar = word
    return sofar

class point:
    def __init__(self, x, y):
        self.pos = (x,y)
        
    def rot90(self,n=1):
        for _ in range (n % 4):
            self.pos = (-self.pos[1],self.pos[0])
        
    def __eq__(self, other):
        return self.pos == other.pos
    
    
    
def todict(lst):
    result = {}
    for word in lst:
        key = word[0].upper()
    if key not in result:
        result[key]=[]
    result[key].append(word)
    
    
def reciprocal(lst):
    return [1/i for i in lst]
print(reciprocal([1,2,3,4,5,6,7]))
    

class Student:
    def __init__(self, first, last):
         self.name = f'{first} {last}'
         self.grade = None
         
         
    def setgrade(self, grade=3):
        if grade not in [0,3,4,5]:
            self.grade = grade
        if self.grade is None or self.grade < grade:
            self.grade = grade
            
    def __str__(self):
        grade = self.grade
        if grade is None:
            grade = '-'
        elif grade == 0:
            grade = 'U'
        return f'{self.name} {self.grade}'
'''   
eb = Student('eva', 'bys')
eb.setgrade(5)
print(eb)
'''

def getgrades(s):
    return s.grade()

#students2 = [student for student in students if student.grade in [3,4,5]]
#students2.sort(key=getgrades)


class Square:
    def __init__(self, side):
        """Initialize a list of lists with spaces in all position, representing
        an empty side * side square."""
        self.map = [[' '] * side for _ in range(side)]
    def plot(self, x, y, c):
        """Plot character c at the appropriate integer location within
        the current map, for x and y coordinates in the range
        0 <= x, y < 1."""
        side = len(self.map)
        self.map[int(y*side)][int(x*side)] = c
    def __str__(self):
        """Present the map as a single string."""
        return '\n'.join([''.join(row) for row in self.map])
s = Square(5)
# We can plot something manually
s.map[3][3] = 'x'
# We should be able to do so using the plot method as well
s.plot(0.45, 0.73, 'y')
print(s)

'''
wordlist = []
    with open(’words.txt’, ’r’) as a:
for line in a: # iterera direkt  ̈over fil
for w in line.split(): # split delar upp i ord vid mellanslag
                wordlist.append(w)
    print(wordlist)
'''

def distort(word):
    new_word = ""
    alphapet = "abcdefghijklmnopqrstuvwxyzabc"
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
    for i in word:
        if i.islower(): #check if i s letter
            index = alphapet.index(i) + 1 #get the index of the following letter
            new_word += alphapet[index]    
        elif i.isupper():
            index = ALPHABET.index(i) + 1
            new_word += ALPHABET[index]
        else:
            new_word += i    
    return new_word
        
print(distort('AAbcd'))