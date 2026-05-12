# ============================================
# Abenteuer-Aufgabenreihe Python — Lösungen
# ============================================


# ============================================
# Aufgabe 1 — Der Name des Helden
# ============================================

name = input("Name deines Helden: ")

if len(name) > 5:
    print("Mächtiger Name")
else:
    print("Kurzer Name")


# ============================================
# Aufgabe 2 — Die Schatztruhe
# ============================================

gold = int(input("Goldmünzen: "))

if gold >= 100:
    print("Du bist reich")
else:
    print("Du brauchst mehr Gold")


# ============================================
# Aufgabe 3 — Die Brücke
# ============================================

level = int(input("Level: "))

if level < 10:
    print("Die Brücke ist gesperrt")
elif level <= 20:
    print("Du darfst passieren")
else:
    print("Die Wachen begrüßen dich")


# ============================================
# Aufgabe 4 — Das magische Passwort
# ============================================

wort = input("Geheimes Wort: ")

if wort == "drache":
    print("Geheime Tür geöffnet")
else:
    print("Nichts passiert")


# ============================================
# Aufgabe 5 — Der Heiltrank
# ============================================

leben = int(input("Lebensenergie: "))

if leben < 30:
    print("Heiltrank benutzen")
else:
    print("Weiterkämpfen")


# ============================================
# Aufgabe 6 — Das Würfelspiel
# ============================================

import random

wuerfel = random.randint(1, 6)

print(wuerfel)

if wuerfel == 6:
    print("Kritischer Treffer")
else:
    print("Normaler Angriff")


# ============================================
# Aufgabe 7 — Die alte Tür
# ============================================

schluessel = input("Hast du einen Schlüssel? ")

if schluessel == "ja":
    print("Die Tür öffnet sich")
else:
    print("Die Tür bleibt verschlossen")


# ============================================
# Aufgabe 8 — Der Dungeon-Wächter
# ============================================

level = int(input("Level: "))
schwert = input("Schwert vorhanden? ")

if level >= 20:
    if schwert == "ja":
        print("Du besiegst den Wächter")
    else:
        print("Du brauchst eine Waffe")
else:
    print("Du bist zu schwach")


# ============================================
# Aufgabe 9 — Der Zufallsgegner
# ============================================

import random

gegner = random.choice(["Goblin", "Skelett", "Drache"])

print(gegner)

if gegner == "Goblin":
    print("Ein Goblin greift an! Schnell und schwach — kein Problem.")
elif gegner == "Skelett":
    print("Ein Skelett erhebt sich! Stumpfe Waffen sind wirkungslos.")
else:
    print("Ein Drache erscheint! Lauf oder kämpfe um dein Leben!")


# ============================================
# Aufgabe 10 — Das magische Artefakt
# ============================================

artefakt = input("Artefaktname: ")

if len(artefakt) > 8:
    print("Legendäres Artefakt")
elif len(artefakt) > 4:
    print("Seltenes Artefakt")
else:
    print("Gewöhnliches Artefakt")


# ============================================
# Aufgabe 11 — Der verbotene Wald
# ============================================

level = int(input("Level: "))
heiltraenke = int(input("Heiltränke: "))

if level >= 15:
    if heiltraenke >= 3:
        print("Du betrittst sicher den Wald")
    else:
        print("Du solltest mehr Heiltränke mitnehmen")
else:
    print("Der Wald ist zu gefährlich")


# ============================================
# Aufgabe 12 — Der Bosskampf
# ============================================

import random

boss = random.choice(["schwach", "mittel", "stark"])

print("Boss:", boss)

staerke = int(input("Deine Stärke: "))

if boss == "schwach":
    if staerke >= 15:
        print("Du besiegst den Boss mühelos")
    else:
        print("Selbst der schwache Boss bereitet dir Probleme")

elif boss == "mittel":
    if staerke >= 35:
        print("Nach hartem Kampf besiegst du den Boss")
    else:
        print("Der Boss ist zu stark — du weichst zurück")

else:
    if staerke >= 50:
        print("In einem epischen Kampf besiegst du den mächtigen Boss")
    else:
        print("Du wurdest besiegt")


# ============================================
# Aufgabe 13 — Das Rätsel der Zahlen
# ============================================

import random

zahl = random.randint(1, 10)

tipp = int(input("Rate die Zahl: "))

if tipp == zahl:
    print("Richtig geraten")
elif tipp == zahl - 1 or tipp == zahl + 1:
    print("Fast richtig")
else:
    print("Falsch geraten")


# ============================================
# Aufgabe 14 — Die Heldenprüfung
# ============================================

name = input("Name: ")
level = int(input("Level: "))
gold = int(input("Gold: "))
ruestung = input("Rüstung vorhanden? ")

if len(name) > 5:
    print("Beeindruckender Name")

if level >= 20:
    if gold >= 100:
        if ruestung == "ja":
            print("Du bestehst die Heldenprüfung")
        else:
            print("Du brauchst besseren Schutz")
    else:
        print("Nicht genug Gold")
else:
    print("Du bist noch nicht bereit")


# ============================================
# Aufgabe 15 — Das Abenteuer-Finale
# ============================================

import random

print("\n=== DIE VERGESSENE RUINE ===\n")

# Entscheidung 1: Heldenname (len)
name = input("Name deines Helden: ")

if len(name) > 5:
    print(f"'{name}' — ein Name, der in der Ruine widerhallen wird.")
else:
    print(f"'{name}' — kurz, aber mutig.")

# Entscheidung 2: Level
level = int(input("Dein Level: "))

if level < 10:
    print("Du bist noch ein Anfänger — die Ruine wird dich fordern.")
elif level < 20:
    print("Du hast Erfahrung. Die Ruine respektiert das.")
else:
    print("Veteran. Die Ruine hat keinen Schrecken mehr für dich.")

# Entscheidung 3: Gold und Heiltränke
gold = int(input("Gold: "))
heiltraenke = int(input("Heiltränke: "))

if heiltraenke < 2:
    print("Warnung: Zu wenige Heiltränke für eine Ruine dieser Größe.")

# Zufallsereignis: Was lauert in der Ruine?
ereignis = random.choice(["Falle", "Schatztruhe", "Geist", "Verbündeter"])

print(f"\nIn der Ruine begegnest du: {ereignis}!")

if ereignis == "Falle":
    print("Die Falle schlägt zu! Du verlierst einen Heiltrank.")
    heiltraenke = max(0, heiltraenke - 1)
    print(f"Verbleibende Heiltränke: {heiltraenke}")
elif ereignis == "Schatztruhe":
    print("Eine Schatztruhe! Du findest 50 Goldmünzen.")
    gold += 50
    print(f"Neues Gold: {gold}")
elif ereignis == "Geist":
    print("Ein Geist flüstert dir Wissen zu. +5 Level!")
    level += 5
    print(f"Neues Level: {level}")
else:
    print("Ein Verbündeter schließt sich an und gibt dir 2 Heiltränke.")
    heiltraenke += 2
    print(f"Neue Heiltränke: {heiltraenke}")

# Entscheidung 4: Rüstung vorhanden?
ruestung = input("\nRüstung vorhanden? (ja/nein): ").strip().lower()

# Entscheidung 5: Nested ifs — Finale
print("\n--- Der Schatz der Ruine ---")

if level >= 20:
    if gold >= 100:
        if ruestung == "ja":
            if heiltraenke >= 2:
                # Ende 1
                print(f"\nEnde 1: Vollständig ausgerüstet!")
                print(f"{name} besiegt den Wächter und nimmt den Schatz mit.")
            else:
                # Ende 2
                print(f"\nEnde 2: Knapper Sieg.")
                print(f"{name} siegt, aber ohne Heiltränke war es lebensgefährlich.")
        else:
            # Ende 3
            print(f"\nEnde 3: Ohne Rüstung.")
            print(f"{name} findet den Schatz, wird aber verletzt. Goldreich, aber angeschlagen.")
    else:
        # Ende 4
        print(f"\nEnde 4: Kein Gold für die Torhüter.")
        print(f"{name} wird vom Wächter aufgehalten — Bestechung gescheitert.")
elif level >= 10:
    # Ende 5
    print(f"\nEnde 5: Zu schwach für den Hauptschatz.")
    print(f"{name} findet einen Nebengang und entkommt mit einem kleinen Fund.")
else:
    # Ende 6
    print(f"\nEnde 6: Die Ruine ist zu gefährlich.")
    print(f"{name} flieht. Noch ist es nicht die Zeit.")