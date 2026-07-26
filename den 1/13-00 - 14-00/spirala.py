import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

barvy = ["red", "yellow", "cyan", "green", "orange", "magenta"]

# 70 kroků spirály
for i in range(100):
    t.color(barvy[i % 6])
    
    # Čára se s každým krokem prodlouží (0, 3, 6, 9, 12... pixelů)
    t.forward(i * 3)
    
    # Mírné odchýlení od 60 stupňů vytvoří zahnutou spirálu
    t.left(59)

t.hideturtle()
turtle.done()