import re

def part2(e):
    return e[1]

''' output: antal ord, antal olika ord. n vanligaste orden,m ovanligaste orden'''
def stat(filnamn):
    n=int(input('antal vanligaste ord: '))
    m=int(input('antal ovanligaste ord: '))
    utfil=open(filnamn,'r')
    Text=utfil.read()
    orden=re.findall(r'[a-zA-ZåäöÅÄÖ]+',Text)
    print('totalt antal ord',len(orden))
    
    '''skapar ett lexikon med frekvens kopplat till varje ord'''
    freq={}
    for e in orden:
        if e in freq:
            freq[e]+=1
        else:
            freq[e]=1
            
    lista=list(freq.items())
    print('antal olika ord',len(lista)) # Beräknar antal unika ord
    lista.sort()

    freq_order=sorted(lista, key=part2, reverse=True) # Sorterar lexikonet utifrån frekvens mha part2 funktionen
    for i, e in enumerate(freq_order, start=1):  # Skriver ut orden och dess frekvens
        print(f'{e[1]:<3} {e[0]}',end='\t')
        if i % 1 ==0:
            print()
    print()
    
    '''Skriver ut de vanligaste och ovanligaste orden utifrån ett valt n och m'''
    nord=[]
    mord=[]
    for i in range(0,n): 
        nord.append((freq_order[i][0], freq_order[i][1]))
    for i in range(len(freq_order)-m,len(freq_order)):
        mord.append((freq_order[i][0], freq_order[i][1]))
    
    print('vanligaste orden: ', nord)
    print('ovanligaste orden: ', mord)
    utfil.close()

'''input'''
stat('test.txt')