import turtle
import random

# --- NASTAVENÍ PLÁTNA ---
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.title("ŠÍLENÝ 2D LABYRINT – NAJDI CESTU VEN")

# Vypneme animaci, algoritmus postaví labyrint bleskově
screen.tracer(0)

b = turtle.Turtle()
b.color("white")
b.pensize(2)
b.hideturtle()

def zed(x1, y1, x2, y2):
    """Pomocná funkce pro rychlé nakreslení čáry"""
    b.penup()
    b.goto(x1, y1)
    b.pendown()
    b.goto(x2, y2)

# --- PARAMETRY BLUDIŠTĚ ---
CELL_SIZE = 30
COLS = 32
ROWS = 24
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

startX = -WIDTH // 2  # -480
startY = HEIGHT // 2  # 360

# Pevný seed = pro všechny počítače se vygeneruje naprosto stejné bludiště
random.seed(42)

# Vytvoření mřížky pro algoritmus
grid = [[{'N': True, 'E': True, 'S': True, 'W': True, 'visited': False} for _ in range(COLS)] for _ in range(ROWS)]

# DFS algoritmus pro generování dokonalého bludiště (žádné cykly, jen 1 správná cesta)
stack = [(0, 0)]
grid[0][0]['visited'] = True

while stack:
    r, c = stack[-1]
    neighbors = []
    
    if r > 0 and not grid[r-1][c]['visited']: neighbors.append(('N', r-1, c))
    if r < ROWS-1 and not grid[r+1][c]['visited']: neighbors.append(('S', r+1, c))
    if c > 0 and not grid[r][c-1]['visited']: neighbors.append(('W', r, c-1))
    if c < COLS-1 and not grid[r][c+1]['visited']: neighbors.append(('E', r, c+1))
    
    if neighbors:
        direction, nr, nc = random.choice(neighbors)
        # Zboříme zeď mezi políčky
        grid[r][c][direction] = False
        opposite = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}[direction]
        grid[nr][nc][opposite] = False
        
        grid[nr][nc]['visited'] = True
        stack.append((nr, nc))
    else:
        stack.pop()

# --- VYKRESLENÍ BLUDIŠTĚ ---
# Horní a levá ohraničující zeď
zed(startX, startY, startX + WIDTH, startY)
zed(startX, startY, startX, startY - HEIGHT)

# Kreslení vnitřních, pravých a spodních zdí
for r in range(ROWS):
    for c in range(COLS):
        x = startX + c * CELL_SIZE
        y = startY - r * CELL_SIZE
        
        # Spodní zeď políčka
        if grid[r][c]['S']:
            # Pokud to není úplně poslední políčko (aby byl východ volný)
            if not (r == ROWS-1 and c == COLS-1):
                zed(x, y - CELL_SIZE, x + CELL_SIZE, y - CELL_SIZE)
                
        # Pravá zeď políčka
        if grid[r][c]['E']:
            zed(x + CELL_SIZE, y, x + CELL_SIZE, y - CELL_SIZE)

# --- ZELENÝ CÍL ---
# Cíl je vpravo dole
b.penup()
b.goto(startX + (COLS-1)*CELL_SIZE + 5, startY - (ROWS-1)*CELL_SIZE - 25)
b.color("lime")
b.begin_fill()
for _ in range(4):
    b.forward(20)
    b.left(90)
b.end_fill()

# Zapneme animace
screen.update()
screen.tracer(1)


# --- HRÁČSKÁ ŽELVA ---
player = turtle.Turtle()
player.shape("turtle")
player.color("gold")

# Želva musí být prťavá! (Chodby mají 30px, želva cca 14px)
player.shapesize(0.7) 
player.pensize(2)

# Nízká rychlost pro dramatičtější ladění chyb
player.speed(2)

# Startovní pozice: Přesný střed levého horního políčka
player.penup()
player.goto(startX + 15, startY - 15)
player.setheading(0) # Kouká doprava
player.pendown()


# =======================================================
# ⬇️ SEM PÍŠÍ DĚTI SVŮJ KÓD ⬇️
# =======================================================
# Nápověda: Pohybujte se vždy o násobky 30 (30, 60, 90...)
# a otáčejte se přesně o 90 stupňů!




turtle.done()