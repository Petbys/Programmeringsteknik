
import turtle
import random

def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

    
def make_turtle(x, y):
    t = turtle.Turtle()
    jump(t, x, y)
    t.color((random.random(),random.random(),random.random()))
    t.speed(0)
    t.width(10)
    t.shape('circle')
    t.shapesize(1)
     
    return t

def move_random(t):
    t.left(random.randint(-45,45))
    t.forward(random.randint(0,25))
    if abs(t.xcor()) > 250 or abs(t.ycor()) > 250: #byter riktning om den är vid kanten
        t.setheading(t.towards(0,0))
    
def rectangle(t, x, y, width, height, color):
    t = make_turtle(x, y)
    t.hideturtle()
    t.penup()
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()
    
rec = turtle.Turtle()
rectangle(rec,-250,-250,500,500,'light blue')

turtles = []

for t in range(0,2):
    turtles.append (make_turtle(random.randint(-250,250),random.randint(-250,250)))

n=0
for i in range(5000):
    for t in turtles:
        move_random(t)
        if turtles[0].distance(turtles[1].pos()) < 50:
            turtle[0].write('close')
            n+=1
print(f'Paddorna var nära varandra {n} gånger')    

