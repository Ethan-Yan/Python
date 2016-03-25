import turtle

def draw_rhombus(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(60)
        if i % 2 == 0:
            some_turtle.right(135)
        else:
            some_turtle.right(45)

def draw_flower():
    window = turtle.Screen
    # window.bgcolor()

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('red')
    brad.speed(4)
    for i in range(1, 37):
        draw_rhombus(brad)
        brad.right(10)
    brad.right(90)
    brad.forward(200)

    window.exitonclick()

draw_flower()
