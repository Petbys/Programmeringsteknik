import re
def matchvarde(a,b):
    mv=0
    for i in range(5):
        mv+=(a[i]-b[i])**2
    return mv
    
def part2(x):
    return x[1]

def matchmaking(individdata):
    infil = open(individdata, 'r')
    data= infil.read().splitlines()
    inddata= [i.replace('  ',',') for i in data]
    inddata= [re.sub(r'\t', ',',i) for i in inddata]
    alla =[]
    mmdata = {}
    for i in inddata:
        alla.append(i.split(','))
    for individ in alla:
        mmperson =individ[0]
        mmegenskap = [float(i)for i in individ[1:]]
        mmdata[mmperson]=mmegenskap
   
    
    ''' hitta matchningsvärde'''
    mvarden= []
    mvarden2 ={}
    
    
    for i in mmdata.values():
        mvarden.append([0 if i==k else matchvarde(i,k) for k in mmdata.values() ])
    j=0
    for i in mmdata:
        mvarden2[i]=mvarden[j]
        j+=1
    print(mvarden[1][2])
    matchvarden={}
    f=0; n=0
    for i in mvarden2:
        for k in mvarden2:
            if k!=i and mvarden[f][n]!=0:
                
                matchvarden[i,k]=mvarden[f][n]
            n+=1
        n=0; f+=1;
    
    resultat=sorted(matchvarden.items(),key=part2)
    
    for i in resultat:
        print(f'{i}')
    
matchmaking('individdata.txt')