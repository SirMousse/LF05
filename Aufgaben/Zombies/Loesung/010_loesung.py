# ============================================================
# Aufgabe: Das Zombie-Verwaltungssystem
# ============================================================

# ---------------------------------------------------
# 1. Variablen speichern
# ---------------------------------------------------
zombies = 6
ueberlebende = 4
schutzbunker = 3

# ---------------------------------------------------
# 2. Figuren insgesamt
# ---------------------------------------------------
figuren_gesamt = zombies + ueberlebende
print(f"Figuren insgesamt unterwegs: {figuren_gesamt}")

# ---------------------------------------------------
# 3. Verlorene Figuren
# ---------------------------------------------------
verlorene = 5
figuren_uebrig = figuren_gesamt - verlorene
print(f"Figuren nach der Flucht noch übrig: {figuren_uebrig}")

# ---------------------------------------------------
# 4. Vorräte berechnen
# ---------------------------------------------------
vorratspakete_gesamt = figuren_uebrig * 3
print(f"Benötigte Vorratspakete insgesamt: {vorratspakete_gesamt}")

# ---------------------------------------------------
# 5. Vorräte gerecht verteilen
# ---------------------------------------------------
pakete_pro_figur = round(vorratspakete_gesamt / figuren_uebrig, 2)
print(f"Vorratspakete pro Figur: {pakete_pro_figur}")

# ---------------------------------------------------
# 6. Rest berechnen (5er-Kisten)
# ---------------------------------------------------
rest = vorratspakete_gesamt % 5
print(f"Übrige Vorratspakete (5er-Kisten): {rest}")

# ---------------------------------------------------
# 7. Zombie-Mutation
# ---------------------------------------------------
mutation = 2 ** 3
print(f"2 ** 3 = {mutation}")

# ---------------------------------------------------
# Bonus
# ---------------------------------------------------
# Eigene Zahlen testen
eigene_zombies = 10
eigene_ueberlebende = 7
print(f"\nBonus – Eigene Zahlen: {eigene_zombies + eigene_ueberlebende} Figuren insgesamt")

# Klammern testen
klammerrechnung = (zombies + ueberlebende) * schutzbunker
print(f"Bonus – (Zombies + Überlebende) * Bunker = {klammerrechnung}")

# round() testen
kommazahl = round(vorratspakete_gesamt / 4, 2)
print(f"Bonus – Vorratspakete / 4 (gerundet): {kommazahl}")