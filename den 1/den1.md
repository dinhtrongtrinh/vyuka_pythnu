# 📜 TAHÁK LEKTORA – 1. DEN TÁBORA: PYTHON & TURTLE

* **Doba trvání:** 09:00 – 17:00
* **Hlavní cíl:** Dát dětem okamžitý pocit úspěchu skrze vizuální výstupy (Turtle) a odbourat strach z psaní kódu a chyb.
* **Potřebné vybavení:** Dataprojektor/televize (pro live coding), Python + prostředí Thonny (ideální pro začátečníky), tabule + fixy.

---

## ⏰ Podrobný časový harmonogram (09:00 - 17:00)

### 09:00 – 09:30 | 🤝 Seznámení & Offline hra „Lektor je robot“

* **09:00 – 09:10 | Kolečko seznámení:**
  * Jméno, věk, oblíbená PC hra nebo aktivita.
* **09:10 – 09:15 | Pravidla tábora:**
  * Kdy se jí / kam se chodí na záchod.
  * **Zlaté pravidlo:** *Když mluví lektor, všichni se nedotýkají myši ani klávesnice.*
* **09:15 – 09:30 | Hra na robota (Algoritmy v praxi):**
  * Stoupni si dopředu. Děti tě musí instrukcemi dostat od tabule ke dveřím a přimět tě otevřít kliku.
  * **Reaguj doslovně:** Když řeknou „jdi ke dveřím“, naraz do zdi. Když řeknou „otoč se“, toč se do nekonečna.
  * **Pointa:** Počítač dělá *přesně* to, co mu řekneme, ne to, co si *myslíme*, že jsme mu řekli.

> ⚠️ **Na co si dát pozor:** Nastav si hned na začátku signál na ztišení (např. zvednutá ruka nebo tlesknutí). Když mluví všichni přes sebe, robot zamrzne (Error 404).

---

### 09:30 – 10:30 | 💻 1. Blok: První kód v Pythonu (Print & Input)

* **Teorie & Ukázka (Live coding):**
  * Vysvětlení vývojového prostředí (Thonny).
  * Příkaz `print("text")` a proměnné.
  * Získání vstupu od uživatele přes `input()`.
* **Praktické cvičení (Chatbot v konzoli):**
  * Ukázkový kód k napsání:
    jmeno = input("Jak se jmenuješ? ")
    print("Ahoj " + jmeno + ", já jsem tvůj počítač!")
    vek = input("Kolik ti je let? ")
    print("Týjo, " + vek + " let? To už jsi dost starej na programování!")

* **Vlastní projekt:**
  * Ukazat teplomer
    Ukazet kurz
    NEZAPOMENOUT NA "round(promena,1)
> ⚠️ **Na co si dát pozor:**
> 1. Nejčastější chyby: chybějící uvozovky, nezavřené závorky nebo překlepy (prnt).
> 2. Nauč je hned hledat na české klávesnici speciální znaky (uvozovky, závorky).
> 3. Rovnou jim ukaz nejake syntax errory, aby vedeli, co je spatne a co ne

---

### 10:30 – 10:45 | 🍎 Svačina & Odpočinek očí
* Odchod od obrazovek, doplňování energie.

---

### 10:45 – 12:00 | 🐢 2. Blok: Želví robot (Knihovna Turtle)

* **Teorie & Ukázka:**
  * Import knihovny: `import turtle` / `from turtle import *`
  * Příkazy pro pohyb: `forward(100)`, `backward(50)`, `left(90)`, `right(90)`.
  * Úprava vzhledu: `color("red")`, `pensize(3)`, `shape("turtle")`.
* **Praktická cvičení:**
  * **Úkol 1:** Nakreslit čtverec a obdélník.
  * **Úkol 2:** Nakreslit domeček (čtverec + trojúhelníková střecha).
  * **Výzva pro rychlejší:** Nakreslit hvězdu nebo vlastní barevné logo/obrázek.

> ⚠️ **Na co si dát pozor:** Úhly! Zdaleka ne všechny děti v tomto věku znají stupně (90°, 60°, 120°). Kresli jim rotace na tabuli vizuálně.

---

### 12:00 – 13:30 | 🍕 Oběd & Venkovní pauza
* Oběd a následně venkovní pauza v Troji (pohybové hry, frisbee, odpočinek pro oči).

---

### 13:30 – 14:30 | 🔄 3. Blok: Cykly `for` & Magické obrazce

* **Teorie & Ukázka:**
  * Ukázka: Proč psát 8 řádků pro čtverec, když stačí 3?
  * Syntaxe cyklu:
    for i in range(4):
        forward(100)
        right(90)
  * Změna `range(4)` na `range(36)` s malým pootočením -> Spirograf.
* **Praktické cvičení:**
  * Tvorba barevných mozaik, spirografů a rotujících víceúhelníků.

> ⚠️ **Na co si dát pozor:** **IndentationError (odsazování).** V Pythonu záleží na mezerách/tabulátorech uvnitř cyklu. Tohle bude hlavní zdroj odpoledních chyb!

---

### 14:30 – 15:00 | 🧃 Odpolední pauza & Rychlá hra
* Svačina + rychlá teambuildingová hra offline (např. Molekuly, Šifrovaná pošta).

---

### 15:00 – 16:15 | 🏆 4. Blok: Odpolední výzva – Bludiště pro želvu

* **Samostatná práce:**
  * Děti dostanou předchystaný kód/souřadnice bludiště (nebo si nakreslí vlastní).
  * **Úkol:** Napsat kód, který provede želvu bludištěm ze startu do cíle.
  * **Bonus pro premianty:** Změna barvy čáry podle úseku, kreslení efektu/ohňostroje v cíli.

> ⚠️ **Na co si dát pozor:** Rozdílné tempo dětí. Rychlejším dávej hned rozšiřující úkoly („přidej do bludiště překážky / nakresli želvě klobouk“) nebo z nich udělej asistenty lektora, kteří pomáhají pomalejším.

---

### 16:15 – 16:45 | 🎤 Showroom & Prezentace výsledků

* Každé dítě promítne svůj výstřižek/program na plátno nebo ukáže sousedům.
* **Ocenění:** Pochvala za nápady, barvy a netradiční řešení.
* **Reflexe:** *„Ráno jste neuměli napsat ani řádek kódu a teď jste naprogramovali bludiště a spirografy!“*

---

### 16:45 – 17:00 | 🧹 Úklid & Odchod domů

* Uložení projektů (např. do složky `den1_prijmeni`).
* Úklid stolů, vypnutí PC/zaklapnutí notebooků.
* Předání dětí rodičům + rychlé shrnutí, co se dnes naučily.

---

## 🛠 Check-list lektora pro 1. den

- [ ] **Pravidlo 3 minut:** Nikdy nevysvětluj teorii u tabule déle než 5 min v kuse. Vždy hned ukaž kód a nech je to vyzkoušet.
- [ ] **Vítání chyb:** Když vyskočí červený Error, oslav to: *"Super, chybová hláška! Pojďme se všichni podívat, co nám Python říká a jak to opravíme."*
- [ ] **Zapojení premiantů:** Rychlejší děti nepouštěj k YouTube, ale udělej z nich "pomocné lektory".