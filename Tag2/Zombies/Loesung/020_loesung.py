# ============================================================
# Aufgabe: Die große Zombie-Überlebensmission
# ============================================================

# ---------------------------------------------------
# Teil 1 — Überlebende erfassen
# ---------------------------------------------------
kaempfer = int(input("Wie viele Kämpfer sind in der Gruppe? "))
sanitaeter = int(input("Wie viele Sanitäter sind in der Gruppe? "))
spaeher = int(input("Wie viele Späher sind in der Gruppe? "))

# ---------------------------------------------------
# Teil 2 — Gruppe berechnen
# ---------------------------------------------------
gesamt_ueberlebende = kaempfer + sanitaeter + spaeher
print(f"Gesamtanzahl Überlebende: {gesamt_ueberlebende}")

# ---------------------------------------------------
# Teil 3 — Verletzte Überlebende
# ---------------------------------------------------
verletzte   = int(input("Wie viele Überlebende wurden verletzt? "))
einsatzbereit = gesamt_ueberlebende - verletzte
print(f"Einsatzbereite Überlebende: {einsatzbereit}")

# ---------------------------------------------------
# Teil 4 — Vorräte berechnen
# ---------------------------------------------------
vorratspakete_gesamt = gesamt_ueberlebende * 5
print(f"Benötigte Vorratspakete insgesamt: {vorratspakete_gesamt}")

# ---------------------------------------------------
# Teil 5 — Vorräte verteilen
# ---------------------------------------------------
pakete_pro_person = round(vorratspakete_gesamt / gesamt_ueberlebende, 2)
print(f"Vorratspakete pro Person: {pakete_pro_person}")

# ---------------------------------------------------
# Teil 6 — Rest berechnen
# ---------------------------------------------------
rest = vorratspakete_gesamt % 6
print(f"Übrige Vorratspakete (6er-Kisten): {rest}")

# ---------------------------------------------------
# Teil 7 — Überlebens-Checks
# ---------------------------------------------------
print("\n--- Überlebens-Checks ---")
print("Mehr als 10 Überlebende?       ", gesamt_ueberlebende > 10)
print("Genau 4 Kämpfer?               ", kaempfer == 4)
print("Weniger als 3 Späher?          ", spaeher < 3)
print("Mindestens 50 Vorratspakete?   ", vorratspakete_gesamt >= 50)
print("Kämpfer ≠ Sanitäter?           ", kaempfer != sanitaeter)

# ---------------------------------------------------
# Teil 8 — Number Manipulation
# ---------------------------------------------------
print("\n--- Number Manipulation ---")
potenz = 2 ** 6
print(f"2 ** 6 = {potenz}")

klammerrechnung = (kaempfer + sanitaeter) * spaeher
print(f"(Kämpfer + Sanitäter) * Späher = {klammerrechnung}")

# Kurzschreibweisen
gesamt_ueberlebende += 2
print(f"gesamt_ueberlebende += 2  → {gesamt_ueberlebende}")
gesamt_ueberlebende -= 1
print(f"gesamt_ueberlebende -= 1  → {gesamt_ueberlebende}")

# ---------------------------------------------------
# Bonus-Aufgaben
# ---------------------------------------------------
unterschlupf = input("\nBonus 1 – Wie heißt der sichere Unterschlupf? ")

durchschnitt = round(gesamt_ueberlebende / 3, 2)
print(f"Bonus 2 – Durchschnitt der Gruppenrollen: {durchschnitt}")

print(f"\nBonus 3 – Die Zombie-Überlebensmission in '{unterschlupf}' wurde erfolgreich gemeistert!")