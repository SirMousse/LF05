# ============================================
#   DIE ARENA-CHALLENGE
# ============================================

# 1. Trainername abfragen
name = input("Name des Trainers: ")
print(f"\nWillkommen, Trainer {name}!\n")

# 2. Orden abfragen
orden = int(input("Anzahl deiner Orden: "))

# 3. Pokemon-Level abfragen
level = int(input("Level deines stärksten Pokémon: "))

# --- Orden-Auswertung ---
if orden < 4:
    print("Du darfst noch nicht zur Liga.")
    orden_status = "wenig"

elif orden <= 7:
    print("Du darfst stärkere Arenen herausfordern.")
    orden_status = "mittel"

else:
    print("Pokémon Liga freigeschaltet.")
    orden_status = "voll"

# BONUS: Level ab 70
if level >= 70:
    print("Dein Pokémon ist sehr stark.")

# 4. Heilitems — nur wenn Orden ab 8
if orden_status == "voll":
    heilitems = input("\nBesitzt du Heilitems? (ja/nein): ").strip().lower()

    if heilitems == "ja":
        print("Du bist bereit für die Liga.")
    else:
        print("Du solltest dich besser vorbereiten.")
else:
    heilitems = "nein"

# 5. Pokémon-Typ abfragen
print("\nWelchen Pokémon-Typ hast du?")
print("  1 - Feuer")
print("  2 - Wasser")
print("  3 - Pflanze")
typ = input("Dein Typ: ").strip().lower()

if typ == "1":
    typ = "feuer"
elif typ == "2":
    typ = "wasser"
elif typ == "3":
    typ = "pflanze"

# 6. Kampf je nach Typ
if typ == "feuer":
    print("Dein Feuer-Pokémon setzt alles in Brand — der Gegner hat keine Chance.")
elif typ == "wasser":
    print("Dein Wasser-Pokémon löscht jeden Angriff aus und kontert mit voller Kraft.")
elif typ == "pflanze":
    print("Dein Pflanzen-Pokémon wächst mit jedem Kampf stärker.")
else:
    print("Unbekannter Typ — Kampf nicht möglich.")
    typ = None

# ============================================
#   VERSCHIEDENE ENDEN (nested ifs)
# ============================================

print("\n--- Liga-Auswertung ---")

if orden_status == "wenig":
    # Ende 1
    print(f"Ende 1: {name} darf die Liga nicht betreten.")
    print("Sammle erst alle Orden und komm zurück.")

elif orden_status == "mittel":

    if level < 40:
        # Ende 2
        print(f"Ende 2: {name} hat einige Orden, aber das Level reicht nicht.")
        print("Trainiere dein Pokémon weiter.")
    else:
        # Ende 3
        print(f"Ende 3: {name} kämpft sich durch die Arenen.")
        print("Die Liga rückt immer näher.")

else:
    # Alle 8 Orden
    if heilitems == "nein":
        # Ende 4
        print(f"Ende 4: {name} tritt ohne Heilitems an.")
        print("Das erste Mitglied des Eliteviers schickt dich nach Hause.")

    else:
        # Heilitems vorhanden — Typ und Level entscheiden

        if typ == "feuer":
            if level >= 70:
                # Ende 5
                print(f"Ende 5: {name}s Feuer-Pokémon verbrennt das gesamte Elitevier.")
                print("Champion!")
            else:
                # Ende 6
                print(f"Ende 6: {name} kämpft tapfer mit Feuer-Typ.")
                print("Level {level} reicht fast — knapp gescheitert.")

        elif typ == "wasser":
            if level >= 70:
                # Ende 7
                print(f"Ende 7: {name}s Wasser-Pokémon überwältigt jeden Gegner.")
                print("Der Championtitel gehört dir!")
            else:
                # Ende 8
                print(f"Ende 8: Wasser-Typ kämpft gut, aber Level {level} ist zu niedrig.")
                print("Das letzte Elitevier-Mitglied gewinnt knapp.")

        elif typ == "pflanze":
            if level >= 70:
                # Ende 9
                print(f"Ende 9: {name}s Pflanzen-Pokémon wächst über alle hinaus.")
                print("Champion!")
            else:
                # Ende 10
                print(f"Ende 10: Pflanze kämpft ausdauernd, aber Level {level} reicht nicht.")
                print("Noch mehr Training und du schaffst es!")

        else:
            # Ende 11
            print(f"Ende 11: Ohne klaren Typ kämpft {name} mit bloßem Willen.")
            print("Gegen alle Wahrscheinlichkeit — irgendwie reicht es.")