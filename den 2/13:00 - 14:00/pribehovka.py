import random
import time

# --- SETUP HRY & PROMĚNNÉ ---
zivoty = 3
inventar = []

def pauza():
    """Pomocná funkce pro dramatické pauzy v textu"""
    time.sleep(1.2)

print("==================================================")
print("  ☣️  TAJEMSTVÍ OPUŠTĚNÉ LABORATOŘE  ☣️")
print("==================================================")
print("Probudil ses v temné mistnosti. Vzduch smrdí chemikáliemi.")
print(f"Tvůj zdravotní stav: ❤️ {zivoty} životy")
pauza()

# ==================================================
# 1. ROZHODNUTÍ: Výběr dveří
# ==================================================
print("\nPřed sebou vidíš dvoje dveře:")
print("1 -> Červené masivní dveře (jde z nich horko)")
print("2 -> Modré poškozené dveře (slyšíš zza nich kapání vody)")

volba1 = input("\nKterými dveřmi projdeš? (1/2): ").strip()

if volba1 == "1":
    print("\nOtevřel jsi červené dveře a vstoupil do kotelny!")
    pauza()
    print("Na zemi vidíš ležet starou heavy-metalovou PÁČIDLO.")
    beru = input("Vezmeš páčidlo? (ano/ne): ").lower().strip()
    
    if beru == "ano":
        inventar.append("páčidlo")
        print("🎒 Páčidlo přidáno do inventáře!")
    else:
        print("Nechal jsi páčidlo ležet na zemi. Snad nebude chybět...")

elif volba1 == "2":
    print("\nProšel jsi modrými dveřmi do zatopené chodby.")
    pauza()
    print("💥 Uklouzl jsi po slizké řase a spadl přímo na koleno!")
    zivoty -= 1
    print(f"Ztrácíš 1 život! Zbývá ti: ❤️ {zivoty}")

else:
    print("\nZmateně jsi koukal na dveře tak dlouho, až jsi zakopl o vlastní tkaničku.")
    zivoty -= 1
    print(f"Ztrácíš 1 život! Zbývá ti: ❤️ {zivoty}")

pauza()

# ==================================================
# 2. ROZHODNUTÍ: Souboj nebo Útěk (Zapojení RANDOM)
# ==================================================
print("\n--------------------------------------------------")
print("Postupuješ hlouběji do komplexu. Najednou z temnoty")
print("vyskočí ZMUTOVANÝ HLODAVEC s červenýma očima! 🐀")
print("--------------------------------------------------")
pauza()

akce = input("Co uděláš? (utect / bojovat): ").lower().strip()

if akce == "utect":
    print("\nDál jsi se na nic neptal a zdrhal, co ti nohy stačily!")
    print("Naštěstí tě krysa nepronásledovala.")

elif akce == "bojovat":
    if "páčidlo" in inventar:
        print("\nVytáhl jsi páčidlo a jedním rozmáchnutím jsi krysu zahnal na útěk!")
        print("Páčidlo se ti fakt hodilo!")
    else:
        print("\nZkusil jsi bojovat holýma rukama...")
        # Náhodná šance na výhru v souboji
        sance = random.randint(1, 6)
        print(f"(Hodil jsi kostkou na útok: {sance} z 6)")
        
        if sance >= 4:
            print("Podařilo se ti krysu odkopnout a utéct!")
        else:
            print("Krysa tě kousla do nohy!")
            zivoty -= 1
            print(f"Ztrácíš 1 život! Zbývá ti: ❤️ {zivoty}")

pauza()

# ==================================================
# 3. ROZHODNUTÍ: Finální Východ / Konec Hry
# ==================================================
print("\n--------------------------------------------------")
print("Přišel jsi k hlavnímu východu z laboratoře.")
print("Dveře jsou zamčené na číselný kód! 🔒")
print("--------------------------------------------------")

if zivoty <= 0:
    print("\n💀 Během cesty ses příliš zranil a vyčerpáním jsi padl...")
    print("=== GAME OVER ===")
else:
    tajny_kod = "1337"
    pokus = input("Zadej 4místný bezpečnostní kód pro únik: ").strip()
    
    if pokus == tajny_kod:
        print("\n🟢 PÍÍÍP! Kód přijat!")
        print("Ocelové dveře se pomalu otevírají a ty vidíš sluneční svit.")
        print(f"🎉 GRATULACE! Unikl jsi z laboratoře se skóre ❤️ {zivoty} životy!")
    else:
        print("\n🔴 BZZZT! Špatný kód! Spustil se alarm a dveře se uzamkly navždy.")
        print("=== GAME OVER ===")

print("\nDíky za hraní!")