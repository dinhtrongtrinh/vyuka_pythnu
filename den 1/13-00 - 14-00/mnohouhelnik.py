import turtle

# Nastavení okna
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(3)
t.pensize(3)
t.color("cyan")

# Šestiúhelník: 6 stran, otočení o 60 stupňů
for i in range(6):
    t.forward(100)
    t.left(60)

t.hideturtle()
turtle.done()