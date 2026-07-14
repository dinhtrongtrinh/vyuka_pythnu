# ==========================================
# 1. TAHÁK: ZKRÁCENÝ IF (Conditional Expression)
# ==========================================
# Někdy je zbytečné psát dlouhý 'if' a 'else' na 4 řádky,
# když to jde napsat chytře na jeden jediný řádek!
#
# Vzoreček:
# VYSLEDEK = (HODNOTA KDYŽ ANO) if (PODMÍNKA) else (HODNOTA KDYŽ NE)

print("--- UKÁZKA: STAV HRÁČE VE HŘE ---")
zivoty = 0

# Dlouhý zápis (takhle jsme to dělali doteď):
# if zivoty > 0:
#     stav = "Živý"
# else:
#     stav = "Vyřazený"

# Zkrácený zápis (Conditional expression):
stav = "Živý" if zivoty > 0 else "Vyřazený"

print(f"Hráč je momentálně: {stav}")
print("\n")


# ==========================================
# 2. TVŮJ ÚKOL: SOUTĚŽ V RUBIKOVĚ KOSTCE
# ==========================================
# Jsi rozhodčí na táborové soutěži ve skládání Rubikovy kostky.
# Tvým úkolem je rozdat hráčům hodnocení a medaile jen pomocí JEDNOHO řádku!

cas_skladani = 25  # Čas v sekundách

print("--- VÝSLEDEK ZÁVODU ---")

# ÚKOL A: HODNOCENÍ RYCHLOSTI
# Pokud je 'cas_skladani' menší nebo roven 30, hráč získá hodnocení "Mistr kostky! 🧊".
# Pokud je čas horší (větší než 30), získá hodnocení "Dobrý pokus! 👍".
# Vše musíš napsat do jednoho řádku!

# DOPLŇ KÓD SEM (přepiš prázdné uvozovky na zkrácený IF):
hodnoceni = "" 
# print(f"Výsledek hráče: {hodnoceni}")


# ÚKOL B: VIP VSTUPENKA
# Chceme zjistit, jestli hráč dostane VIP vstupenku na další turnaj.
# Výsledkem musí být True (Pravda) nebo False (Nepravda).
# Hráč dostane True, pokud složil kostku pod 20 sekund (cas_skladani < 20).
# Jinak dostane False.

# DOPLŇ KÓD SEM (přepiš False na zkrácený IF):
vip_vstupenka = False 
# print(f"Získal hráč VIP vstupenku? {vip_vstupenka}")