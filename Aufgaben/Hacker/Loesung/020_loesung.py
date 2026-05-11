# ============================================================
# Aufgabe: Die geheime Hacker-Mission
# ============================================================

# ---------------------------------------------------
# Teil 1 — Hacker-Team erstellen
# ---------------------------------------------------
coder = int(input("Wie viele Coder sind im Team? "))
analysten = int(input("Wie viele Analysten sind im Team? "))
sicherheitsexperten = int(input("Wie viele Sicherheitsexperten sind im Team? "))

# ---------------------------------------------------
# Teil 2 — Team berechnen
# ---------------------------------------------------
gesamt_team = coder + analysten + sicherheitsexperten
print(f"Teammitglieder insgesamt: {gesamt_team}")

# ---------------------------------------------------
# Teil 3 — Sicherheitslücken schließen
# ---------------------------------------------------
geschlossen = int(input("Wie viele Sicherheitslücken wurden bereits geschlossen? "))
luecken_offen = 20 - geschlossen
print(f"Sicherheitslücken noch offen: {luecken_offen}")

# ---------------------------------------------------
# Teil 4 — Datenpakete berechnen
# ---------------------------------------------------
datenpakete_gesamt = gesamt_team * 5
print(f"Datenpakete insgesamt analysiert: {datenpakete_gesamt}")

# ---------------------------------------------------
# Teil 5 — Datenpakete verteilen
# ---------------------------------------------------
datenpakete_pro_mitglied = round(datenpakete_gesamt / gesamt_team, 2)
print(f"Datenpakete pro Teammitglied: {datenpakete_pro_mitglied}")

# ---------------------------------------------------
# Teil 6 — Rest berechnen (6er-Blöcke)
# ---------------------------------------------------
rest = datenpakete_gesamt % 6
print(f"Übrige Datenpakete (6er-Blöcke): {rest}")

# ---------------------------------------------------
# Teil 7 — Hacker-Checks
# ---------------------------------------------------
print("\n--- Hacker-Checks ---")
print("Mehr als 10 Teammitglieder dabei?             ", gesamt_team > 10)
print("Genau 4 Coder?                                ", coder == 4)
print("Weniger als 3 Analysten?                      ", analysten < 3)
print("Mindestens 50 Datenpakete analysiert?         ", datenpakete_gesamt >= 50)
print("Coder ≠ Sicherheitsexperten?                  ", coder != sicherheitsexperten)

# ---------------------------------------------------
# Teil 8 — Number Manipulation
# ---------------------------------------------------
print("\n--- Number Manipulation ---")
potenz = 2 ** 6
print(f"2 ** 6 = {potenz}")

klammerrechnung = (coder + analysten) * sicherheitsexperten
print(f"(Coder + Analysten) * Sicherheitsexperten = {klammerrechnung}")

# Kurzschreibweisen
gesamt_team += 2
print(f"gesamt_team += 2  → {gesamt_team}")
gesamt_team -= 1
print(f"gesamt_team -= 1  → {gesamt_team}")

# ---------------------------------------------------
# Bonus-Aufgaben
# ---------------------------------------------------
codename = input("\nBonus 1 – Wie lautet der Codename der Mission? ")

durchschnitt = round(gesamt_team / 3, 2)
print(f"Bonus 2 – Durchschnitt der Teamrollen: {durchschnitt}")

print(f"\nBonus 3 – Die ethische Hacker-Mission '{codename}' wurde erfolgreich abgeschlossen!")