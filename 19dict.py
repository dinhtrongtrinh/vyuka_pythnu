# ==========================================
# 1. TAHÁK: DICTIONARY (Slovník)
# ==========================================
# Dictionary (slovník) používá složené závorky {}.
# Funguje jako skutečný telefonní seznam. 
# Hledáš SLOVO (Klíč - Key) a najdeš jeho VÝZNAM (Hodnotu - Value).

print("--- UKÁZKA: PROFIL TÁBORNÍKA ---")
tabornik = {
    "jmeno": "David",
    "vek": 12,
    "tym": "Modří",
    "body": 45
}
# 1. Čtení ze slovníku (Místo indexu [0] napíšeme jméno klíče)
print(f"Jméno hráče: {tabornik['jmeno']}")

# 2. Změna hodnoty a přidání nové
tabornik["body"] = 50          # Změní existující počet bodů
tabornik["odznak"] = "Orel"    # Vytvoří úplně nový klíč a hodnotu

print(f"Aktualizovaný profil: {tabornik}")

# 3. Speciální metody slovníku
print("\n--- CO SE SKRÝVÁ UVNITŘ? ---")
print(f"Jen klíče (.keys): {tabornik.keys()}")
print(f"Jen hodnoty (.values): {tabornik.values()}")

# 4. Bezpečné hledání pomocí .get()
# Když hledáš klíč, který neexistuje (např. tabornik["pes"]), program normálně spadne.
# Funkce .get() program nezabije, jen vrátí náhradní text, který si určíš!
mazlicek = tabornik.get("pes", "Tento táborník nemá psa.")
print(f"Hledání psa: {mazlicek}")
print("\n")


# ==========================================
# 2. TVŮJ ÚKOL: TÁBOROVÁ VÝSLEDKOVKA
# ==========================================
# Je středa odpoledne a sportovní turnaje jsou v plném proudu!
# Jako hlavní rozhodčí musíš spravovat tabulku s body jednotlivých týmů.

print("=== BODOVÁNÍ TÝMŮ ===")
vysledkovka = {
    "Draci": 120,
    "Tygři": 95,
    "Sokoli": 110
}

# ÚKOL A: PŘIDÁNÍ TÝMU
# Do turnaje se na poslední chvíli přihlásil tým "Vlci". Zatím mají 0 bodů.
# Přidej je do slovníku 'vysledkovka'.

# DOPLŇ KÓD SEM:


# ÚKOL B: AKTUALIZACE BODŮ
# Tygři právě vyhráli těžký volejbalový zápas a získali 20 bodů!
# Změň jim skóre na 115 (nebo k jejich aktuální hodnotě přičti 20).

# DOPLŇ KÓD SEM:


# ÚKOL C: BEZPEČNÉ HLEDÁNÍ
# Trenér se ptá, kolik bodů mají "Medvědi". 
# Použij metodu .get(), aby program nespadl (Medvědi totiž nehrají),
# a jako náhradní text si nech vypsat "Tým nenalezen".

# DOPLŇ KÓD SEM:
body_medvedu = ""
# print(f"Hledám Medvědy... Výsledek: {body_medvedu}")


# ÚKOL D: VYPSÁNÍ VÝSLEDKŮ (Profi trik pro smyčku for!)
# Když chceme vypsat slovník krásně pod sebe, použijeme for smyčku 
# a magickou metodu .items(), která nám dá rovnou klíč i hodnotu najednou!
# Odkomentuj tento kód a podívej se, jak to vypíše tabulku:

# print("\n--- AKTUÁLNÍ POŘADÍ ---")
# for tym, body in vysledkovka.items():
#     print(f"Tým {tym} má {body} bodů!")