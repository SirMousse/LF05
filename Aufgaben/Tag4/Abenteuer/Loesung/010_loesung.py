import random

# =========================
# AUFGABE 1 – Münzwurf des Kobolds
# =========================
print("=== Aufgabe 1: Münzwurf des Kobolds ===")
zahl = random.random()
if zahl < 0.5:
    print("Kopf: Der Kobold schenkt dir einen Keks.")
else:
    print("Zahl: Der Kobold klaut deinen Schuh.")

# =========================
# AUFGABE 2 – Würfel des Drachen
# =========================
print("\n=== Aufgabe 2: Würfel des Drachen ===")
wurf = random.randint(1, 6)
print(f"Du würfelst eine {wurf}.")
if wurf == 6:
    print("🐉 Ein Mini-Drache erscheint!")

# =========================
# AUFGABE 3 – Goldfund im Wald
# =========================
print("\n=== Aufgabe 3: Goldfund im Wald ===")
gold = random.randrange(10, 101, 10)
print(f"Du findest {gold} Gold im Wald!")

# =========================
# AUFGABE 4 – Zaubertrank-Stärke
# =========================
print("\n=== Aufgabe 4: Zaubertrank-Stärke ===")
staerke = round(random.uniform(1.0, 10.0), 2)
print(f"Die Stärke des Zaubertranks beträgt: {staerke}")

# =========================
# AUFGABE 5 – Dreieckiger Orakelwert
# =========================
print("\n=== Aufgabe 5: Dreieckiger Orakelwert ===")
orakel = random.triangular(1, 100, 80)
print(f"Das Orakel sagt: {orakel:.1f}% Chance auf Erfolg.")

# =========================
# AUFGABE 6 – Fünf Schatztruhen
# =========================
print("\n=== Aufgabe 6: Fünf Schatztruhen ===")
gesamt = 0
for i in range(1, 6):
    inhalt = random.randint(1, 20)
    print(f"Truhe {i}: {inhalt} Gold")
    gesamt += inhalt
print(f"Gesamtes Gold: {gesamt}")

# =========================
# AUFGABE 7 – Monster-Würfelrunde
# =========================
print("\n=== Aufgabe 7: Monster-Würfelrunde ===")
schaden_liste = []
for runde in range(1, 11):
    schaden = random.randint(1, 12)
    schaden_liste.append(schaden)
    print(f"Runde {runde}: {schaden} Schaden")
print(f"Alle Schadenswerte: {schaden_liste}")
print(f"Gesamtschaden: {sum(schaden_liste)}")
print(f"Höchster Schaden: {max(schaden_liste)}")

# =========================
# AUFGABE 8 – Flucht aus dem Schleim-Sumpf
# =========================
print("\n=== Aufgabe 8: Flucht aus dem Schleim-Sumpf ===")
versuche = 0
while True:
    versuche += 1
    wurf = random.randint(1, 6)
    print(f"Versuch {versuche}: {wurf}")
    if wurf == 6:
        print(f"Entkommen! Du brauchtest {versuche} Versuche.")
        break

# =========================
# AUFGABE 9 – Gold sammeln bis 100
# =========================
print("\n=== Aufgabe 9: Gold sammeln bis 100 ===")
gold = 0
runden = 0
while gold < 100:
    fund = random.randint(5, 25)
    gold += fund
    runden += 1
    print(f"Runde {runden}: +{fund} Gold (Gesamt: {gold})")
print(f"Abenteuer beendet nach {runden} Runden mit {gold} Gold.")

# =========================
# AUFGABE 10 – Zufälliges Inventar
# =========================
print("\n=== Aufgabe 10: Zufälliges Inventar ===")
inventar = ["Schwert", "Käse", "Zauberhut", "Gummiente", "Heiltrank"]
index = random.randint(0, len(inventar) - 1)
print(f"Du findest: {inventar[index]}")

# =========================
# AUFGABE 11 – Monster aus dem Tuple
# =========================
print("\n=== Aufgabe 11: Monster aus dem Tuple ===")
monster_tuple = ("Goblin", "Schleim", "Troll", "Wütendes Huhn")
index = random.randint(0, len(monster_tuple) - 1)
print(f"Ein wildes {monster_tuple[index]} erscheint!")

# =========================
# AUFGABE 12 – Seltene Funde im Set
# =========================
print("\n=== Aufgabe 12: Seltene Funde im Set ===")
moegliche_items = ["Gold", "Trank", "Stein", "Pilz", "Feder"]
funde_set = set()
for _ in range(10):
    item = random.choice(moegliche_items)
    funde_set.add(item)
print(f"Gefundene Items: {funde_set}")
print("Tipp: Ein Set speichert jeden Wert nur einmal – Duplikate werden ignoriert.")

# =========================
# AUFGABE 13 – Abenteuerreise mit Liste
# =========================
print("\n=== Aufgabe 13: Abenteuerreise mit Liste ===")
orte = ["Wald", "Höhle", "Burg", "Sumpf", "Marktplatz"]
reise = []
for tag in range(1, 8):
    ort = random.choice(orte)
    reise.append(ort)
    print(f"Tag {tag}: {ort}")
print(f"Reiseliste: {reise}")
print(f"Wald besucht: {reise.count('Wald')}-mal")
print(f"Burg besucht: {'Ja' if 'Burg' in reise else 'Nein'}")

# =========================
# AUFGABE 14 – Kampf gegen den Käse-Golem
# =========================
print("\n=== Aufgabe 14: Kampf gegen den Käse-Golem ===")
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
# AUFGABE 15 – Händler mit schlechten Preisen
# =========================
print("\n=== Aufgabe 15: Händler mit schlechten Preisen ===")
preise = []
for i in range(1, 6):
    preis = round(random.uniform(1.5, 99.9), 2)
    preise.append(preis)
    print(f"Item {i}: {preis} Gold")
durchschnitt = round(sum(preise) / len(preise), 2)
print(f"Durchschnittspreis: {durchschnitt} Gold")

# =========================
# AUFGABE 16 – Der Dungeon-Generator
# =========================
print("\n=== Aufgabe 16: Der Dungeon-Generator ===")
raumtypen = ("Monster", "Schatz", "Falle", "Leer", "Mysteriöse Ente")
dungeon = []
for i in range(1, 11):
    raum = random.choice(raumtypen)
    dungeon.append(raum)
    print(f"Raum {i}: {raum}")
print(f"Alle Räume: {dungeon}")
print(f"Monster-Räume: {dungeon.count('Monster')}")
print(f"Schatzräume: {dungeon.count('Schatz')}")

# =========================
# AUFGABE 17 – Glücksbasierter Bosskampf
# =========================
print("\n=== Aufgabe 17: Glücksbasierter Bosskampf ===")
boss_hp = 100
spieler_hp = 80
runde = 0
while boss_hp > 0 and spieler_hp > 0:
    runde += 1
    spieler_schaden = random.randint(8, 18)
    boss_schaden = int(random.triangular(5, 20, 10))
    boss_hp -= spieler_schaden
    spieler_hp -= boss_schaden
    print(f"Runde {runde}: Spieler -{spieler_schaden} | Boss -{boss_schaden} "
            f"(Boss HP: {max(0, boss_hp)}, Spieler HP: {max(0, spieler_hp)})")
if boss_hp <= 0 and spieler_hp <= 0:
    print("Unentschieden – beide fallen gleichzeitig!")
elif boss_hp <= 0:
    print("🏆 Der Spieler hat gewonnen!")
else:
    print("💀 Der Boss hat gewonnen!")

# =========================
# AUFGABE 18 – Loot-System mit Set und Liste
# =========================
print("\n=== Aufgabe 18: Loot-System mit Set und Liste ===")
moegliche_items = ["Gold", "Trank", "Diamant", "Legendärer Käse"]
loot_liste = []
loot_set = set()
for i in range(1, 21):
    item = random.choice(moegliche_items)
    loot_liste.append(item)
    loot_set.add(item)
print(f"Komplette Loot-Liste: {loot_liste}")
print(f"Einzigartige Items: {loot_set}")
print(f"Anzahl verschiedener Items: {len(loot_set)}")

# =========================
# AUFGABE 19 – Mini-Rollenspiel: Die Quest der Gummiente
# =========================
print("\n=== Aufgabe 19: Die Quest der Gummiente ===")
leben = 100
gold = 0
inventar = []
besuchte_orte = set()
orte = ["Wald", "Höhle", "Burg", "Sumpf", "Marktplatz", "Wüste", "Vulkan"]
ereignisse = ["Kampf", "Fund", "Falle", "Händler", "Rast"]
runde = 0

while leben > 0 and gold < 100:
    runde += 1
    ort = random.choice(orte)
    besuchte_orte.add(ort)
    ereignis = random.choice(ereignisse)

    if ereignis == "Kampf":
        schaden = random.randint(5, 20)
        leben -= schaden
        print(f"Runde {runde} | {ort}: Kampf! -{schaden} Leben (Leben: {max(0, leben)})")
    elif ereignis == "Fund":
        fund = random.randrange(5, 51, 5)
        gold += fund
        inventar.append("Fundstück")
        print(f"Runde {runde} | {ort}: Fund! +{fund} Gold (Gold: {gold})")
    elif ereignis == "Falle":
        schaden = int(random.triangular(1, 15, 5))
        leben -= schaden
        print(f"Runde {runde} | {ort}: Falle! -{schaden} Leben (Leben: {max(0, leben)})")
    elif ereignis == "Händler":
        preis = round(random.uniform(1.0, 10.0), 2)
        inventar.append("Trank")
        print(f"Runde {runde} | {ort}: Händler! Trank für {preis} Gold gekauft.")
    elif ereignis == "Rast":
        heilung = random.randint(5, 15)
        leben = min(100, leben + heilung)
        print(f"Runde {runde} | {ort}: Rast! +{heilung} Leben (Leben: {leben})")

print("\n--- Ergebnis der Quest ---")
print(f"Leben: {max(0, leben)}")
print(f"Gold: {gold}")
print(f"Inventar: {inventar}")
print(f"Besuchte Orte: {besuchte_orte}")
if leben <= 0:
    print("💀 Die Gummiente ist gestorben.")
else:
    print("🦆 Die Gummiente hat 100 Gold gesammelt – Erfolg!")

# =========================
# AUFGABE 20 – Der verfluchte Abenteuer-Simulator
# =========================
print("\n=== Aufgabe 20: Der verfluchte Abenteuer-Simulator ===")
heldennamen = ["Ritter Bob", "Zauberin Zoe", "Dieb Dirk", "Barbar Berta", "Paladin Pete"]
abenteuer_orte = ["Drachenhöhle", "Verlorenes Königreich", "Pilzwald", "Käse-Festung", "Geisterturm"]
alle_abenteuer = []
erfolgreiche = []
besuchte_abenteuer_orte = set()
niederlagen = []

for _ in range(100):
    name = random.choice(heldennamen)
    ort = random.choice(abenteuer_orte)
    dauer = random.randint(1, 30)
    gefahr = round(random.uniform(1.0, 10.0), 1)
    belohnung = random.randrange(0, 201, 10)
    erfolg = random.random() > 0.4  # 60% Erfolgsrate

    besuchte_abenteuer_orte.add(ort)
    abenteuer = {
        "held": name, "ort": ort, "dauer": dauer,
        "gefahr": gefahr, "belohnung": belohnung, "erfolg": erfolg
    }
    alle_abenteuer.append(abenteuer)

    if erfolg:
        erfolgreiche.append(abenteuer)
    else:
        niederlagen.append(abenteuer)

# Auswertung
durchschnitt_belohnung = round(
    sum(a["belohnung"] for a in erfolgreiche) / len(erfolgreiche), 2
) if erfolgreiche else 0

bester_fund = max(erfolgreiche, key=lambda a: a["belohnung"]) if erfolgreiche else None

lustigste_niederlage = random.choice(niederlagen) if niederlagen else None

print(f"Anzahl erfolgreicher Abenteuer: {len(erfolgreiche)} / 100")
print(f"Durchschnittliche Belohnung (Erfolge): {durchschnitt_belohnung} Gold")
if bester_fund:
    print(f"Bester Fund: {bester_fund['held']} in {bester_fund['ort']} mit {bester_fund['belohnung']} Gold")
print(f"Alle besuchten Orte: {besuchte_abenteuer_orte}")
if lustigste_niederlage:
    print(f"Lustigste Niederlage: {lustigste_niederlage['held']} scheiterte in "
            f"{lustigste_niederlage['ort']} nach {lustigste_niederlage['dauer']} Tagen "
            f"(Gefahr: {lustigste_niederlage['gefahr']})")