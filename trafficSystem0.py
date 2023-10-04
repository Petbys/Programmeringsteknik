
import destinations
from trafficComponentsNew import Light, Lane, Vehicle
from time import sleep


class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self):
        self.time = 0

    def snapshot(self):
        print(f'Time step {self.time}')

    def step(self):
        self.time += 1

    def in_system(self):
        pass  # do nothing

    def print_statistics(self):
        pass # do nothing


def main():
    ts = TrafficSystem()
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
