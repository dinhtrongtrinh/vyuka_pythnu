import turtle
import random
import time 

# --- 1. NASTAVENÍ OBRAZOVKY ---
okno = turtle.Screen()
okno.title("⚡ CHYTNI ŽELVU! ⚡")
okno.bgcolor("black")
okno.setup(width=800, height=600)
okno.tracer(0)  # Vypne plynulé animace pro bleskový skok želv

# --- 2. PROMĚNNÉ HRAČE ---
skore = 0
rychlost_ms = 1000  # Želva skočí sama každých 1000 ms (1 vteřina)

# --- 3. TEXT SE SKÓRE ---
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 250)
text.write(f"SKÓRE: {skore}", align="center", font=("Arial", 24, "bold"))

# --- 4. ZELENÁ ŽELVA (HLAVNÍ TERČ) ---
terc = turtle.Turtle()
terc.shape("turtle")
terc.color("lime")
terc.shapesize(2.5)  # Zvětšení želvy, aby se na ni lépe trefovalo
terc.penup()

# --- 5. ČERVENÁ ŽELVA (PAST) ---
past = turtle.Turtle()
past.shape("turtle")
past.color("red")
past.shapesize(2)
past.penup()

# --- 6. FUNKCE PRO SKOK NA NÁHODNOU POZICI ---
def skok_zelv():
    # Náhodné souřadnice na obrazovce (mimo okraje)
    x_terc = random.randint(-350, 350)
    y_terc = random.randint(-200, 200)
    terc.goto(x_terc, y_terc)
    
    x_past = random.randint(-350, 350)
    y_past = random.randint(-200, 200)
    past.goto(x_past, y_past)

    okno.update()
    
    # Automatický skok za určitý čas, pokud hráč neklikne
    okno.ontimer(skok_zelv, rychlost_ms)

# --- 7. REAKCE NA KLIKNUTÍ ---
def klik_na_terc(x, y):
    global skore, rychlost_ms
    skore += 1
        
    aktualizuj_skore()
    skok_zelv()
    time.sleep(1)

def klik_na_past(x, y):
    global skore
    skore -= 2  # Stržení bodů za kliknutí na červenou
    aktualizuj_skore()
    skok_zelv()

def aktualizuj_skore():
    text.clear()
    text.write(f"SKÓRE: {skore}", align="center", font=("Arial", 24, "bold"))

# --- 8. PROPOJENÍ KLIKNUTÍ A SPUŠTĚNÍ HRY ---
terc.onclick(klik_na_terc)
past.onclick(klik_na_past)

# První skok a spuštění smyčky
skok_zelv()
okno.mainloop()