# # Zombie Abenteuer: Die letzte Stadt

# Die Welt wurde von einem Zombie-Virus zerstört.
# Nur wenige Menschen haben überlebt.

# Du bist einer der letzten Überlebenden.
# Deine Aufgabe:
# Finde Nahrung, sammle Waffen, rette andere Überlebende und überlebe die Zombie-Apokalypse.

# Die Aufgaben werden immer schwieriger und bauen aufeinander auf.
# Am Ende hast du fast alle wichtigen Python-Grundlagen verwendet.


# ==================================================
# LEVEL 1 – DER ÜBERLEBENDE
# ==================================================

# Ziel:
# - Variablen
# - print()
# - input()

# Aufgabe:
# Frage den Spieler:
# - nach seinem Namen
# - seinem Alter
# - seiner Rolle
#     - Sanitäter
#     - Soldat
#     - Mechaniker
#     - Scout

# Speichere alles in Variablen und begrüße den Spieler.

# Beispiel:
# Willkommen in der letzten Stadt!
# Wie heißt du?
# > Alex

# Hallo Alex.
# Du bist jetzt Teil der Überlebenden.


# ==================================================
# LEVEL 2 – DAS SICHERE HAUS
# ==================================================

# Ziel:
# - if / elif / else

# Aufgabe:
# Der Spieler versucht ein sicheres Haus zu betreten.

# Das Passwort lautet:
# survive

# Bedingungen:
# - richtig → Tür geöffnet
# - falsch → Zugang verweigert

# Bonus:
# Zähle Fehlversuche.


# ==================================================
# LEVEL 3 – DER ERSTE ZOMBIE
# ==================================================

# Ziel:
# - random

# Aufgabe:
# Ein Zombie greift den Spieler an.

# Nutze:
# import random

# und:
# random.randint(1, 6)

# Der Spieler und der Zombie erhalten zufällige Angriffswerte.

# Regeln:
# - höhere Zahl gewinnt
# - gleich → Unentschieden
# - niedrigere Zahl verliert


# ==================================================
# LEVEL 4 – DER ÜBERLEBENSRUCKSACK
# ==================================================

# Ziel:
# - Listen

# Aufgabe:
# Erstelle ein Inventar:

# inventar = ["Wasser", "Verbandskasten", "Messer"]

# Aufgaben:
# - Alle Gegenstände anzeigen
# - Neues Item hinzufügen
# - Item entfernen
# - Prüfen, ob „Wasser“ vorhanden ist

# Bonus:
# Lass den Spieler eigene Gegenstände hinzufügen.


# ==================================================
# LEVEL 5 – DIE NACHTWACHE
# ==================================================

# Ziel:
# - while-Schleifen

# Aufgabe:
# Der Spieler hält Nachtwache.

# Zeige immer wieder:

# 1 - Umgebung prüfen
# 2 - Barrikade reparieren
# 3 - Schlafen gehen

# Die Schleife endet erst bei:
# 3


# ==================================================
# LEVEL 6 – DIE ZOMBIEWELLEN
# ==================================================

# Ziel:
# - for-Schleifen

# Aufgabe:
# Der Spieler kämpft gegen 5 Zombies.

# Nutze:
# for i in range(5):

# Für jeden Kampf:
# - zufällige Stärke des Spielers
# - zufällige Stärke des Zombies

# Zeige:
# - Sieg
# - Niederlage
# - Unentschieden

# Bonus:
# Zähle besiegte Zombies.


# ==================================================
# LEVEL 7 – DAS ÜBERLEBENDENREGISTER
# ==================================================

# Ziel:
# - Dictionaries

# Aufgabe:
# Erstelle eine Überlebendenliste:

# ueberlebende = {
#     "Mia": "Sanitäterin",
#     "Jake": "Soldat",
#     "Lena": "Mechanikerin"
# }

# Aufgaben:
# - Alle Überlebenden anzeigen
# - Rolle einer Person ausgeben
# - Neue Person hinzufügen
# - Person entfernen

# Bonus:
# Lass den Spieler nach Überlebenden suchen.


# ==================================================
# LEVEL 8 – DIE KARTE DER STADT
# ==================================================

# Ziel:
# - Tupel

# Aufgabe:
# Speichere Orte als Koordinaten:

# krankenhaus = (8, 14)

# Aufgaben:
# - X- und Y-Koordinate ausgeben
# - Prüfen, ob der Spieler den Ort erreicht hat

# Bonus:
# Nutze mehrere Orte:
# - Krankenhaus
# - Supermarkt
# - Polizeistation
# - Bunker
# - Tankstelle


# ==================================================
# LEVEL 9 – DIE LETZTE STADT
# ==================================================

# Ziel:
# Kombiniere ALLES.

# Baue ein kleines Zombie-Survival-Spiel mit:

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
# - Leben
# - Nahrung
# - Inventar

# Es soll geben:

# Orte
# - mit Koordinaten

# Zombies
# - mit zufälliger Stärke

# Händler oder Überlebende
# - mit Gegenständen

# Waffen
# - im Dictionary

# Kampfsystem
# - mit while-Schleife

# Mehrere Kämpfe
# - mit for-Schleife


# ==================================================
# ENDGEGNER – DER MUTANT
# ==================================================

# Der Spieler kämpft gegen einen riesigen Mutanten-Zombie.

# Aktionen:
# - Angreifen
# - Heilen
# - Fliehen
# - Barrikade nutzen

# Der Mutant verursacht zufälligen Schaden.

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
# - Tag/Nacht-System
# - Levelsystem
# - Erfahrungspunkte
# - kritische Treffer
# - Crafting-System
# - Hunger-System
# - verschiedene Waffen


# ==================================================
# MINI-CHALLENGES
# ==================================================

# Kannst du folgendes einbauen?

# - Inventar mit maximal 10 Plätzen
# - seltene Waffen
# - zufällige Zombie-Arten
# - geheime Bunker
# - Wetter-System
# - Fahrzeug-System
# - Munition
# - verschiedene Überlebende


# ==================================================
# ZIEL DES PROJEKTS
# ==================================================

# Wenn du alles schaffst, hast du:
# - fast alle Python-Grundlagen gelernt
# - ein großes Survival-Projekt gebaut
# - komplexe Logik trainiert
# - Schleifen und Bedingungen gemeistert
# - dein erstes großes Survival-Spiel entwickelt