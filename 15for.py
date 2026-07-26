# ==========================================
# 1. TAHÁK: CYKLUS FOR (Opakování a skenování)
# ==========================================
# 'for' smyčka slouží k tomu, abychom něco zopakovali X-krát,
# nebo abychom prošli nějaký text písmenko po písmenu.

print("--- A) OPAKOVÁNÍ PODLE ČÍSLA (Funkce range) ---")

for cislo in range(3,86):
    print(f"Dělám klik číslo {cislo}")

print("\n--- B) OPAKOVÁNÍ V ROZMEZÍ (Od - Do) ---")

for krok in range(2, 5):
    print(f"Běžím na metu {krok}")

print("\n--- C) PROCHÁZENÍ TEXTU (Písmenko po písmenu) ---")
tajny_kod = "sedesatsedm"

for pismeno in tajny_kod:
    print(f"Skenuji znak: {pismeno}")

print("\n")


# ==========================================
# 2. HACKEŘI VE DVOJICI: KONTROLA RADARU
# ==========================================
# Náš bezpečnostní radar se zbláznil a kód nefunguje.
# Máte za úkol najít 4 chyby a kód opravit!
# Cílem je odpočítat start radaru a pak najít ve zprávě vetřelce "X".

print("=== START RADARU ===")

# --- HACKER 1: Odpočet ---
print("[HACKER 1] Oprav odpočítávání radaru!")
# Úkol: Chceme, aby radar odpočítal 5 sekund (od 0 do 4).
# POZOR: Číslo 5 nelze "procházet". Musíš použít magickou funkci range()!

for sekunda in 5:
    print(f"Nabíjení radaru: {sekunda}...")

print("Radar je zapnutý!\n")


# --- HACKER 2: Hledání vetřelce ---
print("[HACKER 2] Najdi vetřelce na radaru!")
zaznam_radaru = "----X--"

# Úkol: Smyčka musí projít záznam znak po znaku. Pokud narazí na "X",
# vypíše varování a smyčku předčasně ukončí příkazem 'break'.
# Najdi chyby v syntaxi a odsazení!

for znak in zaznam_radaru
print(f"Koukám na: {znak}")
    if znak = "X":
        print("POZOR! Nalezen vetřelec!")
        break