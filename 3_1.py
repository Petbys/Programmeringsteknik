import turtle

# t=turtle.Turtle()
# t.shape('square')
# t.color('red', 'pink')
# t.begin_fill()
# for i in range(36):
#     t.forward(200)
#     t.left(170)
# t.end_fill()

# x=float(input('sidlängd?'))
# t=turtle.Turtle()
# t.color('red','pink')
# t.begin_fill()
# t.forward(x)
# t.left(120)
# t.forward(x)
# t.left(120)
# t.forward(x)
# t.left(120)

t=turtle.Turtle()
t.shape('square')
t.color('red', 'pink')
t.begin_fill()
x=30
n=10
while t.distance(0,0)<200:
    t.forward(n)
    t.left(x)
    x-=1/10
    n+=3
    d=turtle.distance(0,0)
    d
t.end_fill()
'''
import math
t=turtle.Turtle()
t.speed(10000)
for i in range (-360,361,10):
    x=i*math.pi/180
    y=math.sin(x)
    t.goto(50*x, 200*y)
t.home()
'''

'''
t=turtle.Turtle()
t.penup()
t.goto(-150,-100)
t.pendown()
t.begin_fill()
t.fillcolor('blue')
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()
t.left(90)

t.penup()
t.goto(-50,-100)
t.pendown()
t.begin_fill()
t.fillcolor('white')
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()
t.forward(200)
t.left(90)


t.penup()
t.goto(50,-100)
t.pendown()
t.begin_fill()
t.fillcolor('red')
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()
'''