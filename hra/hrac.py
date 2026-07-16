import pygame 

class Hrac():
    def __init__(self, jmeno ,sila=10):
        self.jmeno = jmeno
        self.zivoty = 100
        self.sila = sila

    def vykresleni(self, obrazovka):
        # Vykreslení hráče na obrazov
        pygame.draw.rect(obrazovka, (0, 255, 0), (100, 100, 50, 50))  # Zelený čtverec jako hráč

