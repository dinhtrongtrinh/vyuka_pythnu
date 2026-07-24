import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)
t.speed(2)

# --- 1. ZÁKLAD DOMEČKU (Modrý čtverec) ---
t.color("cyan")

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

# --- 2. STŘECHA (Červený trojúhelník) ---
# Dojedeme do levého horního rohu
t.forward(100)
t.left(90)
t.forward(100)

t.color("red")

# Otočení doprava na první šikmou stranu
t.left(30)
t.forward(100)

# Otočení dolů na druhou šikmou stranu
t.left(120)
t.forward(100)

t.hideturtle()
turtle.done()