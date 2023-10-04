import random
# Direction constants
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

    
class Snake:
    def __init__(self,sz,start):
        self.sz = sz
        self.snake = [start]
        self.direction = LEFT
        self.place_fruit()
        
        
    def xychar(self,pos):
        if pos == self.snake[-1]:
            return '#'

        elif pos == self.snake[:-1]:
            return 'O'
        elif pos == self.fruit_pos:
            return '@'
        else:
            return '.'
    
    def __str__(self):
        return '\n'.join([''.join([self.xychar((x,y))
                    for x in range (self.sz)])
                    for y in range(self.sz)])
    

        

    

    def place_fruit(self):
        while True:
            self.fruit_pos = (random.randint(0, self.sz-1),random.randint(0,self.sz-1))
            if self.fruit_pos not in self.snake:
                break
        
    def check_win(self):
        return len(self.snake) == self.sz**2
    
    
    
    def move(self, turn):
        self.direction = compute_turn(self.direction, turn)
        step = compute_step(self.direction)
        head = self.snake[-1]
        head = [head[0] + step[0], head[1] + step[1]]
        self.snake.append(head)
        if head == self.fruit_pos:
            self.place_fruit()
        else:
            self.snake.pop(0)
        if not 0<=head[0]<=self.sz:
            return False
        if not 0<=head[1]<=self.sz:
            return False
        if head in self.snake[:-1]:
            return False
        return True
    
        

d = {'L': 1, 'l': 1, 'F': 0, 'f': 0, 'R': -1, 'r': -1}

def compute_turn(direction, turn):
    assert(-1 <= turn <= 1)
    new_dir = direction + turn
    if new_dir == -1:
        new_dir = 3
    elif new_dir == 4:
        new_dir = 0
    return new_dir


def compute_step(dir):
    if dir == LEFT:
        return (-1, 0)
    elif dir == DOWN:
        return (0, 1)
    elif dir == RIGHT:
        return (1, 0)
    elif dir == UP:
        return (0, -1)
    else:
        raise ValueError(f'Illegal direction: {dir}')

def main():
   random.seed(0)
   s = Snake(5, (3, 3))
   while True:
       print(s)
       t = input('Move (L, F, R): ')
       if t in d:
           if s.move(d[t]) == False:
               print('Game Over!')
               break
           if s.check_win():
               print('You Win!')
               break
       else:
           print('Illegal move')
if __name__ == '__main__':
   main()

