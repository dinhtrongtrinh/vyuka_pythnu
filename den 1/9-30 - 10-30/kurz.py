# 1. Nastavíme kurz (1 EUR = 25 Kč)
kurz_eur = 25

print("--- ŽELVÍ SMĚNÁRNA ---")

# 2. Zeptáme se uživatele na částku v Kč
kc_text = input("Kolik Kč si chceš vyměnit na eura? ")

# 3. Převod textu ze vstupu na desetinné číslo (float)
kc = float(kc_text)

# 4. Výpočet
eura = kc / kurz_eur

# 5. Výpis výsledku (zaokrouhleno na 2 desetinná místa)
print("Za" ,kc, "Kč dostaneš na dovolenou:", round(eura, 2), "EUR!")