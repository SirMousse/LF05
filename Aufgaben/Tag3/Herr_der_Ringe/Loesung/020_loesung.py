# ============================================
#   DIE REISE NACH MORDOR
# ============================================

# 1. Heldenname abfragen
name = input("Name des Helden: ")
print(f"\nDie Reise beginnt, {name}.\n")

# 2. Stärke abfragen
staerke = int(input("Stärke (0-100): "))

# 3. Gefährten abfragen
gefaehrten = int(input("Anzahl der Gefährten: "))

# --- Stärke-Auswertung ---
if staerke < 30:
    print("Du bist zu schwach für diese Reise.")
    staerke_status = "schwach"

elif staerke < 70:
    print("Du erreichst die Berge.")
    staerke_status = "mittel"

else:
    print("Du erreichst Mordor.")
    staerke_status = "stark"

# BONUS: Gefährten ab 5
if gefaehrten >= 5:
    print("Die Gemeinschaft ist stark.")

# 4. Ring — nur wenn Stärke ab 70
if staerke_status == "stark":
    ring = input("\nWird der Ring getragen? (ja/nein): ").strip().lower()

    if ring == "ja":
        print("Der Ring wird schwerer.")
    else:
        print("Du widerstehst der Macht des Rings.")
else:
    ring = "nein"

# 5. Begleiter abfragen
print("\nWelchen Begleiter hast du?")
print("  1 - Gandalf")
print("  2 - Aragorn")
print("  3 - Legolas")
begleiter = input("Dein Begleiter: ").strip().lower()

if begleiter == "1":
    begleiter = "gandalf"
elif begleiter == "2":
    begleiter = "aragorn"
elif begleiter == "3":
    begleiter = "legolas"

# 6. Ereignis je nach Begleiter
if begleiter == "gandalf":
    print("Gandalf leuchtet den Weg durch die Dunkelheit von Moria.")
elif begleiter == "aragorn":
    print("Aragorn kämpft an deiner Seite und hält die Orks zurück.")
elif begleiter == "legolas":
    print("Legolas trifft jeden Feind aus weiter Ferne — kein Pfeil geht daneben.")
else:
    print("Unbekannter Begleiter — du reist allein.")
    begleiter = None

# ============================================
#   VERSCHIEDENE ENDEN (nested ifs)
# ============================================

print("\n--- Schicksalsberg ---")

if staerke_status == "schwach":
    # Ende 1
    print(f"Ende 1: {name} schafft es nicht.")
    print("Die Reise endet, bevor sie wirklich beginnt.")

elif staerke_status == "mittel":

    if gefaehrten >= 5:
        # Ende 2
        print(f"Ende 2: Die Gemeinschaft hält in den Bergen zusammen.")
        print(f"{name} und seine Gefährten planen den nächsten Schritt nach Mordor.")
    else:
        # Ende 3
        print(f"Ende 3: {name} erreicht die Berge.")
        print("Ohne genug Gefährten ist der Weg nach Mordor versperrt.")

else:
    # Stärke stark — Ring und Begleiter entscheiden

    if ring == "nein":
        # Ende 4
        print(f"Ende 4: {name} widersteht der Macht des Rings.")
        print("Doch ohne den Ring gibt es keine Mission. Die Reise war vergebens.")

    else:
        # Ring wird getragen
        if begleiter == "gandalf":
            # Ende 5
            print(f"Ende 5: Gandalfs Licht hält die Dunkelheit fern.")
            print(f"{name} trägt den Ring bis zum Schicksalsberg — und wirft ihn ins Feuer.")

        elif begleiter == "aragorn":
            # Ende 6
            print(f"Ende 6: Aragorn kämpft jeden Feind nieder.")
            print(f"{name} erreicht den Schicksalsberg. Der Ring fällt ins Feuer.")

        elif begleiter == "legolas":
            # Ende 7
            print(f"Ende 7: Kein Feind kommt nah genug.")
            print(f"{name} erreicht den Schicksalsberg unversehrt. Saurons Reich fällt.")

        else:
            # Ende 8
            print(f"Ende 8: Allein und ohne Begleiter trägt {name} den Ring.")
            print("Gegen alle Wahrscheinlichkeit — die Mission gelingt.")