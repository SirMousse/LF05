import random

# ==================================================
# OPERATION SHADOWBYTE
# Ein komplettes Hacker-Text-Adventure
# ==================================================

print("=" * 50)
print("   [ OPERATION SHADOWBYTE ]")
print("   Initialisiere System...")
print("=" * 50)


# ==================================================
# LEVEL 1 – LOGIN TERMINAL
# Konzepte: Variablen, print(), input()
# ==================================================
print("\n--- LEVEL 1: LOGIN TERMINAL ---")

# input() zeigt Text an und wartet auf Eingabe vom Nutzer.
# Das Ergebnis ist immer ein String und wird in einer Variable gespeichert.
hacker_name = input("Bitte Hacker-Namen eingeben:\n> ")
alter        = input("Alter:\n> ")
spezialgebiet = input("Spezialgebiet (Netzwerk / Malware / Kryptographie):\n> ")

# f-Strings: {} im Text wird durch den Variablenwert ersetzt.
print(f"\n[ SYSTEM START ]")
print(f"Willkommen {hacker_name}.")
print(f"Spezialgebiet: {spezialgebiet} | Alter: {alter}")
print("Zugriff auf das ShadowByte-Netzwerk gewährt.")


# ==================================================
# LEVEL 2 – PASSWORT-KNACKER
# Konzepte: if / elif / else, Fehlversuche zählen
# ==================================================
print("\n--- LEVEL 2: PASSWORT-KNACKER ---")
print("Sicherheitssystem erkannt. Passwort erforderlich.")

richtiges_passwort = "shadow123"
fehlversuche = 0
max_versuche = 3  # Nach 3 Fehlern → Account gesperrt

while fehlversuche < max_versuche:
    eingabe = input("Passwort eingeben: > ")
    
    if eingabe == richtiges_passwort:
        print("Zugriff gewährt! Willkommen im System.")
        break
    else:
        fehlversuche += 1  # fehlversuche = fehlversuche + 1
        verbleibend = max_versuche - fehlversuche
        if verbleibend > 0:
            print(f"Zugriff verweigert! Noch {verbleibend} Versuch(e).")
        else:
            print("Account gesperrt! Zu viele Fehlversuche.")


# ==================================================
# LEVEL 3 – DER ZAHLENCODE
# Konzepte: random, Zahlen vergleichen
# ==================================================
print("\n--- LEVEL 3: ZAHLENCODE ---")
print("Ein Zahlensicherheitscode blockiert den Zugang (1-10).")

# random.randint(1, 10) gibt eine zufällige ganze Zahl von 1 bis 10 zurück.
geheimer_code = random.randint(1, 10)
versuche_code = 0

while True:
    try:
        # int() wandelt den String in eine Ganzzahl um.
        # try/except fängt Fehler ab, falls der Nutzer keine Zahl eingibt.
        eingabe_code = int(input("Code eingeben (1-10): > "))
        versuche_code += 1
    except ValueError:
        print("Nur Zahlen eingeben!")
        continue

    if eingabe_code == geheimer_code:
        print(f"Code geknackt in {versuche_code} Versuch(en)!")
        break
    elif eingabe_code < geheimer_code:
        print("↑ Code ist höher.")
    else:
        print("↓ Code ist niedriger.")


# ==================================================
# LEVEL 4 – DAS DARKNET-INVENTAR
# Konzepte: Listen
# ==================================================
print("\n--- LEVEL 4: DARKNET-INVENTAR ---")

# Eine Liste speichert mehrere Werte. Zugriff über Index (startet bei 0).
tools = ["Keylogger", "VPN", "USB-Exploit"]

# Alle Tools anzeigen
print("Deine Tools:")
for tool in tools:
    print(f"  › {tool}")

# Neues Tool hinzufügen: .append() hängt ans Ende.
tools.append("Rootkit")
print(f"\nRootkit hinzugefügt: {tools}")

# Tool entfernen: .remove() löscht den ersten passenden Wert.
tools.remove("Keylogger")
print(f"Keylogger entfernt: {tools}")

# Prüfen ob Tool vorhanden: "in" gibt True oder False zurück.
if "VPN" in tools:
    print("VPN ist aktiv – Verbindung anonymisiert!")

# Bonus: Spieler fügt eigenes Tool hinzu.
eigenes_tool = input("Eigenes Tool hinzufügen: > ")
if len(tools) < 10:   # Inventar-Limit: max. 10 Slots (Mini-Challenge)
    tools.append(eigenes_tool)
    print(f"Tool hinzugefügt: {tools}")
else:
    print("Inventar voll! (max. 10 Slots)")


# ==================================================
# LEVEL 5 – DIE FIREWALL-SCHLEIFE
# Konzepte: while-Schleife, Menü
# ==================================================
print("\n--- LEVEL 5: FIREWALL-BYPASS ---")
print("Firewall erkannt. Wähle deine Aktion.")

# while True läuft endlos – wir verlassen sie nur mit break.
while True:
    print("\n1 - Port scannen")
    print("2 - Passwort brute-forcen")
    print("3 - Verbindung trennen")

    wahl = input("> ")

    if wahl == "1":
        port = random.randint(1000, 9999)
        print(f"Port {port} gescannt... offen!")
    elif wahl == "2":
        print("Brute-Force läuft... Versuch gescheitert.")
    elif wahl == "3":
        print("Verbindung getrennt. Firewall umgangen!")
        break  # Schleife verlassen
    else:
        print("Unbekannter Befehl.")


# ==================================================
# LEVEL 6 – SERVER-ANGRIFF
# Konzepte: for-Schleifen
# ==================================================
print("\n--- LEVEL 6: SERVER-ANGRIFF ---")
print("Greife 5 Server an!\n")

erfolge = 0
misserfolge = 0

# range(1, 6) erzeugt die Zahlen 1 bis 5.
for i in range(1, 6):
    sicherheitsstufe = random.randint(1, 10)
    hacker_staerke   = random.randint(1, 10)

    print(f"Server {i}: Sicherheit {sicherheitsstufe} | Deine Stärke {hacker_staerke}")

    if hacker_staerke >= sicherheitsstufe:
        print("Hack erfolgreich!")
        erfolge += 1
    else:
        print("Hack fehlgeschlagen!")
        misserfolge += 1

print(f"\nErgebnis: {erfolge} erfolgreich, {misserfolge} fehlgeschlagen.")


# ==================================================
# LEVEL 7 – EXPLOIT-DATENBANK
# Konzepte: Dictionaries
# ==================================================
print("\n--- LEVEL 7: EXPLOIT-DATENBANK ---")

# Dictionary: Schlüssel-Wert-Paare in geschweiften Klammern {}.
# exploits["SQL Injection"] gibt 70 zurück.
exploits = {
    "SQL Injection": 70,
    "DDoS":          50,
    "Zero-Day":      100
}

# Alle Exploits anzeigen: .items() liefert Schlüssel+Wert als Paare.
print("Verfügbare Exploits:")
for name_e, staerke_e in exploits.items():
    print(f"  {name_e}: {staerke_e} Schadenspotenzial")

# Exploit stärke abrufen
print(f"\nZero-Day-Stärke: {exploits['Zero-Day']}")

# Neuen Exploit hinzufügen
exploits["Ransomware"] = 85
print(f"Ransomware hinzugefügt: {exploits}")

# Exploit löschen
del exploits["DDoS"]
print(f"DDoS gelöscht: {exploits}")

# Spieler wählt Exploit
print("\nVerfügbare Exploits:", list(exploits.keys()))
gewaehlter_exploit = input("Welchen Exploit verwendest du? > ")
if gewaehlter_exploit in exploits:
    print(f"{gewaehlter_exploit} aktiviert! Stärke: {exploits[gewaehlter_exploit]}")
else:
    print("Exploit nicht gefunden.")


# ==================================================
# LEVEL 8 – GPS-KOORDINATEN
# Konzepte: Tupel
# ==================================================
print("\n--- LEVEL 8: GPS-KOORDINATEN ---")

# Ein Tupel ist unveränderlich – perfekt für feste Koordinaten.
# Zugriff wie bei Listen: server[0] = X, server[1] = Y
ziel_server = (52, 13)
print(f"Ziel-Server: X={ziel_server[0]}, Y={ziel_server[1]}")

# Mehrere Server als Tupel-Liste (Bonus)
server_liste = [
    ("Alpha-Node",   10, 20),
    ("Beta-Core",    52, 13),
    ("ZER0-Mainframe", 99, 99),
]

print("\nBekannte Server:")
for sname, sx, sy in server_liste:
    print(f"  {sname}: ({sx}, {sy})")

# Spieler gibt Koordinaten ein
try:
    eingabe_x = int(input("\nX-Koordinate eingeben: > "))
    eingabe_y = int(input("Y-Koordinate eingeben: > "))
except ValueError:
    eingabe_x, eingabe_y = 0, 0

if (eingabe_x, eingabe_y) == ziel_server:
    print("Ziel-Server gefunden! Verbindung hergestellt.")
else:
    print(f"Falscher Server. Ziel liegt bei {ziel_server}.")


# ==================================================
# LEVEL 9 & ENDGEGNER – DAS SHADOWBYTE-NETZWERK
# Konzepte: ALLES kombiniert + Klassen + Funktionen
# ==================================================
print("\n" + "=" * 50)
print("   [ LEVEL 9: SHADOWBYTE-NETZWERK ]")
print("   Ziel: KI ZER0 ausschalten")
print("=" * 50)

# ---- Funktionen ----
# def definiert eine Funktion – wiederverwendbarer Codeblock.

def zeige_status(hname, energie, crypto, inv):
    """Zeigt den aktuellen Hacker-Status an."""
    print(f"\n[ {hname} |{energie} Energie |{crypto} Crypto |{inv} ]")

def berechne_angriff(basis, krit_chance=0.2):
    """Berechnet Angriffsstärke mit Chance auf kritischen Treffer."""
    schaden = random.randint(basis - 3, basis + 5)
    # random.random() liefert eine Zahl zwischen 0.0 und 1.0
    if random.random() < krit_chance:
        schaden *= 2
        print("KRITISCHER ANGRIFF! Doppelter Schaden!")
    return schaden

def repariere_system(energie, max_energie, menge):
    """Repariert das System, aber nicht über max_energie."""
    # min() verhindert, dass wir über das Maximum hinaus heilen.
    neue_energie = min(energie + menge, max_energie)
    gewonnen = neue_energie - energie
    print(f"🔧 System repariert: +{gewonnen} Energie.")
    return neue_energie

# ---- Klasse ----
# Eine Klasse ist ein Bauplan für Objekte mit eigenen Variablen (Attributen)
# und Methoden (Funktionen, die zum Objekt gehören).

class KI:
    def __init__(self, name, leben, angriff):
        # __init__ wird beim Erstellen des Objekts automatisch aufgerufen.
        # self.xyz speichert den Wert im Objekt selbst.
        self.name    = name
        self.leben   = leben
        self.angriff = angriff

    def greift_an(self):
        """Gibt zufälligen Schaden zurück."""
        return random.randint(self.angriff - 4, self.angriff + 4)

    def ist_besiegt(self):
        """Gibt True zurück, wenn die KI keine HP mehr hat."""
        return self.leben <= 0

# ---- Spielaufbau ----
print("\nNeue Session startet...")
hacker_name2 = input("Hacker-Identität: > ")
hacker_energie     = 100
hacker_max_energie = 100
hacker_crypto      = 40
hacker_inventar    = ["Firewall-Bypass", "Reparatur-Patch", "Reparatur-Patch"]

# Server als Tupel (Name, X, Y)
netzwerk_server = [
    ("Proxy-Node",       3,  7),
    ("Black-Market",     6,  2),
    ("ZER0-Mainframe",  99, 99),
]

# Exploit-System als Dictionary
exploit_db = {
    "SQL-Injection": 22,
    "Zero-Day":      35,
    "Ransomware":    28,
}

# Firewalls zum Überwinden
firewall_pool = [
    {"name": "Standard-FW",  "staerke": 30, "crypto": 5,  "drop": "Exploit-Key"},
    {"name": "Elite-FW",     "staerke": 55, "crypto": 12, "drop": "Zero-Day"},
    {"name": "Militär-FW",   "staerke": 45, "crypto": 9,  "drop": "Admin-Token"},
]

# ---- Black-Market ----
print("\nBlack Market online!")
# Preise ändern sich zufällig (Mini-Challenge)
black_market = {
    "Reparatur-Patch":  random.randint(8,  15),
    "Exploit-Key":      random.randint(15, 25),
    "Stealth-Module":   random.randint(20, 35),
}

print("Angebote:")
for item_m, preis_m in black_market.items():
    print(f"  {item_m}: {preis_m} Crypto")

kauf_m = input("Was kaufst du? (oder 'weiter'): > ")
if kauf_m in black_market:
    preis_m_wert = black_market[kauf_m]
    if hacker_crypto >= preis_m_wert:
        hacker_crypto -= preis_m_wert
        if len(hacker_inventar) < 10:  # Inventar-Limit
            hacker_inventar.append(kauf_m)
            print(f"Gekauft! {kauf_m} für {preis_m_wert} Crypto.")
        else:
            print("Inventar voll!")
    else:
        print("Nicht genug Crypto!")
else:
    print("Nichts gekauft.")

# ---- Netzwerk-Reise ----
print(f"\n Netzwerk-Karte:")
for sname, sx, sy in netzwerk_server:
    print(f"  [{sx:02d},{sy:02d}] {sname}")

print(f"\n{hacker_name2} dringt ins Netzwerk ein...\n")

for sname, sx, sy in netzwerk_server:
    if hacker_energie <= 0:
        break

    print(f"\nVerbinde mit: {sname} ({sx},{sy})")

    # Zufälliges Event pro Server
    event = random.choice(["firewall", "backdoor", "ruhig"])

    if event == "firewall":
        fw = random.choice(firewall_pool)
        print(f"{fw['name']} blockiert den Zugang! Stärke: {fw['staerke']}")

        fw_leben = fw["staerke"]

        # Kampf gegen Firewall (while-Schleife)
        while fw_leben > 0 and hacker_energie > 0:
            angriff = berechne_angriff(14)
            fw_leben -= angriff
            gegenschaden = random.randint(5, 15)
            hacker_energie -= gegenschaden
            hacker_energie = max(0, hacker_energie)
            print(f"  Dein Angriff: -{angriff} | Firewall-Gegenschlag: -{gegenschaden} "
                    f"(FW: {max(0,fw_leben)} HP, Du: {hacker_energie} Energie)")

        if fw_leben <= 0:
            print(f"Firewall überwunden! +{fw['crypto']} Crypto")
            hacker_crypto += fw["crypto"]
            # 10% Chance auf Admin-Zugriff (Mini-Challenge)
            if random.random() < 0.1:
                print("ADMIN-ZUGRIFF erlangt! +25 Crypto Bonus!")
                hacker_crypto += 25
            # Drop
            if random.random() < 0.4:
                drop = fw["drop"]
                if len(hacker_inventar) < 10:
                    hacker_inventar.append(drop)
                    print(f"Drop: {drop}")
        else:
            print("Energie erschöpft...")

    elif event == "backdoor":
        bonus = random.randrange(10, 51, 10)
        hacker_crypto += bonus
        print(f"Backdoor gefunden! +{bonus} Crypto")

    else:
        rep = random.randint(10, 20)
        hacker_energie = repariere_system(hacker_energie, hacker_max_energie, rep)

    zeige_status(hacker_name2, hacker_energie, hacker_crypto, hacker_inventar)

# ---- ENDGEGNER: ZER0 ----
print("\n" + "=" * 50)
print("   ⚠  ENDGEGNER: KI \"ZER0\"  ⚠")
print("=" * 50)

if hacker_energie <= 0:
    print("Keine Energie mehr. ZER0 hat gewonnen.")
else:
    zer0 = KI("ZER0", 120, 16)
    print(f"\nZER0 online. HP: {zer0.leben}\n")

    while not zer0.ist_besiegt() and hacker_energie > 0:
        zeige_status(hacker_name2, hacker_energie, hacker_crypto, hacker_inventar)
        print(f"ZER0-HP: {zer0.leben}")
        print("\nAktion wählen:")
        print("1 - Angreifen")
        print("2 - System reparieren (Reparatur-Patch nötig)")
        print("3 - Exploit einsetzen")
        print("4 - Verbindung trennen (fliehen)")

        aktion = input("> ")

        if aktion == "1":
            s = berechne_angriff(14)
            zer0.leben -= s
            print(f"Angriff: {s} Schaden auf ZER0!")

        elif aktion == "2":
            if "Reparatur-Patch" in hacker_inventar:
                hacker_inventar.remove("Reparatur-Patch")
                hacker_energie = repariere_system(hacker_energie, hacker_max_energie, 35)
            else:
                print("Kein Reparatur-Patch mehr!")
                continue  # Runde wiederholen, kein Gegenzug

        elif aktion == "3":
            print("Exploits:", list(exploit_db.keys()))
            gewaehlter = input("Welchen Exploit? > ")
            if gewaehlter in exploit_db:
                ez = exploit_db[gewaehlter]
                zer0.leben -= ez
                print(f"{gewaehlter} eingesetzt! {ez} Schaden!")
            else:
                print("Unbekannter Exploit!")
                continue

        elif aktion == "4":
            print("Verbindung getrennt. ZER0 gewinnt diese Runde.")
            break

        else:
            print("Ungültige Eingabe.")
            continue

        # ZER0 schlägt zurück (wenn noch am Leben)
        if not zer0.ist_besiegt():
            zer0_schaden = zer0.greift_an()
            hacker_energie -= zer0_schaden
            hacker_energie = max(0, hacker_energie)
            print(f"ZER0 Gegenschlag: -{zer0_schaden} Energie!")

    # ---- Ergebnis ----
    print("\n" + "=" * 50)
    if zer0.ist_besiegt():
        print(f"{hacker_name2} hat ZER0 ausgeschaltet!")
        print("Operation ShadowByte: ERFOLG.")
        print(f"\nEndstatistik:")
        print(f"  Energie:         {hacker_energie}")
        print(f"  Crypto:          {hacker_crypto}")
        print(f"  Inventar:        {hacker_inventar}")
    else:
        print(f"{hacker_name2} wurde vom System getrennt.")
        print("ZER0 übernimmt das Netzwerk...")
    print("=" * 50)