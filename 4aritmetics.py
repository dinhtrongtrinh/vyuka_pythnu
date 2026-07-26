# ==========================================
# 1. TAHÁK: ZÁKLADNÍ MATEMATIKA V PYTHONU
# ==========================================
# V Pythonu funguje matematika úplně stejně jako na kalkulačce.
# Zde jsou všechny tajné znaky (operátory), které budeš potřebovat:

#   +   Sčítání       (5 + 3 = 8)
#   -   Odčítání      (10 - 2 = 8)
#   * Násobení      (4 * 2 = 8)
#   /   Dělení        (16 / 2 = 8.0)  -> Výsledek je vždy desetinné číslo!
#   ** Mocnina       (2 ** 3 = 8)    -> Dvě na třetí (2 * 2 * 2)
#   %   Modulo        (17 % 5 = 2)    -> Zbytek po dělení (17 dětí, týmy po 5... zbydou 2 děti)

print("--- UKÁZKA Z BOJIŠTĚ ---")



zivoty = 100
poskozeni = 15
zbyvajici_zivoty = zivoty - poskozeni
#print(f"Hrdina dostal zásah! Zbývá mu {zbyvajici_zivoty} životů.")

zlataky = 5
nasobic_pokladu = 3
celkem_zlataku = zlataky * nasobic_pokladu
#print(f"Našel jsi truhlu s násobičem! Máš {celkem_zlataku} zlaťáků.")

#print("\n") # Odřádkování pro přehlednost


# ==========================================
# 2. TVŮJ ÚKOL: TÁBOROVÁ KALKULAČKA
# ==========================================
# Teď jsi na řadě ty! Odstraň křížky (#) u příkazů print a doplň správnou matematiku.

print("--- TVŮJ ÚKOL ---")

# ÚKOL A: ZKOUŠKA SÍLY (Sčítání a odčítání)
# Tvoje postava má sílu 10. Získala kouzelný meč, který přidává 5 síly, 
# ale pak na ni dopadla kletba, která jí 2 síly sebrala. 
# Jaká je její konečná síla? (Nahraď nulu správným výpočtem)

sila = 10
kozelny_mec = 5
kletba = 2
konecna_sila = sila + kozelny_mec - kletba 
# print(f"Úkol A: Tvoje konečná síla je {konecna_sila}.")


# ÚKOL B: ROZDĚLOVÁNÍ DO TÝMŮ (Dělení a Modulo)
# Na táboře je 26 dětí a chceme hrát volejbal. Potřebujeme týmy po 6 hráčích.
# 1. Zjisti, kolik vytvoříme celých týmů. (Použij dělení a funkci int() pro zaokrouhlení)
# 2. Zjisti, kolik dětí zbyde na střídačku. (Použij modulo %)

pocet_deti = 26
velikost_tymu = 6

# Nahraď nuly správnými výpočty pomocí proměnných pocet_deti a velikost_tymu!
cele_tymy = 0 
stridacka = 0

print(f"Úkol B: Vytvoříme {cele_tymy} týmů a na střídačce zbydou {stridacka} děti.")


# ÚKOL C: MAGICKÁ MOCNINA (Exponenciála)
# Kouzelník zdvojnásobí svou sílu každou sekundu. 
# Pokud začíná na síle 2, jakou sílu bude mít za 4 sekundy? (Spočítej 2 na čtvrtou)

magicka_sila = 0
# print(f"Úkol C: Kouzelníkova síla je {magicka_sila}!")