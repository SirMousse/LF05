# ============================================
# Pokemon-Aufgabenreihe Python
# Von leicht -> schwer
# ============================================


# ============================================
# Aufgabe 1 — Trainername prüfen
# ============================================

# Frage den Trainernamen ab.
#
# Wenn der Name länger als 6 Zeichen ist:
# Ausgabe -> "Starker Trainername"
#
# Sonst:
# Ausgabe -> "Kurzer Trainername"
#
# Nutze:
# input()
# if / else
# len()

trainername = input("Trainername: ")

# Dein Code



# ============================================
# Aufgabe 2 — Pokemon-Level
# ============================================

# Frage nach dem Level deines Pokemon.
#
# Ab Level 50:
# Ausgabe -> "Dein Pokemon ist sehr stark"
#
# Sonst:
# Ausgabe -> "Dein Pokemon muss noch trainieren"
#
# Nutze:
# if / else
# Operatoren

level = int(input("Pokemon-Level: "))

# Dein Code



# ============================================
# Aufgabe 3 — Orden prüfen
# ============================================

# Frage nach der Anzahl deiner Orden.
#
# Unter 4:
# Ausgabe -> "Du darfst noch nicht zur Liga"
#
# Zwischen 4 und 7:
# Ausgabe -> "Du darfst stärkere Arenen herausfordern"
#
# Ab 8:
# Ausgabe -> "Pokemon-Liga freigeschaltet"
#
# Nutze:
# if / elif / else

orden = int(input("Anzahl der Orden: "))

# Dein Code



# ============================================
# Aufgabe 4 — Geheimes Trainerpasswort
# ============================================

# Frage nach einem geheimen Passwort.
#
# Wenn das Passwort "pikachu" ist:
# Ausgabe -> "Geheimer Trainingsraum geöffnet"
#
# Sonst:
# Ausgabe -> "Zugang verweigert"
#
# Nutze:
# if / else

passwort = input("Geheimes Passwort: ")

# Dein Code



# ============================================
# Aufgabe 5 — KP prüfen
# ============================================

# Frage nach den KP deines Pokemon.
#
# Unter 30:
# Ausgabe -> "Pokemon braucht einen Trank"
#
# Sonst:
# Ausgabe -> "Pokemon kann weiterkämpfen"
#
# Nutze:
# Operatoren
# if / else

kp = int(input("KP deines Pokemon: "))

# Dein Code



# ============================================
# Aufgabe 6 — Zufälliger Fangversuch
# ============================================

# Nutze random.
#
# Der Fangversuch würfelt eine Zahl zwischen 1 und 6.
#
# Wenn die Zahl 6 ist:
# Ausgabe -> "Pokemon wurde gefangen"
#
# Sonst:
# Ausgabe -> "Pokemon ist ausgebrochen"
#
# Nutze:
# random
# if / else

import random

fangwurf = random.randint(1, 6)

print(fangwurf)

# Dein Code



# ============================================
# Aufgabe 7 — Pokeball vorhanden
# ============================================

# Frage:
# - Ist ein Pokeball vorhanden? (ja/nein)
#
# Wenn ja:
# Ausgabe -> "Du kannst ein Pokemon fangen"
#
# Sonst:
# Ausgabe -> "Du brauchst einen Pokeball"

pokeball = input("Pokeball vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 8 — Arena-Zugang
# ============================================

# Frage:
# - Anzahl der Orden
# - Ist dein Pokemon kampfbereit? (ja/nein)
#
# Wenn Orden >= 4:
#
#     Wenn kampfbereit == ja:
#     Ausgabe -> "Du darfst die Arena betreten"
#
#     Sonst:
#     Ausgabe -> "Dein Pokemon ist nicht kampfbereit"
#
# Sonst:
# Ausgabe -> "Du hast noch nicht genug Orden"
#
# Nutze:
# nested ifs

orden = int(input("Anzahl der Orden: "))
kampfbereit = input("Pokemon kampfbereit? ")

# Dein Code



# ============================================
# Aufgabe 9 — Zufällige Begegnung
# ============================================

# Nutze random.
#
# Zufällig erscheint:
# - Rattfratz
# - Glumanda
# - Relaxo
#
# Je nach Begegnung:
# unterschiedliche Ausgabe
#
# Nutze:
# random
# if / elif / else

import random

begegnung = random.choice(["Rattfratz", "Glumanda", "Relaxo"])

print(begegnung)

# Dein Code



# ============================================
# Aufgabe 10 — Pokemon-Name prüfen
# ============================================

# Frage nach dem Namen deines Pokemon.
#
# Wenn der Name länger als 10 Zeichen ist:
# Ausgabe -> "Legendärer Pokemon-Name"
#
# Wenn der Name länger als 5 Zeichen ist:
# Ausgabe -> "Starker Pokemon-Name"
#
# Sonst:
# Ausgabe -> "Kurzer Pokemon-Name"
#
# Nutze:
# len()
# if / elif / else

pokemon_name = input("Pokemon-Name: ")

# Dein Code



# ============================================
# Aufgabe 11 — Zugang zur Pokemon-Liga
# ============================================

# Frage:
# - Anzahl der Orden
# - Level deines stärksten Pokemon
#
# Wenn Orden >= 8:
#
#     Wenn Level >= 60:
#     Ausgabe -> "Du darfst die Pokemon-Liga betreten"
#
#     Sonst:
#     Ausgabe -> "Dein Pokemon-Level ist zu niedrig"
#
# Sonst:
# Ausgabe -> "Du brauchst alle 8 Orden"
#
# Nutze:
# nested ifs
# Operatoren

orden = int(input("Anzahl der Orden: "))
level = int(input("Level deines stärksten Pokemon: "))

# Dein Code



# ============================================
# Aufgabe 12 — Kampf gegen Arenaleiter
# ============================================

# Nutze random.
#
# Der Arenaleiter ist zufällig:
# - schwach
# - mittel
# - stark
#
# Frage zusätzlich nach deinem Pokemon-Level.
#
# Je nach Kombination:
# unterschiedliche Ergebnisse
#
# Beispiel:
#
# Wenn Arenaleiter stark UND Pokemon-Level unter 50:
# Ausgabe -> "Du verlierst den Kampf"
#
# Nutze:
# random
# nested ifs
# Operatoren

import random

arenaleiter = random.choice(["schwach", "mittel", "stark"])

print("Arenaleiter:", arenaleiter)

level = int(input("Pokemon-Level: "))

# Dein Code



# ============================================
# Aufgabe 13 — Pokeball-Zahlenrätsel
# ============================================

# Erzeuge eine Zufallszahl zwischen 1 und 10.
#
# Der Trainer muss die richtige Pokeball-Nummer raten.
#
# Wenn richtig:
# Ausgabe -> "Seltener Pokeball gefunden"
#
# Sonst:
# Ausgabe -> "Falscher Pokeball"
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

pokeball_nummer = random.randint(1, 10)

tipp = int(input("Rate die Pokeball-Nummer: "))

# Dein Code



# ============================================
# Aufgabe 14 — Die Trainerprüfung
# ============================================

# Frage:
# - Trainername
# - Orden
# - Pokemon-Level
# - Ist ein Pokeball vorhanden? (ja/nein)
#
# Wenn der Trainername länger als 6 Zeichen:
# Ausgabe -> "Trainername akzeptiert"
#
# Wenn Orden >= 8:
#
#     Wenn Pokemon-Level >= 60:
#
#         Wenn Pokeball == ja:
#         Ausgabe -> "Trainerprüfung bestanden"
#
#         Sonst:
#         Ausgabe -> "Pokeball fehlt"
#
#     Sonst:
#     Ausgabe -> "Pokemon-Level zu niedrig"
#
# Sonst:
# Ausgabe -> "Nicht genug Orden"
#
# Nutze:
# len()
# nested ifs
# Operatoren

trainername = input("Trainername: ")
orden = int(input("Orden: "))
level = int(input("Pokemon-Level: "))
pokeball = input("Pokeball vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 15 — Pokemon-Finale
# ============================================

# Erstelle dein eigenes Mini-Pokemon-Abenteuer.
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
# Ein Trainer reist durch eine neue Region,
# sammelt Orden, begegnet wilden Pokemon,
# kämpft gegen Arenaleiter
# und entscheidet, ob er bereit für die Liga ist.