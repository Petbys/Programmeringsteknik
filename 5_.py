# Skriv en funktion rectangle(x, y, width, height, color) som skapar en padda och målar en rektangel med angiven bredd, höjd och färg.
# Rektangelns nedre vänstra hörn ska vara i punkten (x, y). Du behöver göra import turtle i programmet för att kunna använda turtlar.

def rectangle(x, y, width, height, color):
    import turtle
    t=turtle.Turtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x, y+height)
    t.goto(x+width, y+height)
    t.goto(x+width, y)
    t.goto(x,y)
    t.end_fill()
    
rectangle(-50,-50,100,100,'blue')