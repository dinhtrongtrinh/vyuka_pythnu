import turtle

# Nastavení okna a želvy
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.shape("turtle")
t.color("cyan")
t.pensize(3)
t.speed(2)

# Strana 1
t.forward(100)
t.left(90)

# Strana 2
t.forward(100)
t.left(90)

# Strana 3
t.forward(100)
t.left(90)

# Strana 4
t.forward(100)
t.left(90)

t.hideturtle()
turtle.done()