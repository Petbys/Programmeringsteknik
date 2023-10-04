
#Skriv en funktion mean(m) som beräknar och returnerar medelvärdet av talen i listan m! Vad händer om listan innehåller strängar?

list = [1 ,2, -3, -4, 4,-4, 4,4,1,1]
'''
def medellista (x):
    s= sum (x)
    m=s/len(x)
    return m
print(medellista(list))
'''
'''
#median

def median(x):
    l=sorted(x)
    i=int(len(l)/2)
    m=list[i]
    return m
print(median(list))
'''

#Givet en lista med tal. Skriv kod som konstruerar en ny lista utan de negativa talen.
'''
def noneg(x):
    l=[]
    for i in range(0,len(x)):
        if x[i] >= 0:
            l.append(x[i])
    return l
print(noneg(list))
        
        
'''
'''
#Skriv en funktionen between(lista, low, high) som skapar och returnerar en lista av de element i lista som ligger mellan low och high.

def between(lista, low, high):
    l=[]
    for i in lista:
        if low<i<high:
            l.append(i)
    return l
print(between(list, 0,3))
'''
'''
def smooth(x):
    res=[]
    res.append(x[0])
    for a in range(1,len(x)-1):
        res.append(sum(x[(a-1):(a+2)])/3)
    return res
print(smooth(list))
'''
'''
a = [[1, 1], [[1]], [1, 2], [1, 1]]
def counter2(x,lista):
    res=0
    for lst in lista:
        res+=lst.count(lista)
    return res
print(counter2(1,a))

'''
        
def counter(x,lista):
    res=0
    for lst in lista:
        if type(lst)==list:
            res +=lst.count(x)
        elif lst==x:
            res+= 1
    return res


        

