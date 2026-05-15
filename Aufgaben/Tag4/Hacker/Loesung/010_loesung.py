import random

# =========================
# AUFGABE 1 – Der geheime Login-Code
# =========================
print("=== Aufgabe 1: Der geheime Login-Code ===")
code = random.randint(1000, 9999)
print(f"Dein geheimer Hacker-Code: {code}")

# =========================
# AUFGABE 2 – Firewall-Zufallstest
# =========================
print("\n=== Aufgabe 2: Firewall-Zufallstest ===")
wert = random.random()
if wert < 0.3:
    print("Firewall entdeckt!")
else:
    print("Du bist unbemerkt geblieben.")

# =========================
# AUFGABE 3 – Datenpakete scannen
# =========================
print("\n=== Aufgabe 3: Datenpakete scannen ===")
paket = random.randrange(50, 501, 50)
print(f"Gescanntes Datenpaket: {paket} Bytes")

# =========================
# AUFGABE 4 – Netzwerkgeschwindigkeit
# =========================
print("\n=== Aufgabe 4: Netzwerkgeschwindigkeit ===")
geschwindigkeit = round(random.uniform(10.0, 1000.0), 2)
print(f"Aktuelle Downloadgeschwindigkeit: {geschwindigkeit} Mbit/s")

# =========================
# AUFGABE 5 – KI-Risikoanalyse
# =========================
print("\n=== Aufgabe 5: KI-Risikoanalyse ===")
risiko = random.triangular(1, 100, 90)
print(f"KI-Risikowert: {risiko:.1f}%")

# =========================
# AUFGABE 6 – Passwort-Generator
# =========================
print("\n=== Aufgabe 6: Passwort-Generator ===")
passwort = ""
for _ in range(8):
    passwort += str(random.randint(0, 9))
print(f"Generiertes Passwort: {passwort}")

# =========================
# AUFGABE 7 – Virus-Angriffe speichern
# =========================
print("\n=== Aufgabe 7: Virus-Angriffe speichern ===")
schaden_liste = []
for i in range(1, 11):
    schaden = random.randint(1, 50)
    schaden_liste.append(schaden)
    print(f"Angriff {i}: {schaden} Schaden")
print(f"Alle Schäden: {schaden_liste}")
print(f"Gesamtschaden: {sum(schaden_liste)}")
print(f"Höchster Schaden: {max(schaden_liste)}")

# =========================
# AUFGABE 8 – Server knacken
# =========================
print("\n=== Aufgabe 8: Server knacken ===")
versuche = 0
while True:
    versuche += 1
    wurf = random.randint(1, 6)
    print(f"Versuch {versuche}: {wurf}")
    if wurf == 6:
        print(f"Server geknackt! Benötigte Versuche: {versuche}")
        break

# =========================
# AUFGABE 9 – Kryptowährung farmen
# =========================
print("\n=== Aufgabe 9: Kryptowährung farmen ===")
coins = 0
runden = 0
while coins < 100:
    gewinn = random.randint(5, 25)
    coins += gewinn
    runden += 1
    print(f"Runde {runden}: +{gewinn} Coins (Gesamt: {coins})")
print(f"Farming beendet nach {runden} Runden mit {coins} Coins.")

# =========================
# AUFGABE 10 – Hacker-Inventar
# =========================
print("\n=== Aufgabe 10: Hacker-Inventar ===")
inventar = ["Laptop", "USB-Stick", "Energy Drink", "Gummiente", "Linux-CD"]
index = random.randint(0, len(inventar) - 1)
print(f"Zufällig ausgewähltes Item: {inventar[index]}")

# =========================
# AUFGABE 11 – Sicherheitsprogramme
# =========================
print("\n=== Aufgabe 11: Sicherheitsprogramme ===")
programme = ("Firewall", "Antivirus", "Trojaner-Scanner", "Passwortschutz")
index = random.randint(0, len(programme) - 1)
print(f"Aktives Sicherheitsprogramm: {programme[index]}")

# =========================
# AUFGABE 12 – Seltene Datenfunde
# =========================
print("\n=== Aufgabe 12: Seltene Datenfunde ===")
moegliche_dateien = ["geheim.txt", "passwort.db", "hack.exe", "notizen.log", "foto.jpg"]
gefundene_dateien = set()
for _ in range(10):
    datei = random.choice(moegliche_dateien)
    gefundene_dateien.add(datei)
print(f"Gefundene Dateien: {gefundene_dateien}")
print("Tipp: Ein Set speichert jeden Eintrag nur einmal – Duplikate werden ignoriert.")

# =========================
# AUFGABE 13 – Reise durchs Darknet
# =========================
print("\n=== Aufgabe 13: Reise durchs Darknet ===")
server_liste = ["EU-Server", "US-Server", "Geheimserver", "Testserver", "Meme-Server"]
besuchte_server = []
for tag in range(1, 8):
    server = random.choice(server_liste)
    besuchte_server.append(server)
    print(f"Hop {tag}: {server}")
print(f"Serverliste: {besuchte_server}")
print(f"Geheimserver besucht: {besuchte_server.count('Geheimserver')}-mal")
print(f"Meme-Server besucht: {'Ja' if 'Meme-Server' in besuchte_server else 'Nein'}")

# =========================
# AUFGABE 14 – Kampf gegen die Killer-KI
# =========================
print("\n=== Aufgabe 14: Kampf gegen die Killer-KI ===")
ki_hp = 50
angriffe = []
while ki_hp > 0:
    schaden = random.randint(5, 15)
    angriffe.append(schaden)
    ki_hp -= schaden
    print(f"Angriff {len(angriffe)}: {schaden} Schaden (KI HP: {max(0, ki_hp)})")
print(f"Anzahl der Angriffe: {len(angriffe)}")
print(f"Angriffsliste: {angriffe}")
print(f"Stärkster Angriff: {max(angriffe)}")

# =========================
# AUFGABE 15 – Schwarzer Markt
# =========================
print("\n=== Aufgabe 15: Schwarzer Markt ===")
preise = []
for i in range(1, 6):
    preis = round(random.uniform(1.5, 99.9), 2)
    preise.append(preis)
    print(f"Tool {i}: {preis} Coins")
durchschnitt = round(sum(preise) / len(preise), 2)
print(f"Durchschnittspreis: {durchschnitt} Coins")

# =========================
# AUFGABE 16 – Netzwerk-Generator
# =========================
print("\n=== Aufgabe 16: Netzwerk-Generator ===")
servertypen = ("Firewall", "Datenbank", "KI-Knoten", "Leerer Server", "Verdächtige Gummiente")
netzwerk = []
for i in range(1, 11):
    server = random.choice(servertypen)
    netzwerk.append(server)
    print(f"Server {i}: {server}")
print(f"Alle Server: {netzwerk}")
print(f"Anzahl Firewalls: {netzwerk.count('Firewall')}")
print(f"Anzahl Datenbanken: {netzwerk.count('Datenbank')}")

# =========================
# AUFGABE 17 – Hacker gegen Super-KI
# =========================
print("\n=== Aufgabe 17: Hacker gegen Super-KI ===")
ki_hp = 100
hacker_hp = 80
runde = 0
while ki_hp > 0 and hacker_hp > 0:
    runde += 1
    hacker_schaden = random.randint(8, 18)
    ki_schaden = int(random.triangular(5, 20, 10))
    ki_hp -= hacker_schaden
    hacker_hp -= ki_schaden
    print(f"Runde {runde}: Hacker -{hacker_schaden} | KI -{ki_schaden} "
            f"(KI HP: {max(0, ki_hp)}, Hacker HP: {max(0, hacker_hp)})")
if ki_hp <= 0 and hacker_hp <= 0:
    print("Unentschieden – beide crashen gleichzeitig!")
elif ki_hp <= 0:
    print("💻 Der Hacker hat gewonnen!")
else:
    print("🤖 Die Super-KI hat gewonnen!")

# =========================
# AUFGABE 18 – Loot-System im Darknet
# =========================
print("\n=== Aufgabe 18: Loot-System im Darknet ===")
moegliche_funde = ["Bitcoin", "Passwort", "Geheime Datei", "Legendäre Gummiente"]
fund_liste = []
fund_set = set()
for i in range(1, 21):
    fund = random.choice(moegliche_funde)
    fund_liste.append(fund)
    fund_set.add(fund)
print(f"Komplette Fundliste: {fund_liste}")
print(f"Einzigartige Funde: {fund_set}")
print(f"Anzahl unterschiedlicher Funde: {len(fund_set)}")

# =========================
# AUFGABE 19 – Mini-Hacker-Rollenspiel
# =========================
print("\n=== Aufgabe 19: Mini-Hacker-Rollenspiel ===")
leben = 100
coins = 0
inventar = []
besuchte_server = set()
server = ["EU-Server", "US-Server", "Geheimserver", "Darknet-Hub", "Zombie-Netz", "Meme-Server"]
ereignisse = ["Angriff", "Fund", "Falle", "Markt", "Reparatur"]
runde = 0

while leben > 0 and coins < 100:
    runde += 1
    s = random.choice(server)
    besuchte_server.add(s)
    ereignis = random.choice(ereignisse)

    if ereignis == "Angriff":
        schaden = random.randint(5, 20)
        leben -= schaden
        print(f"Runde {runde} | {s}: Gegenangriff! -{schaden} Leben (Leben: {max(0, leben)})")
    elif ereignis == "Fund":
        fund = random.randrange(5, 51, 5)
        coins += fund
        inventar.append("Datenfund")
        print(f"Runde {runde} | {s}: Datenfund! +{fund} Coins (Coins: {coins})")
    elif ereignis == "Falle":
        schaden = int(random.triangular(1, 15, 5))
        leben -= schaden
        print(f"Runde {runde} | {s}: Honeypot-Falle! -{schaden} Leben (Leben: {max(0, leben)})")
    elif ereignis == "Markt":
        preis = round(random.uniform(1.0, 10.0), 2)
        inventar.append("Exploit-Tool")
        print(f"Runde {runde} | {s}: Exploit-Tool für {preis} Coins gekauft.")
    elif ereignis == "Reparatur":
        heilung = random.randint(5, 15)
        leben = min(100, leben + heilung)
        print(f"Runde {runde} | {s}: System repariert! +{heilung} Leben (Leben: {leben})")

print("\n--- Hacker-Statusbericht ---")
print(f"Leben: {max(0, leben)}")
print(f"Coins: {coins}")
print(f"Inventar: {inventar}")
print(f"Besuchte Server: {besuchte_server}")
if leben <= 0:
    print("💀 Der Hacker wurde eliminiert.")
else:
    print("🏆 100 Coins erreicht – Mission erfüllt!")

# =========================
# AUFGABE 20 – Der verfluchte Hacker-Simulator
# =========================
print("\n=== Aufgabe 20: Der verfluchte Hacker-Simulator ===")
hacker_namen = ["h4x0r_bob", "ZeroDay_Zoe", "Phantom_Pete", "GlitchQueen", "NullByte_Niko"]
mission_server = ["Pentagon-Spiegel", "Meme-Archiv", "Käse-Datenbank", "KI-Labor", "Gummiente-Server"]
alle_missionen = []
erfolgreiche = []
niederlagen = []
besuchte_mission_server = set()

for _ in range(100):
    name = random.choice(hacker_namen)
    server_ziel = random.choice(mission_server)
    dauer = random.randint(1, 30)
    gefahr = round(random.uniform(1.0, 10.0), 1)
    belohnung = random.randrange(0, 201, 10)
    erfolg = random.random() > 0.4

    besuchte_mission_server.add(server_ziel)
    mission = {
        "hacker": name, "server": server_ziel, "dauer": dauer,
        "gefahr": gefahr, "belohnung": belohnung, "erfolg": erfolg
    }
    alle_missionen.append(mission)
    if erfolg:
        erfolgreiche.append(mission)
    else:
        niederlagen.append(mission)

durchschnitt = round(
    sum(m["belohnung"] for m in erfolgreiche) / len(erfolgreiche), 2
) if erfolgreiche else 0

bester_fund = max(erfolgreiche, key=lambda m: m["belohnung"]) if erfolgreiche else None
lustigste_niederlage = random.choice(niederlagen) if niederlagen else None

print(f"Erfolgreiche Missionen: {len(erfolgreiche)} / 100")
print(f"Durchschnittliche Belohnung: {durchschnitt} Coins")
if bester_fund:
    print(f"Bester Fund: {bester_fund['hacker']} hackte {bester_fund['server']} "
            f"für {bester_fund['belohnung']} Coins")
print(f"Alle besuchten Server: {besuchte_mission_server}")
if lustigste_niederlage:
    print(f"Lustigste Niederlage: {lustigste_niederlage['hacker']} scheiterte an "
            f"{lustigste_niederlage['server']} nach {lustigste_niederlage['dauer']} Stunden "
            f"(Gefahr: {lustigste_niederlage['gefahr']})")