# ============================================================
# Aufgabe: Die Reise durch Mittelerde
# ============================================================

# ---------------------------------------------------
# Teil 1 — Die Gefährten zählen
# ---------------------------------------------------
hobbits = int(input("Wie viele Hobbits sind in der Gruppe? "))
menschen = int(input("Wie viele Menschen sind in der Gruppe? "))
elben = int(input("Wie viele Elben sind in der Gruppe? "))

# ---------------------------------------------------
# Teil 2 — Gruppe berechnen
# ---------------------------------------------------
gesamt_gefaehrten = hobbits + menschen + elben
print(f"Gefährten insgesamt auf der Reise: {gesamt_gefaehrten}")

# ---------------------------------------------------
# Teil 3 — Gefährten ruhen sich aus
# ---------------------------------------------------
ausruhend = int(input("Wie viele Gefährten müssen sich ausruhen? "))
gefaehrten_aktiv = gesamt_gefaehrten - ausruhend
print(f"Gefährten, die noch weiterziehen: {gefaehrten_aktiv}")

# ---------------------------------------------------
# Teil 4 — Vorräte berechnen
# ---------------------------------------------------
vorraete_gesamt = gefaehrten_aktiv * 5
print(f"Vorratspakete insgesamt benötigt: {vorraete_gesamt}")

# ---------------------------------------------------
# Teil 5 — Vorräte verteilen
# ---------------------------------------------------
vorraete_pro_gefaehrte = round(vorraete_gesamt / gefaehrten_aktiv, 2)
print(f"Vorratspakete pro Gefährte: {vorraete_pro_gefaehrte}")

# ---------------------------------------------------
# Teil 6 — Rest berechnen (6er-Beutel)
# ---------------------------------------------------
rest = vorraete_gesamt % 6
print(f"Übrige Vorratspakete (6er-Beutel): {rest}")

# ---------------------------------------------------
# Teil 7 — Mittelerde-Checks
# ---------------------------------------------------
print("\n--- Mittelerde-Checks ---")
print("Mehr als 10 Gefährten unterwegs?       ", gesamt_gefaehrten > 10)
print("Genau 4 Hobbits?                       ", hobbits == 4)
print("Weniger als 3 Elben?                   ", elben < 3)
print("Mindestens 50 Vorratspakete benötigt?  ", vorraete_gesamt >= 50)
print("Hobbits ≠ Menschen?                    ", hobbits != menschen)

# ---------------------------------------------------
# Teil 8 — Number Manipulation
# ---------------------------------------------------
print("\n--- Number Manipulation ---")
potenz = 2 ** 6
print(f"2 ** 6 = {potenz}")

klammerrechnung = (hobbits + menschen) * elben
print(f"(Hobbits + Menschen) * Elben = {klammerrechnung}")

# Kurzschreibweisen
gesamt_gefaehrten += 2
print(f"gesamt_gefaehrten += 2  → {gesamt_gefaehrten}")
gesamt_gefaehrten -= 1
print(f"gesamt_gefaehrten -= 1  → {gesamt_gefaehrten}")

# ---------------------------------------------------
# Bonus-Aufgaben
# ---------------------------------------------------
ringtraeger = input("\nBonus 1 – Wie heißt der Ringträger? ")

durchschnitt = round(gesamt_gefaehrten / 3, 2)
print(f"Bonus 2 – Durchschnitt der Gruppenarten: {durchschnitt}")

print(f"\nBonus 3 – Die Reise durch Mittelerde mit {ringtraeger} wurde erfolgreich gemeistert!")