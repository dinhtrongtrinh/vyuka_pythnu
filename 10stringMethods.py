# ==========================================
# 1. TAHÁK: KOUZLA S TEXTEM (String Methods)
# ==========================================
# Texty (Stringy) v Pythonu mají tajné superschopnosti (metody).
# Stačí za proměnnou napsat tečku a vybrat si kouzlo!

zprava = "  Tajna Zprava 123  "

# len()      -> Zjistí délku textu (kolik má znaků, včetně mezer).
# .upper()   -> ZMĚNÍ VŠE NA VELKÁ PÍSMENA (jako když křičíš).
# .lower()   -> změní vše na malá písmena (jako když šeptáš).
# .count()   -> Spočítá, kolikrát se nějaké písmeno nebo slovo v textu nachází.
# .replace() -> Nahradí část textu něčím jiným.

print("--- UKÁZKA: ÚPRAVA TEXTU ---")
hrac = "super_hrac_cz"

print(f"Původní jméno: {hrac}")
print(f"Velkými písmeny: {hrac.upper()}")
print(f"Délka jména: {len(hrac)} znaků")
print(f"Kolikrát je tam 'r': {hrac.count('r')}")

# Vyměníme podtržítka za mezery
opravene_jmeno = hrac.replace("_", " ")
print(f"Opravené jméno: {opravene_jmeno}")

print("\n")


# ==========================================
# 2. TVŮJ ÚKOL: ÚPRAVA PROFILU A DEŠIFROVÁNÍ
# ==========================================

print("--- TVŮJ ÚKOL ---")

# ÚKOL A: KŘIČÍCÍ KAPITÁN
# Náš kapitán má moc tichý hlas. Změň jeho jméno tak, 
# aby bylo VŠECHNO VELKÝMI PÍSMENY!
kapitan = "tichy_bob"

# DOPLŇ KÓD SEM (použij správnou metodu za proměnnou kapitan):
kricici_kapitan = kapitan
# print(f"Úkol A: Náš kapitán se jmenuje {kricici_kapitan}!")


# ÚKOL B: DÉLKA HESLA
# Zjisti, kolik znaků má toto tajné heslo. 
# (Použij funkci len() a dej do ní proměnnou heslo)
heslo = "Pudinkovy_Dort_Je_Nejlepsi"

# DOPLŇ KÓD SEM:
delka_hesla = 0
# print(f"Úkol B: Heslo má přesně {delka_hesla} znaků.")


# ÚKOL C: OPRAVA HACKNUTÉ ZPRÁVY
# Zlý hacker nám do zprávy propašoval samé nuly! 
# Tvým úkolem je nuly vymazat. 
# (Použij .replace() a nahraď "0" za úplně prázdný text "")
hacknuta_zprava = "T0a0b0o0r0 0j0e0 0s0u0p0e0r0!"

# DOPLŇ KÓD SEM:
cista_zprava = hacknuta_zprava
# print(f"Úkol C: Očištěná zpráva zní: {cista_zprava}")