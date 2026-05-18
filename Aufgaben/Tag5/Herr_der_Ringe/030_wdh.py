# # Herr der Ringe Abenteuer: Die Reise nach Mordor

# Du bist ein Held aus Mittelerde.
# Deine Aufgabe:
# Reise durch Mittelerde, sammle Verbündete, bekämpfe Orks und zerstöre den Einen Ring im Schicksalsberg.

# Die Aufgaben werden immer schwieriger und bauen aufeinander auf.
# Am Ende hast du fast alle wichtigen Python-Grundlagen verwendet.


# ==================================================
# LEVEL 1 – DER HELD AUS DEM AUENLAND
# ==================================================

# Ziel:
# - Variablen
# - print()
# - input()

# Aufgabe:
# Frage den Spieler:
# - nach seinem Namen
# - seiner Rasse
#     - Hobbit
#     - Mensch
#     - Elb
#     - Zwerg
# - seinem Alter

# Speichere alles in Variablen und begrüße den Spieler.

# Beispiel:
# Willkommen in Mittelerde!
# Wie lautet dein Name?
# > Frodo

# Sei gegrüßt Frodo der Hobbit.
# Deine Reise beginnt im Auenland.


# ==================================================
# LEVEL 2 – DAS TOR VON MORIA
# ==================================================

# Ziel:
# - if / elif / else

# Aufgabe:
# Der Spieler steht vor dem Tor von Moria.

# Das Passwort lautet:
# mellon

# Frage den Spieler nach dem Passwort.

# Bedingungen:
# - richtig → Das Tor öffnet sich
# - falsch → Das Tor bleibt verschlossen

# Bonus:
# Zähle die Fehlversuche.


# ==================================================
# LEVEL 3 – DER WÜRFEL DER ORKS
# ==================================================

# Ziel:
# - random

# Aufgabe:
# Ein Ork greift den Spieler an.

# Nutze:
# import random

# und:
# random.randint(1, 6)

# Der Spieler und der Ork würfeln.

# Regeln:
# - höhere Zahl gewinnt
# - gleich → Unentschieden
# - niedrigere Zahl verliert


# ==================================================
# LEVEL 4 – DAS INVENTAR DER GEFÄHRTEN
# ==================================================

# Ziel:
# - Listen

# Aufgabe:
# Erstelle ein Inventar:

# inventar = ["Lembas", "Dolch", "Ring"]

# Aufgaben:
# - Alle Gegenstände anzeigen
# - Neues Item hinzufügen
# - Item entfernen
# - Prüfen, ob „Ring“ vorhanden ist

# Bonus:
# Lass den Spieler eigene Gegenstände hinzufügen.


# ==================================================
# LEVEL 5 – DER WEG DURCH DEN DÜSTERWALD
# ==================================================

# Ziel:
# - while-Schleifen

# Aufgabe:
# Der Spieler ist im Düsterwald verirrt.

# Zeige immer wieder:

# 1 - Nach Norden gehen
# 2 - Nach Süden gehen
# 3 - Lager aufschlagen

# Die Schleife endet erst bei:
# 3


# ==================================================
# LEVEL 6 – DIE SCHLACHT GEGEN DIE ORKS
# ==================================================

# Ziel:
# - for-Schleifen

# Aufgabe:
# Der Spieler kämpft gegen 5 Orks.

# Nutze:
# for i in range(5):

# Für jeden Kampf:
# - zufällige Stärke des Spielers
# - zufällige Stärke des Orks

# Zeige:
# - Sieg
# - Niederlage
# - Unentschieden

# Bonus:
# Zähle Siege und Niederlagen.


# ==================================================
# LEVEL 7 – DIE BIBLIOTHEK VON BRUCHTAL
# ==================================================

# Ziel:
# - Dictionaries

# Aufgabe:
# Erstelle eine Zauber- oder Waffenliste:

# waffen = {
#     "Anduril": 100,
#     "Sting": 50,
#     "Elbenbogen": 70
# }

# Aufgaben:
# - Alle Waffen anzeigen
# - Stärke einer Waffe ausgeben
# - Neue Waffe hinzufügen
# - Waffe entfernen

# Bonus:
# Lass den Spieler eine Waffe wählen.


# ==================================================
# LEVEL 8 – DIE KARTE VON MITTELERDE
# ==================================================

# Ziel:
# - Tupel

# Aufgabe:
# Speichere Orte als Koordinaten:

# mordor = (10, 25)

# Aufgaben:
# - X- und Y-Koordinate ausgeben
# - Prüfen, ob der Spieler Mordor erreicht hat

# Bonus:
# Nutze mehrere Orte:
# - Auenland
# - Bruchtal
# - Moria
# - Gondor
# - Mordor


# ==================================================
# LEVEL 9 – DIE REISE DER GEFÄHRTEN
# ==================================================

# Ziel:
# Kombiniere ALLES.

# Baue ein kleines Herr-der-Ringe-RPG mit:

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

# Der Spieler soll besitzen:
# - Name
# - Lebenspunkte
# - Gold
# - Inventar

# Es soll geben:

# Orte
# - mit Koordinaten

# Orks
# - mit zufälliger Stärke

# Händler
# - mit Gegenständen

# Waffen
# - im Dictionary

# Kampfsystem
# - mit while-Schleife

# Mehrere Kämpfe
# - mit for-Schleife


# ==================================================
# ENDGEGNER – SAURONS AUGE
# ==================================================

# Der Spieler kämpft gegen Saurons dunkle Macht.

# Aktionen:
# - Angreifen
# - Heilen
# - Fliehen

# Sauron verursacht zufälligen Schaden.

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
# - Speicherstände
# - mehrere Maps
# - Levelsystem
# - Erfahrungspunkte
# - kritische Treffer
# - Händler
# - verschiedene Waffen
# - Begleiter-System
# - Magiesystem


# ==================================================
# MINI-CHALLENGES
# ==================================================

# Kannst du folgendes einbauen?

# - Inventar mit maximal 10 Plätzen
# - seltene Waffen
# - geheime Höhlen
# - 10 % Chance auf einen Nazgûl
# - legendäre Items
# - Zufallsevents
# - verschiedene Gegnerarten


# ==================================================
# ZIEL DES PROJEKTS
# ==================================================

# Wenn du alles schaffst, hast du:
# - fast alle Python-Grundlagen gelernt
# - ein großes Fantasy-Projekt gebaut
# - komplexe Logik trainiert
# - Schleifen und Bedingungen gemeistert
# - dein erstes großes RPG entwickelt