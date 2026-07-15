# ==========================================
# 🕵️‍♂️ HACKEŘI VE DVOJICI: TREZOR TÁBORA 🕵️‍♀️
# ==========================================
# Trezor hlídají dva bezpečnostní systémy. První hacker musí 
# vyřešit matematickou ochranu a druhý musí rozšifrovat text!
# Kód obsahuje 6 záludných chyb. Najděte je, opravte je a otevřete trezor.
# TIP: Pečlivě čtěte chybové hlášky v konzoli!

print("=== PŘIPOJOVÁNÍ K TREZORU ===")

# Skrytá data v paměti trezoru
tajna_zprava = "xX_Tajny_PoKlaD_Xx"
pokusy = 3
heslo_1_splneno = False
heslo_2_splneno = False

while pokusy > 0:
    print(f"\nZbývají pokusy: {pokusy}")
    
    # --- HACKER 1: Matematická ochrana ---
    print("[HACKER 1] Zadej bezpečnostní kód.")
    # Ochrana vyžaduje zbytek po dělení 17 % 5. Počítač srovnává tvůj vstup s číslem 2.
    cislo = input("Zadej výsledek (17 % 5): ")
    
    if cislo == 2:
        heslo_1_splneno = True
        print("✅ První zámek odemčen!")
    else:
        print("❌ Špatné číslo!")
        pokusy = pokusy - 1
        
    # --- HACKER 2: Očištění dat ---
    print("\n[HACKER 2] Rozšifruj textový klíč.")
    # Úkol: Vyřízni ze zprávy POUZE slovo 'PoKlaD' a převeď ho na malá písmena.
    # Nápověda k indexům: P je na pozici 9, D je na pozici 14.
    
    cast_zpravy = tajna_zprava[9:14]
    upraveny_text = cast_zpravy.lower()

    tip_slova = input("Zadej očištěné slovo: ")
    
    if tip_slova == upraveny_text:
        heslo_2_splneno = True
        print("✅ Druhý zámek odemčen!")
    else:
        print("❌ Špatné slovo!")
        pokusy = pokusy - 1
        
    # --- KONTROLA VÝHRY ---
    if heslo_1_splneno and heslo_2_splneno:
        print("🎉 TREZOR JE OTEVŘENÝ! Získáváte zlatý poklad! 🏆")
        pokusy = 0  # Ukončí smyčku