
import destinations
from trafficComponentsNew import Light, Lane, Vehicle
from time import sleep
import statistics
#jinci har rättat

class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self, lane_length,lanews_length, lightperiod, green_west, green_south):
        self.time = 0
        self.lane = Lane(lane_length)
        self.laneW = Lane(lanews_length)
        self.laneS = Lane(lanews_length)
        self.lightW = Light(lightperiod,green_west)
        self.lightS = Light(lightperiod,green_south)
        self.dest = destinations.Destinations()
        self.queue = []
        self.passeraS = []
        self.passeraW =[]
        self.block = ' '
        self.nblock = 0
        self.nbil = 0
        self.tidS = []
        self.tidW = []
        self.vehicles = 0
        self.queuetid = 0
        
    def snapshot(self):
        lista1 =[i.destination for i in self.queue]
        
        print(f' {self.lightW} {self.laneW}{self.block}{self.lane}')
        print(f' {self.lightS} {self.laneS} ')
        print()

    def step(self):
        ''' Passera trafikljusen när de är gröna'''
        if self.laneW.get_first() != None:    
            if self.lightW.is_green():
                self.bilpas = self.laneW.remove_first()
                self.passeraW.append([self.bilpas])
                self.tidW.append(self.time-self.bilpas.get_borntime())
        self.laneW.step()
        self.lightW.step()
        if self.laneS.get_first() != None:        
            if self.lightS.is_green():
                self.bilpas = self.laneS.remove_first()
                self.passeraS.append([self.bilpas])
                self.tidS.append(self.time-self.bilpas.get_borntime())    
        self.laneS.step()
        self.lightS.step()
        
        ''' placerar första bilen från filen till west eller south beroende på dess riktning''' 
        self.bil= self.lane.get_first()
        if self.bil != None and self.bil.get_destination() == 'W' :
            if self.laneW.last_free():
                self.bil = self.lane.remove_first()
                self.laneW.enter(self.bil)
                self.block=' '
            else:
                self.block='X'
                self.nblock +=1
        if self.bil != None and self.bil.get_destination() == 'S' :
            if self.laneS.last_free():
                self.bil = self.lane.remove_first()
                self.laneS.enter(self.bil)
                self.block=' '
            else:
                self.block = 'X'
                self.nblock+=1
        self.lane.step()
        
        ''' Placerar en ny bil i kön och sedan längst bak i filen'''
        dest = self.dest.step()
        if dest != None:
            self.v =Vehicle(dest,self.time)
            self.queue.append(self.v)
            self.vehicles+=1
        if self.lane.last_free() and len(self.queue)>0:
            self.lane.enter(self.queue.pop(0))
        '''räknar kö och tid'''
        if len(self.queue)>0:
            self.queuetid +=1
        self.time += 1

        
    def in_system(self):
        pass  # do nothing

    def print_statistics(self):
        print (f' Statistics after 100 timesteps:')
        
        blocked = self.nblock
        
        
        meanW = statistics.mean(self.tidW)
        meanS = statistics.mean(self.tidS)
        medianW =statistics.median(self.tidW)
        medianS =statistics.median(self.tidS)
        maxW= max(self.tidW)
        maxS= max(self.tidS)
        minW= min(self.tidW)
        minS= min(self.tidS)
        insystem = self.laneW.number_in_lane() + self.laneS.number_in_lane()+ self.lane.number_in_lane()
        print(f' Created veichles: {self.vehicles}')
        print(f' In system       : {insystem}')
        print()
        print(f' at exit       West   South ')
        print()
        print(f' Vehicles out: {len(self.passeraW)}   {len(self.passeraS)} ')
        print(f' Min         : {minW}   {minS} ')
        print(f' Max         : {maxW}   {maxS} ')
        print(f' Mean        : {round(meanW,1)} {round(meanS,1)} ')
        print(f' Median      : {medianW}   {medianS} ')
        
        print(f' Blocked     : {blocked}%')
        print(f' Queue       : {self.queuetid}%')
        
        
        
        pass # do nothing


def main():
    ts = TrafficSystem(11,8,14,6,4)
    # 100 time steps
    for i in range(100):
        ts.snapshot()
        ts.step()
        sleep(0.7)  # sleep 0.1 second
    print('\nFinal state:')
    ts.snapshot()
    print()
    ts.print_statistics()


if __name__ == '__main__':
    main()
