import turtle
import random

# 1. Nastavení plochy
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("CHYTNI ŽELVU!")

# 2. Proměnné pro skóre
skore = 0

# 3. Vytvoření cílové želvy
terc = turtle.Turtle()
terc.shape("turtle")
terc.color("lime")
terc.shapesize(2)
terc.penup()

# 4. Vytvoření počítadla skóre
psaci_zelva = turtle.Turtle()
psaci_zelva.hideturtle()
psaci_zelva.color("white")
psaci_zelva.penup()
psaci_zelva.goto(0, 260)
psaci_zelva.write(f"Skóre: {skore}", align="center", font=("Arial", 24, "bold"))

# 5. Funkce, která se spustí při kliknutí na želvu
def kliknuti(x, y):
    global skore
    skore = skore + 1
    
    # Aktualizace textu se skóre
    psaci_zelva.clear()
    psaci_zelva.write(f"Skóre: {skore}", align="center", font=("Arial", 24, "bold"))
    
    # Skok na novou náhodnou pozici
    nove_x = random.randint(-350, 350)
    nove_y = random.randint(-250, 250)
    terc.goto(nove_x, nove_y)

# Místo složitého posluchače předáme funkci přímo události kliknutí!
terc.onclick(kliknuti)

turtle.done()