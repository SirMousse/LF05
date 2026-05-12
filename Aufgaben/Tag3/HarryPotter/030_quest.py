# ============================================
# Harry-Potter-Aufgabenreihe Python
# Von leicht -> schwer
# ============================================


# ============================================
# Aufgabe 1 — Name des Zauberschülers
# ============================================

# Frage den Namen des Zauberschülers ab.
#
# Wenn der Name länger als 6 Zeichen ist:
# Ausgabe -> "Mächtiger Zaubername"
#
# Sonst:
# Ausgabe -> "Kurzer Zaubername"
#
# Nutze:
# input()
# if / else
# len()

name = input("Name des Zauberschülers: ")

# Dein Code



# ============================================
# Aufgabe 2 — Punkte in Zauberkunde
# ============================================

# Frage nach der Punktzahl in Zauberkunde.
#
# Ab 80 Punkten:
# Ausgabe -> "Sehr gute Zauberleistung"
#
# Sonst:
# Ausgabe -> "Du musst weiter üben"
#
# Nutze:
# if / else
# Operatoren

punkte = int(input("Punkte in Zauberkunde: "))

# Dein Code



# ============================================
# Aufgabe 3 — Hauspunkte prüfen
# ============================================

# Frage nach den Hauspunkten.
#
# Unter 50:
# Ausgabe -> "Dein Haus liegt zurück"
#
# Zwischen 50 und 100:
# Ausgabe -> "Dein Haus ist gut dabei"
#
# Über 100:
# Ausgabe -> "Dein Haus führt den Wettbewerb an"
#
# Nutze:
# if / elif / else

hauspunkte = int(input("Hauspunkte: "))

# Dein Code



# ============================================
# Aufgabe 4 — Geheimer Zauberspruch
# ============================================

# Frage nach einem geheimen Zauberspruch.
#
# Wenn der Zauberspruch "lumos" ist:
# Ausgabe -> "Dein Zauberstab leuchtet"
#
# Sonst:
# Ausgabe -> "Nichts passiert"
#
# Nutze:
# if / else

zauberspruch = input("Geheimer Zauberspruch: ")

# Dein Code



# ============================================
# Aufgabe 5 — Zauberstab-Stärke
# ============================================

# Frage nach der Stärke des Zauberstabs.
#
# Unter 40:
# Ausgabe -> "Der Zauberstab ist noch zu schwach"
#
# Sonst:
# Ausgabe -> "Der Zauberstab ist einsatzbereit"
#
# Nutze:
# Operatoren
# if / else

stab_staerke = int(input("Zauberstab-Stärke: "))

# Dein Code



# ============================================
# Aufgabe 6 — Zufälliger Trank
# ============================================

# Nutze random.
#
# Ein zufälliger Trank wird gebraut.
# Die Zahl liegt zwischen 1 und 6.
#
# Wenn die Zahl 6 ist:
# Ausgabe -> "Perfekter Zaubertrank"
#
# Sonst:
# Ausgabe -> "Der Trank ist brauchbar"
#
# Nutze:
# random
# if / else

import random

trank = random.randint(1, 6)

print(trank)

# Dein Code



# ============================================
# Aufgabe 7 — Bibliothekszugang
# ============================================

# Frage:
# - Hat der Schüler eine Erlaubnis? (ja/nein)
#
# Wenn ja:
# Ausgabe -> "Zugang zur verbotenen Abteilung erlaubt"
#
# Sonst:
# Ausgabe -> "Zugang verweigert"

erlaubnis = input("Erlaubnis vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 8 — Prüfung im Verwandlungsunterricht
# ============================================

# Frage:
# - Punktzahl
# - Hat der Schüler seinen Zauberstab dabei? (ja/nein)
#
# Wenn Punktzahl >= 60:
#
#     Wenn Zauberstab == ja:
#     Ausgabe -> "Prüfung bestanden"
#
#     Sonst:
#     Ausgabe -> "Ohne Zauberstab kannst du nicht antreten"
#
# Sonst:
# Ausgabe -> "Prüfung nicht bestanden"
#
# Nutze:
# nested ifs

punkte = int(input("Punktzahl: "))
zauberstab = input("Zauberstab dabei? ")

# Dein Code



# ============================================
# Aufgabe 9 — Zufällige magische Begegnung
# ============================================

# Nutze random.
#
# Zufällig erscheint:
# - Troll
# - Dementor
# - Hippogreif
#
# Je nach Begegnung:
# unterschiedliche Ausgabe
#
# Nutze:
# random
# if / elif / else

import random

begegnung = random.choice(["Troll", "Dementor", "Hippogreif"])

print(begegnung)

# Dein Code



# ============================================
# Aufgabe 10 — Name des Zaubertranks
# ============================================

# Frage nach dem Namen eines Zaubertranks.
#
# Wenn der Name länger als 10 Zeichen ist:
# Ausgabe -> "Komplexer Zaubertrank"
#
# Wenn der Name länger als 5 Zeichen ist:
# Ausgabe -> "Fortgeschrittener Zaubertrank"
#
# Sonst:
# Ausgabe -> "Einfacher Zaubertrank"
#
# Nutze:
# len()
# if / elif / else

trank_name = input("Name des Zaubertranks: ")

# Dein Code



# ============================================
# Aufgabe 11 — Zugang zur Kammer
# ============================================

# Frage:
# - Magie-Level
# - Anzahl gefundener Hinweise
#
# Wenn Magie-Level >= 70:
#
#     Wenn Hinweise >= 3:
#     Ausgabe -> "Die geheime Kammer öffnet sich"
#
#     Sonst:
#     Ausgabe -> "Du hast noch nicht genug Hinweise"
#
# Sonst:
# Ausgabe -> "Deine Magie ist zu schwach"
#
# Nutze:
# nested ifs
# Operatoren

magie_level = int(input("Magie-Level: "))
hinweise = int(input("Gefundene Hinweise: "))

# Dein Code



# ============================================
# Aufgabe 12 — Duell gegen einen dunklen Magier
# ============================================

# Nutze random.
#
# Der Gegner ist zufällig:
# - schwach
# - mittel
# - stark
#
# Frage zusätzlich nach deiner Zauberkraft.
#
# Je nach Kombination:
# unterschiedliche Ergebnisse
#
# Beispiel:
#
# Wenn Gegner stark UND Zauberkraft unter 60:
# Ausgabe -> "Du verlierst das Duell"
#
# Nutze:
# random
# nested ifs
# Operatoren

import random

gegner = random.choice(["schwach", "mittel", "stark"])

print("Gegner:", gegner)

zauberkraft = int(input("Deine Zauberkraft: "))

# Dein Code



# ============================================
# Aufgabe 13 — Zahlenrätsel der Zauberprüfung
# ============================================

# Erzeuge eine Zufallszahl zwischen 1 und 10.
#
# Der Schüler muss die magische Zahl raten.
#
# Wenn richtig:
# Ausgabe -> "Magische Zahl erkannt"
#
# Sonst:
# Ausgabe -> "Falsche Zahl"
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

magische_zahl = random.randint(1, 10)

tipp = int(input("Rate die magische Zahl: "))

# Dein Code



# ============================================
# Aufgabe 14 — Die Hogwarts-Prüfung
# ============================================

# Frage:
# - Name
# - Magie-Level
# - Hauspunkte
# - Ist der Zauberstab vorhanden? (ja/nein)
#
# Wenn der Name länger als 6 Zeichen:
# Ausgabe -> "Beeindruckender Zaubername"
#
# Wenn Magie-Level >= 80:
#
#     Wenn Hauspunkte >= 100:
#
#         Wenn Zauberstab == ja:
#         Ausgabe -> "Hogwarts-Prüfung bestanden"
#
#         Sonst:
#         Ausgabe -> "Zauberstab fehlt"
#
#     Sonst:
#     Ausgabe -> "Nicht genug Hauspunkte"
#
# Sonst:
# Ausgabe -> "Magie-Level zu niedrig"
#
# Nutze:
# len()
# nested ifs
# Operatoren

name = input("Name: ")
magie_level = int(input("Magie-Level: "))
hauspunkte = int(input("Hauspunkte: "))
zauberstab = input("Zauberstab vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 15 — Hogwarts-Finale
# ============================================

# Erstelle dein eigenes Mini-Hogwarts-Abenteuer.
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
# Der Schüler erkundet nachts Hogwarts,
# findet Hinweise, begegnet magischen Wesen
# und muss entscheiden, ob er mutig weitermacht
# oder zur Sicherheit zurückkehrt.