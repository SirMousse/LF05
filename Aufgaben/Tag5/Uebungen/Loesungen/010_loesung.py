# =========================================
# ÜBUNG: DAS CHAOS IM NERD-LABOR 
# =========================================

# Der verrückte Professor Byte hat sein Gamer-Labor zerstört.
# Jetzt laufen überall Roboterkatzen, Drachen-Drohnen
# und kaputte Konsolen herum.

# Deine Mission:
# Nutze Listen, Tupel, for-Schleifen und while-Schleifen,
# um das Labor wieder unter Kontrolle zu bringen.


# =========================================
# TEIL 1 – DAS INVENTAR 
# =========================================

inventar = ["Lasermaus", "Energydrink", "Gaming-Tastatur", "USB-Schwert"]

# Aufgaben:
# 1. Gib das komplette Inventar aus.
print("Mein Inventar:", inventar)

# 2. Gib nur das erste Item aus.
print("Erstes Item:", inventar[0])

# 3. Füge "Programmier-Socken" zur Liste hinzu.
inventar.append("Programmier-Socken")
print("Erneuerte Liste:", inventar)

# 4. Gib die Länge der Liste aus.
print("Anzahl der Items:", len(inventar))



# =========================================
# TEIL 2 – DIE SICHERHEITSCODES 
# =========================================

koordinaten = (42, 77)

# Aufgaben:
# 1. Gib beide Werte einzeln aus.
print("X-Koordinate:", koordinaten[0])
print("Y-Koordinate:", koordinaten[1])

# 2. Versuche testweise den ersten Wert zu ändern.
# 3. Beobachte den Fehler.

try:                            # try -> Versuche es     
    koordinaten[0] = 77         # Das geht nicht!
except TypeError as fehler:     # except -> Falls es schiefgeht, mache stattdessen das hier: |
                                # TypeError -> Fehler wegen falscher bzw. verbotener Aktion für unseren Datentypen
                                # as fehler -> Speichere die Fehlermeldung in der Variable fehler
    print("Fehler:", fehler)    # Ausgabe unserer Fehlermeldung

# try/except -> Schützt unser Programm davor, direkt abzustürzen!

# 4. Schreibe als Kommentar dazu, WARUM der Fehler entsteht.
# Tupel ist UNVERÄNDERLICH!!!!
# Bedeutet: Einmal erstellt, kann man die Werte des Tuples NICHT mehr ändern!
# Soll davor schützen, das niemand ausversehen unsere Koordinaten überschreibt!



# =========================================
# TEIL 3 – DIE ROBOTER ZÄHLEN 
# =========================================

# Aufgabe:
# Nutze eine for-Schleife, damit folgendes ausgegeben wird:
#
# Roboter 1 aktiviert!
# Roboter 2 aktiviert!
# Roboter 3 aktiviert!
# Roboter 4 aktiviert!
# Roboter 5 aktiviert!



# =========================================
# TEIL 4 – DER BOSSKAMPF 
# =========================================

# Der Endboss "Bugzilla" hat 20 Lebenspunkte.

# Aufgaben:
# 1. Erstelle eine Variable leben = 20
# 2. Nutze eine while-Schleife.
# 3. Bei jedem Angriff verliert Bugzilla 5 Leben.
# 4. Gib nach jedem Treffer die restlichen Lebenspunkte aus.
# 5. Wenn der Boss besiegt ist, soll erscheinen:
#
# Bugzilla wurde besiegt!



# =========================================
# BONUS-MISSION 
# =========================================

# Erstelle eine Liste mit mindestens 5 Lieblingsgames,
# Serien oder Anime.

# Nutze anschließend eine for-Schleife,
# um alles auszugeben.
#
# Beispiel:
# Ich feiere: Zelda
# Ich feiere: One Piece



# =========================================
# EXTRA-CHALLENGE FÜR NERD-LEGENDEN 
# =========================================

# Kombiniere alles:
#
# - Eine Liste mit Gegnern
# - Eine for-Schleife für die Gegner
# - Eine while-Schleife für Lebenspunkte
# - Ein Tupel mit geheimen Koordinaten
#
# Und baue daraus ein kleines Mini-Game.