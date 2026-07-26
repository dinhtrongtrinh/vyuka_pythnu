# ==========================================
# 1. TAHÁK: SMYČKA WHILE (Opakuj, dokud...)
# ==========================================
# Slovo 'while' znamená česky "DOKUD".
# Smyčka while opakuje kód pořád dokola, DOKUD platí nějaká podmínka.
# Je to jako když trenér říká: "Dokud netrefíš koš, budeš házet znovu!"

print("--- UKÁZKA: ODPOČÍTÁVÁNÍ K ODPALU ---")
sekundy = 3


# Čteme jako: DOKUD jsou sekundy větší než 0, dělej toto:
while sekundy > 0:
    print(f"Raketa startuje za: {sekundy}...")
    
    # ⚠️ SUPER DŮLEŽITÉ: 
    # Musíme sekundy zmenšovat, jinak smyčka nikdy neskončí 
    # a počítač se zblázní (vznikne nekonečná smyčka)!
    sekundy = sekundy - 1  

print("BUM! Raketa letí! 🚀\n")


# ==========================================
# 2. TVŮJ ÚKOL: STRÁŽCE POKLADU
# ==========================================
# Našel jsi truhlu, ale hlídá ji nevrlý skřet. 
# Truhlu ti neotevře, dokud mu neřekneš správné heslo ("klobasa").
# Tvým úkolem je vytvořit smyčku, která hráče nepustí dál, dokud neuhodne.

tajne_heslo = "klobasa"
tvuj_pokus = ""  # Zatím jsi nic neřekl, takže je to prázdný text

print("--- TAJNÁ TRUHLA ---")

# ÚKOL: 
# 1. Napiš 'while' smyčku, která poběží DOKUD se tvuj_pokus NEROVNÁ (!=) tajne_heslo.
# 2. Uvnitř smyčky (nezapomeň na odsazení!) se musíš hráče znovu a znovu ptát na heslo.

# DOPLŇ KÓD SEM:
# while ...
    # tvuj_pokus = input("Skřet vrčí: Řekni heslo, nebo truhlu neotevřu! ")

# Až smyčka skončí (to znamená, že hráč konečně napsal "klobasa"),
# program bude pokračovat dál. Odkomentuj poslední řádek:

# print("Skřet se usmál a truhla se otevřela! Získal jsi zlato! 💰")