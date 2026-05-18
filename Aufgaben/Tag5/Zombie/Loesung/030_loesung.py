import random

# ==================================================
#  ZOMBIE ABENTEUER: DIE LETZTE STADT
#  Ein interaktives Python-Lernspiel
# ==================================================

def trennlinie(titel=""):
    print("\n" + "=" * 50)
    if titel:
        print(f"  {titel}")
        print("=" * 50)

def pause():
    input("\n[ Enter drücken um fortzufahren... ]")


# ==================================================
# LEVEL 1 – DER ÜBERLEBENDE
# Konzepte: Variablen, print(), input()
# ==================================================

def level1():
    trennlinie("LEVEL 1 – DER ÜBERLEBENDE")
    print("\nWillkommen in der letzten Stadt!")

    name = input("Wie heißt du?\n> ")
    alter = input("Wie alt bist du?\n> ")

    print("\nWähle deine Rolle:")
    print("  1 - Sanitäter")
    print("  2 - Soldat")
    print("  3 - Mechaniker")
    print("  4 - Scout")

    rollen = {"1": "Sanitäter", "2": "Soldat", "3": "Mechaniker", "4": "Scout"}
    wahl = input("> ")
    rolle = rollen.get(wahl, "Unbekannt")

    print(f"\nHallo {name}!")
    print(f"Alter: {alter} | Rolle: {rolle}")
    print("Du bist jetzt Teil der Überlebenden.")
    print("\n[ Python-Konzept: Variablen, input() ]")

    pause()
    return name, alter, rolle


# ==================================================
# LEVEL 2 – DAS SICHERE HAUS
# Konzepte: if / elif / else
# ==================================================

def level2():
    trennlinie("LEVEL 2 – DAS SICHERE HAUS")
    print("\nDu stehst vor einem sicheren Haus.")
    print("Passwort zum Einlass erforderlich.")

    passwort = "survive"
    versuche = 0

    while True:
        eingabe = input("\nPasswort eingeben:\n> ")
        if eingabe.lower() == passwort:
            print(f" Tür geöffnet! Willkommen im sicheren Haus!")
            print(f"  Fehlversuche: {versuche}")
            break
        else:
            versuche += 1
            print(f"✗ Zugang verweigert! ({versuche}. Fehlversuch)")
            if versuche >= 3:
                print("  Hinweis: Denk ans Überleben...")

    print("\n[ Python-Konzept: if / elif / else ✓ ]")
    pause()


# ==================================================
# LEVEL 3 – DER ERSTE ZOMBIE
# Konzepte: random
# ==================================================

def level3(leben):
    trennlinie("LEVEL 3 – DER ERSTE ZOMBIE")
    print("\nEin Zombie greift an! (random.randint(1, 6))\n")

    spieler_wert = random.randint(1, 6)
    zombie_wert  = random.randint(1, 6)

    print(f"  Dein Angriff:   {spieler_wert}")
    print(f"  Zombie Angriff: {zombie_wert}")

    if spieler_wert > zombie_wert:
        print("\n SIEG! Du hast den Zombie besiegt!")
        zombies_besiegt = 1
    elif spieler_wert < zombie_wert:
        print("\n NIEDERLAGE! Der Zombie trifft dich! -15 HP")
        leben -= 15
        zombies_besiegt = 0
    else:
        print("\n= UNENTSCHIEDEN! Beide weichen zurück.")
        zombies_besiegt = 0

    print(f"  Leben: {leben} HP")
    print("\n[ Python-Konzept: import random ✓ ]")
    pause()
    return leben, zombies_besiegt


# ==================================================
# LEVEL 4 – DER ÜBERLEBENSRUCKSACK
# Konzepte: Listen
# ==================================================

def level4(inventar):
    trennlinie("LEVEL 4 – DER ÜBERLEBENSRUCKSACK")

    while True:
        print("\nDein Inventar:")
        for i, item in enumerate(inventar):
            print(f"  [{i}] {item}")

        print(f'\n"Wasser" vorhanden: {"JA ✓" if "Wasser" in inventar else "NEIN"}')
        print(f"Plätze: {len(inventar)}/10")

        print("\nWas möchtest du tun?")
        print("  1 - Item hinzufügen")
        print("  2 - Item entfernen")
        print("  3 - Weiter")

        wahl = input("> ")

        if wahl == "1":
            if len(inventar) >= 10:
                print("✗ Rucksack ist voll! (Max. 10 Plätze)")
            else:
                item = input("Welches Item hinzufügen?\n> ")
                inventar.append(item)
                print(f'"{item}" wurde hinzugefügt!')

        elif wahl == "2":
            item = input("Welches Item entfernen?\n> ")
            if item in inventar:
                inventar.remove(item)
                print(f'"{item}" wurde entfernt.')
            else:
                print("Item nicht im Inventar gefunden!")

        elif wahl == "3":
            break
        else:
            print("Ungültige Eingabe!")

    print("\n[ Python-Konzept: Listen ]")
    pause()
    return inventar


# ==================================================
# LEVEL 5 – DIE NACHTWACHE
# Konzepte: while-Schleifen
# ==================================================

def level5(nahrung):
    trennlinie("LEVEL 5 – DIE NACHTWACHE")
    print("\nDu hältst Nachtwache. (while-Schleife)")

    beobachtungen = [
        "Alles ruhig.",
        "Ein Geräusch in der Ferne... falscher Alarm.",
        "Du siehst Schatten – nur Bäume.",
        "Eine Katze läuft vorbei.",
        "Verdächtige Bewegung! War nichts."
    ]

    while True:
        print("\n  1 - Umgebung prüfen")
        print("  2 - Barrikade reparieren")
        print("  3 - Schlafen gehen")

        wahl = input("> ")

        if wahl == "1":
            print(random.choice(beobachtungen))
        elif wahl == "2":
            print("Barrikade verstärkt! +5 Sicherheit.")
        elif wahl == "3":
            print("Du schläfst ein. Gute Nacht...")
            nahrung = max(0, nahrung - 2)
            print(f"Nahrung verbraucht: noch {nahrung} übrig.")
            break
        else:
            print("Ungültige Eingabe!")

    print("\n[ Python-Konzept: while-Schleife ✓ ]")
    pause()
    return nahrung


# ==================================================
# LEVEL 6 – DIE ZOMBIEWELLEN
# Konzepte: for-Schleifen
# ==================================================

def level6(leben):
    trennlinie("LEVEL 6 – DIE ZOMBIEWELLEN")
    print("\n5 Zombies greifen an! (for i in range(5))\n")

    zombies_besiegt = 0

    for i in range(1, 6):
        spieler_staerke = random.randint(1, 6)
        zombie_staerke  = random.randint(1, 6)

        print(f"--- Zombie {i}/5 ---")
        print(f"  Du: {spieler_staerke}  |  Zombie: {zombie_staerke}")

        if spieler_staerke > zombie_staerke:
            print("Sieg!")
            zombies_besiegt += 1
        elif spieler_staerke < zombie_staerke:
            print("Treffer! -8 HP")
            leben = max(0, leben - 8)
        else:
            print("  = Unentschieden!")

        if leben <= 0:
            print("\nDu bist den Wunden erlegen!")
            break

    print(f"\nErgebnis: {zombies_besiegt}/5 Zombies besiegt!")
    print(f"Leben: {leben} HP")
    print("\n[ Python-Konzept: for-Schleife ✓ ]")
    pause()
    return leben, zombies_besiegt


# ==================================================
# LEVEL 7 – DAS ÜBERLEBENDENREGISTER
# Konzepte: Dictionaries
# ==================================================

def level7():
    trennlinie("LEVEL 7 – DAS ÜBERLEBENDENREGISTER")

    ueberlebende = {
        "Mia":  "Sanitäterin",
        "Jake": "Soldat",
        "Lena": "Mechanikerin"
    }

    while True:
        print("\nÜberlebende:")
        for name, rolle in ueberlebende.items():
            print(f"  {name}: {rolle}")

        print("\n  1 - Person suchen")
        print("  2 - Person hinzufügen")
        print("  3 - Person entfernen")
        print("  4 - Weiter")

        wahl = input("> ")

        if wahl == "1":
            name = input("Name eingeben:\n> ")
            if name in ueberlebende:
                print(f"{name} ist {ueberlebende[name]}.")
            else:
                print(f"{name} nicht in der Liste gefunden.")

        elif wahl == "2":
            name  = input("Name:\n> ")
            rolle = input("Rolle:\n> ")
            ueberlebende[name] = rolle
            print(f"{name} ({rolle}) hinzugefügt!")

        elif wahl == "3":
            name = input("Wen entfernen?\n> ")
            if name in ueberlebende:
                del ueberlebende[name]
                print(f'"{name}" wurde entfernt.')
            else:
                print("Person nicht gefunden!")

        elif wahl == "4":
            break
        else:
            print("Ungültige Eingabe!")

    print("\n[ Python-Konzept: Dictionaries ✓ ]")
    pause()
    return ueberlebende


# ==================================================
# LEVEL 8 – DIE KARTE DER STADT
# Konzepte: Tupel
# ==================================================

def level8():
    trennlinie("LEVEL 8 – DIE KARTE DER STADT")

    orte = {
        "Krankenhaus":  (8,  14),
        "Supermarkt":   (3,   7),
        "Polizeistation":(12,  5),
        "Bunker":       (15, 15),
        "Tankstelle":   (6,   2)
    }

    print("\nBekannte Orte (Tupel-Koordinaten):")
    for name, (x, y) in orte.items():
        print(f"  {name:18s} → X={x}, Y={y}")

    print("\nWohin möchtest du reisen?")
    for name in orte:
        print(f"  - {name}")

    ziel = input("> ")

    # Schreibweise ignorieren
    treffer = next((k for k in orte if k.lower() == ziel.lower()), None)

    if treffer:
        ziel_x, ziel_y = orte[treffer]
        print(f"\nNavigiere zu {treffer}...")
        print(f"  Ziel-Koordinaten: ({ziel_x}, {ziel_y})")

        pos_x = random.randint(0, 15)
        pos_y = random.randint(0, 15)
        print(f"  Deine Position:   ({pos_x}, {pos_y})")

        entfernung = abs(pos_x - ziel_x) + abs(pos_y - ziel_y)
        if entfernung == 0:
            print("✓ Ziel erreicht!")
        else:
            print(f"  Entfernung zum Ziel: {entfernung} Felder")
            print("  Weiter marschieren...")
    else:
        print("✗ Unbekannter Ort.")

    print("\n[ Python-Konzept: Tupel ✓ ]")
    pause()
    return orte


# ==================================================
# LEVEL 9 – DIE LETZTE STADT (ALLES KOMBINIERT)
# + ENDGEGNER: DER MUTANT
# Konzepte: alles zusammen
# ==================================================

def level9(name, rolle, leben, nahrung, inventar, ueberlebende, orte, zombies_besiegt_gesamt):
    trennlinie("LEVEL 9 – ENDGEGNER: DER MUTANT")

    waffen = {
        "Messer":           5,
        "Pistole":         15,
        "Schrotflinte":    25,
        "Baseballschläger":10,
        "Machete":         18
    }

    print(f"\nEIN RIESIGER MUTANTEN-ZOMBIE ERSCHEINT!")
    print(f"{name}, du musst ihn besiegen!\n")
    print(f"Deine Waffen:")
    for w, s in waffen.items():
        im_inv = "✓" if w in inventar else " "
        print(f"  [{im_inv}] {w}: {s} Schaden")

    pause()

    mutant_leben    = 80
    mutant_max      = 80
    runde           = 0

    # Kampfsystem mit while-Schleife
    while leben > 0 and mutant_leben > 0:
        runde += 1
        print(f"\n{'─'*40}")
        print(f"  Runde {runde}")
        print(f"  Du:     {'█' * (leben // 10):<10} {leben} HP")
        print(f"  Mutant: {'█' * (mutant_leben // 10):<10} {mutant_leben} HP")
        print(f"{'─'*40}")

        print("\n  1 - Angreifen")
        print("  2 - Heilen")
        print("  3 - Fliehen")
        print("  4 - Barrikade nutzen")

        wahl = input("> ")

        mutant_schaden = random.randint(5, 20)

        if wahl == "1":
            # Beste Waffe aus dem Inventar wählen
            beste_waffe   = None
            bester_schaden = 0
            for item in inventar:
                if item in waffen and waffen[item] > bester_schaden:
                    beste_waffe    = item
                    bester_schaden = waffen[item]

            if beste_waffe:
                schaden = random.randint(bester_schaden - 3, bester_schaden + 5)
                schaden = max(1, schaden)
                print(f"⚔ Angriff mit {beste_waffe}: {schaden} Schaden!")
            else:
                schaden = random.randint(2, 6)
                print(f"Faustkampf: {schaden} Schaden!")

            mutant_leben = max(0, mutant_leben - schaden)
            print(f"Mutant schlägt zurück: {mutant_schaden} Schaden!")
            leben = max(0, leben - mutant_schaden)

        elif wahl == "2":
            if "Verbandskasten" in inventar:
                heilung = random.randint(15, 30)
                leben   = min(100, leben + heilung)
                inventar.remove("Verbandskasten")
                print(f"Geheilt! +{heilung} HP (Verbandskasten verbraucht)")
            else:
                print("✗ Kein Verbandskasten im Inventar!")

            print(f"Mutant greift an: {mutant_schaden} Schaden!")
            leben = max(0, leben - mutant_schaden)

        elif wahl == "3":
            flucht = random.randint(1, 3)
            if flucht == 1:
                print("🏃 Du entkamst erfolgreich!")
                break
            else:
                print("✗ Flucht fehlgeschlagen!")
                schaden = mutant_schaden * 2
                leben   = max(0, leben - schaden)
                print(f"Mutant erwischt dich: {schaden} Schaden!")

        elif wahl == "4":
            block = random.randint(5, 15)
            effektiv = max(0, mutant_schaden - block)
            print(f"Barrikade blockiert {block} Schaden!")
            print(f"Verbleibender Schaden: {effektiv}")
            leben = max(0, leben - effektiv)

        else:
            print("Ungültige Eingabe! Der Mutant schlägt trotzdem!")
            leben = max(0, leben - mutant_schaden)

        print(f"\n  Leben nach Runde {runde}: {leben} HP")

    # Kampf-Auswertung
    print("\n" + "=" * 50)
    if leben > 0 and mutant_leben <= 0:
        print("  🎉 DER MUTANT IST BESIEGT!")
    elif leben <= 0:
        print("  ☠  DU BIST GEFALLEN...")
    else:
        print("  🏃 DU BIST GEFLOHEN.")

    print("\n[ Python-Konzept: while + if/elif/else ✓ ]")
    return leben


# ==================================================
# SPIELZUSAMMENFASSUNG
# ==================================================

def zusammenfassung(name, rolle, leben, nahrung, inventar, ueberlebende, zombies_besiegt):
    trennlinie("SPIELZUSAMMENFASSUNG")

    print(f"\n  Spieler:          {name}")
    print(f"  Rolle:            {rolle}")
    print(f"  Leben:            {leben} HP")
    print(f"  Nahrung:          {nahrung}")
    print(f"  Inventar:         {', '.join(inventar) if inventar else '—'}")
    print(f"  Zombies besiegt:  {zombies_besiegt}")
    print(f"  Überlebende:      {len(ueberlebende)}")

    print("\n  Python-Konzepte verwendet:")
    konzepte = [
        "Variablen", "input()", "if / elif / else",
        "while-Schleifen", "for-Schleifen", "import random",
        "Listen", "Dictionaries", "Tupel"
    ]
    for k in konzepte:
        print(f"    ✓ {k}")

    if leben > 0:
        print("\n  🏆 DU HAST DIE ZOMBIE-APOKALYPSE ÜBERLEBT!")
    else:
        print("\n  ☠  GAME OVER – Die Welt gehört den Zombies.")

    print("=" * 50)


# ==================================================
# HAUPTPROGRAMM
# ==================================================

def main():
    print("\n" + "█" * 50)
    print("  ZOMBIE ABENTEUER: DIE LETZTE STADT")
    print("  Ein interaktives Python-Lernspiel")
    print("  Levels 1–9 + Endgegner")
    print("█" * 50)
    input("\n[ Enter drücken um das Abenteuer zu beginnen... ]")

    # Startwerte
    leben   = 100
    nahrung = 10
    inventar = ["Wasser", "Verbandskasten", "Messer"]
    zombies_besiegt = 0

    # Level 1 – Variablen & input()
    name, alter, rolle = level1()

    # Level 2 – if/elif/else
    level2()

    # Level 3 – random
    leben, z = level3(leben)
    zombies_besiegt += z

    # Level 4 – Listen
    inventar = level4(inventar)

    # Level 5 – while
    nahrung = level5(nahrung)

    # Level 6 – for
    leben, z = level6(leben)
    zombies_besiegt += z

    # Level 7 – Dictionaries
    ueberlebende = level7()

    # Level 8 – Tupel
    orte = level8()

    # Level 9 – Alles kombiniert + Endgegner
    leben = level9(
        name, rolle, leben, nahrung, inventar,
        ueberlebende, orte, zombies_besiegt
    )

    # Zusammenfassung
    zusammenfassung(name, rolle, leben, nahrung, inventar, ueberlebende, zombies_besiegt)


if __name__ == "__main__":
    main()