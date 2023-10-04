import re

text = """Kvällens gullmoln fästet kransa.
Älvorna på ängen dansa,
och den bladbekrönta näcken
gigan rör i silverbäcken.
"""
'''
print(len([c for c in text if not c.isalpha() and ' '])) '''

def part2(e):
    return e[1]
'''
lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot']

lst.sort(key=part2)
print(lst)
'''
# utifrån variabeln lista göra en ny lista där man byter ordning på frekvens och bokstav och sedan sorterar

# lista=[('k', 5), ('v', 3), ('ä', 6), ('l', 8), ('e', 8), ('n', 13), ('s', 5), ('g', 4), ('u', 1), ('m', 1), ('o', 3), ('f', 1), ('t', 3), ('r', 6), ('a', 8), ('p', 1), ('å', 1), ('d', 3), ('c', 3), ('h', 1), ('b', 3), ('ö', 2), ('i', 3)]
# swapped=[]
# for i in lista:
#     swapped.append((i[0], i[1]))
# swapped.sort(reverse=False)
# print(swapped)
# alternativt

#swapped=sorted([(x[1],x[0]) for e in lista], reverse=True)

ord=text.split(' ')
print(ord)
               
wordlist= re.findall(r'[a-zA-ZåäöÅÄÖ]+', text)
print (wordlist)