# # Tierheim Abenteuer: Rettung der Pfoteninsel

# Du arbeitest in einem Tierheim namens „Pfoteninsel“.
# Jeden Tag kommen neue Tiere an, Besucher möchten Tiere adoptieren und das Tierheim muss organisiert werden.

# Deine Aufgabe:
# Versorge Tiere, verwalte das Tierheim und finde für alle Tiere ein neues Zuhause.

# Die Aufgaben werden immer schwieriger und bauen aufeinander auf.
# Am Ende hast du fast alle wichtigen Python-Grundlagen verwendet.


# ==================================================
# LEVEL 1 – DAS ERSTE TIER
# ==================================================

# Ziel:
# - Variablen
# - print()
# - input()

# Aufgabe:
# Frage den Nutzer:
# - nach seinem Namen
# - seinem Alter
# - seinem Lieblingstier
#     - Hund
#     - Katze
#     - Kaninchen
#     - Vogel

# Speichere alles in Variablen und begrüße den Spieler.

# Beispiel:
# Willkommen im Tierheim Pfoteninsel!
# Wie heißt du?
# > Victor

# Hallo Victor!
# Heute kümmerst du dich um Hunde.


# ==================================================
# LEVEL 2 – DIE ADOPTION
# ==================================================

# Ziel:
# - if / elif / else

# Aufgabe:
# Ein Besucher möchte ein Tier adoptieren.

# Frage:
# „Ist das Tier geimpft?“

# Bedingungen:
# - ja → Adoption erlaubt
# - nein → Adoption nicht erlaubt
# - andere Eingabe → Ungültige Eingabe

# Bonus:
# Prüfe mehrere Tiere hintereinander.


# ==================================================
# LEVEL 3 – DAS ZUFALLSTIER
# ==================================================

# Ziel:
# - random

# Aufgabe:
# Jeden Tag kommt zufällig ein neues Tier ins Tierheim.

# Nutze:
# import random

# und:
# random.randint(1, 4)

# Beispiel:
# 1 → Hund
# 2 → Katze
# 3 → Kaninchen
# 4 → Vogel

# Zeige an, welches Tier angekommen ist.


# ==================================================
# LEVEL 4 – DAS FUTTERLAGER
# ==================================================

# Ziel:
# - Listen

# Aufgabe:
# Erstelle eine Liste:

# futter = ["Hundefutter", "Katzenfutter", "Karotten"]

# Aufgaben:
# - Alle Futtersorten anzeigen
# - Neues Futter hinzufügen
# - Futter entfernen
# - Prüfen, ob „Katzenfutter“ vorhanden ist

# Bonus:
# Lass den Spieler neue Futtersorten hinzufügen.


# ==================================================
# LEVEL 5 – DIE TÄGLICHE ROUTINE
# ==================================================

# Ziel:
# - while-Schleifen

# Aufgabe:
# Das Tierheim bleibt geöffnet bis Feierabend.

# Zeige immer wieder:

# 1 - Tiere füttern
# 2 - Käfig reinigen
# 3 - Feierabend machen

# Die Schleife endet erst bei:
# 3


# ==================================================
# LEVEL 6 – DIE TIERKONTROLLE
# ==================================================

# Ziel:
# - for-Schleifen

# Aufgabe:
# Überprüfe 5 Tiere.

# Nutze:
# for i in range(5):

# Für jedes Tier:
# - zufälliger Gesundheitswert
# - zufällige Stimmung

# Zeige:
# - Gesund
# - Müde
# - Braucht Hilfe

# Bonus:
# Zähle gesunde Tiere.


# ==================================================
# LEVEL 7 – DIE TIERDATENBANK
# ==================================================

# Ziel:
# - Dictionaries

# Aufgabe:
# Erstelle eine Tierdatenbank:

# tiere = {
#     "Bello": "Hund",
#     "Minka": "Katze",
#     "Hoppel": "Kaninchen"
# }

# Aufgaben:
# - Alle Tiere anzeigen
# - Tierart ausgeben
# - Neues Tier hinzufügen
# - Tier entfernen

# Bonus:
# Lass den Spieler nach einem Tier suchen.


# ==================================================
# LEVEL 8 – DIE KARTE DES TIERHEIMS
# ==================================================

# Ziel:
# - Tupel

# Aufgabe:
# Speichere Orte als Koordinaten:

# hundebereich = (5, 2)

# Aufgaben:
# - X- und Y-Koordinate ausgeben
# - Prüfen, ob der Spieler den richtigen Bereich gefunden hat

# Bonus:
# Nutze mehrere Bereiche:
# - Hundehaus
# - Katzenhaus
# - Vogelraum
# - Lager
# - Büro


# ==================================================
# LEVEL 9 – DAS GROSSE TIERHEIM-SYSTEM
# ==================================================

# Ziel:
# Kombiniere ALLES.

# Baue ein kleines Tierheim-Management-Spiel mit:

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
# - Energie
# - Geld
# - Inventar

# Es soll geben:

# Tiere
# - mit Namen und Arten

# Bereiche
# - mit Koordinaten

# Lager
# - mit Futterlisten

# Datenbank
# - mit Dictionaries

# Tägliche Aufgaben
# - mit while-Schleife

# Mehrere Tierprüfungen
# - mit for-Schleife


# ==================================================
# ENDGEGNER – DIE TIERHEIM-KRISE
# ==================================================

# Das Tierheim ist überfüllt und es fehlt Futter.

# Aktionen:
# - Tiere versorgen
# - Spenden sammeln
# - Tierarzt rufen
# - Lager organisieren

# Die Krise verursacht zufällige Probleme.

# Nutze:
# if / elif / else

# Das Spiel läuft solange:
# while tierheim_offen == True


# ==================================================
# ULTRA-BONUS (SCHWER)
# ==================================================

# Baue zusätzlich:
# - Funktionen
# - Klassen
# - Speicherstände
# - mehrere Tierarten
# - Levelsystem
# - Erfahrungspunkte
# - Shopsystem
# - Tierarzt-System
# - Mitarbeiter-System
# - Adoptionssystem


# ==================================================
# MINI-CHALLENGES
# ==================================================

# Kannst du folgendes einbauen?

# - Inventar mit maximal 10 Plätzen
# - seltene Tiere
# - zufällige Events
# - Notfälle
# - verschiedene Tiercharaktere
# - Adoptionen mit Zufallschance
# - Spendensystem
# - Wettereffekte


# ==================================================
# ZIEL DES PROJEKTS
# ==================================================

# Wenn du alles schaffst, hast du:
# - fast alle Python-Grundlagen gelernt
# - ein großes Praxisprojekt gebaut
# - komplexe Logik trainiert
# - Schleifen und Bedingungen gemeistert
# - dein erstes Management-Spiel entwickelt