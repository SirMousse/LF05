import random

# ==================================================
# MISSION CYBERCORE
# Ein komplettes IT-Text-Adventure
# ==================================================

print("=" * 50)
print("   MISSION CYBERCORE")
print("   Das Netzwerk wird angegriffen...")
print("=" * 50)


# ==================================================
# LEVEL 1 – DAS LOGIN-SYSTEM
# Konzepte: Variablen, print(), input()
# ==================================================
print("\n--- LEVEL 1: LOGIN ---")

# input() zeigt Text an und wartet auf Eingabe.
# Das Ergebnis ist immer ein String und wird in einer Variable gespeichert.
name  = input("Bitte Namen eingeben:\n> ")
rolle = input("IT-Rolle (Administrator / Entwickler / Netzwerktechniker / Support):\n> ")

# f-Strings: {} wird durch den Variablenwert ersetzt.
print(f"\nWillkommen bei CyberCore!")
print(f"Hallo {name}.")
print(f"{rolle}-Zugang aktiviert.")


# ==================================================
# LEVEL 2 – DAS PASSWORT-SYSTEM
# Konzepte: if / elif / else, Fehlversuche, Account sperren
# ==================================================
print("\n--- LEVEL 2: PASSWORT-SYSTEM ---")
print("Sicherheitssystem: Passwort erforderlich.")

richtiges_passwort = "admin123"
fehlversuche = 0
max_versuche = 3

while fehlversuche < max_versuche:
    eingabe = input("Passwort:\n> ")

    if eingabe == richtiges_passwort:
        print("Zugriff erlaubt! Willkommen im System.")
        break
    else:
        fehlversuche += 1  # fehlversuche = fehlversuche + 1
        verbleibend = max_versuche - fehlversuche
        if verbleibend > 0:
            print(f"Zugriff verweigert! Noch {verbleibend} Versuch(e).")
        else:
            print("Account gesperrt! Zu viele Fehlversuche. IT-Abteilung informiert.")


# ==================================================
# LEVEL 3 – SERVER-CHECK
# Konzepte: random
# ==================================================
print("\n--- LEVEL 3: SERVER-CHECK ---")

# random.randint(1, 2) gibt zufaellig 1 oder 2 zurueck.
# Damit simulieren wir einen zufaelligen Server-Status.
for server_nr in range(1, 4):
    status = random.randint(1, 2)
    if status == 1:
        print(f"Server {server_nr}: ONLINE")
    else:
        print(f"Server {server_nr}: OFFLINE – Neustart erforderlich!")


# ==================================================
# LEVEL 4 – DAS ADMIN-INVENTAR
# Konzepte: Listen
# ==================================================
print("\n--- LEVEL 4: ADMIN-INVENTAR ---")

# Eine Liste speichert mehrere Werte. Index startet bei 0.
tools = ["VPN", "Firewall", "Backup"]

# Alle Tools anzeigen
print("Verfuegbare Tools:")
for tool in tools:
    print(f"  - {tool}")

# Neues Tool hinzufuegen: .append() haengt ans Ende.
tools.append("Antivirus")
print(f"\nAntivirus hinzugefuegt: {tools}")

# Tool entfernen: .remove() loescht den ersten passenden Eintrag.
tools.remove("Backup")
print(f"Backup-Tool entfernt: {tools}")

# Pruefen ob Tool vorhanden: "in" gibt True oder False.
if "Firewall" in tools:
    print("Firewall ist aktiv!")

# Bonus: Spieler kann eigene Tools hinzufuegen.
neues_tool = input("Welches Tool fuegest du hinzu?\n> ")
if len(tools) < 10:   # Inventar-Limit: max. 10 Slots (Mini-Challenge)
    tools.append(neues_tool)
    print(f"Tool-Liste: {tools}")
else:
    print("Inventar voll! (max. 10 Slots)")


# ==================================================
# LEVEL 5 – DAS TICKETSYSTEM
# Konzepte: while-Schleife
# ==================================================
print("\n--- LEVEL 5: TICKETSYSTEM ---")
print("Neue Support-Tickets eingegangen!")

# while True laeuft endlos – verlassen nur mit break.
while True:
    print("\nWas tust du?")
    print("1 - Ticket bearbeiten")
    print("2 - System pruefen")
    print("3 - Feierabend")

    wahl = input("> ")

    if wahl == "1":
        ticket_nr = random.randint(1000, 9999)
        print(f"Ticket #{ticket_nr} bearbeitet.")
    elif wahl == "2":
        auslastung = random.randint(20, 95)
        print(f"Systemauslastung: {auslastung}%")
    elif wahl == "3":
        print("Feierabend! Systeme laufen stabil.")
        break  # Schleife verlassen
    else:
        print("Unbekannter Befehl.")


# ==================================================
# LEVEL 6 – DIE SERVERFARM
# Konzepte: for-Schleifen
# ==================================================
print("\n--- LEVEL 6: SERVERFARM ---")
print("5 Server werden geprueft...\n")

fehlerhafte_server = 0

# range(1, 6) erzeugt die Zahlen 1 bis 5.
for i in range(1, 6):
    # CPU-Auslastung und Fehlerstatus zufaellig generieren.
    cpu        = random.randint(1, 100)
    fehlercode = random.randint(0, 2)   # 0 = stabil, 1 = Warnung, 2 = kritisch

    print(f"Server {i}: CPU {cpu}%", end=" | ")

    if fehlercode == 0:
        print("Stabil")
    elif fehlercode == 1:
        print("Warnung!")
        fehlerhafte_server += 1
    else:
        print("Kritischer Fehler!")
        fehlerhafte_server += 1

print(f"\nFehlerhafte Server: {fehlerhafte_server} / 5")


# ==================================================
# LEVEL 7 – DIE DATENBANK
# Konzepte: Dictionaries
# ==================================================
print("\n--- LEVEL 7: BENUTZERDATENBANK ---")

# Dictionary: Schluessel-Wert-Paare in geschweiften Klammern {}.
benutzer = {
    "admin":  "Administrator",
    "victor": "Entwickler",
    "anna":   "Support"
}

# Alle Benutzer anzeigen: .items() liefert Schluessel+Wert als Paare.
print("Registrierte Benutzer:")
for nutzer, nutzer_rolle in benutzer.items():
    print(f"  {nutzer}: {nutzer_rolle}")

# Rolle eines Benutzers abrufen
print(f"\nRolle von 'admin': {benutzer['admin']}")

# Neuen Benutzer hinzufuegen
benutzer["kai"] = "Netzwerktechniker"
print(f"'kai' hinzugefuegt: {benutzer}")

# Benutzer loeschen
del benutzer["anna"]
print(f"'anna' geloescht: {benutzer}")

# Bonus: Spieler sucht Benutzer.
suche = input("Benutzer suchen:\n> ")
if suche in benutzer:
    print(f"Gefunden: {suche} ist {benutzer[suche]}")
else:
    print(f"Benutzer '{suche}' nicht gefunden.")


# ==================================================
# LEVEL 8 – DAS NETZWERK
# Konzepte: Tupel
# ==================================================
print("\n--- LEVEL 8: NETZWERK-KONFIGURATION ---")

# Ein Tupel ist unveraenderlich – perfekt fuer feste Netzwerk-Adressen.
# Zugriff: server[0] = IP, server[1] = Port
haupt_server = ("192.168.0.1", 8080)
print(f"Haupt-Server: IP={haupt_server[0]}, Port={haupt_server[1]}")

# Mehrere Server (Bonus)
netzwerk = [
    ("Webserver",   "192.168.0.10", 80),
    ("Datenbankserver", "192.168.0.20", 5432),
    ("Mailserver",  "192.168.0.30", 25),
    ("Backup-Server", "192.168.0.40", 22),
]

print("\nNetzwerk-Uebersicht:")
for sname, ip, port in netzwerk:
    print(f"  {sname}: {ip}:{port}")

# Verbindung pruefen
try:
    eingabe_ip   = input("\nZiel-IP eingeben:\n> ")
    eingabe_port = int(input("Ziel-Port eingeben:\n> "))
except ValueError:
    eingabe_ip, eingabe_port = "", 0

ziel = (eingabe_ip, eingabe_port)
if ziel == (haupt_server[0], haupt_server[1]):
    print("Verbindung zum Haupt-Server hergestellt!")
else:
    haupt_adresse = f"{haupt_server[0]}:{haupt_server[1]}"
    print(f"Keine Verbindung. Haupt-Server ist unter {haupt_adresse}.")


# ==================================================
# LEVEL 9 & ENDGEGNER – DAS CYBERCORE-SYSTEM
# Konzepte: ALLES kombiniert + Klassen + Funktionen
# ==================================================
print("\n" + "=" * 50)
print("   LEVEL 9: CYBERANGRIFF ERKANNT!")
print("   Rette das CyberCore-Netzwerk!")
print("=" * 50)


# ---- Funktionen ----
def zeige_status(sname, energie, credits, inv):
    """Zeigt den aktuellen Admin-Status an."""
    print(f"\n[ {sname} | Energie {energie} | {credits} Credits | {inv} ]")

def berechne_gegenmassnahme(skill, tool_bonus, krit_chance=0.2):
    """Berechnet Wirkung einer Gegenmassnahme mit Krit-Chance."""
    wirkung = random.randint(skill - 3, skill + 5)
    # random.random() liefert 0.0 bis 1.0 – unter krit_chance = Krit!
    if random.random() < krit_chance:
        wirkung *= 2
        print("Perfekte Gegenmassnahme! Doppelte Wirkung!")
    return wirkung

def repariere_system(energie, max_energie, menge):
    """Repariert das System, aber nicht ueber max_energie."""
    # min() verhindert Ueberheilung.
    neue_energie = min(energie + menge, max_energie)
    print(f"System repariert: +{neue_energie - energie} Energie.")
    return neue_energie


# ---- Klasse ----
# Eine Klasse ist ein Bauplan fuer Objekte.
class Angriff:
    def __init__(self, name, staerke, schaden):
        # __init__ wird beim Erstellen automatisch aufgerufen.
        self.name    = name
        self.staerke = staerke
        self.schaden = schaden

    def greift_an(self):
        """Gibt zufaelligen Schaden zurueck."""
        return random.randint(self.schaden - 4, self.schaden + 4)

    def ist_gestoppt(self):
        """True wenn keine Staerke mehr."""
        return self.staerke <= 0


# ---- Spielaufbau ----
print("\nSession wird gestartet...")
admin_name     = input("Admin-Benutzername:\n> ")
admin_energie     = 100
admin_max_energie = 100
admin_credits     = 40
admin_inventar    = ["Reparatur-Patch", "Reparatur-Patch", "Firewall-Modul"]

# Server als Tupel-Liste (Name, IP, Port)
server_liste = [
    ("Proxy-Server",  "10.0.0.1", 3128),
    ("App-Server",    "10.0.0.2", 8080),
    ("Core-Server",   "10.0.0.3", 443),
]

# Tool-Datenbank als Dictionary
tool_db = {
    "Firewall-Block": 22,
    "DDoS-Filter":    18,
    "Exploit-Patch":  30,
}

# Angriffs-Pool
angriffs_pool = [
    {"name": "Brute-Force",   "staerke": 35, "schaden": 10, "credits": 6,  "drop": "Exploit-Code"},
    {"name": "DDoS-Welle",    "staerke": 50, "schaden": 14, "credits": 12, "drop": "Traffic-Log"},
    {"name": "SQL-Injection", "staerke": 40, "schaden": 11, "credits": 9,  "drop": "DB-Fragment"},
]

# ---- Shop ----
print("\nCyberCore-Shop: Neue Tools verfuegbar!")
# Preise aendern sich zufaellig (Mini-Challenge)
shop = {
    "Reparatur-Patch": random.randint(8,  14),
    "Antivirus-Update": random.randint(12, 20),
    "Verschluesselungs-Key": random.randint(18, 28),
}

print("Angebot:")
for item_s, preis_s in shop.items():
    print(f"  {item_s}: {preis_s} Credits")

kauf = input("Was kaufst du? (oder 'weiter')\n> ")
if kauf in shop:
    preis = shop[kauf]
    if admin_credits >= preis:
        admin_credits -= preis
        if len(admin_inventar) < 10:
            admin_inventar.append(kauf)
            print(f"Gekauft! {kauf} fuer {preis} Credits.")
        else:
            print("Inventar voll! (max. 10 Slots)")
    else:
        print("Nicht genug Credits!")
else:
    print("Nichts gekauft.")

# ---- Netzwerk-Rundgang ----
print(f"\nNetzwerk-Topologie:")
for sname, ip, port in server_liste:
    print(f"  {sname}: {ip}:{port}")

print(f"\n{admin_name} analysiert das Netzwerk...\n")

for sname, ip, port in server_liste:
    if admin_energie <= 0:
        break

    print(f"\n  Knoten: {sname} ({ip}:{port})")

    # Zufaelliges Ereignis pro Server
    ereignis = random.choice(["angriff", "geheimbefund", "stabil"])

    # 10% Chance auf Zero-Day-Exploit (Mini-Challenge)
    if random.random() < 0.1:
        ereignis = "zero_day"

    if ereignis in ("angriff", "zero_day"):
        if ereignis == "zero_day":
            a_daten = {"name": "Zero-Day-Exploit", "staerke": 60,
                       "schaden": 16, "credits": 15, "drop": "Zero-Day-Code"}
            print(f"  Zero-Day-Exploit entdeckt!")
        else:
            a_daten = random.choice(angriffs_pool)

        angriff = Angriff(a_daten["name"], a_daten["staerke"], a_daten["schaden"])
        print(f"  {angriff.name} greift an!")

        # Kampfschleife: laeuft bis Angriff gestoppt ist.
        while not angriff.ist_gestoppt() and admin_energie > 0:
            w = berechne_gegenmassnahme(14, 3)
            angriff.staerke -= w
            schaden_a = angriff.greift_an()
            admin_energie -= schaden_a
            admin_energie = max(0, admin_energie)
            print(f"  Gegenmassnahme: -{schaden_a} Energie | {angriff.name}: -{w} Staerke "
                  f"({angriff.name}: {max(0,angriff.staerke)}, Energie: {admin_energie})")

        if angriff.ist_gestoppt():
            print(f"  {angriff.name} gestoppt! +{a_daten['credits']} Credits")
            admin_credits += a_daten["credits"]
            # Drop
            if random.random() < 0.4:
                drop = a_daten["drop"]
                if len(admin_inventar) < 10:
                    admin_inventar.append(drop)
                    print(f"  Log gesichert: {drop}")
        else:
            print("  Energie erschoepft...")

    elif ereignis == "geheimbefund":
        fund = random.randrange(10, 51, 10)
        admin_credits += fund
        print(f"  Geheimes Admin-Log entdeckt! +{fund} Credits")

    else:
        rep = random.randint(10, 20)
        admin_energie = repariere_system(admin_energie, admin_max_energie, rep)

    zeige_status(admin_name, admin_energie, admin_credits, admin_inventar)

    if admin_energie <= 0:
        print("\nSystem ausgefallen – CyberCore ist kompromittiert.")
        exit()

# ---- ENDGEGNER: DER CYBERANGRIFF ----
print("\n" + "=" * 50)
print("   HAUPT-CYBERANGRIFF ERKANNT!")
print("   Quelle unbekannt. Kritische Systeme bedroht.")
print("=" * 50)

haupt_angriff = Angriff("Haupt-Cyberangriff", 120, 16)
print(f"\nAngriffs-Staerke: {haupt_angriff.staerke}\n")

while not haupt_angriff.ist_gestoppt() and admin_energie > 0:
    zeige_status(admin_name, admin_energie, admin_credits, admin_inventar)
    print(f"Angriffs-Staerke: {haupt_angriff.staerke}")
    print("\nAktion:")
    print("1 - Firewall aktivieren")
    print("2 - System reparieren (Reparatur-Patch noetig)")
    print("3 - Tool einsetzen (Tool-Datenbank)")
    print("4 - Verbindung trennen (Fliehen)")

    aktion = input("> ")

    if aktion == "1":
        w = berechne_gegenmassnahme(14, 3)
        haupt_angriff.staerke -= w
        print(f"Firewall blockiert {w} Angriffs-Punkte!")

    elif aktion == "2":
        if "Reparatur-Patch" in admin_inventar:
            admin_inventar.remove("Reparatur-Patch")
            admin_energie = repariere_system(admin_energie, admin_max_energie, 35)
        else:
            print("Kein Reparatur-Patch mehr!")
            continue  # Runde ohne Gegenzug wiederholen

    elif aktion == "3":
        print("Tool-Datenbank:", list(tool_db.keys()))
        gew = input("Welches Tool?\n> ")
        if gew in tool_db:
            tw = tool_db[gew]
            haupt_angriff.staerke -= tw
            print(f"{gew} eingesetzt! -{tw} Angriffs-Staerke!")
        else:
            print("Tool nicht verfuegbar!")
            continue

    elif aktion == "4":
        print("Verbindung getrennt. CyberCore ist offline.")
        exit()

    else:
        print("Ungueltige Eingabe.")
        continue

    # Angriff schlaegt zurueck
    if not haupt_angriff.ist_gestoppt():
        schaden_a = haupt_angriff.greift_an()
        admin_energie -= schaden_a
        admin_energie = max(0, admin_energie)
        print(f"Angriff trifft Systeme: -{schaden_a} Energie!")

# ---- Ergebnis ----
print("\n" + "=" * 50)
if haupt_angriff.ist_gestoppt():
    print(f"{admin_name} hat den Cyberangriff gestoppt!")
    print("Alle Systeme wieder online. CyberCore ist sicher.")
    print(f"\nEndstatistik:")
    print(f"  Restenergie:  {admin_energie}")
    print(f"  Credits:      {admin_credits}")
    print(f"  Inventar:     {admin_inventar}")
else:
    print(f"{admin_name} wurde ausgeloggt.")
    print("Das Netzwerk ist kompromittiert. Notabschaltung eingeleitet.")
print("=" * 50)