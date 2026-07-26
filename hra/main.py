import pygame
from hrac import Hrac

# 1. Inicializace Pygame
pygame.init()

# Nastavení herního okna
screen = pygame.display.set_mode((1400, 800))
pygame.display.set_caption("Hello Pygame")

# Hodiny pro stabilní FPS (snímkovou frekvenci)
clock = pygame.time.Clock()

# Vytvoření instancí obou hráčů
# (jméno, síla, x_pozice, barva)
hra1 = Hrac("Hráč1", 10, 200, (0, 255, 0))   # Zelený hráč
hra2 = Hrac("Hráč2", 10, 1100, (255, 0, 0))  # Červený hráč

running = True
while running:
    # Omezení hry na stabilních 60 FPS (velmi důležité pro plynulou fyziku!)
    clock.tick(60)

    # --- INPUTY (UDÁLOSTI) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Jednorázové stisknutí kláves (vhodné pro skok)
        if event.type == pygame.KEYDOWN:
            # Hráč 1 (Ovládání šipkami)
            if event.key == pygame.K_UP:
                hra1.pohyb("skok")
            
            # Hráč 2 (Ovládání WASD - klávesa W pro skok)
            if event.key == pygame.K_w:
                hra2.pohyb("skok")

    # Kontrola držených kláves (pro plynulý pohyb do stran)
    keys = pygame.key.get_pressed()
    
    # Ovládání Hráče 1 (Šipky)
    if keys[pygame.K_RIGHT]:
        hra1.pohyb("doprava")
    if keys[pygame.K_LEFT]:
        hra1.pohyb("doleva")
    if keys[pygame.K_DOWN]:
        hra1.pohyb("utok", hra2)  # Hráč 1 útočí na Hráče 2
        
    # Ovládání Hráče 2 (Klávesy A a D)
    if keys[pygame.K_d]:
        hra2.pohyb("doprava")
    if keys[pygame.K_a]:
        hra2.pohyb("doleva")
    if keys[pygame.K_s]:
        hra2.pohyb("utok", hra1)  # Hráč 2 útočí na Hráče 1

    # --- FYZIKA A AKTUALIZACE ---
    hra1.aktualizuj()
    hra2.aktualizuj()

    # --- VYKRESLENÍ ---
    # 1. Vyčištění obrazovky (černá barva)
    screen.fill((0, 0, 0)) 

    # (Volitelné) Nakreslení podlahy, ať hráči nestojí ve vzduchoprázdnu
    # Spodní hrana hráčů s výškou 300px začíná na y = 500, takže podlaha je na y = 800
    pygame.draw.line(screen, (100, 100, 100), (0, 800), (1400, 800), 10)

    # 2. Vykreslení obou hráčů
    hra1.vykresleni(screen)
    hra2.vykresleni(screen)  # Teď se ti správně vykreslí i druhý hráč!

    # 3. Aktualizace monitoru
    pygame.display.flip()

# Ukončení hry
pygame.quit()