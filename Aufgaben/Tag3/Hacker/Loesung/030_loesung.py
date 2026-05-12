# ============================================
# Hacker-Aufgabenreihe Python — Lösungen
# ============================================


# ============================================
# Aufgabe 1 — Hackername prüfen
# ============================================

name = input("Hackername: ")

if len(name) > 6:
    print("Starker Codename")
else:
    print("Kurzer Codename")


# ============================================
# Aufgabe 2 — Passwort-Stärke
# ============================================

passwort_laenge = int(input("Passwortlänge: "))

if passwort_laenge >= 12:
    print("Starkes Passwort")
else:
    print("Passwort zu kurz")


# ============================================
# Aufgabe 3 — Sicherheitslevel
# ============================================

sicherheitslevel = int(input("Sicherheitslevel: "))

if sicherheitslevel < 30:
    print("Niedrige Sicherheit")
elif sicherheitslevel <= 70:
    print("Mittlere Sicherheit")
else:
    print("Hohe Sicherheit")


# ============================================
# Aufgabe 4 — Login-Code
# ============================================

code = input("Login-Code: ")

if code == "root":
    print("Admin-Zugang erlaubt")
else:
    print("Zugriff verweigert")


# ============================================
# Aufgabe 5 — Firewall-Status
# ============================================

firewall = int(input("Firewall-Stärke: "))

if firewall < 50:
    print("Firewall schwach")
else:
    print("Firewall aktiv")


# ============================================
# Aufgabe 6 — Zufälliger Systemscan
# ============================================

import random

scan = random.randint(1, 6)

print(scan)

if scan == 6:
    print("Kritische Schwachstelle gefunden")
else:
    print("Keine kritische Schwachstelle")


# ============================================
# Aufgabe 7 — Zwei-Faktor-Code
# ============================================

zwei_faktor = input("Zwei-Faktor-Code vorhanden? ")

if zwei_faktor == "ja":
    print("Login bestätigt")
else:
    print("Login blockiert")


# ============================================
# Aufgabe 8 — Admin-Bereich
# ============================================

sicherheitslevel = int(input("Sicherheitslevel: "))
admin_key = input("Admin-Key vorhanden? ")

if sicherheitslevel >= 80:
    if admin_key == "ja":
        print("Admin-Bereich geöffnet")
    else:
        print("Admin-Key fehlt")
else:
    print("Sicherheitslevel zu niedrig")


# ============================================
# Aufgabe 9 — Zufälliger Angriffstyp
# ============================================

import random

angriff = random.choice(["Phishing", "Malware", "DDoS"])

print(angriff)

if angriff == "Phishing":
    print("Gefälschte E-Mail erkannt — Absender blockieren und melden.")
elif angriff == "Malware":
    print("Schadsoftware entdeckt — System isolieren und Scan starten.")
else:
    print("DDoS-Angriff läuft — Traffic filtern und CDN aktivieren.")


# ============================================
# Aufgabe 10 — Verschlüsselungsname
# ============================================

verschluesselung = input("Name der Verschlüsselung: ")

if len(verschluesselung) > 10:
    print("Komplexe Verschlüsselung")
elif len(verschluesselung) > 5:
    print("Mittlere Verschlüsselung")
else:
    print("Einfache Verschlüsselung")


# ============================================
# Aufgabe 11 — Zugriff auf Datenbank
# ============================================

sicherheitslevel = int(input("Sicherheitslevel: "))
tokens = int(input("Gültige Tokens: "))

if sicherheitslevel >= 70:
    if tokens >= 2:
        print("Datenbankzugriff erlaubt")
    else:
        print("Nicht genug Tokens")
else:
    print("Zugriff blockiert")


# ============================================
# Aufgabe 12 — Server-Verteidigung
# ============================================

import random

angriff = random.choice(["schwach", "mittel", "stark"])

print("Angriff:", angriff)

firewall = int(input("Firewall-Stärke: "))

if angriff == "schwach":
    if firewall >= 20:
        print("Angriff problemlos abgewehrt")
    else:
        print("Selbst ein schwacher Angriff kommt durch")

elif angriff == "mittel":
    if firewall >= 40:
        print("Angriff abgewehrt — Logs prüfen")
    else:
        print("Mittlerer Angriff durchgebrochen — Schaden begrenzen")

else:
    if firewall >= 60:
        print("Starker Angriff abgewehrt — Firewall hat gehalten")
    else:
        print("Server kompromittiert")


# ============================================
# Aufgabe 13 — Code-Rätsel
# ============================================

import random

code_zahl = random.randint(1, 10)

tipp = int(input("Sicherheitscode raten: "))

if tipp == code_zahl:
    print("Code akzeptiert")
elif tipp == code_zahl - 1 or tipp == code_zahl + 1:
    print("Fast korrekt")
else:
    print("Code falsch")


# ============================================
# Aufgabe 14 — Die Hackerprüfung
# ============================================

name = input("Hackername: ")
sicherheitslevel = int(input("Sicherheitslevel: "))
tokens = int(input("Tokens: "))
admin_key = input("Admin-Key vorhanden? ")

if len(name) > 6:
    print("Professioneller Codename")

if sicherheitslevel >= 80:
    if tokens >= 3:
        if admin_key == "ja":
            print("Hackerprüfung bestanden")
        else:
            print("Admin-Key fehlt")
    else:
        print("Nicht genug Tokens")
else:
    print("Sicherheitslevel zu niedrig")


# ============================================
# Aufgabe 15 — Hacker-Finale
# ============================================

import random

print("\n=== OPERATION: SYSTEM BREACH ===\n")

# Entscheidung 1: Hackername prüfen (len)
name = input("Dein Hackername: ")

if len(name) > 6:
    print(f"Codename '{name}' akzeptiert. Verbindung wird aufgebaut...")
else:
    print(f"Kurzer Codename '{name}' — aber du hast Zugang.")

# Entscheidung 2: Sicherheitslevel des Zielsystems
sicherheit = int(input("Sicherheitslevel des Zielsystems (0-100): "))

if sicherheit < 30:
    print("Schwaches System — einfaches Ziel.")
elif sicherheit < 70:
    print("Mittlere Sicherheit — Vorsicht ist geboten.")
else:
    print("Hochgesichertes System — maximale Konzentration.")

# Entscheidung 3: Tokens und Admin-Key
tokens = int(input("Anzahl gültiger Tokens: "))
admin_key = input("Admin-Key vorhanden? (ja/nein): ").strip().lower()

if tokens < 2:
    print("Warnung: Zu wenige Tokens — der Zugriff könnte scheitern.")

# Zufallsereignis: Was passiert beim Einbruch?
ereignis = random.choice(["Firewall-Alert", "Backdoor gefunden", "Honeypot", "Systemabsturz"])
print(f"\nSystemereignis erkannt: {ereignis}!")

if ereignis == "Firewall-Alert":
    print("Die Firewall schlägt Alarm! Sicherheitslevel +20.")
    sicherheit = min(100, sicherheit + 20)
    print(f"Neues Sicherheitslevel: {sicherheit}")
elif ereignis == "Backdoor gefunden":
    print("Eine Hintertür entdeckt! +1 Token.")
    tokens += 1
    print(f"Neue Token-Anzahl: {tokens}")
elif ereignis == "Honeypot":
    print("Honeypot ausgelöst! Du verlierst einen Token.")
    tokens = max(0, tokens - 1)
    print(f"Verbleibende Tokens: {tokens}")
else:
    print("Systemabsturz! Das Ziel startet neu — Sicherheitslevel sinkt auf 40.")
    sicherheit = 40

# Entscheidung 4 & 5: Nested ifs — Zugriff
print("\n--- Zugriffsversuch ---")

if sicherheit < 30:
    if tokens >= 1:
        # Ende 1
        print(f"\nEnde 1: Einfacher Einbruch.")
        print(f"{name} übernimmt das schwach gesicherte System mühelos.")
    else:
        # Ende 2
        print(f"\nEnde 2: Keine Tokens mehr.")
        print(f"Selbst das schwache System sperrt {name} aus.")

elif sicherheit < 70:
    if tokens >= 2 and admin_key == "ja":
        # Ende 3
        print(f"\nEnde 3: Erfolgreicher Einbruch.")
        print(f"{name} navigiert durch das mittlere Sicherheitssystem. Daten gesichert.")
    elif tokens >= 2:
        # Ende 4
        print(f"\nEnde 4: Teilzugriff.")
        print(f"{name} kommt rein, aber ohne Admin-Key bleiben Kernbereiche gesperrt.")
    else:
        # Ende 5
        print(f"\nEnde 5: Zugriff blockiert.")
        print(f"Zu wenige Tokens — das System erkennt den Einbruch und sperrt {name} aus.")

else:
    if tokens >= 3 and admin_key == "ja":
        # Ende 6
        print(f"\nEnde 6: Vollständiger System-Breach.")
        print(f"{name} überwindet die hohe Sicherheit. Root-Zugang erlangt.")
    else:
        # Ende 7
        print(f"\nEnde 7: Hochgesichertes System hält stand.")
        print(f"{name} wird zurückverfolgt — sofortiger Rückzug.")