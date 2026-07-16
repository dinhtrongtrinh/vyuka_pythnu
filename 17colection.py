# ==========================================
# 1. TAHÁK: LIST, TUPLE A SET (Kolekce věcí)
# ==========================================

# 1. LIST (Seznam) = Hranaté závorky []
# Je jako tvůj táborový batoh. Můžeš do něj přidávat věci, vyndávat je 
# a měnit jejich pořadí.
batoh = ["Míč", "Láhev","bomby" ,"boty"]
batoh.append("Píšťalka")  # Přidá další věc na konec

# 2. TUPLE (N-tice) = Kulaté závorky ()
# Je jako pravidla vytesaná do kamene. Co do něj dáš, to už NIKDY 
# nemůžeš změnit. Je super pro věci, co musí zůstat bezpečně stejné.
souradnice_tabora = (50.08, 14.42)
# souradnice_tabora[0] = 51.0  # TOHLE BY HODILO CHYBU!

# 3. SET (Množina) = Složené závorky {}
# Je jako kouzelný klobouk. Každá věc v něm může být jen JEDNOU! 
# Pokud do něj hodíš dvě stejné věci, ta druhá zmizí. (A nemá žádné pořadí).
barvy = {"červená", "modrá", "červená"} 
# V klobouku zbyde jen: {"červená", "modrá"}

print("--- UKÁZKA ---")
print(f"List (Batoh): {batoh}")
print(f"Tuple (Souřadnice): {souradnice_tabora}")
print(f"Set (Barvy): {barvy}\n")


# ==========================================
# 2. TVŮJ ÚKOL: STŘEDEČNÍ TURNAJ
# ==========================================
# Tábor je v polovině a dnes nás čeká velký sportovní turnaj! 
# Tvým úkolem je dát do pořádku soupisky, vybavení a hřiště.

print("=== PŘÍPRAVA TURNAJE ===")

# ÚKOL A: LIST (Seznam hráčů)
# Náš volejbalový tým potřebuje nutně ještě jednoho hráče.
# Pomocí metody .append() přidej do seznamu jméno "Karel".
tym_a = ["David", "Adam", "Jana"]

# DOPLŇ KÓD SEM:

# Odkomentuj pro kontrolu:
# print(f"Úkol A - Náš tým: {tym_a}")


# ÚKOL B: TUPLE (Rozměry hřiště)
# Hřiště na volejbal je přesně dané a nikdo ho nesmí zvětšovat. 
# Má délku 18 metrů a šířku 9 metrů.
# Vytvoř TUPLE (použij kulaté závorky), ulož do něj čísla 18 a 9 
# a přiřaď ho do proměnné 'rozmery_hriste'.

# DOPLŇ KÓD SEM:
rozmery_hriste = 

# Odkomentuj pro kontrolu:
# print(f"Úkol B - Rozměry hřiště jsou: {rozmery_hriste}")


# ÚKOL C: SET (Unikátní návštěvníci)
# K zápisu na turnaj se nám některé děti zapsaly omylem dvakrát!
# Převeď tento List (seznam) na Set (množinu) pomocí funkce set(), 
# abys automaticky odstranil všechny duplikáty.
zapsane_deti = ["Petr", "Eva", "Petr", "Lukas", "Eva", "Ondra"]

# DOPLŇ KÓD SEM:
skutecni_hraci = zapsane_deti

# Odkomentuj pro kontrolu:
# print(f"Úkol C - Skuteční hráči: {skutecni_hraci}")