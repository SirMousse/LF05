# ============================================================
# Aufgabe: Das Tierheim-Verwaltungssystem
# ============================================================

# ---------------------------------------------------
# 1. Variablen speichern
# ---------------------------------------------------
hunde = 6
katzen = 4
kaninchen = 3

# ---------------------------------------------------
# 2. Tiere insgesamt
# ---------------------------------------------------
tiere_gesamt = hunde + katzen + kaninchen
print(f"Tiere insgesamt im Tierheim: {tiere_gesamt}")

# ---------------------------------------------------
# 3. Vermittelte Tiere
# ---------------------------------------------------
vermittelt    = 5
tiere_uebrig  = tiere_gesamt - vermittelt
print(f"Tiere noch im Tierheim: {tiere_uebrig}")

# ---------------------------------------------------
# 4. Leckerlis berechnen
# ---------------------------------------------------
leckerlis_gesamt = tiere_uebrig * 3
print(f"Leckerlis insgesamt benötigt: {leckerlis_gesamt}")

# ---------------------------------------------------
# 5. Leckerlis gerecht verteilen
# ---------------------------------------------------
leckerlis_pro_tier = round(leckerlis_gesamt / tiere_uebrig, 2)
print(f"Leckerlis pro Tier: {leckerlis_pro_tier}")

# ---------------------------------------------------
# 6. Rest berechnen (5er-Tüten)
# ---------------------------------------------------
rest = leckerlis_gesamt % 5
print(f"Übrige Leckerlis (5er-Tüten): {rest}")

# ---------------------------------------------------
# 7. Kaninchen vermehren sich
# ---------------------------------------------------
vermehrung = 2 ** 3
print(f"2 ** 3 = {vermehrung}")

# ---------------------------------------------------
# Bonus
# ---------------------------------------------------
# Eigene Zahlen testen
eigene_hunde  = 10
eigene_katzen = 7
print(f"\nBonus – Eigene Zahlen: {eigene_hunde + eigene_katzen} Tiere insgesamt")

# Klammern testen
klammerrechnung = (hunde + katzen) * kaninchen
print(f"Bonus – (Hunde + Katzen) * Kaninchen = {klammerrechnung}")

# round() testen
kommazahl = round(leckerlis_gesamt / 4, 2)
print(f"Bonus – Leckerlis / 4 (gerundet): {kommazahl}")