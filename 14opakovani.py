# ==========================================
# 🚨 MISE: OPRAVA ROZBITÉHO ROBOTA 🚨
# ==========================================
# Náš táborový robot "R2-Dřevo" narazil do stromu a jeho kód se poškodil!
# Najdi a oprav 6 chyb, aby robot znovu fungoval. 
# Pokud kód spustíš a spadne to, pozorně čti červenou chybovou hlášku!

print("--- STARTOVÁNÍ ROBOTA ---")

# 1. Nastavení robota
jmeno robota = "R2-Dřevo"
tajne_heslo = "Tabor2026"

# 2. Hlavní systém
baterie = 3

while baterie > 0
    # Robot se snaží zjistit, co má dělat
    akce = input("Zadej příkaz (kricet / heslo): ")
    
    # 3. Zpracování příkazu
    if akce = "kricet":
        # Robot má zakřičet své jméno velkými písmeny
        print("ROBOT ŘÍKÁ:", jmeno_robota.UPPER())
        baterie = baterie - 1
        
    elif akce == "heslo":
        # Chceme zkontrolovat, jestli hráč zná první 3 písmena hesla ("Tab")
        tip = input("Zadej první 3 písmena hesla: ")
        
        if tip == tajne_heslo[1:3]:
            print("Heslo přijato! Robot je opraven.")
            baterie = 0  # Vypne smyčku
            opraveno = True
        else:
            print("Špatný kód!")
            baterie = baterie - 1
            
    else:
        print("Neznámý příkaz.")
        baterie = baterie - 1

# 4. Závěrečná zpráva
if opraveno == True:
    print("Mise úspěšná, robot tě miluje! 🤖❤️")
else:
    print("Robotovi došla baterie a vypnul se. 🪫")