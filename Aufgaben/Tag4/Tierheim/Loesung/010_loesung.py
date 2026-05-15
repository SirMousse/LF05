import random

# =========================
# AUFGABE 1 – Neues Tier angekommen
# =========================
print("=== Aufgabe 1: Neues Tier angekommen ===")
tiere = {1: "Hund", 2: "Katze", 3: "Kaninchen", 4: "sehr verwirrte Ziege"}
zahl = random.randint(1, 4)
print(f"Neues Tier im Tierheim: {tiere[zahl]}!")

# =========================
# AUFGABE 2 – Vermittlungs-Chance
# =========================
print("\n=== Aufgabe 2: Vermittlungs-Chance ===")
wert = random.random()
if wert < 0.5:
    print("Das Tier wurde vermittelt!")
else:
    print("Das Tier klaut erstmal Snacks.")

# =========================
# AUFGABE 3 – Futterlieferung
# =========================
print("\n=== Aufgabe 3: Futterlieferung ===")
pakete = random.randrange(10, 101, 10)
print(f"Futterlieferung angekommen: {pakete} Pakete!")

# =========================
# AUFGABE 4 – Energie-Level eines Welpen
# =========================
print("\n=== Aufgabe 4: Energie-Level eines Welpen ===")
energie = round(random.uniform(1.0, 10.0), 2)
print(f"Welpen-Energie-Level: {energie} / 10")

# =========================
# AUFGABE 5 – Tierarzt-Prognose
# =========================
print("\n=== Aufgabe 5: Tierarzt-Prognose ===")
heilung = random.triangular(1, 100, 80)
print(f"Tierarzt-Prognose: {heilung:.1f}% Heilungschance.")

# =========================
# AUFGABE 6 – Spaziergang-Runden
# =========================
print("\n=== Aufgabe 6: Spaziergang-Runden ===")
spaziergaenge = []
for i in range(1, 9):
    freude = random.randint(1, 9)
    spaziergaenge.append(freude)
    print(f"Spaziergang {i}: +{freude} Freude-Punkte")
print(f"Alle Freude-Punkte: {spaziergaenge}")

# =========================
# AUFGABE 7 – Spielstunde im Tierheim
# =========================
print("\n=== Aufgabe 7: Spielstunde im Tierheim ===")
spass_liste = []
for i in range(1, 11):
    spass = random.randint(1, 12)
    spass_liste.append(spass)
    print(f"Runde {i}: {spass} Spaß-Punkte")
print(f"Alle Punkte: {spass_liste}")
print(f"Gesamtpunkte: {sum(spass_liste)}")
print(f"Höchste Punktzahl: {max(spass_liste)}")

# =========================
# AUFGABE 8 – Die Katze versteckt sich
# =========================
print("\n=== Aufgabe 8: Die Katze versteckt sich ===")
versuche = 0
while True:
    versuche += 1
    wurf = random.randint(1, 6)
    print(f"Suchversuch {versuche}: {wurf}")
    if wurf == 6:
        print(f"Katze gefunden! Benötigte Versuche: {versuche}")
        break

# =========================
# AUFGABE 9 – Spenden sammeln
# =========================
print("\n=== Aufgabe 9: Spenden sammeln ===")
spenden = 0
runden = 0
while spenden < 100:
    spende = random.randint(5, 25)
    spenden += spende
    runden += 1
    print(f"Runde {runden}: +{spende} € (Gesamt: {spenden} €)")
print(f"Spendenziel erreicht nach {runden} Runden mit {spenden} €!")

# =========================
# AUFGABE 10 – Tierheim-Inventar
# =========================
print("\n=== Aufgabe 10: Tierheim-Inventar ===")
inventar = ["Leine", "Napf", "Kuscheldecke", "Ball", "sehr frecher Kater"]
index = random.randint(0, len(inventar) - 1)
print(f"Zufällig gefundenes Item: {inventar[index]}")

# =========================
# AUFGABE 11 – Tierarten im Heim
# =========================
print("\n=== Aufgabe 11: Tierarten im Heim ===")
tierarten_tuple = ("Hund", "Katze", "Kaninchen", "Papagei", "Schildkröte", "dramatisches Meerschweinchen")
index = random.randint(0, len(tierarten_tuple) - 1)
print(f"Zufälliges Tier: {tierarten_tuple[index]}")

# =========================
# AUFGABE 12 – Seltene Tierfunde
# =========================
print("\n=== Aufgabe 12: Seltene Tierfunde ===")
moegliche_tiere = ["Hund", "Katze", "Kaninchen", "Papagei", "Igel"]
tier_set = set()
for _ in range(10):
    tier = random.choice(moegliche_tiere)
    tier_set.add(tier)
print(f"Aufgenommene Tierarten: {tier_set}")
print("Tipp: Ein Set speichert jede Tierart nur einmal – egal wie oft dieselbe Art auftaucht.")

# =========================
# AUFGABE 13 – Rundgang durchs Tierheim
# =========================
print("\n=== Aufgabe 13: Rundgang durchs Tierheim ===")
bereiche = ["Hundehaus", "Katzenzimmer", "Tierarztzimmer", "Spielplatz", "Futterlager"]
rundgang = []
for schicht in range(1, 8):
    bereich = random.choice(bereiche)
    rundgang.append(bereich)
    print(f"Station {schicht}: {bereich}")
print(f"Ortsliste: {rundgang}")
print(f"Katzenzimmer besucht: {rundgang.count('Katzenzimmer')}-mal")
print(f"Futterlager besucht: {'Ja' if 'Futterlager' in rundgang else 'Nein'}")

# =========================
# AUFGABE 14 – Kampf gegen den Staubsauger
# =========================
print("\n=== Aufgabe 14: Kampf gegen den Staubsauger ===")
staubsauger_hp = 50
angriffe = []
while staubsauger_hp > 0:
    schaden = random.randint(5, 15)
    angriffe.append(schaden)
    staubsauger_hp -= schaden
    print(f"Angriff {len(angriffe)}: {schaden} Tatzen-Schaden (Staubsauger HP: {max(0, staubsauger_hp)})")
print(f"Anzahl der Angriffe: {len(angriffe)}")
print(f"Angriffsliste: {angriffe}")
print(f"Stärkster Angriff: {max(angriffe)}")

# =========================
# AUFGABE 15 – Einkauf fürs Tierheim
# =========================
print("\n=== Aufgabe 15: Einkauf fürs Tierheim ===")
preise = []
for i in range(1, 6):
    preis = round(random.uniform(1.5, 99.9), 2)
    preise.append(preis)
    print(f"Artikel {i}: {preis} €")
durchschnitt = round(sum(preise) / len(preise), 2)
print(f"Durchschnittspreis: {durchschnitt} €")

# =========================
# AUFGABE 16 – Tierzimmer-Generator
# =========================
print("\n=== Aufgabe 16: Tierzimmer-Generator ===")
zimmer_tuple = ("Hundezimmer", "Katzenzimmer", "Spielraum", "Leerer Raum", "Raum voller quietschender Enten")
tierheim = []
for i in range(1, 11):
    zimmer = random.choice(zimmer_tuple)
    tierheim.append(zimmer)
    print(f"Bereich {i}: {zimmer}")
print(f"Alle Bereiche: {tierheim}")
print(f"Anzahl Hundezimmer: {tierheim.count('Hundezimmer')}")
print(f"Anzahl Katzenzimmer: {tierheim.count('Katzenzimmer')}")

# =========================
# AUFGABE 17 – Duell gegen den Futterdieb
# =========================
print("\n=== Aufgabe 17: Duell gegen den Futterdieb ===")
dieb_hp = 100
hund_hp = 80
runde = 0
while dieb_hp > 0 and hund_hp > 0:
    runde += 1
    hund_schaden = random.randint(8, 18)
    dieb_schaden = int(random.triangular(5, 20, 10))
    dieb_hp -= hund_schaden
    hund_hp -= dieb_schaden
    print(f"Runde {runde}: Hund -{hund_schaden} | Futterdieb -{dieb_schaden} "
            f"(Dieb HP: {max(0, dieb_hp)}, Hund HP: {max(0, hund_hp)})")
if dieb_hp <= 0 and hund_hp <= 0:
    print("Unentschieden – beide erschöpft auf dem Boden!")
elif dieb_hp <= 0:
    print("🐕 Der Hund hat gewonnen – Futter gerettet!")
else:
    print("🥷 Der Futterdieb entwischt – Verfolgung aufgenommen!")

# =========================
# AUFGABE 18 – Überraschungsboxen
# =========================
print("\n=== Aufgabe 18: Überraschungsboxen ===")
moegliche_funde = ["Leckerli", "Spielzeug", "Kuscheldecke", "Legendäre Quietscheente"]
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
# AUFGABE 19 – Mini-Tierheim-Rollenspiel
# =========================
print("\n=== Aufgabe 19: Mini-Tierheim-Rollenspiel ===")
energie = 100
spenden = 0
inventar = []
besuchte_orte = set()
orte = ["Hundehaus", "Katzenzimmer", "Tierarztzimmer", "Spielplatz", "Futterlager", "Büro", "Außengehege"]
ereignisse = ["Stress", "Spende", "Unfall", "Einkauf", "Pause"]
runde = 0

while energie > 0 and spenden < 100:
    runde += 1
    ort = random.choice(orte)
    besuchte_orte.add(ort)
    ereignis = random.choice(ereignisse)

    if ereignis == "Stress":
        verlust = random.randint(5, 20)
        energie -= verlust
        print(f"Runde {runde} | {ort}: Stressiger Einsatz! -{verlust} Energie (Energie: {max(0, energie)})")
    elif ereignis == "Spende":
        betrag = random.randrange(5, 51, 5)
        spenden += betrag
        inventar.append("Spendeneingang")
        print(f"Runde {runde} | {ort}: Spende eingegangen! +{betrag} € (Spenden: {spenden} €)")
    elif ereignis == "Unfall":
        verlust = int(random.triangular(1, 15, 5))
        energie -= verlust
        print(f"Runde {runde} | {ort}: Kleiner Unfall! -{verlust} Energie (Energie: {max(0, energie)})")
    elif ereignis == "Einkauf":
        preis = round(random.uniform(1.0, 10.0), 2)
        inventar.append("Tierbedarf")
        print(f"Runde {runde} | {ort}: Tierbedarf für {preis} € eingekauft.")
    elif ereignis == "Pause":
        erholung = random.randint(5, 15)
        energie = min(100, energie + erholung)
        print(f"Runde {runde} | {ort}: Wohlverdiente Pause! +{erholung} Energie (Energie: {energie})")

print("\n--- Schichtbericht ---")
print(f"Energie: {max(0, energie)}")
print(f"Spenden: {spenden} €")
print(f"Inventar: {inventar}")
print(f"Besuchte Orte: {besuchte_orte}")
if energie <= 0:
    print("😴 Der Mitarbeiter ist erschöpft – Feierabend!")
else:
    print("🐾 100 € Spenden gesammelt – die Tiere sind versorgt!")

# =========================
# AUFGABE 20 – Der verfluchte Tierheim-Simulator
# =========================
print("\n=== Aufgabe 20: Der verfluchte Tierheim-Simulator ===")
mitarbeiter_namen = ["Sabine", "Markus", "Julia", "Tobias", "Petra"]
tages_bereiche = ["Hundestation", "Katzenflügel", "Kleintierbereich", "Außengehege", "Quarantäne"]
alle_tage = []
erfolgreiche = []
niederlagen = []
besuchte_tages_orte = set()

for _ in range(100):
    name = random.choice(mitarbeiter_namen)
    bereich = random.choice(tages_bereiche)
    dauer = random.randint(1, 12)
    ereignisse_tag = round(random.uniform(1.0, 10.0), 1)
    belohnung = random.randrange(0, 201, 10)
    erfolg = random.random() > 0.4

    besuchte_tages_orte.add(bereich)
    tag = {
        "mitarbeiter": name, "bereich": bereich, "dauer": dauer,
        "ereignisse": ereignisse_tag, "belohnung": belohnung, "erfolg": erfolg
    }
    alle_tage.append(tag)
    if erfolg:
        erfolgreiche.append(tag)
    else:
        niederlagen.append(tag)

durchschnitt = round(
    sum(t["belohnung"] for t in erfolgreiche) / len(erfolgreiche), 2
) if erfolgreiche else 0

bester_tag = max(erfolgreiche, key=lambda t: t["belohnung"]) if erfolgreiche else None
lustigste_niederlage = random.choice(niederlagen) if niederlagen else None

print(f"Erfolgreiche Tage: {len(erfolgreiche)} / 100")
print(f"Durchschnittliche Belohnung: {durchschnitt} Punkte")
if bester_tag:
    print(f"Bester Tag: {bester_tag['mitarbeiter']} im {bester_tag['bereich']} "
            f"mit {bester_tag['belohnung']} Punkten")
print(f"Alle besuchten Bereiche: {besuchte_tages_orte}")
if lustigste_niederlage:
    print(f"Lustigste Niederlage: {lustigste_niederlage['mitarbeiter']} hatte einen schlechten Tag "
            f"im {lustigste_niederlage['bereich']} nach {lustigste_niederlage['dauer']} Stunden "
            f"(Ereignisse: {lustigste_niederlage['ereignisse']})")