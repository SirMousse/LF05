# ============================================================
# Aufgabe: Das Zelda-Verwaltungssystem
# ============================================================

# ---------------------------------------------------
# 1. Variablen speichern
# ---------------------------------------------------
rubine = 6
herzen = 4
pfeile = 3

# ---------------------------------------------------
# 2. Gegenstände insgesamt
# ---------------------------------------------------
gegenstaende_gesamt = rubine + herzen + pfeile
print(f"Gegenstände insgesamt: {gegenstaende_gesamt}")

# ---------------------------------------------------
# 3. Verlorene Gegenstände
# ---------------------------------------------------
verloren = 5
gegenstaende_uebrig = gegenstaende_gesamt - verloren
print(f"Gegenstände nach dem Kampf noch übrig: {gegenstaende_uebrig}")

# ---------------------------------------------------
# 4. Bomben berechnen
# ---------------------------------------------------
bomben_gesamt = gegenstaende_uebrig * 3
print(f"Bomben insgesamt gefunden: {bomben_gesamt}")

# ---------------------------------------------------
# 5. Bomben gerecht verteilen
# ---------------------------------------------------
bomben_pro_gegenstand = round(bomben_gesamt / gegenstaende_uebrig, 2)
print(f"Bomben pro Gegenstand: {bomben_pro_gegenstand}")

# ---------------------------------------------------
# 6. Rest berechnen (5er-Beutel)
# ---------------------------------------------------
rest = bomben_gesamt % 5
print(f"Übrige Bomben (5er-Beutel): {rest}")

# ---------------------------------------------------
# 7. Magische Kraft
# ---------------------------------------------------
magische_kraft = 2 ** 3
print(f"2 ** 3 = {magische_kraft}")

# ---------------------------------------------------
# Bonus
# ---------------------------------------------------
# Eigene Zahlen testen
eigene_rubine = 10
eigene_herzen = 7
print(f"\nBonus – Eigene Zahlen: {eigene_rubine + eigene_herzen} Gegenstände insgesamt")

# Klammern testen
klammerrechnung = (rubine + herzen) * pfeile
print(f"Bonus – (Rubine + Herzen) * Pfeile = {klammerrechnung}")

# round() testen
kommazahl = round(bomben_gesamt / 4, 2)
print(f"Bonus – Bomben / 4 (gerundet): {kommazahl}")