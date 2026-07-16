import pygame 

class Hrac():
    def __init__(self, jmeno, sila=10, x_pozice=0, barva=(0, 255, 0)):
        self.jmeno = jmeno
        self.zivoty = 100
        self.sila = sila
        self.x_pozice = x_pozice
        
        # --- FYZIKA A POZICE ---
        self.vyska_zeme = 500              # Výška, na které hráč stojí
        self.y_pozice = self.vyska_zeme    # Výchozí pozice y
        self.barva = barva
        
        self.rychlost_y = 0                # Vertikální rychlost (pohyb nahoru/dolů)
        self.gravitace = 0.8               # Jak rychle padá k zemi
        self.sila_skoku = -16              # Síla výskoku (záporné číslo letí nahoru)
        self.je_na_zemi = True             # Pojistka proti skákání ve vzduchu

    def vykresleni(self, obrazovka):
        # Vykreslení hráče (obdélník o velikosti 100x300 px)
        pygame.draw.rect(obrazovka, self.barva, (self.x_pozice, self.y_pozice, 100, 300))
    
    def pohyb(self, smer):
        if smer == "doprava":
            # Trochu zrychlíme krok, ať se neplouží o 1 pixel
            self.x_pozice += 5  
        elif smer == "doleva":
            self.x_pozice -= 5
        elif smer == "skok":
            # Skočit můžeš, jen pokud stojíš pevně na zemi
            if self.je_na_zemi:
                self.rychlost_y = self.sila_skoku
                self.je_na_zemi = False

    def aktualizuj(self):
        """Tuto metodu budeš volat v každém snímku hry."""
        # Pokud nejsme na zemi, gravitace neustále táhne hráče dolů
        if not self.je_na_zemi:
            self.rychlost_y += self.gravitace

        # Posuneme pozici o aktuální rychlost
        self.y_pozice += self.rychlost_y

        # Kontrola, zda hráč nedopadl na zem
        if self.y_pozice >= self.vyska_zeme:
            self.y_pozice = self.vyska_zeme  # Zarovnáme ho přesně na zem
            self.rychlost_y = 0              # Zastavíme pád
            self.je_na_zemi = True           # Hráč je opět na zemi