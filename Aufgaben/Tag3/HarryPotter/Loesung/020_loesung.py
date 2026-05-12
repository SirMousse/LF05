# ============================================
#   DIE PRÜFUNG IN HOGWARTS
# ============================================

# 1. Name des Schülers
name = input("Name des Schülers: ")
print(f"\nWillkommen zur Prüfung, {name}!\n")

# 2. Haus abfragen
print("Welchem Haus gehörst du an?")
print("  1 - Gryffindor")
print("  2 - Slytherin")
print("  3 - Ravenclaw")
print("  4 - Hufflepuff")
haus = input("Dein Haus: ").strip()

if haus == "1":
    haus = "Gryffindor"
elif haus == "2":
    haus = "Slytherin"
elif haus == "3":
    haus = "Ravenclaw"
elif haus == "4":
    haus = "Hufflepuff"

# 3. Punktzahl in Zauberkunde
punkte = int(input("\nPunktzahl in Zauberkunde (0-100): "))

if punkte < 50:
    print("Du musst zur Nachprüfung.")
    pruefung = "nachpruefung"

elif punkte <= 79:
    print("Du hast bestanden.")
    pruefung = "bestanden"

else:
    print("Du darfst zur geheimen Prüfung antreten.")
    pruefung = "geheim"

# 4. Zauberstab-Level — nur bei geheimer Prüfung
if pruefung == "geheim":
    zauberstab = int(input("\nZauberstab-Level (0-100): "))

    if zauberstab >= 70:
        print("Dein Zauberstab leuchtet hell.")
        stab_stark = True
    else:
        print("Dein Zauberstab ist noch nicht stark genug.")
        stab_stark = False
else:
    zauberstab = 0
    stab_stark = False

# 5. Zauberspruch abfragen
print("\nWelchen Zauberspruch wählst du?")
print("  1 - Expelliarmus")
print("  2 - Lumos")
print("  3 - Expecto Patronum")
spruch = input("Dein Zauberspruch: ").strip().lower()

if spruch == "1":
    spruch = "expelliarmus"
elif spruch == "2":
    spruch = "lumos"
elif spruch == "3":
    spruch = "expecto patronum"

# 6. Ausgabe je nach Zauberspruch
if spruch == "expelliarmus":
    print("Expelliarmus! Der gegnerische Zauberstab fliegt durch die Luft.")
elif spruch == "lumos":
    print("Lumos! Helles Licht erhellt den dunklen Prüfungsraum.")
elif spruch == "expecto patronum":
    print("Expecto Patronum! Ein silberner Patronus erscheint.")
else:
    print("Unbekannter Spruch — nichts passiert.")

# ============================================
#   BONUS: nested if — Haus + Punktzahl
# ============================================

if haus == "Gryffindor":
    if punkte >= 80:
        print("Mutiger Gryffindor besteht die Prüfung!")
    elif punkte >= 50:
        print("Gryffindor hat bestanden — weiter so!")
    else:
        print("Gryffindor kämpft weiter — zur Nachprüfung!")

elif haus == "Slytherin":
    if punkte >= 80:
        print("Schlaues Slytherin triumphiert in der Prüfung!")
    elif punkte >= 50:
        print("Slytherin hat bestanden und plant seinen nächsten Schritt.")
    else:
        print("Slytherin zieht sich zurück und studiert die Niederlage.")

elif haus == "Ravenclaw":
    if punkte >= 80:
        print("Weises Ravenclaw glänzt in der Prüfung!")
    elif punkte >= 50:
        print("Ravenclaw hat bestanden — Wissen ist Macht.")
    else:
        print("Ravenclaw kehrt in die Bibliothek zurück.")

elif haus == "Hufflepuff":
    if punkte >= 80:
        print("Treues Hufflepuff beweist sein Können!")
    elif punkte >= 50:
        print("Hufflepuff hat bestanden — Fleiß zahlt sich aus.")
    else:
        print("Hufflepuff gibt niemals auf — weiter üben!")

# ============================================
#   VERSCHIEDENE ENDEN
# ============================================

print("\n--- Prüfungsergebnis ---")

if pruefung == "nachpruefung":
    # Ende 1
    print(f"Ende 1: {name} muss nochmal ran.")
    print("Die Bücher warten — Durchhalten!")

elif pruefung == "bestanden":
    if spruch == "expecto patronum":
        # Ende 2
        print(f"Ende 2: {name} hat bestanden und beschwört einen Patronus.")
        print("Die Professoren sind beeindruckt.")
    else:
        # Ende 3
        print(f"Ende 3: {name} verlässt die Prüfung mit einem Lächeln.")
        print("Ein solider Abschluss.")

else:
    # Geheimprüfung
    if not stab_stark:
        # Ende 4
        print(f"Ende 4: {name} hat die Qualifikation erreicht,")
        print("doch der Zauberstab versagt in der Geheimprüfung.")

    else:
        if haus == "Gryffindor":
            # Ende 5
            print(f"Ende 5: {name} besteht die Geheimprüfung mit Bravour.")
            print("Gryffindor gewinnt den Hauspokal!")

        elif spruch == "expecto patronum":
            # Ende 6
            print(f"Ende 6: Mit leuchtendem Zauberstab und perfektem Patronus")
            print(f"wird {name} als bester Absolvent ausgezeichnet.")

        else:
            # Ende 7
            print(f"Ende 7: {name} meistert die Geheimprüfung.")
            print("Ein Name, der in Hogwarts Schriften eingeht.")