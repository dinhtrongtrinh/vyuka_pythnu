import random

# --- VOLBA POČÍTAČE ---
moznosti = ["kamen", "nuzky", "papir"]
pocitac = random.choice(moznosti)

print("=== HRA: KÁMEN, NŮŽKY, PAPÍR ===")
hrac = input("Napiš svou volbu (kamen, nuzky, papir): ").lower().strip()

print(f"\nPočítač vybral: {pocitac}")

# --- VYHODNOCENÍ ---
if hrac == pocitac:
    print("🤝 Remíza! Oba jste dali to samé.")

# Případy, kdy vyhrává hráč
elif (hrac == "kamen" and pocitac == "nuzky") or \
     (hrac == "nuzky" and pocitac == "papir") or \
     (hrac == "papir" and pocitac == "kamen"):
    print("🎉 Vyhrál jsi! Skvělá práce.")

# Případy, kdy hráč zadal správné slovo, ale prohrál
elif hrac in moznosti:
    print("💻 Vyhrál počítač! Zkus to znovu.")

# Když dítě napíše překlep (např. "kamenn")
else:
    print("❌ Neplatná volba! Musíš napsat přesně: kamen, nuzky nebo papir.")