import re

def reflist(fil):
    infil=open(fil, 'r')
    rad = infil.readline()
    rad = re.sub(r'#.*$', '', rad)
    i=1
    print(f'rad {i}:',rad)
    orden=[re.findall(r'[a-zA-ZåäöÅÄÖ]+',rad)]
    radnr=0
    

    while rad != '':
        i+=1
        rad = infil.readline()
        rad = re.sub(r'#.*$', '', rad)
        print(f'rad {i}:',rad)
        orden.append(re.findall(r'[a-zA-ZåäöÅÄÖ]+',rad))
# #         freq={}
# #         for e in orden[i]:
# #             if e in freq:
# #                 freq[e]+=1
# #             else:
# #                 freq[e]=1
#         
        
        
#     for e in range(len(orden)):
        s=1
    for o in orden:
        for q in range(len(o)):
            print(f' {s} , {o[q]}')
        s+=1
    
    infil.close()
    
reflist('uppg3_1.py')