import random

# ==================================================
# DAS GEHEIMNIS VON HOGWARTS
# Ein komplettes Harry-Potter-Text-Adventure
# ==================================================

print("=" * 50)
print("   DAS GEHEIMNIS VON HOGWARTS")
print("   Ein dunkles Artefakt wurde gestohlen...")
print("=" * 50)


# ==================================================
# LEVEL 1 – DER SPRECHENDE HUT
# Konzepte: Variablen, print(), input()
# ==================================================
print("\n--- LEVEL 1: DER SPRECHENDE HUT ---")

# input() zeigt einen Text an und wartet auf Eingabe.
# Das Ergebnis ist immer ein String und wird in einer Variable gespeichert.
name  = input("Wie heisst du?\n> ")
alter = input("Wie alt bist du?\n> ")
haus  = input("Welches Haus? (Gryffindor / Slytherin / Ravenclaw / Hufflepuff)\n> ")

# f-Strings: {} im Text wird durch den Variablenwert ersetzt.
print(f"\nWillkommen in Hogwarts!")
print(f"Willkommen {name} aus {haus}.")
print(f"Du bist {alter} Jahre alt. Dein erstes Schuljahr beginnt.")


# ==================================================
# LEVEL 2 – PASSWORT ZUM GEMEINSCHAFTSRAUM
# Konzepte: if / elif / else, Fehlversuche zaehlen
# ==================================================
print("\n--- LEVEL 2: PASSWORT ZUM GEMEINSCHAFTSRAUM ---")
print("Ein Gemaelde versperrt den Weg. Es verlangt ein Passwort.")

richtiges_passwort = "lumos"
fehlversuche = 0

while True:
    eingabe = input("Passwort eingeben: > ")

    if eingabe.lower() == richtiges_passwort:
        # .lower() wandelt die Eingabe in Kleinbuchstaben um – damit
        # "Lumos" und "LUMOS" beide als richtig erkannt werden.
        print("Zugang erlaubt! Die Tuer oeffnet sich.")
        break
    else:
        fehlversuche += 1  # fehlversuche = fehlversuche + 1
        print(f"Zugang verweigert! Fehlversuche: {fehlversuche}")
        if fehlversuche >= 3:
            print("Das Gemaelde gahnt gelangweilt. Versuch es weiter...")


# ==================================================
# LEVEL 3 – DAS ZAUBERDUELL
# Konzepte: random, Zufallszahlen vergleichen
# ==================================================
print("\n--- LEVEL 3: DAS ZAUBERDUELL ---")
print("Ein Mitschueler fordert dich heraus!")

# random.randint(1, 6) gibt eine zufaellige ganze Zahl von 1 bis 6 zurueck.
meine_staerke   = random.randint(1, 6)
gegner_staerke  = random.randint(1, 6)

print(f"Deine Zauberkraft: {meine_staerke}")
print(f"Gegner-Zauberkraft: {gegner_staerke}")

if meine_staerke > gegner_staerke:
    print("Sieg! Du hast das Duell gewonnen!")
elif meine_staerke == gegner_staerke:
    print("Unentschieden! Beide Zauberer erschoepft sich gleichzeitig.")
else:
    print("Niederlage! Der Gegner ist staerker.")


# ==================================================
# LEVEL 4 – DER KOFFER DER ZAUBERER
# Konzepte: Listen
# ==================================================
print("\n--- LEVEL 4: DER KOFFER ---")

# Eine Liste speichert mehrere Werte. Zugriff ueber Index (startet bei 0).
inventar = ["Zauberstab", "Umhang", "Schokofrosch"]

# Alle Gegenstaende anzeigen
print("Dein Inventar:")
for gegenstand in inventar:
    print(f"  - {gegenstand}")

# Neues Item hinzufuegen: .append() haengt ans Ende.
inventar.append("Zauberbuch")
print(f"\nNach Fund von Zauberbuch: {inventar}")

# Item entfernen: .remove() loescht den ersten passenden Wert.
inventar.remove("Schokofrosch")
print(f"Schokofrosch aufgegessen: {inventar}")

# Pruefen ob Item vorhanden: "in" gibt True oder False zurueck.
if "Zauberstab" in inventar:
    print("Zauberstab bereit!")

# Bonus: Spieler kann selbst Items hinzufuegen.
neues_item = input("Was packst du noch ein? > ")
if len(inventar) < 10:  # Inventar-Limit: max. 10 Plaetze (Mini-Challenge)
    inventar.append(neues_item)
    print(f"Inventar jetzt: {inventar}")
else:
    print("Koffer ist voll! (max. 10 Gegenstaende)")


# ==================================================
# LEVEL 5 – DIE TREPPEN VON HOGWARTS
# Konzepte: while-Schleife, Menuefuehrung
# ==================================================
print("\n--- LEVEL 5: DIE MAGISCHEN TREPPEN ---")
print("Die Treppen bewegen sich staendig!")

# while True laeuft endlos – wir verlassen sie nur mit break.
while True:
    print("\nWo willst du hin?")
    print("1 - Nach oben gehen")
    print("2 - Nach unten gehen")
    print("3 - Klassenraum gefunden")

    wahl = input("> ")

    if wahl == "1":
        print("Die Treppe dreht sich – du landest woanders!")
    elif wahl == "2":
        print("Ein Geist winkt dir zu und verschwindet.")
    elif wahl == "3":
        print("Endlich! Du hast den Trankkunde-Raum gefunden.")
        break  # Schleife verlassen
    else:
        print("Ungueltiger Befehl – die Treppe bewegt sich trotzdem.")


# ==================================================
# LEVEL 6 – DIE VERBOTENEN DUELLE
# Konzepte: for-Schleifen
# ==================================================
print("\n--- LEVEL 6: VERBOTENE DUELLE ---")
print("Fuenf Duelle warten auf dich!\n")

siege       = 0
niederlagen = 0
unentschieden = 0

# range(1, 6) erzeugt die Zahlen 1 bis 5.
for i in range(1, 6):
    mein_wert    = random.randint(1, 10)
    gegner_wert  = random.randint(1, 10)

    print(f"Duell {i}: Du {mein_wert} vs. Gegner {gegner_wert}")

    if mein_wert > gegner_wert:
        print("  Sieg!")
        siege += 1
    elif mein_wert == gegner_wert:
        print("  Unentschieden!")
        unentschieden += 1
    else:
        print("  Niederlage!")
        niederlagen += 1

print(f"\nErgebnis: {siege} Siege, {niederlagen} Niederlagen, {unentschieden} Unentschieden.")


# ==================================================
# LEVEL 7 – DIE BIBLIOTHEK DER ZAUBERSPRUCHE
# Konzepte: Dictionaries
# ==================================================
print("\n--- LEVEL 7: ZAUBERBIBLIOTHEK ---")

# Dictionary: Schluessel-Wert-Paare in geschweiften Klammern {}.
# zauber["Expelliarmus"] gibt 50 zurueck.
zauber = {
    "Expelliarmus": 50,
    "Stupefy":      70,
    "Lumos":        20
}

# Alle Zauber anzeigen: .items() liefert Schluessel+Wert als Paare.
print("Bekannte Zauber:")
for name_z, staerke_z in zauber.items():
    print(f"  {name_z}: {staerke_z} Kraft")

# Staerke abrufen
print(f"\nStupefy-Kraft: {zauber['Stupefy']}")

# Neuen Zauber hinzufuegen
zauber["Accio"] = 40
print(f"Accio gelernt: {zauber}")

# Zauber entfernen
del zauber["Lumos"]
print(f"Lumos vergessen: {zauber}")

# Spieler waehlt Zauber
print("\nVerfuegbare Zauber:", list(zauber.keys()))
gewaehlter = input("Welchen Zauber verwendest du? > ")
if gewaehlter in zauber:
    print(f"{gewaehlter} gewirkt! Kraft: {zauber[gewaehlter]}")
else:
    print("Diesen Zauber kennst du noch nicht.")


# ==================================================
# LEVEL 8 – DIE KARTE DES RUMTREIBERS
# Konzepte: Tupel
# ==================================================
print("\n--- LEVEL 8: KARTE DES RUMTREIBERS ---")

# Ein Tupel ist unveraenderlich – perfekt fuer feste Koordinaten.
# Zugriff wie bei Listen: hogwarts[0] = X, hogwarts[1] = Y
hogwarts_ziel = (12, 8)
print(f"Zielraum: X={hogwarts_ziel[0]}, Y={hogwarts_ziel[1]}")

# Mehrere Orte als Tupel-Liste (Bonus)
orte = [
    ("Grosse Halle",     5,  2),
    ("Gemeinschaftsraum", 3,  7),
    ("Verbotener Wald", 15, 12),
    ("Bibliothek",       8,  4),
    ("Kerker",           2, 10),
]

print("\nKarte von Hogwarts:")
for ort_name, x, y in orte:
    print(f"  {ort_name}: ({x}, {y})")

# Spielerposition pruefen
try:
    sx = int(input("\nDeine X-Position: > "))
    sy = int(input("Deine Y-Position: > "))
except ValueError:
    sx, sy = 0, 0

if (sx, sy) == hogwarts_ziel:
    print("Du hast den geheimen Raum gefunden!")
else:
    print(f"Falscher Ort. Das Artefakt ist bei {hogwarts_ziel}.")


# ==================================================
# LEVEL 9 & ENDGEGNER – DAS GEHEIMNIS VON HOGWARTS
# Konzepte: ALLES kombiniert + Klassen + Funktionen
# ==================================================
print("\n" + "=" * 50)
print("   LEVEL 9: DAS DUNKLE ARTEFAKT")
print("   Rette Hogwarts!")
print("=" * 50)


# ---- Funktionen ----
# def definiert eine wiederverwendbare Funktion.

def zeige_status(sname, leben, galleonen, inv):
    """Zeigt den aktuellen Spielerstatus an."""
    print(f"\n[ {sname} | HP {leben} | {galleonen} Galleonen | {inv} ]")

def berechne_zauber(basis, krit_chance=0.2):
    """Berechnet Zauberschaden mit Chance auf kritischen Treffer."""
    schaden = random.randint(basis - 3, basis + 5)
    # random.random() liefert 0.0 bis 1.0 – unter krit_chance = Krit!
    if random.random() < krit_chance:
        schaden *= 2
        print("Kritischer Zauber! Doppelter Schaden!")
    return schaden

def heile(leben, max_leben, menge):
    """Heilt den Spieler, aber nicht ueber max_leben hinaus."""
    # min() verhindert Ueberheilung.
    neues_leben = min(leben + menge, max_leben)
    print(f"Heilung: +{neues_leben - leben} HP.")
    return neues_leben


# ---- Klasse ----
# Eine Klasse ist ein Bauplan fuer Objekte.

class Zauberer:
    def __init__(self, name, leben, angriff):
        # __init__ wird beim Erstellen des Objekts automatisch aufgerufen.
        # self.xyz speichert den Wert im Objekt selbst.
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
print("\nEin neues Abenteuer beginnt...")
spieler_name     = input("Dein Helden-Name: > ")
spieler_leben     = 100
spieler_max_leben = 100
spieler_galleonen = 35
spieler_inventar  = ["Heiltrank", "Heiltrank", "Zauberstab"]

# Hauspunkte-System (Mini-Challenge)
hauspunkte = 0

# Orte als Tupel (Name, X, Y)
hogwarts_orte = [
    ("Eingangshalle",  1, 1),
    ("Winkelgasse",    4, 3),
    ("Verbotener Wald", 9, 9),
]

# Zauberbuch als Dictionary
zauberbuch = {
    "Expelliarmus": 20,
    "Stupefy":      30,
    "Confringo":    40,
}

# Gegner-Pool
gegner_pool = [
    {"name": "Dementor",        "leben": 35, "angriff": 10, "galleonen": 8,  "drop": "Patronus-Feder"},
    {"name": "Todesser",        "leben": 50, "angriff": 14, "galleonen": 12, "drop": "Zauberstab-Splitter"},
    {"name": "Riesige Spinne",  "leben": 40, "angriff": 11, "galleonen": 7,  "drop": "Spinnenfaden"},
]

# ---- Winkelgasse-Haendler ----
print("\nWinkelgasse: Ein Zaubererhaendler winkt dir zu!")
# Preise aendern sich zufaellig (Mini-Challenge)
haendler = {
    "Heiltrank":    random.randint(8,  14),
    "Staerketrank": random.randint(12, 20),
    "Schutzzauber": random.randint(18, 28),
}

print("Angebot:")
for item_h, preis_h in haendler.items():
    print(f"  {item_h}: {preis_h} Galleonen")

kauf = input("Was kaufst du? (oder 'weiter'): > ")
if kauf in haendler:
    preis = haendler[kauf]
    if spieler_galleonen >= preis:
        spieler_galleonen -= preis
        if len(spieler_inventar) < 10:
            spieler_inventar.append(kauf)
            print(f"Gekauft! {kauf} fuer {preis} Galleonen.")
        else:
            print("Koffer voll! (max. 10 Gegenstaende)")
    else:
        print("Nicht genug Galleonen!")
else:
    print("Nichts gekauft.")

# ---- Reise durch Hogwarts ----
print(f"\nHogwarts-Karte:")
for oname, ox, oy in hogwarts_orte:
    print(f"  [{ox:02d},{oy:02d}] {oname}")

print(f"\n{spieler_name} durchsucht das Schloss...\n")

for oname, ox, oy in hogwarts_orte:
    if spieler_leben <= 0:
        break

    print(f"\n  Ort: {oname} ({ox},{oy})")

    # Zufaelliges Ereignis pro Ort
    ereignis = random.choice(["kampf", "geheimraum", "ruhe"])

    # 10% Chance auf Dementor (Mini-Challenge)
    if random.random() < 0.1:
        ereignis = "dementor"

    if ereignis in ("kampf", "dementor"):
        if ereignis == "dementor":
            g_daten = {"name": "Dementor", "leben": 35, "angriff": 10,
                       "galleonen": 8, "drop": "Patronus-Feder"}
            print(f"  Ein Dementor erscheint! Hauspunkte -5")
            hauspunkte -= 5
        else:
            g_daten = random.choice(gegner_pool)

        feind = Zauberer(g_daten["name"], g_daten["leben"], g_daten["angriff"])
        print(f"  {feind.name} greift an!")

        # Kampfschleife: laeuft bis einer besiegt ist.
        while not feind.ist_besiegt() and spieler_leben > 0:
            s = berechne_zauber(14)
            feind.leben -= s
            gegenschaden = feind.greift_an()
            spieler_leben -= gegenschaden
            spieler_leben = max(0, spieler_leben)
            print(f"  Du: -{gegenschaden} HP | {feind.name}: -{s} HP "
                  f"({feind.name}: {max(0,feind.leben)} HP, Du: {spieler_leben} HP)")

        if feind.ist_besiegt():
            print(f"  {feind.name} besiegt! +{g_daten['galleonen']} Galleonen | +10 Hauspunkte")
            spieler_galleonen += g_daten["galleonen"]
            hauspunkte += 10
            # Drop
            if random.random() < 0.4:
                drop = g_daten["drop"]
                if len(spieler_inventar) < 10:
                    spieler_inventar.append(drop)
                    print(f"  Fund: {drop}")
        else:
            print("  Keine HP mehr...")

    elif ereignis == "geheimraum":
        # Geheimer Raum (Mini-Challenge)
        fund = random.randrange(10, 51, 10)
        spieler_galleonen += fund
        hauspunkte += 5
        print(f"  Geheimer Raum entdeckt! +{fund} Galleonen | +5 Hauspunkte")

    else:
        heilung = random.randint(10, 20)
        spieler_leben = heile(spieler_leben, spieler_max_leben, heilung)

    zeige_status(spieler_name, spieler_leben, spieler_galleonen, spieler_inventar)
    print(f"  Hauspunkte: {hauspunkte}")

    if spieler_leben <= 0:
        print("\nGame Over – Hogwarts liegt in Dunkelheit...")
        exit()

# ---- ENDGEGNER: DER DUNKLE ZAUBERER ----
print("\n" + "=" * 50)
print("   DER DUNKLE ZAUBERER ERSCHEINT!")
print("=" * 50)

dunkel = Zauberer("Dunkler Zauberer", 120, 16)
print(f"\n{dunkel.name}: HP {dunkel.leben}\n")

while not dunkel.ist_besiegt() and spieler_leben > 0:
    zeige_status(spieler_name, spieler_leben, spieler_galleonen, spieler_inventar)
    print(f"Gegner-HP: {dunkel.leben}")
    print("\nAktion:")
    print("1 - Zaubern")
    print("2 - Heilen (Heiltrank noetig)")
    print("3 - Maechtigen Zauber (Zauberbuch)")
    print("4 - Fliehen")

    aktion = input("> ")

    if aktion == "1":
        s = berechne_zauber(14)
        dunkel.leben -= s
        print(f"Treffer! {s} Schaden auf {dunkel.name}!")

    elif aktion == "2":
        if "Heiltrank" in spieler_inventar:
            spieler_inventar.remove("Heiltrank")
            spieler_leben = heile(spieler_leben, spieler_max_leben, 35)
        else:
            print("Kein Heiltrank mehr!")
            continue  # Runde ohne Gegenzug wiederholen

    elif aktion == "3":
        print("Dein Zauberbuch:", list(zauberbuch.keys()))
        gew = input("Welcher Zauber? > ")
        if gew in zauberbuch:
            zs = zauberbuch[gew]
            dunkel.leben -= zs
            hauspunkte += 5
            print(f"{gew}! {zs} Schaden! +5 Hauspunkte")
        else:
            print("Diesen Zauber kennst du nicht!")
            continue

    elif aktion == "4":
        print("Du fliehst... Hogwarts ist verloren.")
        exit()

    else:
        print("Ungueltige Eingabe.")
        continue

    # Dunkel schlaegt zurueck
    if not dunkel.ist_besiegt():
        ds = dunkel.greift_an()
        spieler_leben -= ds
        spieler_leben = max(0, spieler_leben)
        print(f"Der dunkle Zauberer trifft dich fuer {ds} Schaden!")

# ---- Ergebnis ----
print("\n" + "=" * 50)
if dunkel.ist_besiegt():
    hauspunkte += 50
    print(f"{spieler_name} hat den dunklen Zauberer besiegt!")
    print("Das Artefakt ist vernichtet. Hogwarts ist gerettet!")
    print(f"\nEndstatistik:")
    print(f"  Restliche HP:   {spieler_leben}")
    print(f"  Galleonen:      {spieler_galleonen}")
    print(f"  Hauspunkte:     {hauspunkte}")
    print(f"  Inventar:       {spieler_inventar}")
else:
    print(f"{spieler_name} ist gefallen.")
    print("Der dunkle Zauberer uebernimmt Hogwarts...")
print("=" * 50)