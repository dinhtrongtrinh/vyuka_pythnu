import pygame 

class Hrac():
    def __init__(self, jmeno ,sila=10, x_pozice=0):
        self.jmeno = jmeno
        self.zivoty = 100
        self.sila = sila
        self.x_pozice = x_pozice

    def vykresleni(self, obrazovka):
        # Vykreslení hráče na obrazov             
        pygame.draw.rect(obrazovka, (0, 255, 0), (self.x_pozice, 500, 100, 300))  # Zelený čtverec jako hráč
        #pozice (x,y,width,height)
