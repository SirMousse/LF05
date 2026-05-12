# ============================================================
# Aufgabe: Das große Abenteuer der Helden
# ============================================================

# ---------------------------------------------------
# Teil 1 — Abenteurer erstellen
# ---------------------------------------------------
krieger = int(input("Wie viele Krieger gibt es? "))
magier = int(input("Wie viele Magier gibt es? "))
bogenschuetzen = int(input("Wie viele Bogenschützen gibt es? "))

# ---------------------------------------------------
# Teil 2 — Gruppe berechnen
# ---------------------------------------------------
gesamt_helden = krieger + magier + bogenschuetzen
print(f"Abenteurer insgesamt unterwegs: {gesamt_helden}")

# ---------------------------------------------------
# Teil 3 — Kampf gegen Monster
# ---------------------------------------------------
verletzt = int(input("Wie viele Helden wurden im Kampf verletzt? "))
helden_aktiv = gesamt_helden - verletzt
print(f"Helden, die noch kämpfen können: {helden_aktiv}")

# ---------------------------------------------------
# Teil 4 — Gold berechnen
# ---------------------------------------------------
gold_gesamt = helden_aktiv * 5
print(f"Goldmünzen insgesamt gesammelt: {gold_gesamt}")

# ---------------------------------------------------
# Teil 5 — Gold verteilen
# ---------------------------------------------------
gold_pro_held = round(gold_gesamt / helden_aktiv, 2)
print(f"Goldmünzen pro Held: {gold_pro_held}")

# ---------------------------------------------------
# Teil 6 — Rest berechnen (6er-Beutel)
# ---------------------------------------------------
rest = gold_gesamt % 6
print(f"Übrige Goldmünzen (6er-Beutel): {rest}")

# ---------------------------------------------------
# Teil 7 — Helden-Checks
# ---------------------------------------------------
print("\n--- Helden-Checks ---")
print("Mehr als 20 Helden unterwegs?          ", gesamt_helden > 20)
print("Genau 5 Magier?                        ", magier == 5)
print("Weniger als 3 Bogenschützen?           ", bogenschuetzen < 3)
print("Mindestens 50 Goldmünzen gesammelt?    ", gold_gesamt >= 50)
print("Krieger ≠ Magier?                      ", krieger != magier)

# ---------------------------------------------------
# Teil 8 — Number Manipulation
# ---------------------------------------------------
print("\n--- Number Manipulation ---")
potenz = 2 ** 5
print(f"2 ** 5 = {potenz}")

klammerrechnung = (krieger + magier) * bogenschuetzen
print(f"(Krieger + Magier) * Bogenschützen = {klammerrechnung}")

# Kurzschreibweisen
gesamt_helden += 2
print(f"gesamt_helden += 2  → {gesamt_helden}")
gesamt_helden -= 1
print(f"gesamt_helden -= 1  → {gesamt_helden}")

# ---------------------------------------------------
# Bonus-Aufgaben
# ---------------------------------------------------
staerkster_held = input("\nBonus 1 – Wie heißt der stärkste Held? ")

durchschnitt = round(gesamt_helden / 3, 2)
print(f"Bonus 2 – Durchschnitt der Helden: {durchschnitt}")

print(f"\nBonus 3 – {staerkster_held} und die Helden haben das Abenteuer erfolgreich gemeistert!")