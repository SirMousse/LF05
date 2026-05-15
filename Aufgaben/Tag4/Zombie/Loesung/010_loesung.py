import random

# =========================
# AUFGABE 1 – Zombie entdeckt!
# =========================
print("=== Aufgabe 1: Zombie entdeckt! ===")
zombies = {
    1: "Langsamer Zombie",
    2: "Rennender Zombie",
    3: "Zombie-Huhn",
    4: "Sehr verwirrter Wissenschaftler"
}
zahl = random.randint(1, 4)
print(f"Achtung: {zombies[zahl]} in Sicht!")

# =========================
# AUFGABE 2 – Fluchtversuch
# =========================
print("\n=== Aufgabe 2: Fluchtversuch ===")
wert = random.random()
if wert < 0.5:
    print("Du entkommst den Zombies!")
else:
    print("Ein Zombie klaut deinen Snack.")

# =========================
# AUFGABE 3 – Vorräte finden
# =========================
print("\n=== Aufgabe 3: Vorräte finden ===")
vorraete = random.randrange(10, 101, 10)
print(f"Gefundene Vorräte: {vorraete} Einheiten!")

# =========================
# AUFGABE 4 – Waffen-Stärke
# =========================
print("\n=== Aufgabe 4: Waffen-Stärke ===")
staerke = round(random.uniform(1.0, 10.0), 2)
print(f"Waffen-Stärke: {staerke}")

# =========================
# AUFGABE 5 – Risiko-Scanner
# =========================
print("\n=== Aufgabe 5: Risiko-Scanner ===")
chance = random.triangular(1, 100, 80)
print(f"Überlebens-Chance laut Scanner: {chance:.1f}%")

# =========================
# AUFGABE 6 – Training im Bunker
# =========================
print("\n=== Aufgabe 6: Training im Bunker ===")
training = []
for i in range(1, 9):
    ep = random.randint(1, 9)
    training.append(ep)
    print(f"Training {i}: +{ep} EP")
print(f"Alle Trainingswerte: {training}")

# =========================
# AUFGABE 7 – Zombie-Kampf
# =========================
print("\n=== Aufgabe 7: Zombie-Kampf ===")
schaden_liste = []
for i in range(1, 11):
    schaden = random.randint(1, 12)
    schaden_liste.append(schaden)
    print(f"Runde {i}: {schaden} Schaden")
print(f"Alle Schadenswerte: {schaden_liste}")
print(f"Gesamtschaden: {sum(schaden_liste)}")
print(f"Stärkster Treffer: {max(schaden_liste)}")

# =========================
# AUFGABE 8 – Bunker-Tür öffnen
# =========================
print("\n=== Aufgabe 8: Bunker-Tür öffnen ===")
versuche = 0
while True:
    versuche += 1
    wurf = random.randint(1, 6)
    print(f"Versuch {versuche}: {wurf}")
    if wurf == 6:
        print(f"Bunker-Tür offen! Benötigte Versuche: {versuche}")
        break

# =========================
# AUFGABE 9 – Essen sammeln
# =========================
print("\n=== Aufgabe 9: Essen sammeln ===")
essen = 0
runden = 0
while essen < 100:
    fund = random.randint(5, 25)
    essen += fund
    runden += 1
    print(f"Runde {runden}: +{fund} Nahrung (Gesamt: {essen})")
print(f"Vorratsziel erreicht nach {runden} Runden mit {essen} Einheiten!")

# =========================
# AUFGABE 10 – Überlebenden-Inventar
# =========================
print("\n=== Aufgabe 10: Überlebenden-Inventar ===")
inventar = ["Taschenlampe", "Axt", "Erste-Hilfe-Set", "Funkgerät", "leicht verdächtige Bohnen"]
index = random.randint(0, len(inventar) - 1)
print(f"Du greifst in den Rucksack: {inventar[index]}")

# =========================
# AUFGABE 11 – Arten von Zombies
# =========================
print("\n=== Aufgabe 11: Arten von Zombies ===")
zombie_tuple = ("Läufer", "Tank-Zombie", "Schleicher", "Radioaktiver Zombie", "Zombie-Clown")
index = random.randint(0, len(zombie_tuple) - 1)
print(f"Zombie-Typ identifiziert: {zombie_tuple[index]}!")

# =========================
# AUFGABE 12 – Seltene Funde
# =========================
print("\n=== Aufgabe 12: Seltene Funde ===")
moegliche_funde = ["Batterien", "Konservendose", "Karte", "Verbandskasten", "Funkgerät"]
fund_set = set()
for _ in range(10):
    fund = random.choice(moegliche_funde)
    fund_set.add(fund)
print(f"Gefundene Gegenstände: {fund_set}")
print("Tipp: Ein Set speichert jeden Fund nur einmal – doppelte Konserven zählen nicht doppelt.")

# =========================
# AUFGABE 13 – Reise durch die Ruinenstadt
# =========================
print("\n=== Aufgabe 13: Reise durch die Ruinenstadt ===")
orte = ["Krankenhaus", "Supermarkt", "Polizeistation", "Bunker", "Verlassene Schule"]
reise = []
for tag in range(1, 8):
    ort = random.choice(orte)
    reise.append(ort)
    print(f"Tag {tag}: {ort}")
print(f"Ortsliste: {reise}")
print(f"Bunker besucht: {reise.count('Bunker')}-mal")
print(f"Krankenhaus besucht: {'Ja' if 'Krankenhaus' in reise else 'Nein'}")

# =========================
# AUFGABE 14 – Kampf gegen den Zombie-Boss
# =========================
print("\n=== Aufgabe 14: Kampf gegen den Zombie-Boss ===")
boss_hp = 50
angriffe = []
while boss_hp > 0:
    schaden = random.randint(5, 15)
    angriffe.append(schaden)
    boss_hp -= schaden
    print(f"Angriff {len(angriffe)}: {schaden} Schaden (Boss HP: {max(0, boss_hp)})")
print(f"Anzahl der Angriffe: {len(angriffe)}")
print(f"Angriffsliste: {angriffe}")
print(f"Stärkster Angriff: {max(angriffe)}")

# =========================
# AUFGABE 15 – Handel im Bunker
# =========================
print("\n=== Aufgabe 15: Handel im Bunker ===")
preise = []
for i in range(1, 6):
    preis = round(random.uniform(1.5, 99.9), 2)
    preise.append(preis)
    print(f"Artikel {i}: {preis} Kronkorken")
durchschnitt = round(sum(preise) / len(preise), 2)
print(f"Durchschnittspreis: {durchschnitt} Kronkorken")

# =========================
# AUFGABE 16 – Zufälliger Bunker-Generator
# =========================
print("\n=== Aufgabe 16: Zufälliger Bunker-Generator ===")
raumtypen = ("Schlafraum", "Vorratsraum", "Waffenlager", "Leerer Raum", "Raum voller Zombiesocken")
bunker = []
for i in range(1, 11):
    raum = random.choice(raumtypen)
    bunker.append(raum)
    print(f"Raum {i}: {raum}")
print(f"Alle Räume: {bunker}")
print(f"Anzahl Schlafräume: {bunker.count('Schlafraum')}")
print(f"Anzahl Waffenlager: {bunker.count('Waffenlager')}")

# =========================
# AUFGABE 17 – Duell gegen den Mutanten
# =========================
print("\n=== Aufgabe 17: Duell gegen den Mutanten ===")
mutant_hp = 100
ueber_hp = 80
runde = 0
while mutant_hp > 0 and ueber_hp > 0:
    runde += 1
    ueber_schaden = random.randint(8, 18)
    mutant_schaden = int(random.triangular(5, 20, 10))
    mutant_hp -= ueber_schaden
    ueber_hp -= mutant_schaden
    print(f"Runde {runde}: Überlebender -{ueber_schaden} | Mutant -{mutant_schaden} "
            f"(Mutant HP: {max(0, mutant_hp)}, Überlebender HP: {max(0, ueber_hp)})")
if mutant_hp <= 0 and ueber_hp <= 0:
    print("Unentschieden – beide fallen ins Nichts!")
elif mutant_hp <= 0:
    print("🪓 Der Überlebende hat gewonnen – Zone gesichert!")
else:
    print("☣️  Der Mutant triumphiert – Rückzug empfohlen!")

# =========================
# AUFGABE 18 – Loot-System im verlassenen Haus
# =========================
print("\n=== Aufgabe 18: Loot-System im verlassenen Haus ===")
moegliche_items = ["Munition", "Wasser", "Medizin", "Legendäre Bohnen"]
fund_liste = []
fund_set = set()
for i in range(1, 21):
    item = random.choice(moegliche_items)
    fund_liste.append(item)
    fund_set.add(item)
print(f"Komplette Fundliste: {fund_liste}")
print(f"Einzigartige Funde: {fund_set}")
print(f"Anzahl unterschiedlicher Funde: {len(fund_set)}")

# =========================
# AUFGABE 19 – Mini-Zombie-Rollenspiel
# =========================
print("\n=== Aufgabe 19: Mini-Zombie-Rollenspiel ===")
leben = 100
vorraete = 0
inventar = []
besuchte_orte = set()
orte = ["Krankenhaus", "Supermarkt", "Polizeistation", "Bunker", "Verlassene Schule", "Tankstelle", "Dach"]
ereignisse = ["Angriff", "Fund", "Falle", "Tausch", "Rast"]
runde = 0

while leben > 0 and vorraete < 100:
    runde += 1
    ort = random.choice(orte)
    besuchte_orte.add(ort)
    ereignis = random.choice(ereignisse)

    if ereignis == "Angriff":
        schaden = random.randint(5, 20)
        leben -= schaden
        print(f"Runde {runde} | {ort}: Zombie-Angriff! -{schaden} HP (Leben: {max(0, leben)})")
    elif ereignis == "Fund":
        fund = random.randrange(5, 51, 5)
        vorraete += fund
        inventar.append("Vorratsfund")
        print(f"Runde {runde} | {ort}: Vorräte gefunden! +{fund} 🥫 (Vorräte: {vorraete})")
    elif ereignis == "Falle":
        schaden = int(random.triangular(1, 15, 5))
        leben -= schaden
        print(f"Runde {runde} | {ort}: Falle ausgelöst! -{schaden} HP (Leben: {max(0, leben)})")
    elif ereignis == "Tausch":
        preis = round(random.uniform(1.0, 10.0), 2)
        inventar.append("Tauschartikel")
        print(f"Runde {runde} | {ort}: Tausch für {preis} Kronkorken abgeschlossen.")
    elif ereignis == "Rast":
        heilung = random.randint(5, 15)
        leben = min(100, leben + heilung)
        print(f"Runde {runde} | {ort}: Sichere Rast! +{heilung} HP (Leben: {leben})")

print("\n--- Überlebens-Bericht ---")
print(f"Leben: {max(0, leben)}")
print(f"Vorräte: {vorraete}")
print(f"Inventar: {inventar}")
print(f"Besuchte Orte: {besuchte_orte}")
if leben <= 0:
    print("💀 Der Überlebende ist gefallen.")
else:
    print("🏕️  100 Vorräte gesichert – Bunker ist versorgt!")

# =========================
# AUFGABE 20 – Der verfluchte Zombie-Simulator
# =========================
print("\n=== Aufgabe 20: Der verfluchte Zombie-Simulator ===")
namen = ["Max Überleben", "Sara Starkwind", "Rico Robusto", "Lena Laststand", "Kai Kronkorken"]
mission_orte = ["Innenstadt-Ruine", "Verlassene Farm", "U-Bahn-Tunnel", "Militärbasis", "Einkaufszentrum"]
alle_missionen = []
erfolgreiche = []
niederlagen = []
besuchte_mission_orte = set()

for _ in range(100):
    name = random.choice(namen)
    ort = random.choice(mission_orte)
    dauer = random.randint(1, 30)
    gefahr = round(random.uniform(1.0, 10.0), 1)
    belohnung = random.randrange(0, 201, 10)
    erfolg = random.random() > 0.4

    besuchte_mission_orte.add(ort)
    mission = {
        "held": name, "ort": ort, "dauer": dauer,
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
print(f"Durchschnittliche Belohnung: {durchschnitt} Kronkorken")
if bester_fund:
    print(f"Bester Fund: {bester_fund['held']} in {bester_fund['ort']} "
            f"mit {bester_fund['belohnung']} Kronkorken")
print(f"Alle besuchten Orte: {besuchte_mission_orte}")
if lustigste_niederlage:
    print(f"Lustigste Niederlage: {lustigste_niederlage['held']} scheiterte in "
            f"{lustigste_niederlage['ort']} nach {lustigste_niederlage['dauer']} Tagen "
            f"(Gefahr: {lustigste_niederlage['gefahr']})")