# # Zelda Abenteuer: Die Legende von Hyrule

# Du bist ein junger Held aus dem Königreich Hyrule.
# Eine dunkle Macht breitet sich im Land aus und Prinzessin Zelda braucht deine Hilfe.

# Deine Aufgabe:
# Erkunde Dungeons, finde legendäre Waffen, löse Rätsel und besiege Ganons dunkle Armee.

# Die Aufgaben werden immer schwieriger und bauen aufeinander auf.
# Am Ende hast du fast alle wichtigen Python-Grundlagen verwendet.


# ==================================================
# LEVEL 1 – DER HELD VON HYRULE
# ==================================================

# Ziel:
# - Variablen
# - print()
# - input()

# Aufgabe:
# Frage den Spieler:
# - nach seinem Namen
# - seinem Alter
# - seiner Klasse
#     - Schwertkämpfer
#     - Bogenschütze
#     - Magier

# Speichere alles in Variablen und begrüße den Spieler.

# Beispiel:
# Willkommen in Hyrule!
# Wie heißt du?
# > Link

# Sei gegrüßt Link.
# Dein Abenteuer beginnt.


# ==================================================
# LEVEL 2 – DAS TOR DES TEMPELS
# ==================================================

# Ziel:
# - if / elif / else

# Aufgabe:
# Der Spieler muss das richtige Passwort eingeben.

# Das Passwort lautet:
# triforce

# Bedingungen:
# - richtig → Das Tor öffnet sich
# - falsch → Zugang verweigert

# Bonus:
# Zähle Fehlversuche.


# ==================================================
# LEVEL 3 – DER KAMPF GEGEN DIE BOKBLINS
# ==================================================

# Ziel:
# - random

# Aufgabe:
# Ein Bokblin greift den Spieler an.

# Nutze:
# import random

# und:
# random.randint(1, 6)

# Der Spieler und der Gegner erhalten zufällige Angriffswerte.

# Regeln:
# - höhere Zahl gewinnt
# - gleich → Unentschieden
# - niedrigere Zahl verliert


# ==================================================
# LEVEL 4 – DIE ABENTEURERTASCHE
# ==================================================

# Ziel:
# - Listen

# Aufgabe:
# Erstelle ein Inventar:

# inventar = ["Holzschild", "Bogen", "Apfel"]

# Aufgaben:
# - Alle Gegenstände anzeigen
# - Neues Item hinzufügen
# - Item entfernen
# - Prüfen, ob „Bogen“ vorhanden ist

# Bonus:
# Lass den Spieler eigene Gegenstände hinzufügen.


# ==================================================
# LEVEL 5 – DER VERLORENE WALD
# ==================================================

# Ziel:
# - while-Schleifen

# Aufgabe:
# Der Spieler hat sich im Verlorenen Wald verirrt.

# Zeige immer wieder:

# 1 - Nach Norden gehen
# 2 - Nach Osten gehen
# 3 - Ausgang finden

# Die Schleife endet erst bei:
# 3


# ==================================================
# LEVEL 6 – DIE DUNGEON-KÄMPFE
# ==================================================

# Ziel:
# - for-Schleifen

# Aufgabe:
# Der Spieler kämpft gegen 5 Monster.

# Nutze:
# for i in range(5):

# Für jeden Kampf:
# - zufällige Stärke des Spielers
# - zufällige Stärke des Monsters

# Zeige:
# - Sieg
# - Niederlage
# - Unentschieden

# Bonus:
# Zähle Siege und Niederlagen.


# ==================================================
# LEVEL 7 – DIE SCHATZKAMMER
# ==================================================

# Ziel:
# - Dictionaries

# Aufgabe:
# Erstelle eine Waffenliste:

# waffen = {
#     "Master-Schwert": 100,
#     "Bogen der Helden": 70,
#     "Feuerstab": 60
# }

# Aufgaben:
# - Alle Waffen anzeigen
# - Stärke einer Waffe ausgeben
# - Neue Waffe hinzufügen
# - Waffe entfernen

# Bonus:
# Lass den Spieler eine Waffe auswählen.


# ==================================================
# LEVEL 8 – DIE KARTE VON HYRULE
# ==================================================

# Ziel:
# - Tupel

# Aufgabe:
# Speichere Orte als Koordinaten:

# hyrule = (20, 15)

# Aufgaben:
# - X- und Y-Koordinate ausgeben
# - Prüfen, ob der Spieler den Tempel erreicht hat

# Bonus:
# Nutze mehrere Orte:
# - Schloss Hyrule
# - Kakariko
# - Verlorener Wald
# - Wüsten-Tempel
# - Todesberg


# ==================================================
# LEVEL 9 – DIE RETTUNG VON HYRULE
# ==================================================

# Ziel:
# Kombiniere ALLES.

# Baue ein kleines Zelda-RPG mit:

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
# - Herzen (Leben)
# - Rubine
# - Inventar

# Es soll geben:

# Orte
# - mit Koordinaten

# Monster
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
# ENDGEGNER – GANON
# ==================================================

# Der Spieler kämpft gegen Ganon.

# Aktionen:
# - Angreifen
# - Heilen
# - Schild benutzen
# - Fliehen

# Ganon verursacht zufälligen Schaden.

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
# - verschiedene Waffen
# - Rätsel-System
# - Magiesystem
# - Begleiter-System


# ==================================================
# MINI-CHALLENGES
# ==================================================

# Kannst du folgendes einbauen?

# - Inventar mit maximal 10 Plätzen
# - seltene Waffen
# - geheime Schreine
# - 10 % Chance auf seltene Gegner
# - legendäre Items
# - Wetter-System
# - verschiedene Gegnerarten
# - Boss-Dungeons


# ==================================================
# ZIEL DES PROJEKTS
# ==================================================

# Wenn du alles schaffst, hast du:
# - fast alle Python-Grundlagen gelernt
# - ein großes Fantasy-Projekt gebaut
# - komplexe Logik trainiert
# - Schleifen und Bedingungen gemeistert
# - dein erstes großes RPG entwickelt