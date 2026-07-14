# ==========================================
# 1. TAHÁK: HACKOVÁNÍ TEXTU (String Indexing a Slicing)
# ==========================================
# Každé písmenko v textu má své tajné pořadové číslo, kterému říkáme INDEX.
# POZOR: Počítače začínají vždy počítat od NULY (0), ne od jedničky!
#

idk = "ahojJakseMas"
# Slovo:   T  A  B  O  R
# Indexy:  0  1  2  3  4
# 
# Můžeme počítat i odzadu pomocí mínusu:
# Poslední písmeno má index -1, předposlední -2 atd.

slovo = "VOLEJBAL"
print("--- UKÁZKA ---")
# Vytažení jednoho písmene pomocí hranatých závorek [ ]
print(f"První písmeno: {slovo[0]}")   # Vypíše 'V'
print(f"Poslední písmeno: {slovo[-3]}")  # Vypíše 'L'

# Krájení (Slicing) - vybírání kousku textu [od : do]
# Pozor: Písmeno na pozici 'do' už se nepočítá!
print(f"První 4 písmena: {slovo[1:6]}") # Vypíše 'VOLE' (indexy 0, 1, 2, 3)

# Super tajný trik: Obrácení textu naruby pomocí [::-1]
print(f"Slovo pozpátku: {slovo[::-1]}") # Vypíše 'LABLELOV'
print("\n")


# ==========================================
# 2. TVŮJ ÚKOL: LOVCI POKLADŮ A TAJNÉ ŠIFRY
# ==========================================
# Našli jsme starou mapu, ale text je zašifrovaný.
# Musíš použít hranaté závorky [] k odhalení zprávy!

mapa = "PZLATOK"

print("--- DEŠIFROVÁNÍ MAPY ---")

# ÚKOL A: PRVNÍ A POSLEDNÍ PÍSMENO
# Získej první písmeno (index 0) a poslední písmeno (index -1) z proměnné 'mapa'.
# DOPLŇ KÓD SEM:
prvni_pismeno = ""
posledni_pismeno = ""
# print(f"Úkol A: Začíná to na '{prvni_pismeno}' a končí na '{posledni_pismeno}'.")


# ÚKOL B: ODŘÍZNUTÍ KRAJŮ (Krájení)
# Skutečné místo pokladu je schované uvnitř slova 'mapa' ("PZLATOK").
# Odřízni první a poslední písmeno, abys získal slovo "ZLATO".
# (Nápověda: Začni na indexu 1 a skonči na indexu 6)
# DOPLŇ KÓD SEM:
skryty_poklad = ""
# print(f"Úkol B: Našli jsme poklad: {skryty_poklad}! 💰")


# ÚKOL C: ZRCADLOVÁ ZPRÁVA
# Duch lesa nám zanechal vzkaz, ale napsal ho pozpátku!
# Použij magický hackerský trik [::-1] k otočení textu, abychom si ho mohli přečíst.
zrcadlovy_vzkaz = "ROBÁT JELOV ENMIL"

# DOPLŇ KÓD SEM:
spravny_vzkaz = ""
# print(f"Úkol C: Duch říká: {spravny_vzkaz} 👻")