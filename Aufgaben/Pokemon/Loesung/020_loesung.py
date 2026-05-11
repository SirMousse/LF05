# ============================================================
# Aufgabe: Die große Pokémon-Reise
# ============================================================

# ---------------------------------------------------
# Teil 1 — Pokémon-Team erfassen
# ---------------------------------------------------
feuer_pokemon = int(input("Wie viele Feuer-Pokémon sind im Team? "))
wasser_pokemon = int(input("Wie viele Wasser-Pokémon sind im Team? "))
pflanzen_pokemon = int(input("Wie viele Pflanzen-Pokémon sind im Team? "))

# ---------------------------------------------------
# Teil 2 — Team berechnen
# ---------------------------------------------------
gesamt_pokemon = feuer_pokemon + wasser_pokemon + pflanzen_pokemon
print(f"Pokémon insgesamt im Team: {gesamt_pokemon}")

# ---------------------------------------------------
# Teil 3 — Pokémon im Pokémon-Center
# ---------------------------------------------------
im_center = int(input("Wie viele Pokémon erholen sich im Pokémon-Center? "))
kampfbereit = gesamt_pokemon - im_center
print(f"Kampfbereite Pokémon: {kampfbereit}")

# ---------------------------------------------------
# Teil 4 — Pokébälle berechnen
# ---------------------------------------------------
pokeballe_gesamt = gesamt_pokemon * 5
print(f"Pokébälle insgesamt benötigt: {pokeballe_gesamt}")

# ---------------------------------------------------
# Teil 5 — Pokébälle verteilen
# ---------------------------------------------------
pokeballe_pro_pokemon = round(pokeballe_gesamt / gesamt_pokemon, 2)
print(f"Pokébälle pro Pokémon: {pokeballe_pro_pokemon}")

# ---------------------------------------------------
# Teil 6 — Rest berechnen (6er-Pakete)
# ---------------------------------------------------
rest = pokeballe_gesamt % 6
print(f"Übrige Pokébälle (6er-Pakete): {rest}")

# ---------------------------------------------------
# Teil 7 — Trainer-Checks
# ---------------------------------------------------
print("\n--- Trainer-Checks ---")
print("Mehr als 10 Pokémon im Team?              ", gesamt_pokemon > 10)
print("Genau 4 Feuer-Pokémon?                    ", feuer_pokemon == 4)
print("Weniger als 3 Pflanzen-Pokémon?           ", pflanzen_pokemon < 3)
print("Mindestens 50 Pokébälle benötigt?         ", pokeballe_gesamt >= 50)
print("Feuer-Pokémon ≠ Wasser-Pokémon?           ", feuer_pokemon != wasser_pokemon)

# ---------------------------------------------------
# Teil 8 — Number Manipulation
# ---------------------------------------------------
print("\n--- Number Manipulation ---")
potenz = 2 ** 6
print(f"2 ** 6 = {potenz}")

klammerrechnung = (feuer_pokemon + wasser_pokemon) * pflanzen_pokemon
print(f"(Feuer + Wasser) * Pflanzen = {klammerrechnung}")

# Kurzschreibweisen
gesamt_pokemon += 2
print(f"gesamt_pokemon += 2  → {gesamt_pokemon}")
gesamt_pokemon -= 1
print(f"gesamt_pokemon -= 1  → {gesamt_pokemon}")

# ---------------------------------------------------
# Bonus-Aufgaben
# ---------------------------------------------------
liebling = input("\nBonus 1 – Wie heißt dein Lieblings-Pokémon? ")

durchschnitt = round(gesamt_pokemon / 3, 2)
print(f"Bonus 2 – Durchschnitt der Pokémon-Arten: {durchschnitt}")

print(f"\nBonus 3 – Die Pokémon-Reise mit {liebling} wurde erfolgreich gemeistert!")