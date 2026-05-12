# ============================================================
# Aufgabe: Die magische Zauberschul-Mission
# ============================================================

# ---------------------------------------------------
# Teil 1 — Zauberer-Gruppe erstellen
# ---------------------------------------------------
loewe = int(input("Wie viele Schüler aus Haus Löwe sind dabei? "))
dachs = int(input("Wie viele Schüler aus Haus Dachs sind dabei? "))
rabe = int(input("Wie viele Schüler aus Haus Rabe sind dabei? "))

# ---------------------------------------------------
# Teil 2 — Gruppe berechnen
# ---------------------------------------------------
gesamt_schueler = loewe + dachs + rabe
print(f"Zauberschüler insgesamt dabei: {gesamt_schueler}")

# ---------------------------------------------------
# Teil 3 — Zaubertränke benutzen
# ---------------------------------------------------
benutzte_traenke = int(input("Wie viele Zaubertränke wurden bereits benutzt? "))
traenke_uebrig = 20 - benutzte_traenke
print(f"Zaubertränke noch übrig: {traenke_uebrig}")

# ---------------------------------------------------
# Teil 4 — Hauspunkte berechnen
# ---------------------------------------------------
hauspunkte_gesamt = gesamt_schueler * 5
print(f"Hauspunkte insgesamt gesammelt: {hauspunkte_gesamt}")

# ---------------------------------------------------
# Teil 5 — Hauspunkte verteilen
# ---------------------------------------------------
hauspunkte_pro_schueler = round(hauspunkte_gesamt / gesamt_schueler, 2)
print(f"Hauspunkte pro Zauberschüler: {hauspunkte_pro_schueler}")

# ---------------------------------------------------
# Teil 6 — Rest berechnen (6er-Gruppen)
# ---------------------------------------------------
rest = hauspunkte_gesamt % 6
print(f"Übrige Hauspunkte (6er-Gruppen): {rest}")

# ---------------------------------------------------
# Teil 7 — Magische Checks
# ---------------------------------------------------
print("\n--- Magische Checks ---")
print("Mehr als 10 Zauberschüler dabei?        ", gesamt_schueler > 10)
print("Genau 4 Schüler aus Haus Löwe?          ", loewe == 4)
print("Weniger als 3 Schüler aus Haus Rabe?    ", rabe < 3)
print("Mindestens 50 Hauspunkte gesammelt?     ", hauspunkte_gesamt >= 50)
print("Haus Löwe ≠ Haus Dachs?                 ", loewe != dachs)

# ---------------------------------------------------
# Teil 8 — Number Manipulation
# ---------------------------------------------------
print("\n--- Number Manipulation ---")
potenz = 2 ** 6
print(f"2 ** 6 = {potenz}")

klammerrechnung = (loewe + dachs) * rabe
print(f"(Löwe + Dachs) * Rabe = {klammerrechnung}")

# Kurzschreibweisen
gesamt_schueler += 2
print(f"gesamt_schueler += 2  → {gesamt_schueler}")
gesamt_schueler -= 1
print(f"gesamt_schueler -= 1  → {gesamt_schueler}")

# ---------------------------------------------------
# Bonus-Aufgaben
# ---------------------------------------------------
lieblingszauber = input("\nBonus 1 – Wie heißt dein Lieblingszauber? ")

durchschnitt = round(gesamt_schueler / 3, 2)
print(f"Bonus 2 – Durchschnitt der Schülergruppen: {durchschnitt}")

print(f"\nBonus 3 – Die magische Mission mit '{lieblingszauber}' wurde erfolgreich abgeschlossen!")