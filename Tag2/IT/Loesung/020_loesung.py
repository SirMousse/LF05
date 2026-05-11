# ============================================================
# Aufgabe: Die große IT-Mission
# ============================================================

# ---------------------------------------------------
# Teil 1 — IT-Geräte erfassen
# ---------------------------------------------------
computer = int(input("Wie viele Computer werden geprüft? "))
server = int(input("Wie viele Server werden geprüft? "))
router = int(input("Wie viele Router werden geprüft? "))

# ---------------------------------------------------
# Teil 2 — Geräte berechnen
# ---------------------------------------------------
gesamt_geraete = computer + server + router
print(f"Geräte insgesamt geprüft: {gesamt_geraete}")

# ---------------------------------------------------
# Teil 3 — Defekte Geräte
# ---------------------------------------------------
defekt = int(input("Wie viele Geräte sind defekt? "))
geraete_ok = gesamt_geraete - defekt
print(f"Noch funktionierende Geräte: {geraete_ok}")

# ---------------------------------------------------
# Teil 4 — Updates berechnen
# ---------------------------------------------------
updates_gesamt = geraete_ok * 5
print(f"Updates insgesamt benötigt: {updates_gesamt}")

# ---------------------------------------------------
# Teil 5 — Updates verteilen
# ---------------------------------------------------
updates_pro_geraet = round(updates_gesamt / geraete_ok, 2)
print(f"Updates pro Gerät: {updates_pro_geraet}")

# ---------------------------------------------------
# Teil 6 — Rest berechnen (6er-Pakete)
# ---------------------------------------------------
rest = updates_gesamt % 6
print(f"Übrige Updates (6er-Pakete): {rest}")

# ---------------------------------------------------
# Teil 7 — IT-Checks
# ---------------------------------------------------
print("\n--- IT-Checks ---")
print("Mehr als 10 Geräte geprüft?          ", gesamt_geraete > 10)
print("Genau 4 Server?                      ", server == 4)
print("Weniger als 3 Router?                ", router < 3)
print("Mindestens 50 Updates benötigt?      ", updates_gesamt >= 50)
print("Computer ≠ Server?                   ", computer != server)

# ---------------------------------------------------
# Teil 8 — Number Manipulation
# ---------------------------------------------------
print("\n--- Number Manipulation ---")
potenz = 2 ** 6
print(f"2 ** 6 = {potenz}")

klammerrechnung = (computer + server) * router
print(f"(Computer + Server) * Router = {klammerrechnung}")

# Kurzschreibweisen
gesamt_geraete += 2
print(f"gesamt_geraete += 2  → {gesamt_geraete}")
gesamt_geraete -= 1
print(f"gesamt_geraete -= 1  → {gesamt_geraete}")

# ---------------------------------------------------
# Bonus-Aufgaben
# ---------------------------------------------------
wichtigster_server = input("\nBonus 1 – Wie heißt der wichtigste Server? ")

durchschnitt = round(gesamt_geraete / 3, 2)
print(f"Bonus 2 – Durchschnitt der Gerätearten: {durchschnitt}")

print(f"\nBonus 3 – Die IT-Mission auf '{wichtigster_server}' wurde erfolgreich abgeschlossen!")