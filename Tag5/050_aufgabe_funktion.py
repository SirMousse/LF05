# # Abenteueraufgabe: Die verlorene Krone von Pythonia

# Du bist der Entwickler eines kleinen Text-Adventures.
# Der Spieler reist durch das Königreich Pythonia, um die verlorene Krone zurückzubringen.

# Die Aufgaben werden immer schwieriger und bauen aufeinander auf.
# Am Ende hast du fast alle wichtigen Python-Grundlagen verwendet.


# ==================================================
# LEVEL 1 – DER HELD ERWACHT
# ==================================================

# Ziel:
# - Variablen
# - print()
# - input()

# Aufgabe:
# Frage den Spieler:
# - nach seinem Namen
# - seinem Alter
# - seiner Klasse (Magier, Krieger oder Dieb)

# Speichere alles in Variablen und gib eine Begrüßung aus.

# Beispiel:
# Willkommen in Pythonia!
# Wie heißt du?
# > Victor

# Hallo Victor der Magier!
# Dein Abenteuer beginnt...


# ==================================================
# LEVEL 2 – DIE SCHATZTRUHE
# ==================================================

# Ziel:
# - if / elif / else
# - Zahlen vergleichen

# Aufgabe:
# Der Spieler findet eine Schatztruhe mit einem Zahlenschloss.

# Die richtige Zahl ist:
# 7

# Der Spieler darf eine Zahl eingeben.

# Bedingungen:
# - richtige Zahl → Schatz gefunden
# - zu klein → „Die Zahl ist größer“
# - zu groß → „Die Zahl ist kleiner“

# Zusatz:
# Zähle die Versuche mit einer Variable.


# ==================================================
# LEVEL 3 – DER WÜRFEL DES SCHICKSALS
# ==================================================

# Ziel:
# - random
# - einfache Spielmechanik

# Aufgabe:
# Nutze:
# import random

# Erstelle:
# random.randint(1, 6)

# Der Spieler würfelt gegen ein Monster.

# Regeln:
# - Spielerwürfel > Monsterwürfel → Sieg
# - gleich → Unentschieden
# - kleiner → Niederlage


# ==================================================
# LEVEL 4 – DAS HEILTRANK-LAGER
# ==================================================

# Ziel:
# - Listen

# Aufgabe:
# Erstelle eine Inventarliste:

# inventar = ["Schwert", "Apfel", "Heiltrank"]

# Aufgaben:
# - Gib alle Gegenstände aus
# - Füge einen neuen Gegenstand hinzu
# - Entferne einen Gegenstand
# - Prüfe, ob „Heiltrank“ vorhanden ist

# Bonus:
# Lass den Spieler neue Items per input hinzufügen.


# ==================================================
# LEVEL 5 – DIE ENDLOSSCHLEIFE DES DUNGEONS
# ==================================================

# Ziel:
# - while-Schleifen

# Aufgabe:
# Der Spieler steckt in einem Dungeon fest.

# Zeige immer wieder:

# 1 - Nach links
# 2 - Nach rechts
# 3 - Ausgang suchen

# Die Schleife endet erst, wenn der Spieler:
# 3
# eingibt.


# ==================================================
# LEVEL 6 – DIE ARENA DER 5 MONSTER
# ==================================================

# Ziel:
# - for-Schleifen

# Aufgabe:
# Der Spieler kämpft gegen 5 Monster.

# Nutze:
# for

# Beispiel:
# for i in range(5):

# Für jeden Kampf:
# - zufällige Monsterstärke
# - zufällige Spielerstärke
# - Ergebnis anzeigen

# Bonus:
# Zähle Siege und Niederlagen.


# ==================================================
# LEVEL 7 – DIE BIBLIOTHEK DER ZAUBER
# ==================================================

# Ziel:
# - Dictionaries

# Aufgabe:
# Erstelle ein Zauberbuch:

# zauber = {
#     "Feuerball": 50,
#     "Eislanze": 40,
#     "Heilung": 30
# }

# Aufgaben:
# - Alle Zauber anzeigen
# - Schaden eines Zaubers ausgeben
# - Neuen Zauber hinzufügen
# - Zauber entfernen

# Bonus:
# Lass den Spieler einen Zauber auswählen.


# ==================================================
# LEVEL 8 – DIE ALTEN RUNEN
# ==================================================

# Ziel:
# - Tupel

# Aufgabe:
# Speichere Koordinaten eines Schatzes:

# schatz = (4, 7)

# Aufgaben:
# - X- und Y-Koordinate ausgeben
# - Prüfen, ob der Spieler die richtige Position erreicht

# Bonus:
# Nutze mehrere Tupel für verschiedene Orte.


# ==================================================
# LEVEL 9 – DAS GROSSE KÖNIGREICHSSYSTEM
# ==================================================

# Ziel:
# Kombiniere ALLES.

# Aufgabe:
# Baue ein kleines RPG-System mit:

# Pflichtfunktionen:
# - Variablen
# - input()
# - if / elif / else
# - while
# - for
# - random
# - Listen
# - Dictionaries
# - Tupel

# Der Spieler soll:
# - einen Namen besitzen
# - Lebenspunkte haben
# - Gold besitzen
# - ein Inventar besitzen

# Es soll geben:

# Städte
# - mit Koordinaten (Tupel)

# Gegner
# - mit zufälliger Stärke

# Händler
# - mit einer Item-Liste

# Zauber
# - im Dictionary

# Kampfsystem
# - mit while-Schleife

# Mehrere Kämpfe
# - mit for-Schleife


# ==================================================
# ENDGEGNER-LEVEL – DER DRACHENKÖNIG
# ==================================================

# Der Spieler kämpft gegen den Drachenkönig.

# Bedingungen:
# - zufälliger Schaden
# - Heiltränke
# - verschiedene Aktionen:
#     - Angriff
#     - Heilen
#     - Fliehen

# Nutze:
# if / elif / else

# Der Kampf läuft solange:
# while leben > 0


# ==================================================
# ULTRA-BONUS (SCHWER)
# ==================================================

# Baue zusätzlich:
# - Funktionen
# - Klassen
# - Speicherstände in Dateien
# - mehrere Maps
# - Levelsystem
# - Erfahrungspunkte
# - kritische Treffer
# - Shopsystem
# - mehrere Waffen
# - Gegner-KI


# ==================================================
# MINI-CHALLENGES
# ==================================================

# Kannst du folgendes einbauen?

# - Inventar mit maximal 10 Plätzen
# - Gegner droppen zufällige Items
# - Händlerpreise ändern sich zufällig
# - geheime Schatztruhe mit 10 % Chance
# - seltene Monster


# ==================================================
# ZIEL DES PROJEKTS
# ==================================================

# Wenn du alles schaffst, hast du:
# - fast alle Python-Grundlagen gelernt
# - ein richtiges kleines Spiel gebaut
# - sehr viel Praxis gesammelt