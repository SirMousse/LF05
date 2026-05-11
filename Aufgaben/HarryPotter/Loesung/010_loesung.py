# ============================================================
# Aufgabe: Das Harry-Potter-Verwaltungssystem
# ============================================================

# ---------------------------------------------------
# 1. Variablen speichern
# ---------------------------------------------------
zauberstäbe = 6
kessel = 4
zauberbücher = 3

# ---------------------------------------------------
# 2. Magische Gegenstände insgesamt
# ---------------------------------------------------
gegenstaende_gesamt = zauberstäbe + kessel + zauberbücher
print(f"Magische Gegenstände insgesamt in Hogwarts: {gegenstaende_gesamt}")

# ---------------------------------------------------
# 3. Verlorene Gegenstände
# ---------------------------------------------------
verschwunden = 5
gegenstaende_uebrig = gegenstaende_gesamt - verschwunden
print(f"Magische Gegenstände noch übrig: {gegenstaende_uebrig}")

# ---------------------------------------------------
# 4. Schokofrösche berechnen
# ---------------------------------------------------
schokofrosche_gesamt = gegenstaende_uebrig * 3
print(f"Schokofrösche insgesamt benötigt: {schokofrosche_gesamt}")

# ---------------------------------------------------
# 5. Schokofrösche gerecht verteilen
# ---------------------------------------------------
schokofrosche_pro_gegenstand = round(schokofrosche_gesamt / gegenstaende_uebrig, 2)
print(f"Schokofrösche pro Gegenstand: {schokofrosche_pro_gegenstand}")

# ---------------------------------------------------
# 6. Rest berechnen (5er-Schachteln)
# ---------------------------------------------------
rest = schokofrosche_gesamt % 5
print(f"Übrige Schokofrösche (5er-Schachteln): {rest}")

# ---------------------------------------------------
# 7. Magische Zauberkraft
# ---------------------------------------------------
zauberkraft = 2 ** 3
print(f"2 ** 3 = {zauberkraft}")

# ---------------------------------------------------
# Bonus
# ---------------------------------------------------
# Eigene Zahlen testen
eigene_zauberstäbe = 10
eigene_kessel      = 7
print(f"\nBonus – Eigene Zahlen: {eigene_zauberstäbe + eigene_kessel} Gegenstände insgesamt")

# Klammern testen
klammerrechnung = (zauberstäbe + kessel) * zauberbücher
print(f"Bonus – (Zauberstäbe + Kessel) * Zauberbücher = {klammerrechnung}")

# round() testen
kommazahl = round(schokofrosche_gesamt / 4, 2)
print(f"Bonus – Schokofrösche / 4 (gerundet): {kommazahl}")