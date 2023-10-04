
'''Ersätter elementet med medelvärdet för elementets angränsadne element '''

def smooth_b (x,n):
    res = []
    for a in range(0,len(x)):
        if a-n<0:
            y = x[0:a+1+n]   # specialfall, då man vill börja från första elementet
        else:
            y = x[a-n:a+1+n] # lista med elementen som angränsar det specifika elementet
        res.append(sum(y)/len(y))
    return res

list = [2, 7, 6, 5, 4, 0]

print(smooth_b(list,20))