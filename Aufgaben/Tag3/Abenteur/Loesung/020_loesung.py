# ============================================
#   DIE VERBOTENE INSEL
# ============================================

# 1. Name des Abenteurers
name = input("Name des Abenteurers: ")
print(f"\nWillkommen, {name}. Die Insel erwartet dich.\n")

# 2. Level abfragen
level = int(input("Dein Level: "))

# 3. Goldmünzen abfragen
gold = int(input("Goldmünzen: "))

# --- Level-Auswertung ---
if level < 10:
    print("Du bist noch nicht bereit für die Insel.")
    level_status = "schwach"

elif level < 30:
    print("Du darfst die Küste betreten.")
    level_status = "mittel"

else:
    print("Du darfst zum Tempel der Insel reisen.")
    level_status = "stark"

# BONUS: Heiltrank kaufen wenn Gold >= 100
heiltrank = False
if gold >= 100:
    kauf = input("\nDu hast genug Gold. Möchtest du einen Heiltrank kaufen? (ja/nein): ").strip().lower()
    if kauf == "ja":
        print("Heiltrank gekauft — du bist gut vorbereitet.")
        heiltrank = True
    else:
        print("Du verzichtest auf den Heiltrank.")

# 4. Karte — nur wenn Level ab 30
if level_status == "stark":
    karte = input("\nBesitzt du eine Karte? (ja/nein): ").strip().lower()

    if karte == "ja":
        print("Du findest den versteckten Tempel.")
    else:
        print("Du verirrst dich im Dschungel.")
else:
    karte = "nein"

# 5. Waffe abfragen
print("\nWelche Waffe hast du?")
print("  1 - Schwert")
print("  2 - Bogen")
print("  3 - Magie")
waffe = input("Deine Waffe: ").strip().lower()

if waffe == "1":
    waffe = "schwert"
elif waffe == "2":
    waffe = "bogen"
elif waffe == "3":
    waffe = "magie"

# 6. Kampf-Ausgang je nach Waffe
if waffe == "schwert":
    print("Das Schwert trifft den Wächter mit voller Wucht.")
elif waffe == "bogen":
    print("Ein Pfeil aus sicherer Distanz — präzise und lautlos.")
elif waffe == "magie":
    print("Ein Zauberblitz lähmt den Gegner augenblicklich.")
else:
    print("Unbekannte Waffe — du kämpfst mit bloßen Händen.")
    waffe = None

# ============================================
#   VERSCHIEDENE ENDEN (nested ifs)
# ============================================

print("\n--- Tempel der Insel ---")

if level_status == "schwach":
    # Ende 1
    print(f"Ende 1: {name} wird am Strand zurückgewiesen.")
    print("Die Insel wartet auf Stärkere. Trainiere weiter.")

elif level_status == "mittel":

    if waffe == "magie":
        # Ende 2
        print(f"Ende 2: {name} verteidigt die Küste mit Magie.")
        print("Imposant — aber der Tempel bleibt unerreichbar.")
    else:
        # Ende 3
        print(f"Ende 3: {name} erkundet die Küste.")
        print("Ein paar Fundstücke, aber der Tempel bleibt ein Rätsel.")

else:
    # Level stark
    if karte == "nein":
        # Ende 4
        print(f"Ende 4: {name} irrt durch den Dschungel.")
        print("Ohne Karte kein Tempel. Erschöpft, aber lebendig.")

    else:
        # Karte vorhanden — Waffe und Heiltrank entscheiden
        if waffe == "schwert":
            if heiltrank:
                # Ende 5
                print(f"Ende 5: {name} schlägt den Tempelwächter nieder.")
                print("Vollständig ausgerüstet — der Schatz gehört dir.")
            else:
                # Ende 6
                print(f"Ende 6: {name} besiegt den Wächter — knapp ohne Heiltrank.")
                print("Der Schatz ist gewonnen, aber der Kampf hat Spuren hinterlassen.")

        elif waffe == "bogen":
            # Ende 7
            print(f"Ende 7: {name} erledigt jeden Wächter lautlos.")
            print("Der Tempel gehört ihr, bevor die Insel es merkt.")

        elif waffe == "magie":
            # Ende 8
            print(f"Ende 8: Blitze und Feuer — {name} bezwingt den Tempel.")
            print("Spektakulär. Der Schatz leuchtet.")

        else:
            # Ende 9
            print(f"Ende 9: Ohne Waffe kämpft {name} mit bloßen Händen.")
            print("Gegen alle Wahrscheinlichkeit — der Tempel ist offen.")