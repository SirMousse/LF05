# ============================================
# Herr-der-Ringe-Aufgabenreihe Python — Lösungen
# ============================================


# ============================================
# Aufgabe 1 — Name des Gefährten
# ============================================

name = input("Name des Gefährten: ")

if len(name) > 6:
    print("Würdiger Name für eine Legende")
else:
    print("Kurzer Name für einen mutigen Gefährten")


# ============================================
# Aufgabe 2 — Stärke des Helden
# ============================================

staerke = int(input("Stärke des Helden: "))

if staerke >= 80:
    print("Du bist bereit für die Reise nach Mordor")
else:
    print("Du musst noch trainieren")


# ============================================
# Aufgabe 3 — Anzahl der Gefährten
# ============================================

gefaehrten = int(input("Anzahl der Gefährten: "))

if gefaehrten < 3:
    print("Die Gemeinschaft ist zu klein")
elif gefaehrten <= 8:
    print("Die Gemeinschaft ist bereit")
else:
    print("Die Gemeinschaft des Rings ist vollständig")


# ============================================
# Aufgabe 4 — Das geheime Wort von Moria
# ============================================

wort = input("Geheimes Wort: ")

if wort == "mellon":
    print("Das Tor von Moria öffnet sich")
else:
    print("Das Tor bleibt verschlossen")


# ============================================
# Aufgabe 5 — Mut gegen die Orks
# ============================================

mut = int(input("Mut-Wert: "))

if mut < 50:
    print("Du versteckst dich vor den Orks")
else:
    print("Du stellst dich den Orks")


# ============================================
# Aufgabe 6 — Zufällige Reiseprobe
# ============================================

import random

wurf = random.randint(1, 6)

print(wurf)

if wurf == 6:
    print("Ein Adler erscheint zur Hilfe")
else:
    print("Die Reise bleibt gefährlich")


# ============================================
# Aufgabe 7 — Zugang nach Bruchtal
# ============================================

einladung = input("Einladung vorhanden? ")

if einladung == "ja":
    print("Du darfst Bruchtal betreten")
else:
    print("Die Elben lassen dich nicht passieren")


# ============================================
# Aufgabe 8 — Die Minen von Moria
# ============================================

staerke = int(input("Stärke: "))
fackel = input("Fackel vorhanden? ")

if staerke >= 60:
    if fackel == "ja":
        print("Du betrittst sicher die Minen von Moria")
    else:
        print("Ohne Fackel ist der Weg zu gefährlich")
else:
    print("Du bist zu schwach für Moria")


# ============================================
# Aufgabe 9 — Zufällige Begegnung in Mittelerde
# ============================================

import random

begegnung = random.choice(["Ork", "Nazgul", "Ent"])

print(begegnung)

if begegnung == "Ork":
    print("Ein Ork greift an! Zieh dein Schwert und kämpfe.")
elif begegnung == "Nazgul":
    print("Ein Nazgul erscheint! Verbirg den Ring und lauf!")
else:
    print("Ein Ent tritt aus dem Wald. Er könnte ein Verbündeter sein.")


# ============================================
# Aufgabe 10 — Name des Schwertes
# ============================================

schwert_name = input("Name des Schwertes: ")

if len(schwert_name) > 10:
    print("Legendäres Schwert")
elif len(schwert_name) > 5:
    print("Edles Schwert")
else:
    print("Einfaches Schwert")


# ============================================
# Aufgabe 11 — Aufbruch nach Mordor
# ============================================

staerke = int(input("Stärke: "))
vorraete = int(input("Vorräte: "))

if staerke >= 70:
    if vorraete >= 5:
        print("Du kannst nach Mordor aufbrechen")
    else:
        print("Du brauchst mehr Vorräte")
else:
    print("Du bist noch nicht bereit für Mordor")


# ============================================
# Aufgabe 12 — Kampf gegen Saurons Diener
# ============================================

import random

gegner = random.choice(["schwach", "mittel", "stark"])

print("Gegner:", gegner)

kampfkraft = int(input("Deine Kampfkraft: "))

if gegner == "schwach":
    if kampfkraft >= 20:
        print("Du besiegst den Gegner ohne Mühe")
    else:
        print("Selbst der schwache Gegner ist zu viel für dich")

elif gegner == "mittel":
    if kampfkraft >= 40:
        print("Nach hartem Kampf siegst du")
    else:
        print("Du wirst zurückgedrängt")

else:
    if kampfkraft >= 60:
        print("In einem epischen Kampf besiegst du Saurons Diener")
    else:
        print("Du verlierst den Kampf")


# ============================================
# Aufgabe 13 — Rätsel am Tor
# ============================================

import random

geheime_zahl = random.randint(1, 10)

tipp = int(input("Rate die geheime Zahl: "))

if tipp == geheime_zahl:
    print("Das Tor öffnet sich")
elif tipp == geheime_zahl - 1 or tipp == geheime_zahl + 1:
    print("Fast richtig")
else:
    print("Das Tor bleibt verschlossen")


# ============================================
# Aufgabe 14 — Die Prüfung der Gemeinschaft
# ============================================

name = input("Name: ")
staerke = int(input("Stärke: "))
gefaehrten = int(input("Gefährten: "))
ring = input("Ring vorhanden? ")

if len(name) > 6:
    print("Ein Name, der in Liedern besungen wird")

if staerke >= 80:
    if gefaehrten >= 4:
        if ring == "ja":
            print("Die Gemeinschaft kann nach Mordor ziehen")
        else:
            print("Ohne Ring gibt es keine Mission")
    else:
        print("Die Gemeinschaft ist zu klein")
else:
    print("Du bist nicht stark genug")


# ============================================
# Aufgabe 15 — Mittelerde-Finale
# ============================================

import random

print("\n=== DIE REISE NACH MORDOR ===\n")

# Entscheidung 1: Name prüfen (len)
name = input("Name des Gefährten: ")

if len(name) > 6:
    print(f"'{name}' — ein Name, der in den Annalen Mittelerdes stehen wird.")
else:
    print(f"'{name}' — kurz, aber mutig.")

# Entscheidung 2: Stärke
staerke = int(input("Stärke (0-100): "))

if staerke < 40:
    print("Du bist kaum für diese Reise gerüstet.")
elif staerke < 70:
    print("Du bist kampfbereit — aber Mordor ist kein gewöhnlicher Weg.")
else:
    print("Deine Stärke ist legendär. Sauron soll zittern.")

# Entscheidung 3: Gefährten und Vorräte
gefaehrten = int(input("Anzahl der Gefährten: "))
vorraete = int(input("Vorräte (0-20): "))

if vorraete < 5:
    print("Warnung: Die Vorräte reichen kaum bis zum Schicksalsberg.")

# Zufallsereignis: Begegnung auf dem Weg
ereignis = random.choice(["Ork-Horde", "Gandalf", "Nazgul"])
print(f"\nAuf dem Weg nach Mordor: {ereignis}!")

if ereignis == "Ork-Horde":
    print("Die Orks greifen an! Du verlierst einen Gefährten.")
    gefaehrten = max(0, gefaehrten - 1)
    print(f"Verbleibende Gefährten: {gefaehrten}")
elif ereignis == "Gandalf":
    print("Gandalf erscheint und stärkt deine Truppe. +10 Stärke!")
    staerke = min(100, staerke + 10)
    print(f"Neue Stärke: {staerke}")
else:
    print("Ein Nazgul verfolgt euch! Die Reise wird gefährlicher.")

# Entscheidung 4: Ring vorhanden?
ring = input("\nIst der Eine Ring in deinem Besitz? (ja/nein): ").strip().lower()

# Entscheidung 5: Nested ifs — Finale
print("\n--- Schicksalsberg ---")

if staerke >= 70:
    if gefaehrten >= 3:
        if ring == "ja":
            if vorraete >= 5:
                # Ende 1
                print(f"\nEnde 1: Triumph!")
                print(f"{name} und die Gemeinschaft erreichen den Schicksalsberg.")
                print("Der Ring wird vernichtet. Saurons Reich fällt.")
            else:
                # Ende 2
                print(f"\nEnde 2: Erschöpft, aber siegreich.")
                print(f"{name} erreicht das Ziel — knapp ohne Vorräte.")
                print("Der Ring wird vernichtet. Der Preis war hoch.")
        else:
            # Ende 3
            print(f"\nEnde 3: Ohne Ring keine Mission.")
            print(f"{name} kehrt um. Der Ring muss zuerst gefunden werden.")
    else:
        # Ende 4
        print(f"\nEnde 4: Zu wenige Gefährten.")
        print(f"Die Gemeinschaft ist zu klein für Mordor. {name} wartet auf Verstärkung.")
else:
    if staerke >= 40:
        # Ende 5
        print(f"\nEnde 5: Gescheitert an den Toren Mordors.")
        print(f"{name} kämpft tapfer, aber Saurons Wächter sind zu stark.")
    else:
        # Ende 6
        print(f"\nEnde 6: Die Reise endet früh.")
        print(f"{name} war nicht bereit. Mordor bleibt unerreicht.")