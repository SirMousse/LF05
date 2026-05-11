# ============================================================
# Aufgabe: Das Pokémon-Verwaltungssystem
# ============================================================

# ---------------------------------------------------
# 1. Variablen speichern
# ---------------------------------------------------
pikachu = 6
glumanda = 4
schiggy = 3

# ---------------------------------------------------
# 2. Pokémon insgesamt
# ---------------------------------------------------
pokemon_gesamt = pikachu + glumanda + schiggy
print(f"Pokémon insgesamt im Center: {pokemon_gesamt}")

# ---------------------------------------------------
# 3. Freigelassene Pokémon
# ---------------------------------------------------
weitergereist = 5
pokemon_uebrig = pokemon_gesamt - weitergereist
print(f"Pokémon noch im Center: {pokemon_uebrig}")

# ---------------------------------------------------
# 4. Pokériegel berechnen
# ---------------------------------------------------
pokeriegel_gesamt = pokemon_uebrig * 3
print(f"Pokériegel insgesamt benötigt: {pokeriegel_gesamt}")

# ---------------------------------------------------
# 5. Pokériegel gerecht verteilen
# ---------------------------------------------------
pokeriegel_pro_pokemon = round(pokeriegel_gesamt / pokemon_uebrig, 2)
print(f"Pokériegel pro Pokémon: {pokeriegel_pro_pokemon}")

# ---------------------------------------------------
# 6. Rest berechnen (5er-Boxen)
# ---------------------------------------------------
rest = pokeriegel_gesamt % 5
print(f"Übrige Pokériegel (5er-Boxen): {rest}")

# ---------------------------------------------------
# 7. Pokémon-Energie
# ---------------------------------------------------
energie = 2 ** 3
print(f"2 ** 3 = {energie}")

# ---------------------------------------------------
# Bonus
# ---------------------------------------------------
# Eigene Zahlen testen
eigene_pikachu = 10
eigene_glumanda = 7
print(f"\nBonus – Eigene Zahlen: {eigene_pikachu + eigene_glumanda} Pokémon insgesamt")

# Klammern testen
klammerrechnung = (pikachu + glumanda) * schiggy
print(f"Bonus – (Pikachu + Glumanda) * Schiggy = {klammerrechnung}")

# round() testen
kommazahl = round(pokeriegel_gesamt / 4, 2)
print(f"Bonus – Pokériegel / 4 (gerundet): {kommazahl}")