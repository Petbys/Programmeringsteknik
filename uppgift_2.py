import turtle

def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
def make_turtle(x, y):
    t = turtle.Turtle()
    jump(t, x, y)
    return t


def rectangle(x, y, width, height, color):
    t = make_turtle(x, y)
    t.hideturtle()
    t.penup()
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()

def redrectangle(x, y, h):
    w = 3/2*h
    rectangle(x, y, w, h, 'red')
    
def pentagram(x, y, side):
    t = make_turtle(x, y)
    t.penup()
    t.hideturtle()
    t.fillcolor('yellow')
    t.begin_fill()
    t.setheading(270-36/2)
    for i in range(5):
        t.forward(side/3)
        t.right(72)
        t.forward(side/3)
        t.left(180-36)
    t.end_fill()

def vietnamese_flag(x,y,h):       
    redrectangle(x,y,h)
    pentagram(x+h*3/4, y+h/1.6,h/4)
    
vietnamese_flag(-300,-300,400)