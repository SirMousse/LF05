# ============================================================
# Aufgabe: Das IT-Verwaltungssystem
# ============================================================

# ---------------------------------------------------
# 1. Variablen speichern
# ---------------------------------------------------
computer = 6
server = 4
router = 3

# ---------------------------------------------------
# 2. Geräte insgesamt
# ---------------------------------------------------
geraete_gesamt = computer + server + router
print(f"Geräte insgesamt in der IT-Abteilung: {geraete_gesamt}")

# ---------------------------------------------------
# 3. Defekte Geräte
# ---------------------------------------------------
defekt = 5
geraete_ok = geraete_gesamt - defekt
print(f"Noch funktionierende Geräte: {geraete_ok}")

# ---------------------------------------------------
# 4. Updates berechnen
# ---------------------------------------------------
updates_gesamt = geraete_ok * 3
print(f"Updates insgesamt benötigt: {updates_gesamt}")

# ---------------------------------------------------
# 5. Updates gerecht verteilen
# ---------------------------------------------------
updates_pro_geraet = round(updates_gesamt / geraete_ok, 2)
print(f"Updates pro Gerät: {updates_pro_geraet}")

# ---------------------------------------------------
# 6. Rest berechnen (5er-Pakete)
# ---------------------------------------------------
rest = updates_gesamt % 5
print(f"Übrige Updates (5er-Pakete): {rest}")

# ---------------------------------------------------
# 7. Rechenleistung
# ---------------------------------------------------
rechenleistung = 2 ** 3
print(f"2 ** 3 = {rechenleistung}")

# ---------------------------------------------------
# Bonus
# ---------------------------------------------------
# Eigene Zahlen testen
eigene_computer = 10
eigene_server   = 7
print(f"\nBonus – Eigene Zahlen: {eigene_computer + eigene_server} Geräte insgesamt")

# Klammern testen
klammerrechnung = (computer + server) * router
print(f"Bonus – (Computer + Server) * Router = {klammerrechnung}")

# round() testen
kommazahl = round(updates_gesamt / 4, 2)
print(f"Bonus – Updates / 4 (gerundet): {kommazahl}")