import random
import time

# --- SEZNAM ODPOVĚDÍ ---
odpovedi = [
    "Určitě ano!",
    "Vypadá to velmi nadějně.",
    "Spíše ano.",
    "Ptej se zítra, teď nemám čas.",
    "O tom raději nechtěj vědět...",
    "Spíše ne.",
    "Určitě ne!",
    "To je naprostá blbost."
]

print("=== MAGICKÁ 8-KOULE ===")
print("Ptej se na cokoliv, na co lze odpovědět ANO/NE.")
print()

# --- OTÁZKA OD UŽIVATELE ---
otazka = input("Zadej svou otázku: ")

print("\nMagická koule přemýšlí...")
time.sleep(1.5)  # Dělá to napětí! (Čeká 1.5 vteřiny)

# --- NÁHODNÝ VÝBĚR ODPOVĚDI ---
vybrana_odpoved = random.choice(odpovedi)

print()
print("🔮 Odpověď koule:", vybrana_odpoved)