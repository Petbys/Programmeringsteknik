import matplotlib.pyplot as plt



def nylist(x, n):
    ny = [e for e in x]
    for i in range(n):
        ny.insert(0, x[0])
        ny.append(x[len(x)-1])
    return ny


def smooth_a(x,n):
    res = []
    y = nylist(x, n)                           # Ny förlängd lista
    for a in range(n, len(y)-n):               # Itererar så att första elementets medelvärde tas
        res.append(sum(y[a-n:a+1+n])/(2*n+1))
    return res

def smooth_b (x,n):
    res = []
    for a in range(0,len(x)):
        if a-n<0:
            y = x[0:a+1+n]   # specialfall, då man vill börja från första elementet
        else:
            y = x[a-n:a+1+n] # lista med elementen som angränsar det specifika elementet
        res.append(sum(y)/len(y))
    return res

def load_csv(filename):
    
    import csv

    with open(filename, 'r') as csvFile:
        reader = csv.reader(csvFile)
        d={}
        for row in reader:
            landskod = str(row[1].lower())
            utslapp = [float(s) for s in row[3:]]
            d[landskod]= utslapp
    return d
data=load_csv('CO2Emissions_filtered.csv')


# Data for plotting

time = list(range(1960,2015))
y= [data['dnk'],data['fin'], data['isl'], data['nor'], data['swe']]

plt.plot(time,smooth_a(y[0],5),'b')
plt.plot(time,smooth_a(y[1],5),'r')
plt.plot(time, smooth_a(y[2],5),'g')
plt.plot(time, smooth_a(y[3],5),'c')
plt.plot(time, smooth_a(y[4],5),'m')

plt.plot(time, smooth_b(y[0],5),'b--')
plt.plot(time, smooth_b(y[1],5),'r--')
plt.plot(time,smooth_b(y[2],5),'g--')
plt.plot(time, smooth_b(y[3],5),'c--')
plt.plot(time, smooth_b(y[4],5),'m--')

plt.plot(time,  y[0],'b:',label='dnk')
plt.plot(time, y[1],'r:',label='fin')
plt.plot(time, y[2],'g:',label='isl')
plt.plot(time,y[3],'c:',label='nor')
plt.plot(time, y[4],'m:',label='swe')
plt.legend(loc='best')
plt.title('Yearly CO2 emissions in the nordic countries')
plt.ylabel('CO2 emissions (kt)')
plt.xlabel('year')

plt.show()
