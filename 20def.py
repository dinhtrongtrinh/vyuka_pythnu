# ==========================================
# 1. TAHÁK: FUNKCE (Vlastní příkazy)
# ==========================================
# Funkce (začíná slovem 'def' = define) je jako továrna nebo recept.
# Naučíš počítač nový trik, pojmenuješ ho a pak ho můžeš kdykoliv zavolat.
a = 5

def kolikrat_ahoj(a):
    for i in range(a):
        print("ahoj")


print("--- A) ZÁKLADNÍ FUNKCE (Bez vstupů) ---")
# Jen provede kód uvnitř. Nepotřebuje žádné suroviny.
def zatrub():
    print("TÚÚÚ TÚÚÚ! 🎺")

# Aby funkce něco udělala, musíme ji ZAVOLAT jménem a přidat závorky!
zatrub()
zatrub()  # Můžeme ji zavolat kolikrát chceme


print("\n--- B) FUNKCE S ARGUMENTY (Vstupy/Suroviny) ---")
# Do závorek můžeme přidat "proměnné", které funkce potřebuje ke své práci.
def pozdrav_hrace(jmeno, cislo_dresu):
    print(f"Na hřiště nastupuje {jmeno} s číslem {cislo_dresu}!")

pozdrav_hrace("David", 7)
pozdrav_hrace("Jana", 12)


print("\n--- C) FUNKCE S VÝCHOZÍ HODNOTOU (Dobrovolné vstupy) ---")
# Co když někdo zapomene zadat vstup? Můžeme nastavit výchozí (záložní) hodnotu.
def rozdej_svacinu(jidlo="Jablko"):
    print(f"Tady máš svačinu: {jidlo} 🍎")

rozdej_svacinu("Bageta")  # Použije se zadaná Bageta
rozdej_svacinu()          # Nic jsme nezadali, použije se záložní Jablko


print("\n--- D) FUNKCE S NÁVRATOVOU HODNOTOU (Příkaz return) ---")
# TOTO JE NEJDŮLEŽITĚJŠÍ!
# print() jen vypíše text na obrazovku. 
# return() vezme výsledek a VRÁTÍ ho zpět do programu, abychom s ním mohli dál počítat.
def secti_skore(set1, set2, set3):
    celkem = set1 + set2 + set3
    return celkem  # Továrna odevzdává hotový výrobek!

# Zavoláme funkci a to, co nám 'return' vrátí, si schováme do krabice (proměnné)
konecne_skore = secti_skore(25, 22, 15)
print(f"Náš tým dnes nahrál celkem {konecne_skore} bodů!")

# Kdybychom uvnitř funkce měli jen print(), do proměnné by se nic neuložilo!
print("\n")


# ==========================================
# 2. TVŮJ ÚKOL: ASISTENT TRENÉRA
# ==========================================
# Jsi hlavní asistent trenéra pro dnešní volejbalový turnaj.
# Tvým úkolem je naprogramovat 3 chytré funkce, které ušetří trenérovi práci.

print("=== TRENÉRSKÝ SYSTÉM ===")

# ÚKOL 1: ODBYCHOVÝ ČAS (Základní funkce)
# Vytvoř funkci jménem 'oddechovy_cas', která nepotřebuje žádné vstupy (závorky budou prázdné).
# Když ji zavoláš, musí vypsat "PÍÍÍSK! Oddechový čas pro náš tým! ⏱️".

# DOPLŇ KÓD SEM (nezapomeň ji pod tím hned zavolat!):




# ÚKOL 2: KONTROLA PITNÉHO REŽIMU (Funkce s argumentem a výchozí hodnotou)
# Vytvoř funkci 'napoj_hrace', která má jeden argument 'piti'.
# Nastav 'piti' tak, aby jeho VÝCHOZÍ hodnota byla "Voda".
# Funkce vypíše: "Hráč se napil nápoje: [tvoje_piti]".

# DOPLŇ KÓD SEM:




# Zavolání pro kontrolu (odkomentuj po dopsání funkce):
# napoj_hrace("Iontový nápoj")  # Mělo by vypsat Iontový nápoj
# napoj_hrace()                 # Mělo by vypsat Voda


# ÚKOL 3: VYHODNOCENÍ ZÁPASU (Funkce s return)
# Vytvoř funkci 'vyhrali_jsme', která přijme dva argumenty: 'nase_body' a 'body_souper'.
# Pokud jsou naše body VĚTŠÍ než soupeřovy, funkce musí VRÁTIT (return) hodnotu True.
# Jinak musí vrátit False.
# Pozor: Tady se nesmí použít žádný print()!

# DOPLŇ KÓD SEM:




# Zavolání pro kontrolu (odkomentuj po dopsání funkce):
# vysledek = vyhrali_jsme(25, 18)
#
# if vysledek == True:
#     print("Slavíme vítězství! 🏆")
# else:
#     print("Dneska to nevyšlo, jdeme trénovat dál. 🏐")