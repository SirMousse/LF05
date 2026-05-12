# ============================================
# Herr-der-Ringe-Aufgabenreihe Python
# Von leicht -> schwer
# ============================================


# ============================================
# Aufgabe 1 — Name des Gefährten
# ============================================

# Frage den Namen des Gefährten ab.
#
# Wenn der Name länger als 6 Zeichen ist:
# Ausgabe -> "Würdiger Name für eine Legende"
#
# Sonst:
# Ausgabe -> "Kurzer Name für einen mutigen Gefährten"
#
# Nutze:
# input()
# if / else
# len()

name = input("Name des Gefährten: ")

# Dein Code



# ============================================
# Aufgabe 2 — Stärke des Helden
# ============================================

# Frage nach der Stärke des Helden.
#
# Ab 80:
# Ausgabe -> "Du bist bereit für die Reise nach Mordor"
#
# Sonst:
# Ausgabe -> "Du musst noch trainieren"
#
# Nutze:
# if / else
# Operatoren

staerke = int(input("Stärke des Helden: "))

# Dein Code



# ============================================
# Aufgabe 3 — Anzahl der Gefährten
# ============================================

# Frage nach der Anzahl der Gefährten.
#
# Unter 3:
# Ausgabe -> "Die Gemeinschaft ist zu klein"
#
# Zwischen 3 und 8:
# Ausgabe -> "Die Gemeinschaft ist bereit"
#
# Ab 9:
# Ausgabe -> "Die Gemeinschaft des Rings ist vollständig"
#
# Nutze:
# if / elif / else

gefaehrten = int(input("Anzahl der Gefährten: "))

# Dein Code



# ============================================
# Aufgabe 4 — Das geheime Wort von Moria
# ============================================

# Frage nach einem geheimen Wort.
#
# Wenn das Wort "mellon" ist:
# Ausgabe -> "Das Tor von Moria öffnet sich"
#
# Sonst:
# Ausgabe -> "Das Tor bleibt verschlossen"
#
# Nutze:
# if / else

wort = input("Geheimes Wort: ")

# Dein Code



# ============================================
# Aufgabe 5 — Mut gegen die Orks
# ============================================

# Frage nach dem Mut-Wert.
#
# Unter 50:
# Ausgabe -> "Du versteckst dich vor den Orks"
#
# Sonst:
# Ausgabe -> "Du stellst dich den Orks"
#
# Nutze:
# Operatoren
# if / else

mut = int(input("Mut-Wert: "))

# Dein Code



# ============================================
# Aufgabe 6 — Zufällige Reiseprobe
# ============================================

# Nutze random.
#
# Das Reiseereignis wird zufällig gewürfelt.
# Die Zahl liegt zwischen 1 und 6.
#
# Wenn die Zahl 6 ist:
# Ausgabe -> "Ein Adler erscheint zur Hilfe"
#
# Sonst:
# Ausgabe -> "Die Reise bleibt gefährlich"
#
# Nutze:
# random
# if / else

import random

wurf = random.randint(1, 6)

print(wurf)

# Dein Code



# ============================================
# Aufgabe 7 — Zugang nach Bruchtal
# ============================================

# Frage:
# - Hat der Gefährte eine Einladung? (ja/nein)
#
# Wenn ja:
# Ausgabe -> "Du darfst Bruchtal betreten"
#
# Sonst:
# Ausgabe -> "Die Elben lassen dich nicht passieren"

einladung = input("Einladung vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 8 — Die Minen von Moria
# ============================================

# Frage:
# - Stärke
# - Hat der Gefährte eine Fackel? (ja/nein)
#
# Wenn Stärke >= 60:
#
#     Wenn Fackel == ja:
#     Ausgabe -> "Du betrittst sicher die Minen von Moria"
#
#     Sonst:
#     Ausgabe -> "Ohne Fackel ist der Weg zu gefährlich"
#
# Sonst:
# Ausgabe -> "Du bist zu schwach für Moria"
#
# Nutze:
# nested ifs

staerke = int(input("Stärke: "))
fackel = input("Fackel vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 9 — Zufällige Begegnung in Mittelerde
# ============================================

# Nutze random.
#
# Zufällig erscheint:
# - Ork
# - Nazgul
# - Ent
#
# Je nach Begegnung:
# unterschiedliche Ausgabe
#
# Nutze:
# random
# if / elif / else

import random

begegnung = random.choice(["Ork", "Nazgul", "Ent"])

print(begegnung)

# Dein Code



# ============================================
# Aufgabe 10 — Name des Schwertes
# ============================================

# Frage nach dem Namen eines Schwertes.
#
# Wenn der Name länger als 10 Zeichen ist:
# Ausgabe -> "Legendäres Schwert"
#
# Wenn der Name länger als 5 Zeichen ist:
# Ausgabe -> "Edles Schwert"
#
# Sonst:
# Ausgabe -> "Einfaches Schwert"
#
# Nutze:
# len()
# if / elif / else

schwert_name = input("Name des Schwertes: ")

# Dein Code



# ============================================
# Aufgabe 11 — Aufbruch nach Mordor
# ============================================

# Frage:
# - Stärke
# - Anzahl Vorräte
#
# Wenn Stärke >= 70:
#
#     Wenn Vorräte >= 5:
#     Ausgabe -> "Du kannst nach Mordor aufbrechen"
#
#     Sonst:
#     Ausgabe -> "Du brauchst mehr Vorräte"
#
# Sonst:
# Ausgabe -> "Du bist noch nicht bereit für Mordor"
#
# Nutze:
# nested ifs
# Operatoren

staerke = int(input("Stärke: "))
vorraete = int(input("Vorräte: "))

# Dein Code



# ============================================
# Aufgabe 12 — Kampf gegen Saurons Diener
# ============================================

# Nutze random.
#
# Der Gegner ist zufällig:
# - schwach
# - mittel
# - stark
#
# Frage zusätzlich nach deiner Kampfkraft.
#
# Je nach Kombination:
# unterschiedliche Ergebnisse
#
# Beispiel:
#
# Wenn Gegner stark UND Kampfkraft unter 60:
# Ausgabe -> "Du verlierst den Kampf"
#
# Nutze:
# random
# nested ifs
# Operatoren

import random

gegner = random.choice(["schwach", "mittel", "stark"])

print("Gegner:", gegner)

kampfkraft = int(input("Deine Kampfkraft: "))

# Dein Code



# ============================================
# Aufgabe 13 — Rätsel am Tor
# ============================================

# Erzeuge eine Zufallszahl zwischen 1 und 10.
#
# Der Spieler muss die geheime Zahl raten.
#
# Wenn richtig:
# Ausgabe -> "Das Tor öffnet sich"
#
# Sonst:
# Ausgabe -> "Das Tor bleibt verschlossen"
#
# Bonus:
# Wenn die Zahl nur um 1 daneben liegt:
# Ausgabe -> "Fast richtig"
#
# Nutze:
# random
# if / elif / else
# Operatoren

import random

geheime_zahl = random.randint(1, 10)

tipp = int(input("Rate die geheime Zahl: "))

# Dein Code



# ============================================
# Aufgabe 14 — Die Prüfung der Gemeinschaft
# ============================================

# Frage:
# - Name
# - Stärke
# - Gefährten
# - Ist der Ring vorhanden? (ja/nein)
#
# Wenn der Name länger als 6 Zeichen:
# Ausgabe -> "Ein Name, der in Liedern besungen wird"
#
# Wenn Stärke >= 80:
#
#     Wenn Gefährten >= 4:
#
#         Wenn Ring == ja:
#         Ausgabe -> "Die Gemeinschaft kann nach Mordor ziehen"
#
#         Sonst:
#         Ausgabe -> "Ohne Ring gibt es keine Mission"
#
#     Sonst:
#     Ausgabe -> "Die Gemeinschaft ist zu klein"
#
# Sonst:
# Ausgabe -> "Du bist nicht stark genug"
#
# Nutze:
# len()
# nested ifs
# Operatoren

name = input("Name: ")
staerke = int(input("Stärke: "))
gefaehrten = int(input("Gefährten: "))
ring = input("Ring vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 15 — Mittelerde-Finale
# ============================================

# Erstelle dein eigenes Mini-Mittelerde-Abenteuer.
#
# Nutze:
# - input()
# - random
# - len()
# - if
# - elif
# - else
# - nested ifs
# - Operatoren
#
# Anforderungen:
#
# - Mindestens 5 Entscheidungen
# - Mindestens 3 verschiedene Enden
# - Mindestens 1 Zufallsereignis
# - Mindestens 1 nested if
# - Mindestens 1 len()-Abfrage
#
# Idee:
#
# Der Gefährte reist durch Mittelerde,
# trifft Orks, Elben und alte Verbündete,
# sammelt Vorräte und entscheidet,
# ob die Reise nach Mordor gelingt.