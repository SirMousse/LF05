# ============================================================
# Aufgabe: Das Abenteuer-Verwaltungssystem
# ============================================================

# ---------------------------------------------------
# 1. Variablen speichern
# ---------------------------------------------------
schwerter = 6
schilde = 4
schatzkarten = 3

# ---------------------------------------------------
# 2. Gegenstände insgesamt
# ---------------------------------------------------
gegenstaende_gesamt = schwerter + schilde + schatzkarten
print(f"Abenteuer-Gegenstände insgesamt: {gegenstaende_gesamt}")

# ---------------------------------------------------
# 3. Verlorene Gegenstände
# ---------------------------------------------------
verloren = 5
gegenstaende_uebrig = gegenstaende_gesamt - verloren
print(f"Gegenstände noch übrig: {gegenstaende_uebrig}")

# ---------------------------------------------------
# 4. Goldmünzen berechnen
# ---------------------------------------------------
gold_gesamt = gegenstaende_uebrig * 3
print(f"Goldmünzen insgesamt gesammelt: {gold_gesamt}")

# ---------------------------------------------------
# 5. Goldmünzen gerecht verteilen
# ---------------------------------------------------
gold_pro_gegenstand = round(gold_gesamt / gegenstaende_uebrig, 2)
print(f"Goldmünzen pro Gegenstand: {gold_pro_gegenstand}")

# ---------------------------------------------------
# 6. Rest berechnen (5er-Beutel)
# ---------------------------------------------------
rest = gold_gesamt % 5
print(f"Übrige Goldmünzen (5er-Beutel): {rest}")

# ---------------------------------------------------
# 7. Magische Kraft
# ---------------------------------------------------
magische_kraft = 2 ** 3
print(f"2 ** 3 = {magische_kraft}")

# ---------------------------------------------------
# Bonus
# ---------------------------------------------------
# Eigene Zahlen testen
eigene_schwerter = 10
eigene_schilde = 7
print(f"\nBonus – Eigene Zahlen: {eigene_schwerter + eigene_schilde} Gegenstände insgesamt")

# Klammern testen
klammerrechnung = (schwerter + schilde) * schatzkarten
print(f"Bonus – (Schwerter + Schilde) * Schatzkarten = {klammerrechnung}")

# round() testen
kommazahl = round(gold_gesamt / 4, 2)
print(f"Bonus – Goldmünzen / 4 (gerundet): {kommazahl}")