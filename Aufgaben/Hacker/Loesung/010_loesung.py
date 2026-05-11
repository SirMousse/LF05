# ============================================================
# Aufgabe: Das Hacker-Verwaltungssystem
# ============================================================

# ---------------------------------------------------
# 1. Variablen speichern
# ---------------------------------------------------
laptops = 6
server = 4
firewalls = 3

# ---------------------------------------------------
# 2. Geräte insgesamt
# ---------------------------------------------------
geraete_gesamt = laptops + server + firewalls
print(f"Geräte insgesamt im Trainingsnetzwerk: {geraete_gesamt}")

# ---------------------------------------------------
# 3. Gesperrte Geräte
# ---------------------------------------------------
gesperrt = 5
geraete_aktiv = geraete_gesamt - gesperrt
print(f"Noch aktive Geräte: {geraete_aktiv}")

# ---------------------------------------------------
# 4. Sicherheitsupdates berechnen
# ---------------------------------------------------
updates_gesamt = geraete_aktiv * 3
print(f"Sicherheitsupdates insgesamt benötigt: {updates_gesamt}")

# ---------------------------------------------------
# 5. Sicherheitsupdates gerecht verteilen
# ---------------------------------------------------
updates_pro_geraet = round(updates_gesamt / geraete_aktiv, 2)
print(f"Sicherheitsupdates pro Gerät: {updates_pro_geraet}")

# ---------------------------------------------------
# 6. Rest berechnen (5er-Pakete)
# ---------------------------------------------------
rest = updates_gesamt % 5
print(f"Übrige Sicherheitsupdates (5er-Pakete): {rest}")

# ---------------------------------------------------
# 7. Passwort-Stärke
# ---------------------------------------------------
passwort_staerke = 2 ** 3
print(f"2 ** 3 = {passwort_staerke}")

# ---------------------------------------------------
# Bonus
# ---------------------------------------------------
# Eigene Zahlen testen
eigene_laptops = 10
eigene_server = 7
print(f"\nBonus – Eigene Zahlen: {eigene_laptops + eigene_server} Geräte insgesamt")

# Klammern testen
klammerrechnung = (laptops + server) * firewalls
print(f"Bonus – (Laptops + Server) * Firewalls = {klammerrechnung}")

# round() testen
kommazahl = round(updates_gesamt / 4, 2)
print(f"Bonus – Updates / 4 (gerundet): {kommazahl}")