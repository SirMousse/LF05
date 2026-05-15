import random

# =========================
# AUFGABE 1 – Ein wildes Abenteuer beginnt
# =========================
print("=== Aufgabe 1: Ein wildes Abenteuer beginnt ===")
ereignisse = {
    1: "Link findet einen Rubin.",
    2: "Navi ruft: Hey!",
    3: "Ein Huhn schaut verdächtig.",
    4: "Eine Truhe erscheint."
}
zahl = random.randint(1, 4)
print(ereignisse[zahl])

# =========================
# AUFGABE 2 – Truhe öffnen
# =========================
print("\n=== Aufgabe 2: Truhe öffnen ===")
wert = random.random()
if wert < 0.5:
    print("Du findest einen Schatz!")
else:
    print("Die Truhe ist leer. Sehr unhöflich.")

# =========================
# AUFGABE 3 – Rubine sammeln
# =========================
print("\n=== Aufgabe 3: Rubine sammeln ===")
rubine = random.randrange(5, 101, 5)
print(f"Link findet {rubine} Rubine!")

# =========================
# AUFGABE 4 – Schwert-Stärke
# =========================
print("\n=== Aufgabe 4: Schwert-Stärke ===")
staerke = round(random.uniform(1.0, 10.0), 2)
print(f"Schwert-Stärke: {staerke}")

# =========================
# AUFGABE 5 – Sheikah-Stein-Orakel
# =========================
print("\n=== Aufgabe 5: Sheikah-Stein-Orakel ===")
orakel = random.triangular(1, 100, 75)
print(f"Sheikah-Stein-Orakel: {orakel:.1f}% Erfolgswahrscheinlichkeit.")

# =========================
# AUFGABE 6 – Bogen-Training
# =========================
print("\n=== Aufgabe 6: Bogen-Training ===")
pfeile = []
for i in range(1, 9):
    schaden = random.randint(1, 9)
    pfeile.append(schaden)
    print(f"Pfeil {i}: {schaden} Schaden")
print(f"Alle Treffer: {pfeile}")

# =========================
# AUFGABE 7 – Kampf gegen Bokblins
# =========================
print("\n=== Aufgabe 7: Kampf gegen Bokblins ===")
schaden_liste = []
for i in range(1, 11):
    schaden = random.randint(1, 12)
    schaden_liste.append(schaden)
    print(f"Runde {i}: {schaden} Schaden")
print(f"Alle Schadenswerte: {schaden_liste}")
print(f"Gesamtschaden: {sum(schaden_liste)}")
print(f"Stärkster Treffer: {max(schaden_liste)}")

# =========================
# AUFGABE 8 – Schrein öffnen
# =========================
print("\n=== Aufgabe 8: Schrein öffnen ===")
versuche = 0
while True:
    versuche += 1
    wurf = random.randint(1, 6)
    print(f"Versuch {versuche}: {wurf}")
    if wurf == 6:
        print(f"Der Schrein öffnet sich! Benötigte Versuche: {versuche}")
        break

# =========================
# AUFGABE 9 – Ausdauer sammeln
# =========================
print("\n=== Aufgabe 9: Ausdauer sammeln ===")
ausdauer = 0
runden = 0
while ausdauer < 100:
    gewinn = random.randint(5, 25)
    ausdauer += gewinn
    runden += 1
    print(f"Runde {runden}: +{gewinn} Ausdauer (Gesamt: {ausdauer})")
print(f"Ziel erreicht nach {runden} Runden mit {ausdauer} Ausdauerpunkten!")

# =========================
# AUFGABE 10 – Links Inventar
# =========================
print("\n=== Aufgabe 10: Links Inventar ===")
inventar = ["Schwert", "Schild", "Bogen", "Bombe", "sehr verdächtiges Huhn"]
index = random.randint(0, len(inventar) - 1)
print(f"Link greift ins Inventar und zieht heraus: {inventar[index]}")

# =========================
# AUFGABE 11 – Völker von Hyrule
# =========================
print("\n=== Aufgabe 11: Völker von Hyrule ===")
voelker_tuple = ("Hylianer", "Zora", "Gorone", "Gerudo", "Krogs", "beleidigtes Huhn")
index = random.randint(0, len(voelker_tuple) - 1)
print(f"Link trifft auf: {voelker_tuple[index]}!")

# =========================
# AUFGABE 12 – Seltene Funde in Hyrule
# =========================
print("\n=== Aufgabe 12: Seltene Funde in Hyrule ===")
moegliche_funde = ["Rubinstein", "Herzteil", "Okarinen-Note", "Sheikah-Splitter", "Pilzkrone"]
fund_set = set()
for _ in range(10):
    fund = random.choice(moegliche_funde)
    fund_set.add(fund)
print(f"Gefundene Gegenstände: {fund_set}")
print("Tipp: Ein Set speichert jeden Fund nur einmal – doppelte Rubine verschwinden wie durch Magie.")

# =========================
# AUFGABE 13 – Reise durch Hyrule
# =========================
print("\n=== Aufgabe 13: Reise durch Hyrule ===")
orte = ["Kokiri-Wald", "Todesberg", "Hylia-See", "Schloss Hyrule", "Kakariko"]
reise = []
for tag in range(1, 8):
    ort = random.choice(orte)
    reise.append(ort)
    print(f"Tag {tag}: {ort}")
print(f"Ortsliste: {reise}")
print(f"Kakariko besucht: {reise.count('Kakariko')}-mal")
print(f"Schloss Hyrule besucht: {'Ja' if 'Schloss Hyrule' in reise else 'Nein'}")

# =========================
# AUFGABE 14 – Kampf gegen den Hühner-Schwarm
# =========================
print("\n=== Aufgabe 14: Kampf gegen den Hühner-Schwarm ===")
schwarm_hp = 50
angriffe = []
while schwarm_hp > 0:
    schaden = random.randint(5, 15)
    angriffe.append(schaden)
    schwarm_hp -= schaden
    print(f"Angriff {len(angriffe)}: {schaden} Schaden (Schwarm HP: {max(0, schwarm_hp)})")
print(f"Anzahl der Angriffe: {len(angriffe)}")
print(f"Angriffsliste: {angriffe}")
print(f"Stärkster Angriff: {max(angriffe)}")

# =========================
# AUFGABE 15 – Einkauf beim fahrenden Händler
# =========================
print("\n=== Aufgabe 15: Einkauf beim fahrenden Händler ===")
preise = []
for i in range(1, 6):
    preis = round(random.uniform(1.5, 99.9), 2)
    preise.append(preis)
    print(f"Artikel {i}: {preis} Rubine")
durchschnitt = round(sum(preise) / len(preise), 2)
print(f"Durchschnittspreis: {durchschnitt} Rubine")

# =========================
# AUFGABE 16 – Dungeon-Generator
# =========================
print("\n=== Aufgabe 16: Dungeon-Generator ===")
raumtypen = ("Bokblin-Raum", "Schatzraum", "Rätselraum", "Leerer Gang", "Raum voller wütender Hühner")
dungeon = []
for i in range(1, 11):
    raum = random.choice(raumtypen)
    dungeon.append(raum)
    print(f"Raum {i}: {raum}")
print(f"Alle Räume: {dungeon}")
print(f"Anzahl Bokblin-Räume: {dungeon.count('Bokblin-Raum')}")
print(f"Anzahl Schatzräume: {dungeon.count('Schatzraum')}")

# =========================
# AUFGABE 17 – Duell gegen Ganons Schatten
# =========================
print("\n=== Aufgabe 17: Duell gegen Ganons Schatten ===")
ganon_hp = 100
link_hp = 80
runde = 0
while ganon_hp > 0 and link_hp > 0:
    runde += 1
    link_schaden = random.randint(8, 18)
    ganon_schaden = int(random.triangular(5, 20, 10))
    ganon_hp -= link_schaden
    link_hp -= ganon_schaden
    print(f"Runde {runde}: Link -{link_schaden} | Ganon -{ganon_schaden} "
          f"(Ganon HP: {max(0, ganon_hp)}, Link HP: {max(0, link_hp)})")
if ganon_hp <= 0 and link_hp <= 0:
    print("Unentschieden – beide fallen gleichzeitig!")
elif ganon_hp <= 0:
    print("🗡️  Link hat gewonnen – Hyrule ist gerettet!")
else:
    print("🌑 Ganons Schatten triumphiert – die Dunkelheit breitet sich aus!")

# =========================
# AUFGABE 18 – Loot-System im Tempel
# =========================
print("\n=== Aufgabe 18: Loot-System im Tempel ===")
moegliche_items = ["Rubin", "Bombe", "Herzteil", "Legendäres Huhn"]
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
# AUFGABE 19 – Mini-Hyrule-Rollenspiel
# =========================
print("\n=== Aufgabe 19: Mini-Hyrule-Rollenspiel ===")
leben = 100
rubine = 0
inventar = []
besuchte_orte = set()
orte = ["Kokiri-Wald", "Todesberg", "Hylia-See", "Schloss Hyrule", "Kakariko", "Wüste Gerudo", "Zora-Domäne"]
ereignisse = ["Kampf", "Fund", "Falle", "Händler", "Heilung"]
runde = 0

while leben > 0 and rubine < 100:
    runde += 1
    ort = random.choice(orte)
    besuchte_orte.add(ort)
    ereignis = random.choice(ereignisse)

    if ereignis == "Kampf":
        schaden = random.randint(5, 20)
        leben -= schaden
        print(f"Runde {runde} | {ort}: Bokblin-Angriff! -{schaden} HP (Leben: {max(0, leben)})")
    elif ereignis == "Fund":
        fund = random.randrange(5, 51, 5)
        rubine += fund
        inventar.append("Rubinfund")
        print(f"Runde {runde} | {ort}: Rubine gefunden! +{fund} 💎 (Rubine: {rubine})")
    elif ereignis == "Falle":
        schaden = int(random.triangular(1, 15, 5))
        leben -= schaden
        print(f"Runde {runde} | {ort}: Fallenstein! -{schaden} HP (Leben: {max(0, leben)})")
    elif ereignis == "Händler":
        preis = round(random.uniform(1.0, 10.0), 2)
        inventar.append("Trank")
        print(f"Runde {runde} | {ort}: Roter Trank für {preis} Rubine gekauft.")
    elif ereignis == "Heilung":
        heilung = random.randint(5, 15)
        leben = min(100, leben + heilung)
        print(f"Runde {runde} | {ort}: Herzcontainer! +{heilung} HP (Leben: {leben})")

print("\n--- Hyrule-Reisebericht ---")
print(f"Leben: {max(0, leben)}")
print(f"Rubine: {rubine}")
print(f"Inventar: {inventar}")
print(f"Besuchte Orte: {besuchte_orte}")
if leben <= 0:
    print("💀 Link ist gefallen – Game Over.")
else:
    print("🌟 100 Rubine gesammelt – die Triforce leuchtet!")

# =========================
# AUFGABE 20 – Der verfluchte Hyrule-Simulator
# =========================
print("\n=== Aufgabe 20: Der verfluchte Hyrule-Simulator ===")
heldennamen = ["Link", "Zelda", "Impa", "Revali", "Urbosa"]
mission_orte = ["Schlossberg", "Zora-Brücke", "Gerudofestung", "Drachenpfad", "Hutsprung-Ebene"]
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
print(f"Durchschnittliche Belohnung: {durchschnitt} Rubine")
if bester_fund:
    print(f"Bester Fund: {bester_fund['held']} in {bester_fund['ort']} "
          f"mit {bester_fund['belohnung']} Rubinen")
print(f"Alle besuchten Orte: {besuchte_mission_orte}")
if lustigste_niederlage:
    print(f"Lustigste Niederlage: {lustigste_niederlage['held']} scheiterte in "
          f"{lustigste_niederlage['ort']} nach {lustigste_niederlage['dauer']} Tagen "
          f"(Gefahr: {lustigste_niederlage['gefahr']})")