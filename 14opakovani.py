# ==========================================
# 📻 HACKEŘI VE DVOJICI: TÁBOROVÝ ROZHLAS 📻
# ==========================================
# Hlavní vedoucí zamkl táborový rozhlas! Abychom do něj mohli pustit 
# vlastní písničky, musíme prolomit dva bezpečnostní systémy.
# Kód obsahuje 7 chyb. Pozorně čtěte červené chybové hlášky!

print("=== PŘIPOJOVÁNÍ K ROZHLASU ===")

tajny_kod = "Zprava_pro_vedouci"
pocet_pokusu = 3

while pocet_pokusu > 0
    print(f"\nZbývají pokusy: {pocet_pokusu}")
    
    # --- HACKER 1: Ladění frekvence (Matematika) ---
    print("[HACKER 1] Zadej frekvenci rádia.")
    # Frekvence musí být zbytek po dělení 25 % 7. Počítač čeká číslo 4.
    frekvence = input("Zadej výsledek (25 % 7): ")
    
    if frekvence = 4:
        okruh_1_hotovo = True
        print("✅ Frekvence naladěna!")
    else:
        print("❌ Šum a praskání...")
        pocet_pokusu = pocet_pokusu - 1
        
    # --- HACKER 2: Úprava kódu (Text a metody) ---
    print("\n[HACKER 2] Získej heslo z tajného kódu.")
    # Úkol: Z proměnné 'tajny_kod' vyřízni pouze slovo 'vedouci' 
    # a převeď ho VŠE NA VELKÁ PÍSMENA.
    # Nápověda k indexům: 'v' je na pozici 11, 'i' je na pozici 17.
    
    vyriznute_slovo = tajny_kod[11:17]
    heslo_k_rozhlasu = vyriznute_slovo.UPPER()
    
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
        break  # Ukončí smyčku a jde se slavit

# Závěrečný odpočet do vysílání (For loop)
if okruh_1_hotovo and okruh_2_hotovo:
    print("\nStart vysílání za:")
    # Robot má odpočítat 5 sekund
    for vterina in 5:
        print(f"{vterina}...")