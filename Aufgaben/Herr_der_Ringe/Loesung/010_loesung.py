# ============================================================
# Aufgabe: Das Herr-der-Ringe-Verwaltungssystem
# ============================================================

# ---------------------------------------------------
# 1. Variablen speichern
# ---------------------------------------------------
hobbits = 6
elben = 4
zwerge = 3

# ---------------------------------------------------
# 2. Gefährten insgesamt
# ---------------------------------------------------
gefaehrten_gesamt = hobbits + elben + zwerge
print(f"Gefährten insgesamt in Mittelerde: {gefaehrten_gesamt}")

# ---------------------------------------------------
# 3. Getrennte Gefährten
# ---------------------------------------------------
getrennt = 5
gefaehrten_uebrig = gefaehrten_gesamt - getrennt
print(f"Gefährten noch zusammen: {gefaehrten_uebrig}")

# ---------------------------------------------------
# 4. Lembas-Brote berechnen
# ---------------------------------------------------
lembas_gesamt = gefaehrten_uebrig * 3
print(f"Lembas-Brote insgesamt benötigt: {lembas_gesamt}")

# ---------------------------------------------------
# 5. Lembas-Brote gerecht verteilen
# ---------------------------------------------------
lembas_pro_gefaehrte = round(lembas_gesamt / gefaehrten_uebrig, 2)
print(f"Lembas-Brote pro Gefährte: {lembas_pro_gefaehrte}")

# ---------------------------------------------------
# 6. Rest berechnen (5er-Päckchen)
# ---------------------------------------------------
rest = lembas_gesamt % 5
print(f"Übrige Lembas-Brote (5er-Päckchen): {rest}")

# ---------------------------------------------------
# 7. Magische Ringkraft
# ---------------------------------------------------
ringkraft = 2 ** 3
print(f"2 ** 3 = {ringkraft}")

# ---------------------------------------------------
# Bonus
# ---------------------------------------------------
# Eigene Zahlen testen
eigene_hobbits = 10
eigene_elben   = 7
print(f"\nBonus – Eigene Zahlen: {eigene_hobbits + eigene_elben} Gefährten insgesamt")

# Klammern testen
klammerrechnung = (hobbits + elben) * zwerge
print(f"Bonus – (Hobbits + Elben) * Zwerge = {klammerrechnung}")

# round() testen
kommazahl = round(lembas_gesamt / 4, 2)
print(f"Bonus – Lembas-Brote / 4 (gerundet): {kommazahl}")