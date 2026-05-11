# ============================================================
# Aufgabe: Der große Tierheim-Notfalltag
# ============================================================

# ---------------------------------------------------
# Teil 1 — Neue Tiere aufnehmen
# ---------------------------------------------------
hunde = int(input("Wie viele Hunde sind angekommen? "))
katzen = int(input("Wie viele Katzen sind angekommen? "))
kaninchen = int(input("Wie viele Kaninchen sind angekommen? "))

# ---------------------------------------------------
# Teil 2 — Tiere zählen
# ---------------------------------------------------
gesamt_tiere = hunde + katzen + kaninchen
print(f"Tiere insgesamt angekommen: {gesamt_tiere}")

# ---------------------------------------------------
# Teil 3 — Tiere werden abgeholt
# ---------------------------------------------------
abgeholt = int(input("Wie viele Tiere wurden abgeholt? "))
tiere_uebrig = gesamt_tiere - abgeholt
print(f"Tiere noch im Tierheim: {tiere_uebrig}")

# ---------------------------------------------------
# Teil 4 — Futter berechnen
# ---------------------------------------------------
leckerlis_gesamt = tiere_uebrig * 4
print(f"Leckerlis insgesamt benötigt: {leckerlis_gesamt}")

# ---------------------------------------------------
# Teil 5 — Leckerlis verteilen
# ---------------------------------------------------
leckerlis_pro_tier = round(leckerlis_gesamt / tiere_uebrig, 2)
print(f"Leckerlis pro Tier: {leckerlis_pro_tier}")

# ---------------------------------------------------
# Teil 6 — Rest berechnen (6er-Tüten)
# ---------------------------------------------------
rest = leckerlis_gesamt % 6
print(f"Übrige Leckerlis (6er-Tüten): {rest}")

# ---------------------------------------------------
# Teil 7 — Tierheim-Checks
# ---------------------------------------------------
print("\n--- Tierheim-Checks ---")
print("Mehr als 15 Tiere im Tierheim?       ", gesamt_tiere > 15)
print("Genau 4 Hunde angekommen?            ", hunde == 4)
print("Weniger als 2 Kaninchen da?          ", kaninchen < 2)
print("Mindestens 30 Leckerlis benötigt?    ", leckerlis_gesamt >= 30)
print("Hunde ≠ Katzen?                      ", hunde != katzen)

# ---------------------------------------------------
# Teil 8 — Number Manipulation
# ---------------------------------------------------
print("\n--- Number Manipulation ---")
potenz = 2 ** 4
print(f"2 ** 4 = {potenz}")

klammerrechnung = (hunde + katzen) * kaninchen
print(f"(Hunde + Katzen) * Kaninchen = {klammerrechnung}")

# Kurzschreibweisen
gesamt_tiere += 3
print(f"gesamt_tiere += 3  → {gesamt_tiere}")
gesamt_tiere -= 2
print(f"gesamt_tiere -= 2  → {gesamt_tiere}")

# ---------------------------------------------------
# Bonus-Aufgaben
# ---------------------------------------------------
lieblingshund = input("\nBonus 1 – Wie heißt dein Lieblingshund im Tierheim? ")

durchschnitt = round(gesamt_tiere / 3, 2)
print(f"Bonus 2 – Durchschnitt der Tiere: {durchschnitt}")

print(f"\nBonus 3 – Der Tierheim-Notfall mit '{lieblingshund}' wurde erfolgreich organisiert!")