import random

class Lotteri:
    
    def __init__(self, lotter, vinster):
        self.lottnr= [i for i in range(1,lotter+1)]
        self.vinster = vinster
        self.omgang = 1
        
    def __str__(self):
        return f'Följande lottnr är med i lotteriet: \n{self.lottnr} '
        
    def draLott(self):
        self.dragen = self.lottnr[random.randint(0,len(self.lottnr)-1)]
        self.lottnr.pop(self.dragen)
        self.omgang+=1
            
    def presenteraDragning(self):
        print (f'vinst {self.omgang} lottnr {self.dragen}')
        
        
def main():
    lotter = 20
    vinster = 5
    l = Lotteri(lotter,vinster)
    for _ in range(1,vinster):
        print(l)
        l.draLott()
        l.presenteraDragning()
if __name__ == '__main__':
    main()