# ============================================
# Hacker-Aufgabenreihe Python
# Von leicht -> schwer
# ============================================


# ============================================
# Aufgabe 1 — Hackername prüfen
# ============================================

# Frage den Hackernamen ab.
#
# Wenn der Name länger als 6 Zeichen ist:
# Ausgabe -> "Starker Codename"
#
# Sonst:
# Ausgabe -> "Kurzer Codename"
#
# Nutze:
# input()
# if / else
# len()

name = input("Hackername: ")

# Dein Code



# ============================================
# Aufgabe 2 — Passwort-Stärke
# ============================================

# Frage nach der Länge eines Passworts.
#
# Ab 12 Zeichen:
# Ausgabe -> "Starkes Passwort"
#
# Sonst:
# Ausgabe -> "Passwort zu kurz"
#
# Nutze:
# if / else
# Operatoren

passwort_laenge = int(input("Passwortlänge: "))

# Dein Code



# ============================================
# Aufgabe 3 — Sicherheitslevel
# ============================================

# Frage nach dem Sicherheitslevel eines Systems.
#
# Unter 30:
# Ausgabe -> "Niedrige Sicherheit"
#
# Zwischen 30 und 70:
# Ausgabe -> "Mittlere Sicherheit"
#
# Über 70:
# Ausgabe -> "Hohe Sicherheit"
#
# Nutze:
# if / elif / else

sicherheitslevel = int(input("Sicherheitslevel: "))

# Dein Code



# ============================================
# Aufgabe 4 — Login-Code
# ============================================

# Frage nach einem geheimen Login-Code.
#
# Wenn der Code "root" ist:
# Ausgabe -> "Admin-Zugang erlaubt"
#
# Sonst:
# Ausgabe -> "Zugriff verweigert"
#
# Nutze:
# if / else

code = input("Login-Code: ")

# Dein Code



# ============================================
# Aufgabe 5 — Firewall-Status
# ============================================

# Frage nach der Firewall-Stärke.
#
# Unter 50:
# Ausgabe -> "Firewall schwach"
#
# Sonst:
# Ausgabe -> "Firewall aktiv"
#
# Nutze:
# Operatoren
# if / else

firewall = int(input("Firewall-Stärke: "))

# Dein Code



# ============================================
# Aufgabe 6 — Zufälliger Systemscan
# ============================================

# Nutze random.
#
# Das Systemscan-Ergebnis ist zufällig:
# 1 bis 6
#
# Wenn die Zahl 6 ist:
# Ausgabe -> "Kritische Schwachstelle gefunden"
#
# Sonst:
# Ausgabe -> "Keine kritische Schwachstelle"
#
# Nutze:
# random
# if / else

import random

scan = random.randint(1, 6)

print(scan)

# Dein Code



# ============================================
# Aufgabe 7 — Zwei-Faktor-Code
# ============================================

# Frage:
# - Ist der Zwei-Faktor-Code vorhanden? (ja/nein)
#
# Wenn ja:
# Ausgabe -> "Login bestätigt"
#
# Sonst:
# Ausgabe -> "Login blockiert"

zwei_faktor = input("Zwei-Faktor-Code vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 8 — Admin-Bereich
# ============================================

# Frage:
# - Sicherheitslevel
# - Ist der Admin-Key vorhanden? (ja/nein)
#
# Wenn Sicherheitslevel >= 80:
#
#     Wenn Admin-Key == ja:
#     Ausgabe -> "Admin-Bereich geöffnet"
#
#     Sonst:
#     Ausgabe -> "Admin-Key fehlt"
#
# Sonst:
# Ausgabe -> "Sicherheitslevel zu niedrig"
#
# Nutze:
# nested ifs

sicherheitslevel = int(input("Sicherheitslevel: "))
admin_key = input("Admin-Key vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 9 — Zufälliger Angriffstyp
# ============================================

# Nutze random.
#
# Zufällig erscheint:
# - Phishing
# - Malware
# - DDoS
#
# Je nach Angriff:
# unterschiedliche Ausgabe
#
# Nutze:
# random
# if / elif / else

import random

angriff = random.choice(["Phishing", "Malware", "DDoS"])

print(angriff)

# Dein Code



# ============================================
# Aufgabe 10 — Verschlüsselungsname
# ============================================

# Frage nach dem Namen einer Verschlüsselung.
#
# Wenn der Name länger als 10 Zeichen ist:
# Ausgabe -> "Komplexe Verschlüsselung"
#
# Wenn der Name länger als 5 Zeichen ist:
# Ausgabe -> "Mittlere Verschlüsselung"
#
# Sonst:
# Ausgabe -> "Einfache Verschlüsselung"
#
# Nutze:
# len()
# if / elif / else

verschluesselung = input("Name der Verschlüsselung: ")

# Dein Code



# ============================================
# Aufgabe 11 — Zugriff auf Datenbank
# ============================================

# Frage:
# - Sicherheitslevel
# - Anzahl gültiger Tokens
#
# Wenn Sicherheitslevel >= 70:
#
#     Wenn Tokens >= 2:
#     Ausgabe -> "Datenbankzugriff erlaubt"
#
#     Sonst:
#     Ausgabe -> "Nicht genug Tokens"
#
# Sonst:
# Ausgabe -> "Zugriff blockiert"
#
# Nutze:
# nested ifs
# Operatoren

sicherheitslevel = int(input("Sicherheitslevel: "))
tokens = int(input("Gültige Tokens: "))

# Dein Code



# ============================================
# Aufgabe 12 — Server-Verteidigung
# ============================================

# Nutze random.
#
# Der Angriff ist zufällig:
# - schwach
# - mittel
# - stark
#
# Frage zusätzlich nach der Firewall-Stärke.
#
# Je nach Kombination:
# unterschiedliche Ergebnisse
#
# Beispiel:
#
# Wenn Angriff stark UND Firewall-Stärke unter 60:
# Ausgabe -> "Server kompromittiert"
#
# Nutze:
# random
# nested ifs
# Operatoren

import random

angriff = random.choice(["schwach", "mittel", "stark"])

print("Angriff:", angriff)

firewall = int(input("Firewall-Stärke: "))

# Dein Code



# ============================================
# Aufgabe 13 — Code-Rätsel
# ============================================

# Erzeuge eine Zufallszahl zwischen 1 und 10.
#
# Der Benutzer muss den Sicherheitscode raten.
#
# Wenn richtig:
# Ausgabe -> "Code akzeptiert"
#
# Sonst:
# Ausgabe -> "Code falsch"
#
# Bonus:
# Wenn die Zahl nur um 1 daneben liegt:
# Ausgabe -> "Fast korrekt"
#
# Nutze:
# random
# if / elif / else
# Operatoren

import random

code_zahl = random.randint(1, 10)

tipp = int(input("Sicherheitscode raten: "))

# Dein Code



# ============================================
# Aufgabe 14 — Die Hackerprüfung
# ============================================

# Frage:
# - Hackername
# - Sicherheitslevel
# - Tokens
# - Ist ein Admin-Key vorhanden? (ja/nein)
#
# Wenn der Hackername länger als 6 Zeichen:
# Ausgabe -> "Professioneller Codename"
#
# Wenn Sicherheitslevel >= 80:
#
#     Wenn Tokens >= 3:
#
#         Wenn Admin-Key == ja:
#         Ausgabe -> "Hackerprüfung bestanden"
#
#         Sonst:
#         Ausgabe -> "Admin-Key fehlt"
#
#     Sonst:
#     Ausgabe -> "Nicht genug Tokens"
#
# Sonst:
# Ausgabe -> "Sicherheitslevel zu niedrig"
#
# Nutze:
# len()
# nested ifs
# Operatoren

name = input("Hackername: ")
sicherheitslevel = int(input("Sicherheitslevel: "))
tokens = int(input("Tokens: "))
admin_key = input("Admin-Key vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 15 — Hacker-Finale
# ============================================

# Erstelle dein eigenes Mini-Hacker-Abenteuer.
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
# Der Spieler versucht, ein sicheres System zu analysieren,
# muss Codes prüfen, Risiken einschätzen
# und entscheidet, ob er weitermacht oder sich ausloggt.