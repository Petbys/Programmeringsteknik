
''' Hjälpfunktion, genererar en ny lista där fösta och sista elementen blir förlängda '''
def nylist(x, n):
    ny = [e for e in x]
    for i in range(n):
        ny.insert(0, x[0])
        ny.append(x[len(x)-1])
    return ny


'''Ersätter elementet med medelvärdet för elementets angränsadne element '''
def smooth_a(x,n):
    res = []
    y = nylist(x, n)                           # Ny förlängd lista
    for a in range(n, len(y)-n):               # Itererar så att första elementets medelvärde tas
        res.append(sum(y[a-n:a+1+n])/(2*n+1))
    return res


''' input '''
list= [2, 7, 6, 5, 4, 0]
print(smooth_a(list,))