# ==========================================
# 1. TAHÁK: ROZHODOVÁNÍ (IF, ELIF, ELSE)
# ==========================================
# V programu se často musíme rozhodovat. 
# 'if' funguje jako křižovatka: KDYŽ platí nějaká podmínka, udělej tohle. 
# ELIF (else if) znamená: JINAK KDYŽ platí něco jiného, udělej toto.
# ELSE znamená: JINAK (když neplatí vůbec nic), udělej tohle jako záchranu.

# Značky pro porovnávání (na tohle bacha!):
# ==  Rovná se (pozor, jsou to DVE rovnítka! Jedno rovnítko dává věci do krabice)
# !=  Nerovná se
# >   Větší než
# <   Menší než
# >=  Větší nebo rovno
# <=  Menší nebo rovno

print("--- UKÁZKA: HLÍDAČ U TÁBORÁKU ---")
heslo = "rohlik"

# Všimni si dvojtečky na konci a mezery (odsazení) na dalším řádku!
if heslo == "buřt":
    print("Správné heslo, můžeš k ohni!")
elif heslo == "párek":
    print("Skoro... ale dneska pečeme něco jiného.")
else:
    print("Špatné heslo, k ohni nesmíš!")

print("\n") # Jen prázdný řádek pro pořádek


# ==========================================
# 2. TVŮJ ÚKOL: ROZHODČÍ VOLEJBALOVÉHO ZÁPASU
# ==========================================
# Tvým úkolem je naprogramovat automatického rozhodčího, 
# který podle skóre určí, kdo vyhrál táborový zápas ve volejbale!

nase_body = 25
body_soupere = 18

print("--- VÝSLEDEK ZÁPASU ---")


# ÚKOL: Napiš podmínky (if, elif, else), které porovnají 'nase_body' a 'body_soupere'.
# Nezapomeň na dvojtečku [:] na konci podmínky a odsazení na dalším řádku!

# 1. KROK: Napiš 'if' podmínku pro případ, že nase_body jsou VĚTŠÍ než body_soupere.
# DOPLŇ KÓD SEM:
# if ...
    # print("Vyhráli jsme! Zlato je naše! 🥇")

# 2. KROK: Napiš 'elif' podmínku pro případ, že se body ROVNAJÍ (==).
# DOPLŇ KÓD SEM:
# elif ...
    # print("Je to remíza! Bude se hrát tie-break. 🏐")

# 3. KROK: Napiš 'else' pro všechny ostatní případy (když soupeř vyhrál).
# (U 'else' už se žádná podmínka nepíše, jen dvojtečka!)
# DOPLŇ KÓD SEM:
# else:
    # print("Soupeř vyhrál, příště jim to natřeme! 🥈")