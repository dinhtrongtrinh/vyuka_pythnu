# ==========================================
# 1. TAHÁK: LOGICKÉ OPERÁTORY (A, NEBO, NE)
# ==========================================
# Logické operátory nám pomáhají spojovat více podmínek dohromady.
# 
# and  (A ZÁROVEŇ) - Musí platit VŠECHNO.
# or   (NEBO)      - Stačí, když platí alespoň JEDNA věc.
# not  (NE / OPAK) - Obrátí pravdu na nepravdu a naopak.

print("--- UKÁZKA: STRÁŽCE BRÁNY ---")

ma_vstupenku = True
ma_vip_naramek = True

# AND: Musíš mít obojí
if ma_vstupenku and ma_vip_naramek:
    print("Můžeš jít do VIP zóny!")
else:
    print("Do VIP zóny nemůžeš, chybí ti náramek nebo vstupenka.")

# OR: Stačí jedno z toho
if ma_vstupenku or ma_vip_naramek:
    print("Můžeš jít na festival!")
else:
    print("Nemáš vstupenku ani náramek, máš smůlu.")

# NOT: Změní True na False a False na True
je_noc = True
if not je_noc:
    print("Je den, svítí sluníčko! ☀️")

print("\n")


# ==========================================
# 2. TVŮJ ÚKOL: VÝPRAVA DO DRAČÍ JESKYNĚ
# ==========================================
# Tvým úkolem je naprogramovat pravidla pro dobrodruha, 
# který se chystá do nebezpečné jeskyně. 
# Zvládne to s vybavením, které má u sebe?

ma_mec = True
ma_stit = False
ma_kouzelny_plast = True

print("--- VÝSLEDEK VÝPRAVY ---")

# ÚKOL A: ZKOUŠKA ODVAHY (and)
# Hrdina přežije útok skřeta, KDYŽ má meč (ma_mec) A ZÁROVEŇ má štít (ma_stit).
# DOPLŇ KÓD SEM:
# if ...
    # print("Hrdina porazil skřeta! ⚔️")
# else:
    # print("Skřet hrdinu přemohl, chybí mu výbava. 💀")


# ÚKOL B: OHNIVÁ PAST (or)
# Hrdina projde ohnivou pastí, KDYŽ má štít (ma_stit) NEBO má kouzelný plášť (ma_kouzelny_plast).
# DOPLŇ KÓD SEM:
# if ...
    # print("Hrdina prošel ohněm bez zranění! 🔥")
# else:
    # print("Au! Hrdina se spálil. 🚑")


# ÚKOL C: TAJNÝ VCHOD (not)
# Tajný vchod do jeskyně se otevře jen ve dne (tedy když NENÍ noc).
# Máme proměnnou 'je_noc'. Doplň podmínku pomocí operátoru 'not'.
je_noc = False

# DOPLŇ KÓD SEM:
# if ...
    # print("Tajný vchod se otevřel! 🚪")