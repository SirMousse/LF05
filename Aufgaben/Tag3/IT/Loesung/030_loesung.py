# ============================================
# IT-Aufgabenreihe Python — Lösungen
# ============================================


# ============================================
# Aufgabe 1 — Benutzername prüfen
# ============================================

benutzername = input("Benutzername: ")

if len(benutzername) > 6:
    print("Gültiger Benutzername")
else:
    print("Benutzername zu kurz")


# ============================================
# Aufgabe 2 — CPU-Auslastung
# ============================================

cpu = int(input("CPU-Auslastung: "))

if cpu < 70:
    print("CPU läuft stabil")
else:
    print("CPU ist stark ausgelastet")


# ============================================
# Aufgabe 3 — Speicherplatz prüfen
# ============================================

speicher = int(input("Freier Speicherplatz in GB: "))

if speicher < 10:
    print("Speicher fast voll")
elif speicher <= 50:
    print("Speicherplatz ausreichend")
else:
    print("Viel Speicherplatz verfügbar")


# ============================================
# Aufgabe 4 — Admin-Passwort
# ============================================

passwort = input("Admin-Passwort: ")

if passwort == "admin123":
    print("Admin-Zugang erlaubt")
else:
    print("Zugriff verweigert")


# ============================================
# Aufgabe 5 — RAM-Auslastung
# ============================================

ram = int(input("RAM-Auslastung: "))

if ram < 80:
    print("RAM-Auslastung normal")
else:
    print("RAM fast voll")


# ============================================
# Aufgabe 6 — Zufälliger Systemcheck
# ============================================

import random

check = random.randint(1, 6)

print(check)

if check == 6:
    print("Kritischer Fehler gefunden")
else:
    print("Keine kritischen Fehler gefunden")


# ============================================
# Aufgabe 7 — Backup vorhanden
# ============================================

backup = input("Backup vorhanden? ")

if backup == "ja":
    print("System kann wiederhergestellt werden")
else:
    print("Kein Backup gefunden")


# ============================================
# Aufgabe 8 — Server-Neustart
# ============================================

cpu = int(input("CPU-Auslastung: "))
backup = input("Backup vorhanden? ")

if cpu >= 85:
    if backup == "ja":
        print("Server kann sicher neu gestartet werden")
    else:
        print("Neustart riskant ohne Backup")
else:
    print("Kein Neustart nötig")


# ============================================
# Aufgabe 9 — Zufälliger Fehlertyp
# ============================================

import random

fehler = random.choice(["Netzwerk", "Datenbank", "Login"])

print(fehler)

if fehler == "Netzwerk":
    print("Netzwerkverbindung prüfen und Router neu starten.")
elif fehler == "Datenbank":
    print("Datenbankdienst neu starten und Logs prüfen.")
else:
    print("Anmeldedaten zurücksetzen und Zugang prüfen.")


# ============================================
# Aufgabe 10 — Ticket-Titel prüfen
# ============================================

ticket = input("Ticket-Titel: ")

if len(ticket) > 15:
    print("Ausführlicher Ticket-Titel")
elif len(ticket) > 5:
    print("Kurzer Ticket-Titel")
else:
    print("Ticket-Titel zu kurz")


# ============================================
# Aufgabe 11 — Zugriff auf Serverraum
# ============================================

sicherheitslevel = int(input("Sicherheitslevel: "))
zugangskarte = input("Zugangskarte vorhanden? ")

if sicherheitslevel >= 70:
    if zugangskarte == "ja":
        print("Zugang zum Serverraum erlaubt")
    else:
        print("Zugangskarte fehlt")
else:
    print("Sicherheitslevel zu niedrig")


# ============================================
# Aufgabe 12 — Serverzustand prüfen
# ============================================

import random

server = random.choice(["stabil", "langsam", "kritisch"])

print("Serverzustand:", server)

cpu = int(input("CPU-Auslastung: "))

if server == "stabil":
    print("Alles in Ordnung — kein Eingriff nötig.")

elif server == "langsam":
    if cpu >= 70:
        print("Server ist langsam und CPU stark belastet — Neustart empfohlen.")
    else:
        print("Server ist langsam, aber CPU noch stabil — Prozesse prüfen.")

else:
    if cpu > 85:
        print("Sofortige Wartung erforderlich")
    else:
        print("Kritischer Serverzustand — CPU noch kontrollierbar, Logs sofort prüfen.")


# ============================================
# Aufgabe 13 — Fehlercode raten
# ============================================

import random

fehlercode = random.randint(1, 10)

tipp = int(input("Fehlercode raten: "))

if tipp == fehlercode:
    print("Fehlercode erkannt")
elif tipp == fehlercode - 1 or tipp == fehlercode + 1:
    print("Fast richtig")
else:
    print("Falscher Fehlercode")


# ============================================
# Aufgabe 14 — Die IT-Prüfung
# ============================================

benutzername = input("Benutzername: ")
sicherheitslevel = int(input("Sicherheitslevel: "))
cpu = int(input("CPU-Auslastung: "))
backup = input("Backup vorhanden? ")

if len(benutzername) > 6:
    print("Benutzername akzeptiert")

if sicherheitslevel >= 80:
    if cpu < 85:
        if backup == "ja":
            print("IT-Prüfung bestanden")
        else:
            print("Backup fehlt")
    else:
        print("CPU-Auslastung zu hoch")
else:
    print("Sicherheitslevel zu niedrig")


# ============================================
# Aufgabe 15 — IT-Finale
# ============================================

import random

print("\n=== IT-NOTFALL: SERVER AUSGEFALLEN ===\n")

# Entscheidung 1: Benutzername prüfen (len)
benutzername = input("Dein Benutzername: ")

if len(benutzername) > 6:
    print(f"Zugang gewährt, {benutzername}. Incident-Management gestartet.")
else:
    print(f"Kurzer Name, {benutzername} — aber du hast Zugang.")

# Entscheidung 2: Sicherheitslevel
sicherheit = int(input("Dein Sicherheitslevel (0-100): "))

if sicherheit < 50:
    print("Eingeschränkter Zugang — du siehst nur Basis-Logs.")
elif sicherheit < 80:
    print("Standard-Zugang — alle Logs sichtbar.")
else:
    print("Admin-Zugang — du siehst alles.")

# Entscheidung 3: CPU und RAM
cpu = int(input("Aktuelle CPU-Auslastung: "))
backup = input("Backup vorhanden? (ja/nein): ").strip().lower()

# Zufallsereignis: Was ist der Fehler?
fehler = random.choice(["Netzwerk", "Datenbank", "Hardwaredefekt"])
print(f"\nFehleranalyse abgeschlossen: {fehler}-Problem erkannt!")

if fehler == "Netzwerk":
    print("Netzwerkkabel und Router prüfen.")
elif fehler == "Datenbank":
    print("Datenbankdienst hängt — Neustart wird vorbereitet.")
else:
    print("Hardware beschädigt — externe Wartung nötig.")

# Entscheidung 4: Backup-Prüfung
if backup == "ja":
    print("Backup gefunden — Wiederherstellung möglich.")
else:
    print("Kein Backup — Risiko bei Neustart.")

# Entscheidung 5: Nested ifs — Neustart-Entscheidung
print("\n--- Neustart-Entscheidung ---")

if sicherheit >= 80:

    if cpu < 85:

        if backup == "ja":
            if fehler == "Hardwaredefekt":
                # Ende 1
                print("\nEnde 1: Neustart läuft — aber Hardwaredefekt bleibt.")
                print("Externe Techniker werden angefordert. Server läuft instabil.")
            else:
                # Ende 2
                print("\nEnde 2: Neustart erfolgreich!")
                print(f"{benutzername} behebt den {fehler}-Fehler. System wieder online.")

        else:
            # Ende 3
            print("\nEnde 3: Neustart ohne Backup riskiert Datenverlust.")
            print("Entscheidung: Neustart abgebrochen. Backup wird zuerst erstellt.")

    else:
        # Ende 4
        print("\nEnde 4: CPU zu hoch für sicheren Neustart.")
        print("Prozesse werden beendet — bitte in 10 Minuten erneut versuchen.")

elif sicherheit >= 50:
    # Ende 5
    print("\nEnde 5: Dein Sicherheitslevel reicht nicht für den Neustart.")
    print("Admin wird benachrichtigt und übernimmt den Eingriff.")

else:
    # Ende 6
    print("\nEnde 6: Zugriff verweigert.")
    print(f"{benutzername} hat keine Berechtigung für diesen Server.")
    print("Vorfall wird protokolliert.")