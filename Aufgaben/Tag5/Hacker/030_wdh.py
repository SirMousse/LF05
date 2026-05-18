# # Hacker-Abenteuer: Operation ShadowByte

# Du bist ein Elite-Hacker der geheimen Gruppe ShadowByte.
# Deine Mission:
# Dringe in verschiedene Systeme ein, löse Sicherheitsrätsel und besiege die KI „ZER0“.

# Die Aufgaben werden immer schwieriger und bauen aufeinander auf.
# Am Ende hast du fast alle wichtigen Python-Grundlagen verwendet.


# ==================================================
# LEVEL 1 – LOGIN TERMINAL
# ==================================================

# Ziel:
# - Variablen
# - print()
# - input()

# Aufgabe:
# Frage den Nutzer:
# - nach seinem Hacker-Namen
# - seinem Alter
# - seinem Spezialgebiet
#     - Netzwerk
#     - Malware
#     - Kryptographie

# Speichere alles in Variablen und begrüße den Spieler.

# Beispiel:
# [ SYSTEM START ]

# Bitte Hacker-Namen eingeben:
# > ShadowFox

# Willkommen ShadowFox.
# Zugriff auf das ShadowByte-Netzwerk gewährt.


# ==================================================
# LEVEL 2 – PASSWORT-KNACKER
# ==================================================

# Ziel:
# - if / elif / else
# - Vergleiche

# Aufgabe:
# Der Spieler muss ein Passwort erraten.

# Das richtige Passwort ist:
# shadow123

# Bedingungen:
# - richtig → Zugriff gewährt
# - falsch → Zugriff verweigert

# Bonus:
# - Zähle die Fehlversuche
# - Sperre den Account nach 3 falschen Eingaben


# ==================================================
# LEVEL 3 – DER ZAHLENCODE
# ==================================================

# Ziel:
# - random
# - Zahlen vergleichen

# Aufgabe:
# Ein Sicherheitssystem generiert einen zufälligen Zahlencode zwischen 1 und 10.

# Nutze:
# import random

# und:
# random.randint(1, 10)

# Der Spieler muss den Code erraten.

# Hinweise:
# - „Code höher“
# - „Code niedriger“


# ==================================================
# LEVEL 4 – DAS DARKNET-INVENTAR
# ==================================================

# Ziel:
# - Listen

# Aufgabe:
# Erstelle ein Hacker-Inventar:

# tools = ["Keylogger", "VPN", "USB-Exploit"]

# Aufgaben:
# - Alle Tools anzeigen
# - Neues Tool hinzufügen
# - Tool entfernen
# - Prüfen, ob „VPN“ vorhanden ist

# Bonus:
# Lass den Spieler eigene Tools hinzufügen.


# ==================================================
# LEVEL 5 – DIE FIREWALL-SCHLEIFE
# ==================================================

# Ziel:
# - while-Schleifen

# Aufgabe:
# Der Spieler versucht eine Firewall zu umgehen.

# Zeige immer wieder:

# 1 - Port scannen
# 2 - Passwort brute-forcen
# 3 - Verbindung trennen

# Die Schleife endet erst bei:
# 3


# ==================================================
# LEVEL 6 – SERVER-ANGRIFF
# ==================================================

# Ziel:
# - for-Schleifen

# Aufgabe:
# Der Spieler greift 5 Server an.

# Nutze:
# for i in range(5):

# Für jeden Server:
# - zufällige Sicherheitsstufe
# - zufällige Hacker-Stärke

# Zeige:
# - Hack erfolgreich
# - Hack fehlgeschlagen

# Bonus:
# Zähle erfolgreiche Angriffe.


# ==================================================
# LEVEL 7 – DIE DATENBANK DER EXPLOITS
# ==================================================

# Ziel:
# - Dictionaries

# Aufgabe:
# Erstelle eine Exploit-Datenbank:

# exploits = {
#     "SQL Injection": 70,
#     "DDoS": 50,
#     "Zero-Day": 100
# }

# Aufgaben:
# - Alle Exploits anzeigen
# - Stärke eines Exploits ausgeben
# - Neuen Exploit hinzufügen
# - Exploit löschen

# Bonus:
# Lass den Spieler einen Exploit auswählen.


# ==================================================
# LEVEL 8 – DIE GPS-KOORDINATEN
# ==================================================

# Ziel:
# - Tupel

# Aufgabe:
# Speichere Server-Koordinaten:

# server = (52, 13)

# Aufgaben:
# - X- und Y-Koordinate ausgeben
# - Prüfen, ob der Spieler den richtigen Server gefunden hat

# Bonus:
# Nutze mehrere Server-Koordinaten.


# ==================================================
# LEVEL 9 – DAS SHADOWBYTE-NETZWERK
# ==================================================

# Ziel:
# Kombiniere ALLES.

# Baue ein kleines Hacker-Spiel mit:

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
# - Hacker-Name
# - Energie
# - Kryptowährung
# - Inventar

# Es soll geben:

# Server
# - mit Koordinaten

# Firewalls
# - mit zufälliger Stärke

# Black-Market
# - mit Tool-Listen

# Exploit-System
# - mit Dictionaries

# Hack-Kämpfe
# - mit while-Schleife

# Mehrere Angriffe
# - mit for-Schleife


# ==================================================
# ENDGEGNER – DIE KI "ZER0"
# ==================================================

# Der Spieler kämpft gegen die Sicherheits-KI „ZER0“.

# Aktionen:
# - Angriff
# - System reparieren
# - Fliehen

# Die KI verursacht zufälligen Schaden.

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
# - Login-System
# - Datei-Speicherung
# - Verschlüsselung
# - mehrere Maps
# - Levelsystem
# - Erfahrungspunkte
# - kritische Angriffe
# - Shopsystem
# - verschiedene Hackerklassen


# ==================================================
# MINI-CHALLENGES
# ==================================================

# Kannst du folgendes einbauen?

# - Inventar mit maximal 10 Slots
# - seltene Exploits
# - zufällige Serverevents
# - geheime Backdoors
# - 10 % Chance auf Adminzugriff
# - seltene Elite-Firewalls
# - Kryptowährungen als Belohnung


# ==================================================
# ZIEL DES PROJEKTS
# ==================================================

# Wenn du alles schaffst, hast du:
# - fast alle Python-Grundlagen gelernt
# - ein großes Praxisprojekt gebaut
# - Schleifen und Bedingungen trainiert
# - komplexe Logik verwendet
# - dein erstes großes Konsolen-Spiel entwickelt