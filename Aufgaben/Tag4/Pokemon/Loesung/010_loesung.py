import random

# =========================
# AUFGABE 1 – Das wilde Pokemon erscheint
# =========================
print("=== Aufgabe 1: Das wilde Pokemon erscheint ===")
pokemon = {1: "Pikachu", 2: "Glumanda", 3: "Bisasam", 4: "Schiggy"}
zahl = random.randint(1, 4)
print(f"Ein wildes {pokemon[zahl]} erscheint!")

# =========================
# AUFGABE 2 – Pokeball-Wurf
# =========================
print("\n=== Aufgabe 2: Pokeball-Wurf ===")
wert = random.random()
if wert < 0.5:
    print("Gefangen!")
else:
    print("Oh nein! Das Pokemon ist ausgebrochen.")

# =========================
# AUFGABE 3 – Pokemünzen sammeln
# =========================
print("\n=== Aufgabe 3: Pokemünzen sammeln ===")
muenzen = random.randrange(10, 101, 10)
print(f"Du findest {muenzen} Pokemünzen!")

# =========================
# AUFGABE 4 – Attacken-Stärke
# =========================
print("\n=== Aufgabe 4: Attacken-Stärke ===")
staerke = round(random.uniform(1.0, 10.0), 2)
print(f"Attacken-Stärke: {staerke}")

# =========================
# AUFGABE 5 – Pokedex-Analyse
# =========================
print("\n=== Aufgabe 5: Pokedex-Analyse ===")
trefferchance = random.triangular(1, 100, 70)
print(f"Pokedex-Analyse: {trefferchance:.1f}% Erfolgswahrscheinlichkeit.")

# =========================
# AUFGABE 6 – Trainingsrunde
# =========================
print("\n=== Aufgabe 6: Trainingsrunde ===")
training = []
for i in range(1, 9):
    ep = random.randint(1, 9)
    training.append(ep)
    print(f"Training {i}: +{ep} EP")
print(f"Alle Trainingswerte: {training}")

# =========================
# AUFGABE 7 – Arena-Kampf
# =========================
print("\n=== Aufgabe 7: Arena-Kampf ===")
schaden_liste = []
for i in range(1, 11):
    schaden = random.randint(1, 12)
    schaden_liste.append(schaden)
    print(f"Runde {i}: {schaden} Schaden")
print(f"Alle Schadenswerte: {schaden_liste}")
print(f"Gesamtschaden: {sum(schaden_liste)}")
print(f"Stärkste Attacke: {max(schaden_liste)}")

# =========================
# AUFGABE 8 – Pokemon fangen
# =========================
print("\n=== Aufgabe 8: Pokemon fangen ===")
versuche = 0
while True:
    versuche += 1
    wurf = random.randint(1, 6)
    print(f"Pokeball-Wurf {versuche}: {wurf}")
    if wurf == 6:
        print(f"Klick! Gefangen nach {versuche} Versuchen!")
        break

# =========================
# AUFGABE 9 – Erfahrungspunkte sammeln
# =========================
print("\n=== Aufgabe 9: Erfahrungspunkte sammeln ===")
ep_gesamt = 0
runden = 0
while ep_gesamt < 100:
    ep = random.randint(5, 25)
    ep_gesamt += ep
    runden += 1
    print(f"Runde {runden}: +{ep} EP (Gesamt: {ep_gesamt})")
print(f"Level-Up nach {runden} Runden mit {ep_gesamt} EP!")

# =========================
# AUFGABE 10 – Trainer-Inventar
# =========================
print("\n=== Aufgabe 10: Trainer-Inventar ===")
inventar = ["Pokeball", "Trank", "Beere", "Fahrrad", "sehr verdächtiger Karpador"]
index = random.randint(0, len(inventar) - 1)
print(f"Du greifst in den Rucksack und findest: {inventar[index]}")

# =========================
# AUFGABE 11 – Pokemon-Typen
# =========================
print("\n=== Aufgabe 11: Pokemon-Typen ===")
typen_tuple = ("Feuer", "Wasser", "Pflanze", "Elektro", "Geist", "sehr verwirrter Käfer")
index = random.randint(0, len(typen_tuple) - 1)
print(f"Zufälliger Pokemon-Typ: {typen_tuple[index]}")

# =========================
# AUFGABE 12 – Seltene Pokemon-Funde
# =========================
print("\n=== Aufgabe 12: Seltene Pokemon-Funde ===")
moegliche_pokemon = ["Pikachu", "Evoli", "Relaxo", "Mauzi", "Ditto"]
begegnungen = set()
for _ in range(10):
    p = random.choice(moegliche_pokemon)
    begegnungen.add(p)
print(f"Begegnete Pokemon: {begegnungen}")
print("Tipp: Ein Set speichert jedes Pokemon nur einmal – wie im echten Pokedex!")

# =========================
# AUFGABE 13 – Reise durch die Region
# =========================
print("\n=== Aufgabe 13: Reise durch die Region ===")
orte = ["Alabastia", "Vertania", "Azuria", "Lavandia", "Pokecenter"]
reise = []
for tag in range(1, 8):
    ort = random.choice(orte)
    reise.append(ort)
    print(f"Tag {tag}: {ort}")
print(f"Ortsliste: {reise}")
print(f"Pokecenter besucht: {reise.count('Pokecenter')}-mal")
print(f"Lavandia besucht: {'Ja' if 'Lavandia' in reise else 'Nein'}")

# =========================
# AUFGABE 14 – Kampf gegen Team Fehler
# =========================
print("\n=== Aufgabe 14: Kampf gegen Team Fehler ===")
team_fehler_hp = 50
angriffe = []
while team_fehler_hp > 0:
    schaden = random.randint(5, 15)
    angriffe.append(schaden)
    team_fehler_hp -= schaden
    print(f"Angriff {len(angriffe)}: {schaden} Schaden (Team Fehler HP: {max(0, team_fehler_hp)})")
print(f"Anzahl der Angriffe: {len(angriffe)}")
print(f"Angriffsliste: {angriffe}")
print(f"Stärkster Angriff: {max(angriffe)}")

# =========================
# AUFGABE 15 – Einkauf im Pokemon-Markt
# =========================
print("\n=== Aufgabe 15: Einkauf im Pokemon-Markt ===")
preise = []
for i in range(1, 6):
    preis = round(random.uniform(1.5, 99.9), 2)
    preise.append(preis)
    print(f"Item {i}: {preis} Pokemünzen")
durchschnitt = round(sum(preise) / len(preise), 2)
print(f"Durchschnittspreis: {durchschnitt} Pokemünzen")

# =========================
# AUFGABE 16 – Höhlen-Generator
# =========================
print("\n=== Aufgabe 16: Höhlen-Generator ===")
bereiche_tuple = ("Zubat-Raum", "Schatz-Ecke", "Trainer-Kampf", "Leerer Gang", "Raum voller singender Enton")
hoehle = []
for i in range(1, 11):
    bereich = random.choice(bereiche_tuple)
    hoehle.append(bereich)
    print(f"Bereich {i}: {bereich}")
print(f"Alle Bereiche: {hoehle}")
print(f"Anzahl Zubat-Räume: {hoehle.count('Zubat-Raum')}")
print(f"Anzahl Schatz-Ecken: {hoehle.count('Schatz-Ecke')}")

# =========================
# AUFGABE 17 – Duell gegen das legendäre Pokemon
# =========================
print("\n=== Aufgabe 17: Duell gegen das legendäre Pokemon ===")
legendary_hp = 100
trainer_hp = 80
runde = 0
while legendary_hp > 0 and trainer_hp > 0:
    runde += 1
    trainer_schaden = random.randint(8, 18)
    legendary_schaden = int(random.triangular(5, 20, 10))
    legendary_hp -= trainer_schaden
    trainer_hp -= legendary_schaden
    print(f"Runde {runde}: Trainer -{trainer_schaden} | Legendäres -{legendary_schaden} "
            f"(Legendary HP: {max(0, legendary_hp)}, Trainer HP: {max(0, trainer_hp)})")
if legendary_hp <= 0 and trainer_hp <= 0:
    print("Unentschieden – beide sind kampfunfähig!")
elif legendary_hp <= 0:
    print("🏆 Dein Pokemon hat das Legendäre besiegt!")
else:
    print("💫 Das legendäre Pokemon war zu stark – nächstes Mal!")

# =========================
# AUFGABE 18 – Loot-System im Pokecenter
# =========================
print("\n=== Aufgabe 18: Loot-System im Pokecenter ===")
moegliche_items = ["Pokeball", "Trank", "Sonderbonbon", "Legendäre Socke"]
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
# AUFGABE 19 – Mini-Pokemon-Rollenspiel
# =========================
print("\n=== Aufgabe 19: Mini-Pokemon-Rollenspiel ===")
leben = 100
pokemuenzen = 0
inventar = []
besuchte_orte = set()
orte = ["Alabastia", "Vertania", "Azuria", "Lavandia", "Pokecenter", "Safari-Zone", "Kampfturm"]
ereignisse = ["Kampf", "Fund", "Falle", "Shop", "Heilung"]
runde = 0

while leben > 0 and pokemuenzen < 100:
    runde += 1
    ort = random.choice(orte)
    besuchte_orte.add(ort)
    ereignis = random.choice(ereignisse)

    if ereignis == "Kampf":
        schaden = random.randint(5, 20)
        leben -= schaden
        print(f"Runde {runde} | {ort}: Wilder Pokemon-Kampf! -{schaden} HP (Leben: {max(0, leben)})")
    elif ereignis == "Fund":
        fund = random.randrange(5, 51, 5)
        pokemuenzen += fund
        inventar.append("Pokemünzen-Fund")
        print(f"Runde {runde} | {ort}: Münzen gefunden! +{fund} ₽ (Münzen: {pokemuenzen})")
    elif ereignis == "Falle":
        schaden = int(random.triangular(1, 15, 5))
        leben -= schaden
        print(f"Runde {runde} | {ort}: Giftstachel! -{schaden} HP (Leben: {max(0, leben)})")
    elif ereignis == "Shop":
        preis = round(random.uniform(1.0, 10.0), 2)
        inventar.append("Trank")
        print(f"Runde {runde} | {ort}: Trank für {preis} ₽ gekauft.")
    elif ereignis == "Heilung":
        heilung = random.randint(5, 15)
        leben = min(100, leben + heilung)
        print(f"Runde {runde} | {ort}: Pokecenter-Heilung! +{heilung} HP (Leben: {leben})")

print("\n--- Trainer-Abschlussbericht ---")
print(f"Leben: {max(0, leben)}")
print(f"Pokemünzen: {pokemuenzen}")
print(f"Inventar: {inventar}")
print(f"Besuchte Orte: {besuchte_orte}")
if leben <= 0:
    print("💀 Dein Pokemon ist kampfunfähig – ab ins Pokecenter!")
else:
    print("🌟 100 Pokemünzen gesammelt – du bist der beste Trainer!")

# =========================
# AUFGABE 20 – Der verfluchte Pokemon-Simulator
# =========================
print("\n=== Aufgabe 20: Der verfluchte Pokemon-Simulator ===")
trainer_namen = ["Ash", "Misty", "Brock", "Gary", "Serena"]
mission_orte = ["Azuria-Arena", "Lavandia-Turm", "Safari-Zone", "Kampfturm", "Karpador-See"]
alle_missionen = []
erfolgreiche = []
niederlagen = []
besuchte_mission_orte = set()

for _ in range(100):
    name = random.choice(trainer_namen)
    ort = random.choice(mission_orte)
    dauer = random.randint(1, 30)
    gefahr = round(random.uniform(1.0, 10.0), 1)
    belohnung = random.randrange(0, 201, 10)
    erfolg = random.random() > 0.4

    besuchte_mission_orte.add(ort)
    mission = {
        "trainer": name, "ort": ort, "dauer": dauer,
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
print(f"Durchschnittliche Belohnung: {durchschnitt} Pokemünzen")
if bester_fund:
    print(f"Bester Fund: {bester_fund['trainer']} in {bester_fund['ort']} "
            f"mit {bester_fund['belohnung']} Pokemünzen")
print(f"Alle besuchten Orte: {besuchte_mission_orte}")
if lustigste_niederlage:
    print(f"Lustigste Niederlage: {lustigste_niederlage['trainer']} scheiterte in "
            f"{lustigste_niederlage['ort']} nach {lustigste_niederlage['dauer']} Tagen "
            f"(Gefahr: {lustigste_niederlage['gefahr']})")