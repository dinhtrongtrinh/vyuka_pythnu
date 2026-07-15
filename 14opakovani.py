# ==========================================
# 📻 HACKEŘI VE DVOJICI: TÁBOROVÝ ROZHLAS (ŘEŠENÍ) 📻
# ==========================================

print("=== PŘIPOJOVÁNÍ K ROZHLASU ===")

tajny_kod = "Zprava_pro_vedouci"
print(tajny_kod[11:18])
pocet_pokusu = 3

# OPRAVA 6: Založení proměnných před začátkem smyčky
okruh_1_hotovo = False
okruh_2_hotovo = False

# OPRAVA 1: Přidána chybějící dvojtečka na konec řádku
while pocet_pokusu > 0:
    print(f"\nZbývají pokusy: {pocet_pokusu}")
    
    # --- HACKER 1: Ladění frekvence (Matematika) ---
    print("[HACKER 1] Zadej frekvenci rádia.")
    
    # OPRAVA 2: Přidána funkce int() pro převod textu na číslo
    frekvence = int(input("Zadej výsledek (25 % 7): "))
    
    # OPRAVA 3: Použita dvě rovnítka (==) pro porovnání
    if frekvence == 4:
        okruh_1_hotovo = True
        print("✅ Frekvence naladěna!")
    else:
        print("❌ Šum a praskání...")
        pocet_pokusu = pocet_pokusu - 1
        
    # --- HACKER 2: Úprava kódu (Text a metody) ---
    print("\n[HACKER 2] Získej heslo z tajného kódu.")
    
    # OPRAVA 4: Změna horní hranice indexu na 18
    vyriznute_slovo = tajny_kod[11:18]
    
    # OPRAVA 5: Metoda přepsána na malá písmena (.upper())
    heslo_k_rozhlasu = vyriznute_slovo.upper()
    
    tip = input("Zadej dešifrované heslo: ")
    
    if tip == heslo_k_rozhlasu:
        okruh_2_hotovo = True
        print("✅ Heslo přijato!")
    else:
        print("❌ Špatné heslo!")
        pocet_pokusu = pocet_pokusu - 1
        
    # --- KONTROLA HACKU ---
    if okruh_1_hotovo and okruh_2_hotovo:
        print("🎉 ROZHLAS HACKNUT! Můžeme hrát! 🎵")
        break 

# Závěrečný odpočet do vysílání
if okruh_1_hotovo and okruh_2_hotovo:
    print("\nStart vysílání za:")
    
    # OPRAVA 7: Přidána funkce range(), protože samotné číslo nelze iterovat
    for vterina in range(5):
        print(f"{vterina}...")