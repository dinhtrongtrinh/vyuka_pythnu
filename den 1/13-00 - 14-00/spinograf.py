import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)  # Nejrychlejší kreslení
t.pensize(2)

barvy = ["red", "yellow", "cyan", "green", "orange", "magenta"]

# Vnější cyklus: Otoká kytičku dokola (36 * 10 = 360 stupňů)
for i in range(36):
    t.color(barvy[i % 6])  # Střídání barev
    
    # Vnitřní cyklus: Nakreslí 1 čtverec
    for j in range(4):
        t.forward(100)
        t.left(90)
    
    # Pootočení před dalším čtvercem
    t.left(10)

t.hideturtle()
turtle.done()