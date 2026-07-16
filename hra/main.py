import pygame

from hrac import Hrac

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((1400, 800))
pygame.display.set_caption("Hello Pygame")

# Game loop
hra1 = Hrac("Hráč1")  # Call the vykresleni method to draw the player

  # Create an instance of the Hrac class
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 2. Vyčištění obrazovky (např. černou barvou)
    # Bez tohoto kroku by se ti objekty "rozmazávaly" po obrazovce
    screen.fill((0, 0, 0)) 

    # 3. Vykreslení všech herních objektů
    hra1.vykresleni(screen)

    # 4. AKTUALIZACE OBRAZOVKY (to nejdůležitější, co ti chybělo!)
    pygame.display.flip()
# Quit Pygame
pygame.quit()