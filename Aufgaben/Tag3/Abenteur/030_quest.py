# ============================================
# Abenteuer-Aufgabenreihe Python
# Von leicht -> schwer
# ============================================


# ============================================
# Aufgabe 1 — Der Name des Helden
# ============================================

# Frage den Spielernamen ab.
#
# Wenn der Name länger als 5 Zeichen ist:
# Ausgabe -> "Mächtiger Name"
#
# Sonst:
# Ausgabe -> "Kurzer Name"
#
# Nutze:
# input()
# if / else
# len()

name = input("Name deines Helden: ")

# Dein Code



# ============================================
# Aufgabe 2 — Die Schatztruhe
# ============================================

# Frage nach der Anzahl der Goldmünzen.
#
# Ab 100:
# Ausgabe -> "Du bist reich"
#
# Sonst:
# Ausgabe -> "Du brauchst mehr Gold"
#
# Nutze:
# if / else
# Operatoren

gold = int(input("Goldmünzen: "))

# Dein Code



# ============================================
# Aufgabe 3 — Die Brücke
# ============================================

# Frage nach dem Level des Spielers.
#
# Unter 10:
# Ausgabe -> "Die Brücke ist gesperrt"
#
# Zwischen 10 und 20:
# Ausgabe -> "Du darfst passieren"
#
# Über 20:
# Ausgabe -> "Die Wachen begrüßen dich"
#
# Nutze:
# if / elif / else

level = int(input("Level: "))

# Dein Code



# ============================================
# Aufgabe 4 — Das magische Passwort
# ============================================

# Frage nach einem geheimen Wort.
#
# Wenn das Wort "drache" ist:
# Ausgabe -> "Geheime Tür geöffnet"
#
# Sonst:
# Ausgabe -> "Nichts passiert"
#
# Nutze:
# if / else

wort = input("Geheimes Wort: ")

# Dein Code



# ============================================
# Aufgabe 5 — Der Heiltrank
# ============================================

# Frage nach der Lebensenergie.
#
# Unter 30:
# Ausgabe -> "Heiltrank benutzen"
#
# Sonst:
# Ausgabe -> "Weiterkämpfen"
#
# Nutze:
# Operatoren
# if / else

leben = int(input("Lebensenergie: "))

# Dein Code



# ============================================
# Aufgabe 6 — Das Würfelspiel
# ============================================

# Nutze random.
#
# Der Spieler würfelt eine Zahl zwischen 1 und 6.
#
# Wenn die Zahl 6 ist:
# Ausgabe -> "Kritischer Treffer"
#
# Sonst:
# Ausgabe -> "Normaler Angriff"
#
# Nutze:
# random
# if / else

import random

wuerfel = random.randint(1, 6)

print(wuerfel)

# Dein Code



# ============================================
# Aufgabe 7 — Die alte Tür
# ============================================

# Frage:
# - Hat der Spieler einen Schlüssel? (ja/nein)
#
# Wenn ja:
# Ausgabe -> "Die Tür öffnet sich"
#
# Sonst:
# Ausgabe -> "Die Tür bleibt verschlossen"

schluessel = input("Hast du einen Schlüssel? ")

# Dein Code



# ============================================
# Aufgabe 8 — Der Dungeon-Wächter
# ============================================

# Frage:
# - Level
# - Hat der Spieler ein Schwert? (ja/nein)
#
# Wenn Level >= 20:
#
#     Wenn Schwert == ja:
#     Ausgabe -> "Du besiegst den Wächter"
#
#     Sonst:
#     Ausgabe -> "Du brauchst eine Waffe"
#
# Sonst:
# Ausgabe -> "Du bist zu schwach"
#
# Nutze:
# nested ifs

level = int(input("Level: "))
schwert = input("Schwert vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 9 — Der Zufallsgegner
# ============================================

# Nutze random.
#
# Zufällig erscheint:
# - Goblin
# - Skelett
# - Drache
#
# Je nach Gegner:
# unterschiedliche Ausgabe
#
# Nutze:
# random
# if / elif / else

import random

gegner = random.choice(["Goblin", "Skelett", "Drache"])

print(gegner)

# Dein Code



# ============================================
# Aufgabe 10 — Das magische Artefakt
# ============================================

# Frage nach dem Namen eines Artefakts.
#
# Wenn der Name länger als 8 Zeichen ist:
# Ausgabe -> "Legendäres Artefakt"
#
# Wenn der Name länger als 4 Zeichen ist:
# Ausgabe -> "Seltenes Artefakt"
#
# Sonst:
# Ausgabe -> "Gewöhnliches Artefakt"
#
# Nutze:
# len()
# if / elif / else

artefakt = input("Artefaktname: ")

# Dein Code



# ============================================
# Aufgabe 11 — Der verbotene Wald
# ============================================

# Frage:
# - Level
# - Anzahl Heiltränke
#
# Wenn Level >= 15:
#
#     Wenn Heiltränke >= 3:
#     Ausgabe -> "Du betrittst sicher den Wald"
#
#     Sonst:
#     Ausgabe -> "Du solltest mehr Heiltränke mitnehmen"
#
# Sonst:
# Ausgabe -> "Der Wald ist zu gefährlich"
#
# Nutze:
# nested ifs
# Operatoren

level = int(input("Level: "))
heiltraenke = int(input("Heiltränke: "))

# Dein Code



# ============================================
# Aufgabe 12 — Der Bosskampf
# ============================================

# Nutze random.
#
# Der Boss hat zufällig:
# - schwach
# - mittel
# - stark
#
# Frage zusätzlich nach der Stärke des Spielers.
#
# Je nach Kombination:
# unterschiedliche Ergebnisse
#
# Beispiel:
#
# Wenn Boss stark UND Stärke unter 50:
# Ausgabe -> "Du wurdest besiegt"
#
# Nutze:
# random
# nested ifs
# Operatoren

import random

boss = random.choice(["schwach", "mittel", "stark"])

print("Boss:", boss)

staerke = int(input("Deine Stärke: "))

# Dein Code



# ============================================
# Aufgabe 13 — Das Rätsel der Zahlen
# ============================================

# Erzeuge eine Zufallszahl zwischen 1 und 10.
#
# Der Spieler muss raten.
#
# Wenn richtig:
# Ausgabe -> "Richtig geraten"
#
# Sonst:
# Ausgabe -> "Falsch geraten"
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

zahl = random.randint(1, 10)

tipp = int(input("Rate die Zahl: "))

# Dein Code



# ============================================
# Aufgabe 14 — Die Heldenprüfung
# ============================================

# Frage:
# - Name
# - Level
# - Gold
# - Hat der Spieler eine Rüstung? (ja/nein)
#
# Wenn der Name länger als 5 Zeichen:
# Ausgabe -> "Beeindruckender Name"
#
# Wenn Level >= 20:
#
#     Wenn Gold >= 100:
#
#         Wenn Rüstung == ja:
#         Ausgabe -> "Du bestehst die Heldenprüfung"
#
#         Sonst:
#         Ausgabe -> "Du brauchst besseren Schutz"
#
#     Sonst:
#     Ausgabe -> "Nicht genug Gold"
#
# Sonst:
# Ausgabe -> "Du bist noch nicht bereit"
#
# Nutze:
# len()
# nested ifs
# Operatoren

name = input("Name: ")
level = int(input("Level: "))
gold = int(input("Gold: "))
ruestung = input("Rüstung vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 15 — Das Abenteuer-Finale
# ============================================

# Erstelle dein eigenes Mini-Abenteuer.
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
# Der Spieler erkundet eine gefährliche Ruine
# und muss Entscheidungen treffen.