import turtle

class rektangel:
    
    
    def __init__(self,b,h,x,y):
        self.height = h
        self.base = b
        self.x = x
        self.y = y
        
    
    def __str__(self):
        return f'Rectangle({self.baase}, {self.heigt}, '+ \
            f'{self.x}, {self.y})'

    def area(self):
        return self.height*self.base
    
    def draw(self):
        t = turtle.Turtle()
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.left(90)
        t.forward(self.height)
        t.right(90)
        t.forward(self.base)
        t.right(90)
        t.forward(self.height)
        t.right(90)
        t.forward(self.base)
        
rek1=rektangel(300,200,-50,-50)
    
print(rek1.area())
rek1.draw()