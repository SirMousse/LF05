import random

# ==================================================
# DIE REISE NACH MORDOR
# Ein komplettes Herr-der-Ringe-Text-Adventure
# ==================================================

print("=" * 50)
print("   DIE REISE NACH MORDOR")
print("   Zerstoere den Einen Ring!")
print("=" * 50)


# ==================================================
# LEVEL 1 – DER HELD AUS DEM AUENLAND
# Konzepte: Variablen, print(), input()
# ==================================================
print("\n--- LEVEL 1: DER HELD ---")

# input() zeigt Text an und wartet auf Eingabe.
# Das Ergebnis ist immer ein String.
name  = input("Wie lautet dein Name?\n> ")
rasse = input("Deine Rasse (Hobbit / Mensch / Elb / Zwerg):\n> ")
alter = input("Dein Alter:\n> ")

# f-Strings: {} wird durch den Variablenwert ersetzt.
print(f"\nWillkommen in Mittelerde!")
print(f"Sei gegruesst {name} der {rasse}.")
print(f"Du bist {alter} Jahre alt. Deine Reise beginnt im Auenland.")


# ==================================================
# LEVEL 2 – DAS TOR VON MORIA
# Konzepte: if / elif / else, Fehlversuche
# ==================================================
print("\n--- LEVEL 2: DAS TOR VON MORIA ---")
print("Vor dir ragt das Tor von Moria auf.")
print("Sprich Freund und tritt ein.")

richtiges_passwort = "mellon"
fehlversuche = 0

while True:
    eingabe = input("Passwort:\n> ")

    # .lower() macht die Eingabe kleingeschrieben,
    # damit "Mellon" und "MELLON" auch akzeptiert werden.
    if eingabe.lower() == richtiges_passwort:
        print("Das Tor von Moria oeffnet sich!")
        break
    else:
        fehlversuche += 1
        print(f"Das Tor bleibt verschlossen. Fehlversuche: {fehlversuche}")
        if fehlversuche >= 3:
            print("Ein Watcher in the Water taucht auf... versuche es weiter!")


# ==================================================
# LEVEL 3 – DER WUERFEL DER ORKS
# Konzepte: random
# ==================================================
print("\n--- LEVEL 3: ORK-ANGRIFF ---")
print("Ein Ork versperrt dir den Weg!")

# random.randint(1, 6) gibt eine zufaellige Zahl von 1 bis 6.
spieler_wert = random.randint(1, 6)
ork_wert     = random.randint(1, 6)

print(f"Deine Staerke: {spieler_wert}")
print(f"Ork-Staerke:   {ork_wert}")

if spieler_wert > ork_wert:
    print("Sieg! Der Ork flieht.")
elif spieler_wert == ork_wert:
    print("Unentschieden! Beide weichen zurueck.")
else:
    print("Niederlage! Du musst dich zurueckziehen.")


# ==================================================
# LEVEL 4 – DAS INVENTAR DER GEFAEHRTEN
# Konzepte: Listen
# ==================================================
print("\n--- LEVEL 4: INVENTAR ---")

# Eine Liste speichert mehrere Werte. Index startet bei 0.
inventar = ["Lembas", "Dolch", "Ring"]

# Alle Gegenstaende anzeigen
print("Dein Inventar:")
for item in inventar:
    print(f"  - {item}")

# Neues Item hinzufuegen: .append() haengt ans Ende.
inventar.append("Elbenbogen")
print(f"\nNach Fund von Elbenbogen: {inventar}")

# Item entfernen: .remove() loescht den ersten passenden Wert.
inventar.remove("Lembas")
print(f"Lembas aufgegessen: {inventar}")

# Pruefen ob Item vorhanden: "in" gibt True oder False.
if "Ring" in inventar:
    print("Der Eine Ring liegt schwer in deiner Tasche...")

# Bonus: Spieler kann eigene Items hinzufuegen.
neues_item = input("Was findest du noch?\n> ")
if len(inventar) < 10:   # Inventar-Limit: max. 10 Plaetze
    inventar.append(neues_item)
    print(f"Inventar: {inventar}")
else:
    print("Rucksack voll! (max. 10 Plaetze)")


# ==================================================
# LEVEL 5 – DER WEG DURCH DEN DUSTERWALD
# Konzepte: while-Schleife
# ==================================================
print("\n--- LEVEL 5: DER DUSTERWALD ---")
print("Du bist im Dusterwald verirrt!")

# while True laeuft endlos – verlassen nur mit break.
while True:
    print("\nWas tust du?")
    print("1 - Nach Norden gehen")
    print("2 - Nach Sueden gehen")
    print("3 - Lager aufschlagen")

    wahl = input("> ")

    if wahl == "1":
        print("Riesige Spinnen lauern in den Baeumen...")
    elif wahl == "2":
        print("Ein Lichtschimmer – doch es ist ein Irrlicht.")
    elif wahl == "3":
        print("Du schlagst Lager auf. Die Nacht ist ruhig.")
        break  # Schleife verlassen
    else:
        print("Der Wald schweigt.")


# ==================================================
# LEVEL 6 – DIE SCHLACHT GEGEN DIE ORKS
# Konzepte: for-Schleifen
# ==================================================
print("\n--- LEVEL 6: ORC-SCHLACHT ---")
print("Fuenf Orks greifen an!\n")

siege        = 0
niederlagen  = 0
unentschieden = 0

# range(1, 6) erzeugt die Zahlen 1 bis 5.
for i in range(1, 6):
    spieler_staerke = random.randint(1, 10)
    ork_staerke     = random.randint(1, 10)

    print(f"Ork {i}: Du {spieler_staerke} vs. Ork {ork_staerke}")

    if spieler_staerke > ork_staerke:
        print("  Sieg!")
        siege += 1
    elif spieler_staerke == ork_staerke:
        print("  Unentschieden!")
        unentschieden += 1
    else:
        print("  Niederlage!")
        niederlagen += 1

print(f"\nSchlacht-Ergebnis: {siege} Siege, {niederlagen} Niederlagen, {unentschieden} Unentschieden.")


# ==================================================
# LEVEL 7 – DIE BIBLIOTHEK VON BRUCHTAL
# Konzepte: Dictionaries
# ==================================================
print("\n--- LEVEL 7: WAFFENKAMMER VON BRUCHTAL ---")

# Dictionary: Schluessel-Wert-Paare in geschweiften Klammern {}.
waffen = {
    "Anduril":   100,
    "Sting":      50,
    "Elbenbogen": 70
}

# Alle Waffen anzeigen: .items() liefert Schluessel+Wert als Paare.
print("Verfuegbare Waffen:")
for name_w, staerke_w in waffen.items():
    print(f"  {name_w}: {staerke_w} Staerke")

# Staerke einer Waffe abrufen
print(f"\nAnduril-Staerke: {waffen['Anduril']}")

# Neue Waffe hinzufuegen
waffen["Glamdring"] = 85
print(f"Glamdring hinzugefuegt: {waffen}")

# Waffe entfernen
del waffen["Elbenbogen"]
print(f"Elbenbogen verloren: {waffen}")

# Spieler waehlt Waffe
print("\nVerfuegbare Waffen:", list(waffen.keys()))
gewaehlte_waffe = input("Welche Waffe nimmst du?\n> ")
if gewaehlte_waffe in waffen:
    print(f"{gewaehlte_waffe} ausgewaehlt! Staerke: {waffen[gewaehlte_waffe]}")
else:
    print("Diese Waffe gibt es nicht.")


# ==================================================
# LEVEL 8 – DIE KARTE VON MITTELERDE
# Konzepte: Tupel
# ==================================================
print("\n--- LEVEL 8: KARTE VON MITTELERDE ---")

# Ein Tupel ist unveraenderlich – perfekt fuer feste Koordinaten.
mordor = (10, 25)
print(f"Mordor liegt bei X={mordor[0]}, Y={mordor[1]}")

# Mehrere Orte als Tupel-Liste (Bonus)
orte = [
    ("Auenland",  1,  2),
    ("Bruchtal",  4,  6),
    ("Moria",     6, 10),
    ("Gondor",    8, 18),
    ("Mordor",   10, 25),
]

print("\nKarte von Mittelerde:")
for ort_name, x, y in orte:
    print(f"  {ort_name}: ({x}, {y})")

# Spielerposition pruefen
try:
    sx = int(input("\nDeine X-Position:\n> "))
    sy = int(input("Deine Y-Position:\n> "))
except ValueError:
    sx, sy = 0, 0

if (sx, sy) == mordor:
    print("Du hast Mordor erreicht! Der Schicksalsberg wartet.")
else:
    print(f"Noch nicht da. Mordor liegt bei {mordor}.")


# ==================================================
# LEVEL 9 & ENDGEGNER – DIE REISE DER GEFAEHRTEN
# Konzepte: ALLES kombiniert + Klassen + Funktionen
# ==================================================
print("\n" + "=" * 50)
print("   LEVEL 9: DIE REISE BEGINNT")
print("   Ziel: Sauron besiegen!")
print("=" * 50)


# ---- Funktionen ----
def zeige_status(sname, leben, gold, inv):
    """Zeigt den aktuellen Spielerstatus an."""
    print(f"\n[ {sname} | HP {leben} | {gold} Gold | {inv} ]")

def berechne_angriff(basis, krit_chance=0.2):
    """Berechnet Angriff mit Chance auf kritischen Treffer."""
    schaden = random.randint(basis - 3, basis + 5)
    # random.random() liefert 0.0 bis 1.0 – unter krit_chance = Krit!
    if random.random() < krit_chance:
        schaden *= 2
        print("Kritischer Treffer! Doppelter Schaden!")
    return schaden

def heile(leben, max_leben, menge):
    """Heilt den Spieler, aber nicht ueber max_leben."""
    # min() verhindert Ueberheilung.
    neues_leben = min(leben + menge, max_leben)
    print(f"Geheilt: +{neues_leben - leben} HP.")
    return neues_leben


# ---- Klasse ----
class Feind:
    def __init__(self, name, leben, angriff):
        # __init__ wird beim Erstellen automatisch aufgerufen.
        # self.xyz speichert den Wert im Objekt.
        self.name    = name
        self.leben   = leben
        self.angriff = angriff

    def greift_an(self):
        """Gibt zufaelligen Schaden zurueck."""
        return random.randint(self.angriff - 4, self.angriff + 4)

    def ist_besiegt(self):
        """True wenn keine HP mehr."""
        return self.leben <= 0


# ---- Spielaufbau ----
print("\nNeues Abenteuer startet...")
spieler_name     = input("Dein Heldenname:\n> ")
spieler_leben     = 100
spieler_max_leben = 100
spieler_gold      = 30
spieler_inventar  = ["Heiltrank", "Heiltrank", "Dolch"]

# Reiseroute als Tupel-Liste (Name, X, Y)
reiseroute = [
    ("Auenland",  1,  2),
    ("Rohan",     6,  8),
    ("Mordor",   10, 25),
]

# Waffenkammer als Dictionary
waffenkammer = {
    "Anduril":  25,
    "Sting":    18,
    "Glamdring": 30,
}

# Feind-Pool
feind_pool = [
    {"name": "Ork",      "leben": 35, "angriff": 10, "gold": 6,  "drop": "Ork-Schwert"},
    {"name": "Nazgul",   "leben": 55, "angriff": 15, "gold": 14, "drop": "Ringgeist-Klinge"},
    {"name": "Troll",    "leben": 45, "angriff": 12, "gold": 10, "drop": "Trolle-Keule"},
]

# ---- Haendler in Rohan ----
print("\nEin Haendler in Rohan bietet seine Waren an!")
# Preise aendern sich zufaellig (Mini-Challenge)
haendler = {
    "Heiltrank":    random.randint(8,  14),
    "Staerketrank": random.randint(12, 20),
    "Mithrilhemd":  random.randint(25, 40),
}

print("Angebot:")
for item_h, preis_h in haendler.items():
    print(f"  {item_h}: {preis_h} Gold")

kauf = input("Was kaufst du? (oder 'weiter')\n> ")
if kauf in haendler:
    preis = haendler[kauf]
    if spieler_gold >= preis:
        spieler_gold -= preis
        if len(spieler_inventar) < 10:
            spieler_inventar.append(kauf)
            print(f"Gekauft! {kauf} fuer {preis} Gold.")
        else:
            print("Rucksack voll!")
    else:
        print("Nicht genug Gold!")
else:
    print("Nichts gekauft.")

# ---- Reise durch Mittelerde ----
print(f"\nReiseroute:")
for oname, ox, oy in reiseroute:
    print(f"  [{ox:02d},{oy:02d}] {oname}")

print(f"\n{spieler_name} bricht auf...\n")

for oname, ox, oy in reiseroute:
    if spieler_leben <= 0:
        break

    print(f"\n  Ort: {oname} ({ox},{oy})")

    # Zufaelliges Ereignis pro Ort
    ereignis = random.choice(["kampf", "geheimhoehle", "rast"])

    # 10% Chance auf Nazgul (Mini-Challenge)
    if random.random() < 0.1:
        ereignis = "nazgul"

    if ereignis in ("kampf", "nazgul"):
        if ereignis == "nazgul":
            f_daten = {"name": "Nazgul", "leben": 55, "angriff": 15,
                         "gold": 14, "drop": "Ringgeist-Klinge"}
            print(f"  Ein Nazgul taucht aus dem Nebel auf!")
        else:
            f_daten = random.choice(feind_pool)

        feind = Feind(f_daten["name"], f_daten["leben"], f_daten["angriff"])
        print(f"  {feind.name} greift an!")

        # Kampfschleife: laeuft bis einer besiegt ist.
        while not feind.ist_besiegt() and spieler_leben > 0:
            s = berechne_angriff(14)
            feind.leben -= s
            gegenschaden = feind.greift_an()
            spieler_leben -= gegenschaden
            spieler_leben = max(0, spieler_leben)
            print(f"  Du: -{gegenschaden} HP | {feind.name}: -{s} HP "
                    f"({feind.name}: {max(0,feind.leben)} HP, Du: {spieler_leben} HP)")

        if feind.ist_besiegt():
            print(f"  {feind.name} besiegt! +{f_daten['gold']} Gold")
            spieler_gold += f_daten["gold"]
            # Drop
            if random.random() < 0.4:
                drop = f_daten["drop"]
                if len(spieler_inventar) < 10:
                    spieler_inventar.append(drop)
                    print(f"  Fund: {drop}")
        else:
            print("  Du bist gefallen...")

    elif ereignis == "geheimhoehle":
        # Geheime Hoehle (Mini-Challenge)
        fund = random.randrange(10, 51, 10)
        spieler_gold += fund
        print(f"  Geheime Hoehle entdeckt! +{fund} Gold")

    else:
        heilung = random.randint(10, 20)
        spieler_leben = heile(spieler_leben, spieler_max_leben, heilung)

    zeige_status(spieler_name, spieler_leben, spieler_gold, spieler_inventar)

    if spieler_leben <= 0:
        print("\nGame Over – Der Ring siegte...")
        exit()

# ---- ENDGEGNER: SAURONS AUGE ----
print("\n" + "=" * 50)
print("   DAS AUGE SAURONS ERBLICKT DICH!")
print("=" * 50)

sauron = Feind("Saurons Macht", 120, 17)
print(f"\nSaurons Macht: HP {sauron.leben}\n")

while not sauron.ist_besiegt() and spieler_leben > 0:
    zeige_status(spieler_name, spieler_leben, spieler_gold, spieler_inventar)
    print(f"Gegner-HP: {sauron.leben}")
    print("\nAktion:")
    print("1 - Angreifen")
    print("2 - Heilen (Heiltrank noetig)")
    print("3 - Waffe einsetzen (Waffenkammer)")
    print("4 - Fliehen")

    aktion = input("> ")

    if aktion == "1":
        s = berechne_angriff(14)
        sauron.leben -= s
        print(f"Treffer! {s} Schaden auf Sauron!")

    elif aktion == "2":
        if "Heiltrank" in spieler_inventar:
            spieler_inventar.remove("Heiltrank")
            spieler_leben = heile(spieler_leben, spieler_max_leben, 35)
        else:
            print("Kein Heiltrank mehr!")
            continue  # Runde ohne Gegenzug wiederholen

    elif aktion == "3":
        print("Waffenkammer:", list(waffenkammer.keys()))
        gew = input("Welche Waffe?\n> ")
        if gew in waffenkammer:
            ws = waffenkammer[gew]
            sauron.leben -= ws
            print(f"{gew} eingesetzt! {ws} Schaden!")
        else:
            print("Diese Waffe kennst du nicht!")
            continue

    elif aktion == "4":
        print("Du fluechtest... der Ring bleibt in Mittelerde.")
        exit()

    else:
        print("Ungueltige Eingabe.")
        continue

    # Sauron schlaegt zurueck
    if not sauron.ist_besiegt():
        ds = sauron.greift_an()
        spieler_leben -= ds
        spieler_leben = max(0, spieler_leben)
        print(f"Sauron trifft dich fuer {ds} Schaden!")

# ---- Ergebnis ----
print("\n" + "=" * 50)
if sauron.ist_besiegt():
    print(f"{spieler_name} hat Sauron besiegt!")
    print("Der Eine Ring wird in den Schicksalsberg geworfen.")
    print("Mittelerde ist gerettet!")
    print(f"\nEndstatistik:")
    print(f"  Restliche HP: {spieler_leben}")
    print(f"  Gold:         {spieler_gold}")
    print(f"  Inventar:     {spieler_inventar}")
else:
    print(f"{spieler_name} ist gefallen.")
    print("Das Auge Saurons brennt weiter ueber Mittelerde...")
print("=" * 50)