# ============================================
# IT-Aufgabenreihe Python
# Von leicht -> schwer
# ============================================


# ============================================
# Aufgabe 1 — Benutzername prüfen
# ============================================

# Frage den Benutzernamen ab.
#
# Wenn der Name länger als 6 Zeichen ist:
# Ausgabe -> "Gültiger Benutzername"
#
# Sonst:
# Ausgabe -> "Benutzername zu kurz"
#
# Nutze:
# input()
# if / else
# len()

benutzername = input("Benutzername: ")

# Dein Code



# ============================================
# Aufgabe 2 — CPU-Auslastung
# ============================================

# Frage nach der CPU-Auslastung.
#
# Unter 70:
# Ausgabe -> "CPU läuft stabil"
#
# Sonst:
# Ausgabe -> "CPU ist stark ausgelastet"
#
# Nutze:
# if / else
# Operatoren

cpu = int(input("CPU-Auslastung: "))

# Dein Code



# ============================================
# Aufgabe 3 — Speicherplatz prüfen
# ============================================

# Frage nach dem freien Speicherplatz in GB.
#
# Unter 10:
# Ausgabe -> "Speicher fast voll"
#
# Zwischen 10 und 50:
# Ausgabe -> "Speicherplatz ausreichend"
#
# Über 50:
# Ausgabe -> "Viel Speicherplatz verfügbar"
#
# Nutze:
# if / elif / else

speicher = int(input("Freier Speicherplatz in GB: "))

# Dein Code



# ============================================
# Aufgabe 4 — Admin-Passwort
# ============================================

# Frage nach einem Admin-Passwort.
#
# Wenn das Passwort "admin123" ist:
# Ausgabe -> "Admin-Zugang erlaubt"
#
# Sonst:
# Ausgabe -> "Zugriff verweigert"
#
# Nutze:
# if / else

passwort = input("Admin-Passwort: ")

# Dein Code



# ============================================
# Aufgabe 5 — RAM-Auslastung
# ============================================

# Frage nach der RAM-Auslastung.
#
# Unter 80:
# Ausgabe -> "RAM-Auslastung normal"
#
# Sonst:
# Ausgabe -> "RAM fast voll"
#
# Nutze:
# Operatoren
# if / else

ram = int(input("RAM-Auslastung: "))

# Dein Code



# ============================================
# Aufgabe 6 — Zufälliger Systemcheck
# ============================================

# Nutze random.
#
# Der Systemcheck würfelt eine Zahl zwischen 1 und 6.
#
# Wenn die Zahl 6 ist:
# Ausgabe -> "Kritischer Fehler gefunden"
#
# Sonst:
# Ausgabe -> "Keine kritischen Fehler gefunden"
#
# Nutze:
# random
# if / else

import random

check = random.randint(1, 6)

print(check)

# Dein Code



# ============================================
# Aufgabe 7 — Backup vorhanden
# ============================================

# Frage:
# - Ist ein Backup vorhanden? (ja/nein)
#
# Wenn ja:
# Ausgabe -> "System kann wiederhergestellt werden"
#
# Sonst:
# Ausgabe -> "Kein Backup gefunden"

backup = input("Backup vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 8 — Server-Neustart
# ============================================

# Frage:
# - CPU-Auslastung
# - Ist ein Backup vorhanden? (ja/nein)
#
# Wenn CPU >= 85:
#
#     Wenn Backup == ja:
#     Ausgabe -> "Server kann sicher neu gestartet werden"
#
#     Sonst:
#     Ausgabe -> "Neustart riskant ohne Backup"
#
# Sonst:
# Ausgabe -> "Kein Neustart nötig"
#
# Nutze:
# nested ifs

cpu = int(input("CPU-Auslastung: "))
backup = input("Backup vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 9 — Zufälliger Fehlertyp
# ============================================

# Nutze random.
#
# Zufällig erscheint:
# - Netzwerk
# - Datenbank
# - Login
#
# Je nach Fehler:
# unterschiedliche Ausgabe
#
# Nutze:
# random
# if / elif / else

import random

fehler = random.choice(["Netzwerk", "Datenbank", "Login"])

print(fehler)

# Dein Code



# ============================================
# Aufgabe 10 — Ticket-Titel prüfen
# ============================================

# Frage nach dem Titel eines Support-Tickets.
#
# Wenn der Titel länger als 15 Zeichen ist:
# Ausgabe -> "Ausführlicher Ticket-Titel"
#
# Wenn der Titel länger als 5 Zeichen ist:
# Ausgabe -> "Kurzer Ticket-Titel"
#
# Sonst:
# Ausgabe -> "Ticket-Titel zu kurz"
#
# Nutze:
# len()
# if / elif / else

ticket = input("Ticket-Titel: ")

# Dein Code



# ============================================
# Aufgabe 11 — Zugriff auf Serverraum
# ============================================

# Frage:
# - Sicherheitslevel
# - Hat die Person eine Zugangskarte? (ja/nein)
#
# Wenn Sicherheitslevel >= 70:
#
#     Wenn Zugangskarte == ja:
#     Ausgabe -> "Zugang zum Serverraum erlaubt"
#
#     Sonst:
#     Ausgabe -> "Zugangskarte fehlt"
#
# Sonst:
# Ausgabe -> "Sicherheitslevel zu niedrig"
#
# Nutze:
# nested ifs
# Operatoren

sicherheitslevel = int(input("Sicherheitslevel: "))
zugangskarte = input("Zugangskarte vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 12 — Serverzustand prüfen
# ============================================

# Nutze random.
#
# Der Serverzustand ist zufällig:
# - stabil
# - langsam
# - kritisch
#
# Frage zusätzlich nach der CPU-Auslastung.
#
# Je nach Kombination:
# unterschiedliche Ergebnisse
#
# Beispiel:
#
# Wenn Server kritisch UND CPU über 85:
# Ausgabe -> "Sofortige Wartung erforderlich"
#
# Nutze:
# random
# nested ifs
# Operatoren

import random

server = random.choice(["stabil", "langsam", "kritisch"])

print("Serverzustand:", server)

cpu = int(input("CPU-Auslastung: "))

# Dein Code



# ============================================
# Aufgabe 13 — Fehlercode raten
# ============================================

# Erzeuge eine Zufallszahl zwischen 1 und 10.
#
# Der Benutzer muss den Fehlercode raten.
#
# Wenn richtig:
# Ausgabe -> "Fehlercode erkannt"
#
# Sonst:
# Ausgabe -> "Falscher Fehlercode"
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

fehlercode = random.randint(1, 10)

tipp = int(input("Fehlercode raten: "))

# Dein Code



# ============================================
# Aufgabe 14 — Die IT-Prüfung
# ============================================

# Frage:
# - Benutzername
# - Sicherheitslevel
# - CPU-Auslastung
# - Ist ein Backup vorhanden? (ja/nein)
#
# Wenn der Benutzername länger als 6 Zeichen:
# Ausgabe -> "Benutzername akzeptiert"
#
# Wenn Sicherheitslevel >= 80:
#
#     Wenn CPU < 85:
#
#         Wenn Backup == ja:
#         Ausgabe -> "IT-Prüfung bestanden"
#
#         Sonst:
#         Ausgabe -> "Backup fehlt"
#
#     Sonst:
#     Ausgabe -> "CPU-Auslastung zu hoch"
#
# Sonst:
# Ausgabe -> "Sicherheitslevel zu niedrig"
#
# Nutze:
# len()
# nested ifs
# Operatoren

benutzername = input("Benutzername: ")
sicherheitslevel = int(input("Sicherheitslevel: "))
cpu = int(input("CPU-Auslastung: "))
backup = input("Backup vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 15 — IT-Finale
# ============================================

# Erstelle dein eigenes Mini-IT-Support-Abenteuer.
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
# Ein Server fällt aus.
# Der Benutzer muss Logs prüfen, Backups kontrollieren,
# Fehlercodes auswerten und entscheiden,
# ob ein Neustart sicher ist.