print("--- AMERICKÝ TEPLOMĚR ---")

# 1. Načtení teploty v °C
celsius_text = input("Kolik stupňů °C je teď venku? ")

# 2. Převod vstupu na číslo
celsius = float(celsius_text)

# 3. Vzorec pro převod na °F
fahrenheit = (celsius * 1.8) + 32

# 4. Výpis výsledku
print("Kdybys byl v Americe, na teploměru by bylo:", round(fahrenheit, 1), "°F!")