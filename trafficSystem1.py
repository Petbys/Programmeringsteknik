
import destinations
from trafficComponentsNew import Light, Lane, Vehicle
from time import sleep


class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self, length, period, green_period):
        self.time = 0
        self.lane1 = Lane(length)
        self.lane2 = Lane(length)
        
        self.light = Light(period, green_period)
        self.dest = destinations.Destinations() 
        self.queue = []

    def snapshot(self): #överblicksbild av systemet
        lista =[i.destination for i in self.queue]
        
        
        print(f'Time step {self.time} {self.lane1} {self.light} {self.lane2} {lista}')
        print()

    def step(self): #flyttar fordon
        self.time += 1
        self.lane1.remove_first()
        self.lane1.step()
        
        self.light.step()
        self.lane2.step()
        
        dest=self.dest.step()
        if dest != None:
            self.v =Vehicle(dest,self.time)
            self.queue.append(self.v)
            
            
        if self.lane2.last_free() and len(self.queue)>0:
            self.lane2.enter(self.queue.pop(0))
        
        if self.light.is_green():
            self.lane1.enter(self.lane2.remove_first())
        
    def in_system(self): # Returnerar antalet fordon
        pass  # do nothing

    def print_statistics(self):
        pass # do nothing


def main():
    ts = TrafficSystem(5,10,8)
    # 100 time steps
    for i in range(100):
        ts.snapshot()
        ts.step()
        sleep(0.1)  # sleep 0.1 second
    print('\nFinal state:')
    ts.snapshot()
    print()
    ts.print_statistics()


if __name__ == '__main__':
    main()


