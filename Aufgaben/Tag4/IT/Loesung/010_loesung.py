import random

# =========================
# AUFGABE 1 – Der zufällige Support-Fall
# =========================
print("=== Aufgabe 1: Der zufällige Support-Fall ===")
ereignisse = {
    1: "Drucker streikt.",
    2: "WLAN ist beleidigt.",
    3: "Passwort wurde vergessen.",
    4: "Tastatur macht Kunst."
}
zahl = random.randint(1, 4)
print(f"Support-Ticket: {ereignisse[zahl]}")

# =========================
# AUFGABE 2 – Server-Status
# =========================
print("\n=== Aufgabe 2: Server-Status ===")
wert = random.random()
if wert < 0.4:
    print("Server läuft stabil.")
else:
    print("Server macht kurz dramatische Geräusche.")

# =========================
# AUFGABE 3 – Tickets bearbeiten
# =========================
print("\n=== Aufgabe 3: Tickets bearbeiten ===")
tickets = random.randrange(5, 51, 5)
print(f"Neue Tickets eingegangen: {tickets}")

# =========================
# AUFGABE 4 – Download-Geschwindigkeit
# =========================
print("\n=== Aufgabe 4: Download-Geschwindigkeit ===")
geschwindigkeit = round(random.uniform(1.0, 100.0), 2)
print(f"Aktuelle Download-Geschwindigkeit: {geschwindigkeit} MB/s")

# =========================
# AUFGABE 5 – System-Risikoanalyse
# =========================
print("\n=== Aufgabe 5: System-Risikoanalyse ===")
risiko = random.triangular(1, 100, 75)
print(f"System-Risikowert: {risiko:.1f}%")

# =========================
# AUFGABE 6 – Acht Log-Einträge
# =========================
print("\n=== Aufgabe 6: Acht Log-Einträge ===")
logs = []
for i in range(1, 9):
    level = random.randint(1, 9)
    logs.append(level)
    print(f"Log {i}: Level {level}")
print(f"Alle Log-Level: {logs}")

# =========================
# AUFGABE 7 – Bug-Jagd im Code
# =========================
print("\n=== Aufgabe 7: Bug-Jagd im Code ===")
bug_liste = []
for i in range(1, 11):
    bugs = random.randint(1, 12)
    bug_liste.append(bugs)
    print(f"Datei {i}: {bugs} Bugs gefunden")
print(f"Alle Bug-Zahlen: {bug_liste}")
print(f"Gesamtzahl der Bugs: {sum(bug_liste)}")
print(f"Höchste Bug-Zahl: {max(bug_liste)}")

# =========================
# AUFGABE 8 – Router neu starten
# =========================
print("\n=== Aufgabe 8: Router neu starten ===")
print("Haben Sie ihn schon aus- und eingeschaltet?")
versuche = 0
while True:
    versuche += 1
    wurf = random.randint(1, 6)
    print(f"Neustart {versuche}: {wurf}")
    if wurf == 6:
        print(f"Router läuft wieder! Benötigte Neustarts: {versuche}")
        break

# =========================
# AUFGABE 9 – Speicherplatz freiräumen
# =========================
print("\n=== Aufgabe 9: Speicherplatz freiräumen ===")
speicher = 0
runden = 0
while speicher < 100:
    freigabe = random.randint(5, 25)
    speicher += freigabe
    runden += 1
    print(f"Runde {runden}: +{freigabe} GB (Gesamt: {speicher} GB)")
print(f"Ziel erreicht nach {runden} Runden mit {speicher} GB freigeräumt.")

# =========================
# AUFGABE 10 – IT-Inventar
# =========================
print("\n=== Aufgabe 10: IT-Inventar ===")
inventar = ["Laptop", "Maus", "Tastatur", "USB-Stick", "sehr müder Drucker"]
index = random.randint(0, len(inventar) - 1)
print(f"Zufällig ausgewähltes Gerät: {inventar[index]}")

# =========================
# AUFGABE 11 – Netzwerkgeräte
# =========================
print("\n=== Aufgabe 11: Netzwerkgeräte ===")
geraete_tuple = ("Router", "Switch", "Server", "Access Point", "beleidigter Drucker")
index = random.randint(0, len(geraete_tuple) - 1)
print(f"Zufälliges Netzwerkgerät: {geraete_tuple[index]}")

# =========================
# AUFGABE 12 – Einzigartige Fehlermeldungen
# =========================
print("\n=== Aufgabe 12: Einzigartige Fehlermeldungen ===")
moegliche_fehler = ["404 Not Found", "500 Internal Error", "Timeout", "Kernel Panic", "DNS Error"]
fehler_set = set()
for _ in range(10):
    fehler = random.choice(moegliche_fehler)
    fehler_set.add(fehler)
print(f"Aufgetretene Fehlermeldungen: {fehler_set}")
print("Tipp: Ein Set speichert jeden Fehler nur einmal – gleiche Fehler zählen nicht doppelt.")

# =========================
# AUFGABE 13 – Reise durchs Firmennetzwerk
# =========================
print("\n=== Aufgabe 13: Reise durchs Firmennetzwerk ===")
systeme = ["Mailserver", "Datenbank", "Webserver", "Backup-System", "Meme-Ordner"]
besuchte = []
for hop in range(1, 8):
    system = random.choice(systeme)
    besuchte.append(system)
    print(f"Hop {hop}: {system}")
print(f"Systemliste: {besuchte}")
print(f"Datenbank besucht: {besuchte.count('Datenbank')}-mal")
print(f"Meme-Ordner besucht: {'Ja' if 'Meme-Ordner' in besuchte else 'Nein'}")

# =========================
# AUFGABE 14 – Kampf gegen den Bug-Golem
# =========================
print("\n=== Aufgabe 14: Kampf gegen den Bug-Golem ===")
golem_hp = 50
angriffe = []
while golem_hp > 0:
    schaden = random.randint(5, 15)
    angriffe.append(schaden)
    golem_hp -= schaden
    print(f"Angriff {len(angriffe)}: {schaden} Schaden (Golem HP: {max(0, golem_hp)})")
print(f"Anzahl der Angriffe: {len(angriffe)}")
print(f"Angriffsliste: {angriffe}")
print(f"Stärkster Angriff: {max(angriffe)}")

# =========================
# AUFGABE 15 – IT-Einkauf
# =========================
print("\n=== Aufgabe 15: IT-Einkauf ===")
preise = []
for i in range(1, 6):
    preis = round(random.uniform(1.5, 99.9), 2)
    preise.append(preis)
    print(f"Gerät {i}: {preis} Credits")
durchschnitt = round(sum(preise) / len(preise), 2)
print(f"Durchschnittspreis: {durchschnitt} Credits")

# =========================
# AUFGABE 16 – Serverraum-Generator
# =========================
print("\n=== Aufgabe 16: Serverraum-Generator ===")
bereiche_tuple = ("Rack", "Switch-Schrank", "Backup-Ecke", "Leerer Platz", "Raum voller Kabelsalat")
serverraum = []
for i in range(1, 11):
    bereich = random.choice(bereiche_tuple)
    serverraum.append(bereich)
    print(f"Bereich {i}: {bereich}")
print(f"Alle Bereiche: {serverraum}")
print(f"Anzahl Racks: {serverraum.count('Rack')}")
print(f"Anzahl Switch-Schränke: {serverraum.count('Switch-Schrank')}")

# =========================
# AUFGABE 17 – Duell gegen die Absturz-KI
# =========================
print("\n=== Aufgabe 17: Duell gegen die Absturz-KI ===")
ki_hp = 100
admin_hp = 80
runde = 0
while ki_hp > 0 and admin_hp > 0:
    runde += 1
    admin_schaden = random.randint(8, 18)
    ki_schaden = int(random.triangular(5, 20, 10))
    ki_hp -= admin_schaden
    admin_hp -= ki_schaden
    print(f"Runde {runde}: Admin -{admin_schaden} | KI -{ki_schaden} "
            f"(KI HP: {max(0, ki_hp)}, Admin HP: {max(0, admin_hp)})")
if ki_hp <= 0 and admin_hp <= 0:
    print("Unentschieden – System und Admin stürzen gleichzeitig ab!")
elif ki_hp <= 0:
    print("💻 Der Admin hat gewonnen – Bug erfolgreich behoben!")
else:
    print("🤖 Die Absturz-KI hat gewonnen – Neustart empfohlen.")

# =========================
# AUFGABE 18 – Loot-System im Serverraum
# =========================
print("\n=== Aufgabe 18: Loot-System im Serverraum ===")
moegliche_funde = ["RAM", "SSD", "Netzwerkkabel", "Legendäre Gummiente"]
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
# AUFGABE 19 – Mini-IT-Rollenspiel
# =========================
print("\n=== Aufgabe 19: Mini-IT-Rollenspiel ===")
leben = 100
credits = 0
inventar = []
besuchte_systeme = set()
systeme = ["Mailserver", "Datenbank", "Webserver", "Backup-System", "Firewall", "Cloud", "Meme-Ordner"]
ereignisse = ["Angriff", "Fund", "Fehler", "Shop", "Wartung"]
runde = 0

while leben > 0 and credits < 100:
    runde += 1
    system = random.choice(systeme)
    besuchte_systeme.add(system)
    ereignis = random.choice(ereignisse)

    if ereignis == "Angriff":
        schaden = random.randint(5, 20)
        leben -= schaden
        print(f"Runde {runde} | {system}: Cyberangriff! -{schaden} HP (Leben: {max(0, leben)})")
    elif ereignis == "Fund":
        fund = random.randrange(5, 51, 5)
        credits += fund
        inventar.append("Datenfund")
        print(f"Runde {runde} | {system}: Datenfund! +{fund} Credits (Credits: {credits})")
    elif ereignis == "Fehler":
        schaden = int(random.triangular(1, 15, 5))
        leben -= schaden
        print(f"Runde {runde} | {system}: Systemfehler! -{schaden} HP (Leben: {max(0, leben)})")
    elif ereignis == "Shop":
        preis = round(random.uniform(1.0, 10.0), 2)
        inventar.append("Tool")
        print(f"Runde {runde} | {system}: Tool für {preis} Credits gekauft.")
    elif ereignis == "Wartung":
        heilung = random.randint(5, 15)
        leben = min(100, leben + heilung)
        print(f"Runde {runde} | {system}: Wartung! +{heilung} HP (Leben: {leben})")

print("\n--- Admin-Statusbericht ---")
print(f"Leben: {max(0, leben)}")
print(f"Credits: {credits}")
print(f"Inventar: {inventar}")
print(f"Besuchte Systeme: {besuchte_systeme}")
if leben <= 0:
    print("💀 Der Admin ist abgestürzt.")
else:
    print("🏆 100 Credits erreicht – Feierabend verdient!")

# =========================
# AUFGABE 20 – Der verfluchte IT-Simulator
# =========================
print("\n=== Aufgabe 20: Der verfluchte IT-Simulator ===")
admin_namen = ["root_Rita", "sudo_Sam", "Admin_Achim", "patch_Paula", "reboot_Rolf"]
mission_systeme = ["Prod-Server", "Dev-Umgebung", "Backup-Cluster", "Firewall-Node", "Kaffeemaschinen-API"]
alle_missionen = []
erfolgreiche = []
niederlagen = []
besuchte_mission_systeme = set()

for _ in range(100):
    name = random.choice(admin_namen)
    system = random.choice(mission_systeme)
    dauer = random.randint(1, 30)
    gefahr = round(random.uniform(1.0, 10.0), 1)
    belohnung = random.randrange(0, 201, 10)
    erfolg = random.random() > 0.4

    besuchte_mission_systeme.add(system)
    mission = {
        "admin": name, "system": system, "dauer": dauer,
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
print(f"Durchschnittliche Belohnung: {durchschnitt} Credits")
if bester_fund:
    print(f"Bester Fund: {bester_fund['admin']} an {bester_fund['system']} "
            f"mit {bester_fund['belohnung']} Credits")
print(f"Alle besuchten Systeme: {besuchte_mission_systeme}")
if lustigste_niederlage:
    print(f"Lustigste Niederlage: {lustigste_niederlage['admin']} scheiterte an "
            f"{lustigste_niederlage['system']} nach {lustigste_niederlage['dauer']} Stunden "
            f"(Gefahr: {lustigste_niederlage['gefahr']})")