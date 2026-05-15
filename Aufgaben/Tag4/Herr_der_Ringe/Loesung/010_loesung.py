import random

# =========================
# AUFGABE 1 – Der Ring entscheidet
# =========================
print("=== Aufgabe 1: Der Ring entscheidet ===")
ereignisse = {
    1: "Der Ring flüstert.",
    2: "Ein Hobbit stolpert.",
    3: "Ein Ork niest.",
    4: "Gandalf schaut streng."
}
zahl = random.randint(1, 4)
print(ereignisse[zahl])

# =========================
# AUFGABE 2 – Schicksal in Mordor
# =========================
print("\n=== Aufgabe 2: Schicksal in Mordor ===")
wert = random.random()
if wert < 0.4:
    print("Du schleichst unbemerkt vorbei.")
else:
    print("Ein Ork ruft: Wer hat da Kartoffeln gesagt?")

# =========================
# AUFGABE 3 – Lembas-Brot sammeln
# =========================
print("\n=== Aufgabe 3: Lembas-Brot sammeln ===")
lembas = random.randrange(5, 51, 5)
print(f"Die Gefährten finden {lembas} Lembas-Brote!")

# =========================
# AUFGABE 4 – Elbischer Zauberwert
# =========================
print("\n=== Aufgabe 4: Elbischer Zauberwert ===")
zauberwert = round(random.uniform(1.0, 10.0), 2)
print(f"Elbische Zauberstärke: {zauberwert}")

# =========================
# AUFGABE 5 – Palantir-Vorhersage
# =========================
print("\n=== Aufgabe 5: Palantir-Vorhersage ===")
vorhersage = random.triangular(1, 100, 70)
print(f"Der Palantir zeigt: {vorhersage:.1f}% Erfolgswahrscheinlichkeit.")

# =========================
# AUFGABE 6 – Pfeile von Legolas
# =========================
print("\n=== Aufgabe 6: Pfeile von Legolas ===")
pfeile = []
for i in range(1, 9):
    schaden = random.randint(1, 9)
    pfeile.append(schaden)
    print(f"Pfeil {i}: {schaden} Schaden")
print(f"Alle Treffer: {pfeile}")

# =========================
# AUFGABE 7 – Ork-Kampf in Moria
# =========================
print("\n=== Aufgabe 7: Ork-Kampf in Moria ===")
schaden_liste = []
for i in range(1, 11):
    schaden = random.randint(1, 12)
    schaden_liste.append(schaden)
    print(f"Runde {i}: {schaden} Schaden")
print(f"Alle Schadenswerte: {schaden_liste}")
print(f"Gesamtschaden: {sum(schaden_liste)}")
print(f"Stärkster Treffer: {max(schaden_liste)}")

# =========================
# AUFGABE 8 – Tor von Moria öffnen
# =========================
print("\n=== Aufgabe 8: Tor von Moria öffnen ===")
print("Sprich Freund und tritt ein!")
versuche = 0
while True:
    versuche += 1
    wurf = random.randint(1, 6)
    print(f"Versuch {versuche}: {wurf}")
    if wurf == 6:
        print(f"Das Tor öffnet sich! Benötigte Versuche: {versuche}")
        break

# =========================
# AUFGABE 9 – Reiseproviant sammeln
# =========================
print("\n=== Aufgabe 9: Reiseproviant sammeln ===")
vorraete = 0
runden = 0
while vorraete < 100:
    fund = random.randint(5, 25)
    vorraete += fund
    runden += 1
    print(f"Runde {runden}: +{fund} Vorräte (Gesamt: {vorraete})")
print(f"Ziel erreicht nach {runden} Runden mit {vorraete} Vorräten.")

# =========================
# AUFGABE 10 – Gefährten-Inventar
# =========================
print("\n=== Aufgabe 10: Gefährten-Inventar ===")
inventar = ["Ring", "Schwert", "Lembas", "Elbenumhang", "verdächtige Kartoffel"]
index = random.randint(0, len(inventar) - 1)
print(f"Du trägst: {inventar[index]}")

# =========================
# AUFGABE 11 – Wesen Mittelerdes
# =========================
print("\n=== Aufgabe 11: Wesen Mittelerdes ===")
wesen_tuple = ("Hobbit", "Elb", "Zwerg", "Ork", "Balrog", "sehr beleidigter Ent")
index = random.randint(0, len(wesen_tuple) - 1)
print(f"Du begegnest einem: {wesen_tuple[index]}!")

# =========================
# AUFGABE 12 – Seltene Funde im Auenland
# =========================
print("\n=== Aufgabe 12: Seltene Funde im Auenland ===")
moegliche_funde = ["Pfeifenkraut", "Mondstein", "Zwergengold", "Elbenpfeil", "Mithrilschuppe"]
fund_set = set()
for _ in range(10):
    fund = random.choice(moegliche_funde)
    fund_set.add(fund)
print(f"Gefundene Gegenstände: {fund_set}")
print("Tipp: Ein Set speichert jeden Wert nur einmal – wie ein Ring, der nur einen Meister kennt.")

# =========================
# AUFGABE 13 – Reise durch Mittelerde
# =========================
print("\n=== Aufgabe 13: Reise durch Mittelerde ===")
orte = ["Auenland", "Bruchtal", "Moria", "Rohan", "Mordor"]
reise = []
for tag in range(1, 8):
    ort = random.choice(orte)
    reise.append(ort)
    print(f"Tag {tag}: {ort}")
print(f"Ortsliste: {reise}")
print(f"Mordor besucht: {reise.count('Mordor')}-mal")
print(f"Bruchtal besucht: {'Ja' if 'Bruchtal' in reise else 'Nein'}")

# =========================
# AUFGABE 14 – Kampf gegen den Kartoffel-Ork
# =========================
print("\n=== Aufgabe 14: Kampf gegen den Kartoffel-Ork ===")
ork_hp = 50
angriffe = []
while ork_hp > 0:
    schaden = random.randint(5, 15)
    angriffe.append(schaden)
    ork_hp -= schaden
    print(f"Angriff {len(angriffe)}: {schaden} Schaden (Ork HP: {max(0, ork_hp)})")
print(f"Anzahl der Angriffe: {len(angriffe)}")
print(f"Angriffsliste: {angriffe}")
print(f"Stärkster Angriff: {max(angriffe)}")

# =========================
# AUFGABE 15 – Handel in Bree
# =========================
print("\n=== Aufgabe 15: Handel in Bree ===")
preise = []
for i in range(1, 6):
    preis = round(random.uniform(1.5, 99.9), 2)
    preise.append(preis)
    print(f"Ware {i}: {preis} Silbermünzen")
durchschnitt = round(sum(preise) / len(preise), 2)
print(f"Durchschnittspreis: {durchschnitt} Silbermünzen")

# =========================
# AUFGABE 16 – Moria-Raum-Generator
# =========================
print("\n=== Aufgabe 16: Moria-Raum-Generator ===")
raumtypen = ("Ork-Raum", "Schatzkammer", "Trollhöhle", "Leerer Gang", "Raum voller singender Zwerge")
moria = []
for i in range(1, 11):
    raum = random.choice(raumtypen)
    moria.append(raum)
    print(f"Raum {i}: {raum}")
print(f"Alle Räume: {moria}")
print(f"Anzahl Ork-Räume: {moria.count('Ork-Raum')}")
print(f"Anzahl Schatzkammern: {moria.count('Schatzkammer')}")

# =========================
# AUFGABE 17 – Duell gegen den Balrog
# =========================
print("\n=== Aufgabe 17: Duell gegen den Balrog ===")
print("Du kommst nicht vorbei!")
balrog_hp = 100
held_hp = 80
runde = 0
while balrog_hp > 0 and held_hp > 0:
    runde += 1
    held_schaden = random.randint(8, 18)
    balrog_schaden = int(random.triangular(5, 20, 10))
    balrog_hp -= held_schaden
    held_hp -= balrog_schaden
    print(f"Runde {runde}: Held -{held_schaden} | Balrog -{balrog_schaden} "
            f"(Balrog HP: {max(0, balrog_hp)}, Held HP: {max(0, held_hp)})")
if balrog_hp <= 0 and held_hp <= 0:
    print("Unentschieden – beide stürzen in die Tiefe!")
elif balrog_hp <= 0:
    print("🧙 Gandalf der Weiße triumphiert!")
else:
    print("🔥 Der Balrog hat gewonnen – flieh, du Narr!")

# =========================
# AUFGABE 18 – Loot-System in der Zwergentruhe
# =========================
print("\n=== Aufgabe 18: Loot-System in der Zwergentruhe ===")
moegliche_items = ["Silber", "Lembas", "Elbenklinge", "Legendäre Kartoffel"]
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
# AUFGABE 19 – Mini-Mittelerde-Rollenspiel
# =========================
print("\n=== Aufgabe 19: Mini-Mittelerde-Rollenspiel ===")
leben = 100
silber = 0
inventar = []
besuchte_orte = set()
orte = ["Auenland", "Bruchtal", "Moria", "Rohan", "Mordor", "Fangorn", "Gondor"]
ereignisse = ["Kampf", "Fund", "Falle", "Händler", "Rast"]
runde = 0

while leben > 0 and silber < 100:
    runde += 1
    ort = random.choice(orte)
    besuchte_orte.add(ort)
    ereignis = random.choice(ereignisse)

    if ereignis == "Kampf":
        schaden = random.randint(5, 20)
        leben -= schaden
        print(f"Runde {runde} | {ort}: Ork-Angriff! -{schaden} Leben (Leben: {max(0, leben)})")
    elif ereignis == "Fund":
        fund = random.randrange(5, 51, 5)
        silber += fund
        inventar.append("Schatzfund")
        print(f"Runde {runde} | {ort}: Schatzfund! +{fund} Silber (Silber: {silber})")
    elif ereignis == "Falle":
        schaden = int(random.triangular(1, 15, 5))
        leben -= schaden
        print(f"Runde {runde} | {ort}: Ork-Falle! -{schaden} Leben (Leben: {max(0, leben)})")
    elif ereignis == "Händler":
        preis = round(random.uniform(1.0, 10.0), 2)
        inventar.append("Lembas")
        print(f"Runde {runde} | {ort}: Lembas für {preis} Silber gekauft.")
    elif ereignis == "Rast":
        heilung = random.randint(5, 15)
        leben = min(100, leben + heilung)
        print(f"Runde {runde} | {ort}: Rast am Lagerfeuer! +{heilung} Leben (Leben: {leben})")

print("\n--- Reisebericht ---")
print(f"Leben: {max(0, leben)}")
print(f"Silber: {silber}")
print(f"Inventar: {inventar}")
print(f"Besuchte Orte: {besuchte_orte}")
if leben <= 0:
    print("💀 Der Held fiel im Kampf.")
else:
    print("🌄 100 Silber gesammelt – die Gefährten feiern im Auenland!")

# =========================
# AUFGABE 20 – Der verfluchte Mittelerde-Simulator
# =========================
print("\n=== Aufgabe 20: Der verfluchte Mittelerde-Simulator ===")
heldennamen = ["Frodo", "Samweis", "Aragorn", "Legolas", "Gimli"]
mission_orte = ["Schicksalsberg", "Mirkwald", "Helm's Klamm", "Amon Hen", "Cirith Ungol"]
alle_missionen = []
erfolgreiche = []
niederlagen = []
besuchte_mission_orte = set()

for _ in range(100):
    name = random.choice(heldennamen)
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
print(f"Durchschnittliche Belohnung: {durchschnitt} Silber")
if bester_fund:
    print(f"Bester Fund: {bester_fund['held']} in {bester_fund['ort']} "
            f"mit {bester_fund['belohnung']} Silber")
print(f"Alle besuchten Orte: {besuchte_mission_orte}")
if lustigste_niederlage:
    print(f"Lustigste Niederlage: {lustigste_niederlage['held']} scheiterte in "
            f"{lustigste_niederlage['ort']} nach {lustigste_niederlage['dauer']} Tagen "
            f"(Gefahr: {lustigste_niederlage['gefahr']})")