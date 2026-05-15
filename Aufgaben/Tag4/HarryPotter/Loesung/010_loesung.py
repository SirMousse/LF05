import random

# =========================
# AUFGABE 1 – Der sprechende Zauberhut
# =========================
print("=== Aufgabe 1: Der sprechende Zauberhut ===")
haeuser = {1: "Gryffindor", 2: "Hufflepuff", 3: "Ravenclaw", 4: "Slytherin"}
zahl = random.randint(1, 4)
print(f"Der Zauberhut ruft: {haeuser[zahl]}!")

# =========================
# AUFGABE 2 – Magischer Zufallstest
# =========================
print("\n=== Aufgabe 2: Magischer Zufallstest ===")
wert = random.random()
if wert < 0.4:
    print("Der Zauber funktioniert!")
else:
    print("Der Zauber explodiert leicht beleidigt.")

# =========================
# AUFGABE 3 – Berties Bohnen
# =========================
print("\n=== Aufgabe 3: Berties Bohnen ===")
bohnen = random.randrange(5, 51, 5)
print(f"Du findest {bohnen} Bertie-Bott-Bohnen!")

# =========================
# AUFGABE 4 – Zaubertrank-Stärke
# =========================
print("\n=== Aufgabe 4: Zaubertrank-Stärke ===")
staerke = round(random.uniform(1.0, 10.0), 2)
print(f"Zaubertrank-Stärke: {staerke}")

# =========================
# AUFGABE 5 – Wahrsagekugel
# =========================
print("\n=== Aufgabe 5: Wahrsagekugel ===")
erfolg = random.triangular(1, 100, 75)
print(f"Die Wahrsagekugel sieht: {erfolg:.1f}% Erfolgswahrscheinlichkeit.")

# =========================
# AUFGABE 6 – Zauberstab-Funken
# =========================
print("\n=== Aufgabe 6: Zauberstab-Funken ===")
funken = []
for i in range(1, 9):
    staerke = random.randint(1, 9)
    funken.append(staerke)
    print(f"Funke {i}: Stärke {staerke}")
print(f"Alle Funken: {funken}")

# =========================
# AUFGABE 7 – Duell-Unterricht
# =========================
print("\n=== Aufgabe 7: Duell-Unterricht ===")
schaden_liste = []
for i in range(1, 11):
    schaden = random.randint(1, 12)
    schaden_liste.append(schaden)
    print(f"Zauber {i}: {schaden} Schaden")
print(f"Alle Schadenswerte: {schaden_liste}")
print(f"Gesamtschaden: {sum(schaden_liste)}")
print(f"Stärkster Zauber: {max(schaden_liste)}")

# =========================
# AUFGABE 8 – Tür zur verbotenen Abteilung
# =========================
print("\n=== Aufgabe 8: Tür zur verbotenen Abteilung ===")
versuche = 0
while True:
    versuche += 1
    wurf = random.randint(1, 6)
    print(f"Versuch {versuche}: {wurf}")
    if wurf == 6:
        print(f"Die Tür öffnet sich! Benötigte Versuche: {versuche}")
        break

# =========================
# AUFGABE 9 – Hauspunkte sammeln
# =========================
print("\n=== Aufgabe 9: Hauspunkte sammeln ===")
punkte = 0
runden = 0
while punkte < 100:
    gewinn = random.randint(5, 25)
    punkte += gewinn
    runden += 1
    print(f"Runde {runden}: +{gewinn} Punkte (Gesamt: {punkte})")
print(f"Spiel beendet nach {runden} Runden mit {punkte} Hauspunkten.")

# =========================
# AUFGABE 10 – Magisches Inventar
# =========================
print("\n=== Aufgabe 10: Magisches Inventar ===")
inventar = ["Zauberstab", "Umhang", "Schokofrosch", "Feder", "sehr verdächtige Socke"]
index = random.randint(0, len(inventar) - 1)
print(f"Du findest: {inventar[index]}")

# =========================
# AUFGABE 11 – Magische Wesen
# =========================
print("\n=== Aufgabe 11: Magische Wesen ===")
wesen_tuple = ("Eule", "Hippogreif", "Basilisk", "Niffler", "beleidigter Kürbis")
index = random.randint(0, len(wesen_tuple) - 1)
print(f"Du begegnest einem: {wesen_tuple[index]}!")

# =========================
# AUFGABE 12 – Seltene Zauberfunde
# =========================
print("\n=== Aufgabe 12: Seltene Zauberfunde ===")
moegliche_gegenstaende = ["Phönixfeder", "Drachenschuppe", "Mondstein", "Tränkstein", "Glitzerpulver"]
fund_set = set()
for _ in range(10):
    gegenstand = random.choice(moegliche_gegenstaende)
    fund_set.add(gegenstand)
print(f"Gefundene Gegenstände: {fund_set}")
print("Tipp: Ein Set speichert jeden Wert nur einmal – Duplikate verschwinden wie durch Magie.")

# =========================
# AUFGABE 13 – Reise durch die Zauberschule
# =========================
print("\n=== Aufgabe 13: Reise durch die Zauberschule ===")
orte = ["Große Halle", "Bibliothek", "Kerker", "Gewächshaus", "Krankenflügel"]
reise = []
for tag in range(1, 8):
    ort = random.choice(orte)
    reise.append(ort)
    print(f"Tag {tag}: {ort}")
print(f"Ortsliste: {reise}")
print(f"Bibliothek besucht: {reise.count('Bibliothek')}-mal")
print(f"Kerker besucht: {'Ja' if 'Kerker' in reise else 'Nein'}")

# =========================
# AUFGABE 14 – Kampf gegen den Bücher-Troll
# =========================
print("\n=== Aufgabe 14: Kampf gegen den Bücher-Troll ===")
troll_hp = 50
angriffe = []
while troll_hp > 0:
    schaden = random.randint(5, 15)
    angriffe.append(schaden)
    troll_hp -= schaden
    print(f"Angriff {len(angriffe)}: {schaden} Schaden (Troll HP: {max(0, troll_hp)})")
print(f"Anzahl der Angriffe: {len(angriffe)}")
print(f"Angriffsliste: {angriffe}")
print(f"Stärkster Angriff: {max(angriffe)}")

# =========================
# AUFGABE 15 – Winkelgasse-Shopping
# =========================
print("\n=== Aufgabe 15: Winkelgasse-Shopping ===")
preise = []
for i in range(1, 6):
    preis = round(random.uniform(1.5, 99.9), 2)
    preise.append(preis)
    print(f"Artikel {i}: {preis} Galleonen")
durchschnitt = round(sum(preise) / len(preise), 2)
print(f"Durchschnittspreis: {durchschnitt} Galleonen")

# =========================
# AUFGABE 16 – Schlossraum-Generator
# =========================
print("\n=== Aufgabe 16: Schlossraum-Generator ===")
raumtypen = ("Klassenzimmer", "Geheimgang", "Bibliothek", "Kerker", "Raum voller tanzender Besen")
schloss = []
for i in range(1, 11):
    raum = random.choice(raumtypen)
    schloss.append(raum)
    print(f"Raum {i}: {raum}")
print(f"Alle Räume: {schloss}")
print(f"Anzahl Geheimgänge: {schloss.count('Geheimgang')}")
print(f"Anzahl Bibliotheken: {schloss.count('Bibliothek')}")

# =========================
# AUFGABE 17 – Duell gegen die Schatten-KI
# =========================
print("\n=== Aufgabe 17: Duell gegen die Schatten-KI ===")
ki_hp = 100
schueler_hp = 80
runde = 0
while ki_hp > 0 and schueler_hp > 0:
    runde += 1
    schueler_schaden = random.randint(8, 18)
    ki_schaden = int(random.triangular(5, 20, 10))
    ki_hp -= schueler_schaden
    schueler_hp -= ki_schaden
    print(f"Runde {runde}: Schüler -{schueler_schaden} | Schatten-KI -{ki_schaden} "
            f"(KI HP: {max(0, ki_hp)}, Schüler HP: {max(0, schueler_hp)})")
if ki_hp <= 0 and schueler_hp <= 0:
    print("Unentschieden – beide fallen gleichzeitig in Ohnmacht!")
elif ki_hp <= 0:
    print("🧙 Der Schüler hat gewonnen!")
else:
    print("👾 Die Schatten-KI hat gewonnen!")

# =========================
# AUFGABE 18 – Loot-System in der Zauberkiste
# =========================
print("\n=== Aufgabe 18: Loot-System in der Zauberkiste ===")
moegliche_funde = ["Galleone", "Schokofrosch", "Zaubertrank", "Legendäre Socke"]
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
# AUFGABE 19 – Mini-Zauberschul-Rollenspiel
# =========================
print("\n=== Aufgabe 19: Mini-Zauberschul-Rollenspiel ===")
leben = 100
galleonen = 0
inventar = []
besuchte_orte = set()
orte = ["Große Halle", "Bibliothek", "Kerker", "Gewächshaus", "Krankenflügel", "Turm", "Verbotener Wald"]
ereignisse = ["Kampf", "Fund", "Falle", "Händler", "Rast"]
runde = 0

while leben > 0 and galleonen < 100:
    runde += 1
    ort = random.choice(orte)
    besuchte_orte.add(ort)
    ereignis = random.choice(ereignisse)

    if ereignis == "Kampf":
        schaden = random.randint(5, 20)
        leben -= schaden
        print(f"Runde {runde} | {ort}: Duellangriff! -{schaden} Leben (Leben: {max(0, leben)})")
    elif ereignis == "Fund":
        fund = random.randrange(5, 51, 5)
        galleonen += fund
        inventar.append("Zauberfund")
        print(f"Runde {runde} | {ort}: Zauberfund! +{fund} Galleonen (Galleonen: {galleonen})")
    elif ereignis == "Falle":
        schaden = int(random.triangular(1, 15, 5))
        leben -= schaden
        print(f"Runde {runde} | {ort}: Fluch-Falle! -{schaden} Leben (Leben: {max(0, leben)})")
    elif ereignis == "Händler":
        preis = round(random.uniform(1.0, 10.0), 2)
        inventar.append("Zaubertrank")
        print(f"Runde {runde} | {ort}: Zaubertrank für {preis} Galleonen gekauft.")
    elif ereignis == "Rast":
        heilung = random.randint(5, 15)
        leben = min(100, leben + heilung)
        print(f"Runde {runde} | {ort}: Rast im Schlafsaal! +{heilung} Leben (Leben: {leben})")

print("\n--- Abschlussbericht ---")
print(f"Leben: {max(0, leben)}")
print(f"Galleonen: {galleonen}")
print(f"Inventar: {inventar}")
print(f"Besuchte Orte: {besuchte_orte}")
if leben <= 0:
    print("💀 Der Schüler wurde vom Fluch erwischt.")
else:
    print("🏆 100 Galleonen gesammelt – Schuljahr bestanden!")

# =========================
# AUFGABE 20 – Der verfluchte Zauberschul-Simulator
# =========================
print("\n=== Aufgabe 20: Der verfluchte Zauberschul-Simulator ===")
schuelernamen = ["Hermine G.", "Ron W.", "Neville L.", "Luna L.", "Draco M."]
mission_orte = ["Verbotener Wald", "Kammer des Schreckens", "Winkelgasse", "Hogwarts-Express", "Ministerium"]
alle_missionen = []
erfolgreiche = []
niederlagen = []
besuchte_mission_orte = set()

for _ in range(100):
    name = random.choice(schuelernamen)
    ort = random.choice(mission_orte)
    dauer = random.randint(1, 30)
    gefahr = round(random.uniform(1.0, 10.0), 1)
    belohnung = random.randrange(0, 201, 10)
    erfolg = random.random() > 0.4

    besuchte_mission_orte.add(ort)
    mission = {
        "schueler": name, "ort": ort, "dauer": dauer,
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
print(f"Durchschnittliche Belohnung: {durchschnitt} Galleonen")
if bester_fund:
    print(f"Bester Fund: {bester_fund['schueler']} in {bester_fund['ort']} "
            f"mit {bester_fund['belohnung']} Galleonen")
print(f"Alle besuchten Orte: {besuchte_mission_orte}")
if lustigste_niederlage:
    print(f"Lustigste Niederlage: {lustigste_niederlage['schueler']} scheiterte in "
            f"{lustigste_niederlage['ort']} nach {lustigste_niederlage['dauer']} Tagen "
            f"(Gefahr: {lustigste_niederlage['gefahr']})")