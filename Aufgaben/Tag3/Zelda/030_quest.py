# ============================================
# Zelda-Aufgabenreihe Python
# Von leicht -> schwer
# ============================================


# ============================================
# Aufgabe 1 — Heldenname prüfen
# ============================================

# Frage den Namen des Helden ab.
#
# Wenn der Name länger als 6 Zeichen ist:
# Ausgabe -> "Würdiger Heldenname"
#
# Sonst:
# Ausgabe -> "Kurzer Heldenname"
#
# Nutze:
# input()
# if / else
# len()

heldenname = input("Heldenname: ")

# Dein Code



# ============================================
# Aufgabe 2 — Herzen prüfen
# ============================================

# Frage nach der Anzahl deiner Herzen.
#
# Ab 10 Herzen:
# Ausgabe -> "Du bist gut vorbereitet"
#
# Sonst:
# Ausgabe -> "Du brauchst mehr Herzen"
#
# Nutze:
# if / else
# Operatoren

herzen = int(input("Anzahl Herzen: "))

# Dein Code



# ============================================
# Aufgabe 3 — Rubine prüfen
# ============================================

# Frage nach der Anzahl deiner Rubine.
#
# Unter 50:
# Ausgabe -> "Du bist noch arm"
#
# Zwischen 50 und 199:
# Ausgabe -> "Du kannst dir Ausrüstung kaufen"
#
# Ab 200:
# Ausgabe -> "Du bist reich genug für seltene Items"
#
# Nutze:
# if / elif / else

rubine = int(input("Anzahl Rubine: "))

# Dein Code



# ============================================
# Aufgabe 4 — Geheimes Tempelwort
# ============================================

# Frage nach einem geheimen Wort.
#
# Wenn das Wort "triforce" ist:
# Ausgabe -> "Der Tempel öffnet sich"
#
# Sonst:
# Ausgabe -> "Der Tempel bleibt verschlossen"
#
# Nutze:
# if / else

wort = input("Geheimes Wort: ")

# Dein Code



# ============================================
# Aufgabe 5 — Ausdauer prüfen
# ============================================

# Frage nach der Ausdauer des Helden.
#
# Unter 40:
# Ausgabe -> "Du bist zu erschöpft zum Klettern"
#
# Sonst:
# Ausgabe -> "Du kannst weiterklettern"
#
# Nutze:
# Operatoren
# if / else

ausdauer = int(input("Ausdauer: "))

# Dein Code



# ============================================
# Aufgabe 6 — Zufälliger Schatzfund
# ============================================

# Nutze random.
#
# Eine Schatztruhe würfelt eine Zahl zwischen 1 und 6.
#
# Wenn die Zahl 6 ist:
# Ausgabe -> "Du findest ein seltenes Item"
#
# Sonst:
# Ausgabe -> "Du findest ein paar Rubine"
#
# Nutze:
# random
# if / else

import random

truhe = random.randint(1, 6)

print(truhe)

# Dein Code



# ============================================
# Aufgabe 7 — Schlüssel vorhanden
# ============================================

# Frage:
# - Ist ein Schlüssel vorhanden? (ja/nein)
#
# Wenn ja:
# Ausgabe -> "Die Tür öffnet sich"
#
# Sonst:
# Ausgabe -> "Die Tür bleibt verschlossen"

schluessel = input("Schlüssel vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 8 — Tempel-Zugang
# ============================================

# Frage:
# - Anzahl der Herzen
# - Ist ein Schlüssel vorhanden? (ja/nein)
#
# Wenn Herzen >= 8:
#
#     Wenn Schlüssel == ja:
#     Ausgabe -> "Du darfst den Tempel betreten"
#
#     Sonst:
#     Ausgabe -> "Du brauchst einen Schlüssel"
#
# Sonst:
# Ausgabe -> "Du hast nicht genug Herzen"
#
# Nutze:
# nested ifs

herzen = int(input("Anzahl Herzen: "))
schluessel = input("Schlüssel vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 9 — Zufällige Begegnung
# ============================================

# Nutze random.
#
# Zufällig erscheint:
# - Bokblin
# - Wächter
# - Fee
#
# Je nach Begegnung:
# unterschiedliche Ausgabe
#
# Nutze:
# random
# if / elif / else

import random

begegnung = random.choice(["Bokblin", "Wächter", "Fee"])

print(begegnung)

# Dein Code



# ============================================
# Aufgabe 10 — Itemname prüfen
# ============================================

# Frage nach dem Namen eines Items.
#
# Wenn der Name länger als 10 Zeichen ist:
# Ausgabe -> "Legendäres Item"
#
# Wenn der Name länger als 5 Zeichen ist:
# Ausgabe -> "Besonderes Item"
#
# Sonst:
# Ausgabe -> "Einfaches Item"
#
# Nutze:
# len()
# if / elif / else

item = input("Itemname: ")

# Dein Code



# ============================================
# Aufgabe 11 — Bossraum öffnen
# ============================================

# Frage:
# - Anzahl der Herzen
# - Anzahl der Schlüssel
#
# Wenn Herzen >= 12:
#
#     Wenn Schlüssel >= 3:
#     Ausgabe -> "Der Bossraum öffnet sich"
#
#     Sonst:
#     Ausgabe -> "Du brauchst mehr Schlüssel"
#
# Sonst:
# Ausgabe -> "Du bist zu schwach für den Bossraum"
#
# Nutze:
# nested ifs
# Operatoren

herzen = int(input("Anzahl Herzen: "))
schluessel = int(input("Anzahl Schlüssel: "))

# Dein Code



# ============================================
# Aufgabe 12 — Kampf gegen den Tempelboss
# ============================================

# Nutze random.
#
# Der Boss ist zufällig:
# - schwach
# - mittel
# - stark
#
# Frage zusätzlich nach deiner Angriffskraft.
#
# Je nach Kombination:
# unterschiedliche Ergebnisse
#
# Beispiel:
#
# Wenn Boss stark UND Angriffskraft unter 60:
# Ausgabe -> "Du verlierst den Kampf"
#
# Nutze:
# random
# nested ifs
# Operatoren

import random

boss = random.choice(["schwach", "mittel", "stark"])

print("Boss:", boss)

angriffskraft = int(input("Angriffskraft: "))

# Dein Code



# ============================================
# Aufgabe 13 — Schrein-Rätsel
# ============================================

# Erzeuge eine Zufallszahl zwischen 1 und 10.
#
# Der Spieler muss die richtige Schreinzahl raten.
#
# Wenn richtig:
# Ausgabe -> "Der Schrein ist gelöst"
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

schreinzahl = random.randint(1, 10)

tipp = int(input("Rate die Schreinzahl: "))

# Dein Code



# ============================================
# Aufgabe 14 — Die Heldenprüfung
# ============================================

# Frage:
# - Heldenname
# - Herzen
# - Rubine
# - Ist das Masterschwert vorhanden? (ja/nein)
#
# Wenn der Heldenname länger als 6 Zeichen:
# Ausgabe -> "Heldenname akzeptiert"
#
# Wenn Herzen >= 12:
#
#     Wenn Rubine >= 100:
#
#         Wenn Masterschwert == ja:
#         Ausgabe -> "Heldenprüfung bestanden"
#
#         Sonst:
#         Ausgabe -> "Masterschwert fehlt"
#
#     Sonst:
#     Ausgabe -> "Nicht genug Rubine"
#
# Sonst:
# Ausgabe -> "Nicht genug Herzen"
#
# Nutze:
# len()
# nested ifs
# Operatoren

heldenname = input("Heldenname: ")
herzen = int(input("Herzen: "))
rubine = int(input("Rubine: "))
masterschwert = input("Masterschwert vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 15 — Zelda-Finale
# ============================================

# Erstelle dein eigenes Mini-Zelda-Abenteuer.
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
# Der Held erkundet einen alten Tempel,
# sammelt Rubine, Schlüssel und Herzen,
# begegnet Gegnern und entscheidet,
# ob er bereit für den Bosskampf ist.