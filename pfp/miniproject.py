import turtle

def draw():
    window = turtle.Screen()
    
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('blue')
    brad.speed(2)

    brad.right(90)
    brad.forward(200)


    window.exitonclick()

draw()
