import matplotlib.pyplot as plt
import statistics

'''hjälpfunktion som gör om till float'''
def is_float(string):
    """ True om inpur är float annars False"""
    try:
        return float(string)
    except ValueError:
        return False


'''Öppna filen och lägg in data som listor'''
data=[]   
with open('uppsala_tm_1722-2019.dat', 'r') as f:
    d = f.readlines()
    for i in d:
        k = i.rstrip().split()
        data.append([float(i) if is_float(i) else i for i in k]) 


'''Lägg in i listor för maj varje år'''
year1700=[];year1800=[];year1900=[];year2000=[]
for r in data:
    if r[0]//100 == 17 and r[1]== 5 :
        year1700.append(r)
    if r[0]//100 == 18 and r[1]== 5 :
        year1800.append(r)
    if r[0]//100 == 19 and r[1]== 5 :
        year1900.append(r)
    if r[0]//100 == 20 and r[1]== 5 :
        year2000.append(r)
        
        
'''medeltemp för varje år'''

n=0
summa=[]
yearavg1=[]
for lines in year1700:
    if type(lines[3]) == float:
        summa.append(lines[3])
    n+=1
    if  n == 31:
        n=0
        yearavg1.append(statistics.mean(summa))
        summa=[]
n=0
summa=[]
yearavg2=[]
for lines in year1800:
    if type(lines[3]) == float:
        summa.append(lines[3])
    n+=1
    if  n == 31:
        n=0
        yearavg2.append(statistics.mean(summa))
        summa=[]
n=0
summa=[]
yearavg3=[]
for lines in year1900:
    if type(lines[3]) == float:
        summa.append(lines[3])
    n+=1
    if  n == 31:
        n=0
        yearavg3.append(statistics.mean(summa))
        summa=[]
n=0
summa=[]
yearavg4=[]
for lines in year2000:
    if type(lines[3]) == float:
        summa.append(lines[3])
    n+=1
    if  n == 31:
        n=0
        yearavg4.append(statistics.mean(summa))
        summa=[]

'''plotta'''

plt.boxplot([yearavg1,yearavg2,yearavg3,yearavg4])
plt.title('Medeltemperatur i Uppsala, 1722-2019')
plt.xticks([1, 2, 3,4], ['1722-1799', '1800-1899', '1900-1999', '2000-2019'])
plt.xlabel('''Bergström, H., Moberg, A
 Daily air temperature and pressure series for Uppsala (1722-1998), 
Climate Change, 53:213-252.''')
plt.ylabel('Temperatur')
plt.show()

