# # Pokémon Abenteuer: Die Reise zum Pokémon-Meister

# Du bist ein neuer Pokémon-Trainer.
# Professor Eich gibt dir dein erstes Pokémon und schickt dich auf eine große Reise durch die Region.

# Deine Aufgabe:
# Sammle Pokémon, besiege Arenaleiter, kämpfe gegen Team Rocket und werde Pokémon-Meister.

# Die Aufgaben werden immer schwieriger und bauen aufeinander auf.
# Am Ende hast du fast alle wichtigen Python-Grundlagen verwendet.


# ==================================================
# LEVEL 1 – DEIN ERSTES POKÉMON
# ==================================================

# Ziel:
# - Variablen
# - print()
# - input()

# Aufgabe:
# Frage den Spieler:
# - nach seinem Namen
# - seinem Alter
# - seinem Starter-Pokémon
#     - Bisasam
#     - Glumanda
#     - Schiggy

# Speichere alles in Variablen und begrüße den Spieler.

# Beispiel:
# Willkommen in der Pokémon-Welt!
# Wie heißt du?
# > Victor

# Hallo Victor!
# Du hast Glumanda gewählt.
# Deine Reise beginnt.


# ==================================================
# LEVEL 2 – DAS POKÉMON-CENTER
# ==================================================

# Ziel:
# - if / elif / else

# Aufgabe:
# Der Spieler möchte sein Pokémon heilen.

# Frage:
# „Möchtest du dein Pokémon heilen?“

# Bedingungen:
# - ja → Pokémon geheilt
# - nein → Reise geht weiter
# - andere Eingabe → Ungültige Eingabe

# Bonus:
# Lass den Spieler mehrfach antworten.


# ==================================================
# LEVEL 3 – DER WILDE KAMPF
# ==================================================

# Ziel:
# - random

# Aufgabe:
# Ein wildes Pokémon erscheint.

# Nutze:
# import random

# und:
# random.randint(1, 6)

# Der Spieler und das wilde Pokémon erhalten zufällige Angriffsstärken.

# Regeln:
# - höhere Zahl gewinnt
# - gleich → Unentschieden
# - niedrigere Zahl verliert


# ==================================================
# LEVEL 4 – DER TRAINER-RUCKSACK
# ==================================================

# Ziel:
# - Listen

# Aufgabe:
# Erstelle einen Rucksack:

# rucksack = ["Pokéball", "Trank", "Supertrank"]

# Aufgaben:
# - Alle Items anzeigen
# - Neues Item hinzufügen
# - Item entfernen
# - Prüfen, ob „Pokéball“ vorhanden ist

# Bonus:
# Lass den Spieler eigene Items hinzufügen.


# ==================================================
# LEVEL 5 – DER VERIRRTE WALD
# ==================================================

# Ziel:
# - while-Schleifen

# Aufgabe:
# Der Spieler hat sich im Vertania-Wald verlaufen.

# Zeige immer wieder:

# 1 - Nach links gehen
# 2 - Nach rechts gehen
# 3 - Ausgang gefunden

# Die Schleife endet erst bei:
# 3


# ==================================================
# LEVEL 6 – DIE TRAINERKÄMPFE
# ==================================================

# Ziel:
# - for-Schleifen

# Aufgabe:
# Der Spieler kämpft gegen 5 Trainer.

# Nutze:
# for i in range(5):

# Für jeden Kampf:
# - zufällige Stärke des Spielers
# - zufällige Stärke des Gegners

# Zeige:
# - Sieg
# - Niederlage
# - Unentschieden

# Bonus:
# Zähle Siege und Niederlagen.


# ==================================================
# LEVEL 7 – DER POKÉDEX
# ==================================================

# Ziel:
# - Dictionaries

# Aufgabe:
# Erstelle einen Pokédex:

# pokemon = {
#     "Pikachu": 55,
#     "Glurak": 100,
#     "Relaxo": 85
# }

# Aufgaben:
# - Alle Pokémon anzeigen
# - Stärke eines Pokémon ausgeben
# - Neues Pokémon hinzufügen
# - Pokémon entfernen

# Bonus:
# Lass den Spieler ein Pokémon auswählen.


# ==================================================
# LEVEL 8 – DIE KARTE DER REGION
# ==================================================

# Ziel:
# - Tupel

# Aufgabe:
# Speichere Orte als Koordinaten:

# arena = (15, 9)

# Aufgaben:
# - X- und Y-Koordinate ausgeben
# - Prüfen, ob der Spieler die Arena erreicht hat

# Bonus:
# Nutze mehrere Orte:
# - Alabastia
# - Vertania City
# - Azuria City
# - Lavandia
# - Pokémon Liga


# ==================================================
# LEVEL 9 – DIE POKÉMON-LIGA
# ==================================================

# Ziel:
# Kombiniere ALLES.

# Baue ein kleines Pokémon-RPG mit:

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
# - Pokémon-Team
# - Geld
# - Inventar

# Es soll geben:

# Orte
# - mit Koordinaten

# Pokémon
# - mit zufälliger Stärke

# PokéMarts
# - mit Items

# Pokédex
# - mit Dictionaries

# Kampfsystem
# - mit while-Schleife

# Mehrere Kämpfe
# - mit for-Schleife


# ==================================================
# ENDGEGNER – DER POKÉMON-MEISTER
# ==================================================

# Der Spieler kämpft gegen den Pokémon-Meister.

# Aktionen:
# - Angreifen
# - Heilen
# - Pokémon wechseln
# - Fliehen

# Der Gegner verursacht zufälligen Schaden.

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
# - mehrere Regionen
# - Levelsystem
# - Erfahrungspunkte
# - kritische Treffer
# - Fangsystem
# - verschiedene Pokémon-Typen
# - Entwicklungen
# - Arenasystem


# ==================================================
# MINI-CHALLENGES
# ==================================================

# Kannst du folgendes einbauen?

# - Inventar mit maximal 10 Plätzen
# - seltene Shiny-Pokémon
# - zufällige Events
# - Team Rocket Kämpfe
# - legendäre Pokémon
# - verschiedene Attacken
# - Status-Effekte
# - Pokémon entwickeln


# ==================================================
# ZIEL DES PROJEKTS
# ==================================================

# Wenn du alles schaffst, hast du:
# - fast alle Python-Grundlagen gelernt
# - ein großes Game-Projekt gebaut
# - komplexe Logik trainiert
# - Schleifen und Bedingungen gemeistert
# - dein erstes RPG entwickelt