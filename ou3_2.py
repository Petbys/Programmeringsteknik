import re
import keyword

''' hjälpfunktion '''
def part2(e):
    return len(e[1])


def reflist(fil):
    infil=open(fil, 'r')
    orgtext= infil.readlines()
    nytext=[]
    
    
    for i, e in enumerate(orgtext, start=1):
        print(f'{i}  {e}',end=' ')
        print()
    ''' tar bort kommenterarer, funktioner och annat som inte är ord'''
    for line in orgtext:
        line = re.sub(r'#.*$', '', line)
        line = re.findall(r'[a-zA-ZåäöÅÄÖ]+',line)
        nyrad = [e for e in line if keyword.iskeyword(e) !=True]
        

        nytext.append(nyrad)

    ''' skapar ett lexikon med radnummer och ord'''
    ordlista={}
    n=1
    for line in nytext:
        print('rad',n,end=' ')
        for e in line:
            print(e, end=' ')
            if e in ordlista:
                ordlista[e].append(n)
            else:
                ordlista[e]= [n]
        n+=1
        print()
    print()
    
    print('referenslista: ')
    lista = list(ordlista.items())
    
    ''' sorterar utifrån mest förekommande ord'''
    freq_order=sorted(lista, key=part2, reverse=True)
    for i, e in enumerate(freq_order, start=1):
        print(f'{e[0]:<13}  {e[1]}',end='\t')
        print()

    
    
''' input '''
reflist('counter.py')   