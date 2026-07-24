import turtle
import time

# --- NASTAVENÍ PLÁTNA A ŽELVY ---
screen = turtle.Screen()
screen.bgcolor("black")          # Černé pozadí dá barvám vyniknout
screen.title("Ukázka: Víceúhelníky, Spirograf a Mozaika")

t = turtle.Turtle()
t.speed(0)                       # Maximální rychlost kreslení
t.pensize(2)

# Seznam barev, které budeme střídat
barvy = ["red", "yellow", "cyan", "green", "orange", "magenta"]


# ==========================================
# 1. ČÁST: ROTUJÍCÍ VÍCEÚHELNÍK (Šestiúhelník)
# ==========================================
t.color("cyan")
t.penup()
t.goto(-250, 0)                  # Posuneme želvu vlevo
t.pendown()

# 6-úhelník (vnější úhel = 360 / 6 = 60°)
for i in range(6):
    t.forward(80)
    t.left(60)

time.sleep(1)                    # Krátká pauza, aby si děti prohlédly tvar


# ==========================================
# 2. ČÁST: SPIROGRAF / KYTIČKA Z ČTVERCŮ
# ==========================================
t.penup()
t.goto(0, 0)                     # Posuneme želvu do středu
t.pendown()

# Opakujeme 36krát: po každém čtverci se otočíme o 10 stupňů
for i in range(36):
    t.color(barvy[i % 6])        # Střídání barev ze seznamu
    
    # --- Vnitřní cyklus pro 1 čtverec ---
    for j in range(4):
        t.forward(70)
        t.left(90)
    
    t.left(10)                   # Pootočení celého čtverce

time.sleep(1)


# ==========================================
# 3. ČÁST: BAREVNÁ MOZAIKA / SPIRÁLA
# ==========================================
t.penup()
t.goto(250, -50)                 # Posuneme želvu vpravo
t.pendown()

# 60 kroků spirály - čára se postupně prodlužuje
for i in range(60):
    t.color(barvy[i % 6])
    t.forward(i * 3)             # Každý krok je o kousek delší
    t.left(59)                   # Úhel 59° vytvoří efektní zahnutou mozaiku


# --- SCHOVÁME ŽELVU A UDRŽÍME OKNO OTEVŘENÉ ---
t.hideturtle()
turtle.done()