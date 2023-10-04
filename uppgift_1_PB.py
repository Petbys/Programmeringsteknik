import turtle


def uppg_1(x,y,side, h):
 
  
    
    def jump(t, x, y):
        '''förflyttar paddan till position (x,y)'''
        t.penup()
        t.goto(x, y)
        t.pendown()
        
    def make_turtle(x, y):
       t = turtle.Turtle()
       t.speed(0)
       jump(t, x, y)
       return t
    
    def rectangle(x, y, width, height, color):
        t = make_turtle(x, y)
        t.hideturtle()
        t.fillcolor(color)
        t.begin_fill()
        for dist in [width, height, width, height]:
            t.forward(dist)
            t.left(90)
        t.end_fill()
    
    
    
    def pentagram(x, y, side, color):
        t = make_turtle(x, y)
        t.hideturtle()
        t.fillcolor(color)
        t.begin_fill()
        t.setheading(270 - 36/2)
        for i in range(5):
            t.forward(side/3)
            t.right(72)
            t.forward(side/3)
            t.left(180-36)
        t.end_fill()
       
        
    def tricolore(x, y, h):
        w = h/2  	#färgfältens bredd
        rectangle(x, y, w, h, 'blue')
        rectangle(x+w, y, w, h, 'white')
        rectangle(x+2*w, y, w, h, 'red')

   
    for i in range(5):
        pentagram(i*h/2-h, -(h/2+h/4), h/2, 'yellow')
        pentagram(i*h/2-h,h+h/4,h/2, 'yellow')

    tricolore(h/4-h, -h/2, h)
uppg_1(-100,-100, 100, 200)