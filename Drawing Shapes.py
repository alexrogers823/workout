#Drawing a square
import turtle

def draw():
    window = turtle.Screen()
    window.bgcolor('black')
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('red')
    brad.speed(1)
    for i in range(6):
        brad.forward(100)
        brad.right(60)

    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    angie.circle(100)

    taylor = turtle.Turtle()
    taylor.shape('turtle')
    taylor.color('green')
    taylor.speed(1)
    for i in range(4):
        taylor.left(90)
        taylor.forward(100)

    window.exitonclick()

def squares_and_diamonds():
    x = 450
    y = (x/2)**2
    c = x**2
    window = turtle.Screen()
    window.bgcolor('black')
    d = turtle.Turtle()
    d.shape('arrow')
 #   d.color('red')
    d.penup()
    d.setpos(-250,250)
    d.pendown()
    for s in range(6):
        for i in range(4):
            d.color('red')
            d.forward(x)
            d.right(90)
        d.penup()
        d.left(45)
        d.forward((c+c)**(1/2)/4)
        d.right(45)
        d.forward((((((c+c)**(1/2)/4)**2)+(((c+c)**(1/2)/4)**2))**(1/2))/2)
        d.pendown()
        d.right(45)
        for i in range(4):
            d.color('blue')
            d.forward(x+(((((c+c)**(1/2)/4)**2)+(((c+c)**(1/2)/4)**2))**(1/2))/8)
            d.right(90)
        d.penup()
        d.right(45)
        d.forward(x/4)
        d.left(45)
        d.pendown()
        x = (y+y)**(1/2)
        y = (x/2)**2
        c = x**2
        
        

#Advanced code from class
def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('black')
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('gold')
    for i in range(36):
        draw_square(brad)
        brad.right(10)

#Main
squares_and_diamonds()
