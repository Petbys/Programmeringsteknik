""" linked_list.py

Student: Petter Byström
Mail:
Reviewed by: Ben Bucknall
Date reviewed:
"""

class LinkedList:
    
    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ      
        
            
    def __init__(self):
        self.first = None

    
    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ
            
    def __in__(self, x):           # Discussed in the section on operator overloading 
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False 
        return False
        
    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')            
    
    
    # To be implemented
    
    def length(self):
        f = self.first
        if f == None:
            return 0
        l = 1
        while f.succ:
            f = f.succ
            l += 1
        return l
  
  
    def mean(self):               # Optional
        f = self.first
        sum = 0
        while f:
            sum += f.data
            f = f.succ
        return sum/self.length()
    
    
    def remove_last(self):        # Optional
        f = self.first
        while f:
            if f is None:
                val = f.data
                f.data = None
                return val
            temp = f
            if f.succ is not None:
                f = f.succ
            if f.succ is None:
                val = f.data
                temp.succ = None
                f.data = None
                return val
        
    
    def remove(self, x):          # Compulsory
        #if self.first is x:
        if self.first is None or x < self.first.data:
            return False
        else:
            f = self.first
            temp = f
            while f and x > f.data:
                temp = f
                f = f.succ
            if f.data is x:
                temp.succ = f.succ
                return True
            else:
                return False
    
    
    def count(self, x):           # Optional
        return self._count(x,self.first)

    def _count(self,x,f):
        if f.succ is None:
            if f.data is x:
                return 1
            else:
                return 0
        if f.data is x:
            return 1 + self._count(x, f.succ)
        else:
            return self._count(x, f.succ)

    def to_list(self):            # Compulsory
        return self._to_list(self.first)
    
    def _to_list(self,f):
        if f == None:
            return []
        if f.succ != None:
            return [f.data] + self._to_list(f.succ)
        else:
            return [f.data]

    
    def remove_all(self, x):      # Compulsory
        self.first = self._remove_all(x, self.first)

    def _remove_all(self,x,f):
        if f.succ != None:
            if f.data == x:
                return self._remove_all(x,f.succ)
            else:
                f.succ = self._remove_all(x,f.succ)
                return f
        else:
            if f.data == x:
                return
            else:
                return f
       


    def __str__(self):
        string='(' 
        i = 0
        for f in self:
            if i != 0:
                string += ', '
            string += str(f)
            i += 1
        return string + ')'
    
    
    def merge(self, lst):         # Compulsory
        for x in lst:
            self.insert(x)
        return self
        
        # lst = lst.to_list()
        # n =0
        # result =[]
        # for i in self:
        #     while i > lst[n] and n < len(lst) - 1 :
        #         result.append(lst[n])
        #         n+=1
        #         if n == len(lst)-1:
        #             result.append(lst[n-1])
        #     result.append(i)
        
   
        
    
    #def __setitem__(self, ind, data):
    #self.first[ind] = data
    def __getitem__(self, ind):   # Compulsory
        return list(self)[ind]


class Person:                     # Compulsory to complete
    def __init__(self,name, pnr):
        self.name = name
        self.pnr = pnr
        
    def __str__(self):
        return f"{self.name}:{self.pnr}"
    
    def __lt__(self,other):
        self.name < other.name
    def __le__(self, other):
        self.name <= other.name
    def __gt__(self,other):
        self.name > other.name
    def __ge__(self, other):
        self.name >= other.name
def main():
    lars = Person('LARS',99)
    maja = Person('MAJA', 00)
    lst = LinkedList()
    #for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        #lst.insert(x)
    lst.insert(lars)
    lst.insert(maja)
    lst.print()
    #lst.remove(7)
    #print(lst.count(3))
    print(lst.to_list())
    lst.print()
    #lst.remove_all(3)
    lst.print()
    print(str(lst))
    #print(lst.merge(lst2))
    print(lst[0])
    #print(lst.length())
    #print(lst.mean())
    # Test code:
    
    


if __name__ == '__main__':
    main()
    


    

