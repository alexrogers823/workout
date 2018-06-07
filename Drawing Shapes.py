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

def squares_and_diamonds(): #Will draw cool pattern using Pythagorean theorem
    x = 450
    y = (x/2)**2
    c = x**2
    window = turtle.Screen()
    window.bgcolor('black')
    shape = turtle.Turtle()
    shape.shape('arrow')
 #   shape.color('red')
    shape.penup()
    shape.setpos(-250,250)
    shape.pendown()
    for s in range(6):
        for i in range(4):
            shape.color('red')
            shape.forward(x)
            shape.right(90)
        shape.penup()
        shape.left(45)
        shape.forward((c+c)**(1/2)/4)
        shape.right(45)
        shape.forward((((((c+c)**(1/2)/4)**2)+(((c+c)**(1/2)/4)**2))**(1/2))/2)
        shape.pendown()
        shape.right(45)
        for i in range(4):
            shape.color('blue')
            shape.forward(x+(((((c+c)**(1/2)/4)**2)+(((c+c)**(1/2)/4)**2))**(1/2))/8)
            shape.right(90)
        shape.penup()
        shape.right(45)
        shape.forward(x/4)
        shape.left(45)
        shape.pendown()
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
