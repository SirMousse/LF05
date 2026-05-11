# ============================================================
# Aufgabe: Die große Zelda-Mission
# ============================================================

# ---------------------------------------------------
# Teil 1 — Ausrüstung erfassen
# ---------------------------------------------------
schwerter = int(input("Wie viele Schwerter wurden gefunden? "))
schilde = int(input("Wie viele Schilde wurden gefunden? "))
boegen = int(input("Wie viele Bögen wurden gefunden? "))

# ---------------------------------------------------
# Teil 2 — Ausrüstung berechnen
# ---------------------------------------------------
gesamt_ausruestung = schwerter + schilde + boegen
print(f"Ausrüstungsgegenstände insgesamt: {gesamt_ausruestung}")

# ---------------------------------------------------
# Teil 3 — Ausrüstung verloren
# ---------------------------------------------------
verloren = int(input("Wie viele Ausrüstungsgegenstände wurden verloren? "))
ausruestung_uebrig = gesamt_ausruestung - verloren
print(f"Ausrüstung noch übrig: {ausruestung_uebrig}")

# ---------------------------------------------------
# Teil 4 — Rubine berechnen
# ---------------------------------------------------
rubine_gesamt = ausruestung_uebrig * 5
print(f"Rubine insgesamt gesammelt: {rubine_gesamt}")

# ---------------------------------------------------
# Teil 5 — Rubine verteilen
# ---------------------------------------------------
rubine_pro_gegenstand = round(rubine_gesamt / ausruestung_uebrig, 2)
print(f"Rubine pro Ausrüstungsgegenstand: {rubine_pro_gegenstand}")

# ---------------------------------------------------
# Teil 6 — Rest berechnen (6er-Beutel)
# ---------------------------------------------------
rest = rubine_gesamt % 6
print(f"Übrige Rubine (6er-Beutel): {rest}")

# ---------------------------------------------------
# Teil 7 — Helden-Checks
# ---------------------------------------------------
print("\n--- Helden-Checks ---")
print("Mehr als 10 Ausrüstungsgegenstände?  ", gesamt_ausruestung > 10)
print("Genau 4 Schwerter?                   ", schwerter == 4)
print("Weniger als 3 Bögen?                 ", boegen < 3)
print("Mindestens 50 Rubine gesammelt?      ", rubine_gesamt >= 50)
print("Schwerter ≠ Schilde?                 ", schwerter != schilde)

# ---------------------------------------------------
# Teil 8 — Number Manipulation
# ---------------------------------------------------
print("\n--- Number Manipulation ---")
potenz = 2 ** 6
print(f"2 ** 6 = {potenz}")

klammerrechnung = (schwerter + schilde) * boegen
print(f"(Schwerter + Schilde) * Bögen = {klammerrechnung}")

# Kurzschreibweisen
gesamt_ausruestung += 2
print(f"gesamt_ausruestung += 2  → {gesamt_ausruestung}")
gesamt_ausruestung -= 1
print(f"gesamt_ausruestung -= 1  → {gesamt_ausruestung}")

# ---------------------------------------------------
# Bonus-Aufgaben
# ---------------------------------------------------
lieblingsort = input("\nBonus 1 – Wie heißt dein Lieblingsort im Königreich? ")

durchschnitt = round(gesamt_ausruestung / 3, 2)
print(f"Bonus 2 – Durchschnitt der Ausrüstungsarten: {durchschnitt}")

print(f"\nBonus 3 – Die Zelda-Mission in '{lieblingsort}' wurde erfolgreich gemeistert!")
