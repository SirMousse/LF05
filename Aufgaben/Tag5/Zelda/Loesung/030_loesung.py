import random

# ==================================================
# DIE LEGENDE VON HYRULE
# Ein komplettes Zelda-Text-Adventure
# ==================================================

print("=" * 50)
print("   DIE LEGENDE VON HYRULE")
print("   Hyrule braucht einen Helden!")
print("=" * 50)


# ==================================================
# LEVEL 1 – DER HELD VON HYRULE
# Konzepte: Variablen, print(), input()
# ==================================================
print("\n--- LEVEL 1: DER HELD ---")

# input() zeigt Text an und wartet auf Eingabe.
# Das Ergebnis ist immer ein String.
name   = input("Wie heisst du?\n> ")
alter  = input("Wie alt bist du?\n> ")
klasse = input("Deine Klasse (Schwertkampfer / Bogenschutze / Magier):\n> ")

# f-Strings: {} wird durch den Variablenwert ersetzt.
print(f"\nWillkommen in Hyrule!")
print(f"Sei gegruesst {name} der {klasse}.")
print(f"Du bist {alter} Jahre alt. Dein Abenteuer beginnt.")


# ==================================================
# LEVEL 2 – DAS TOR DES TEMPELS
# Konzepte: if / elif / else, Fehlversuche
# ==================================================
print("\n--- LEVEL 2: TOR DES TEMPELS ---")
print("Ein steinernes Tor versperrt den Weg.")

richtiges_passwort = "triforce"
fehlversuche = 0

while True:
    eingabe = input("Passwort des Tempels:\n> ")

    # .lower() wandelt Eingabe in Kleinbuchstaben um –
    # damit "Triforce" und "TRIFORCE" auch erkannt werden.
    if eingabe.lower() == richtiges_passwort:
        print("Das Tor oeffnet sich! Die Triforce leuchtet kurz auf.")
        break
    else:
        fehlversuche += 1
        print(f"Zugang verweigert! Fehlversuche: {fehlversuche}")
        if fehlversuche >= 3:
            print("Ein Wachgeist erscheint... aber er laesst dich weiter versuchen.")


# ==================================================
# LEVEL 3 – KAMPF GEGEN DIE BOKBLINS
# Konzepte: random
# ==================================================
print("\n--- LEVEL 3: BOKBLIN-ANGRIFF ---")
print("Ein Bokblin springt aus dem Gebuesch!")

# random.randint(1, 6) gibt eine zufaellige Zahl von 1 bis 6.
held_wert   = random.randint(1, 6)
bokblin_wert = random.randint(1, 6)

print(f"Dein Angriff: {held_wert}")
print(f"Bokblin-Angriff: {bokblin_wert}")

if held_wert > bokblin_wert:
    print("Sieg! Der Bokblin flieht.")
elif held_wert == bokblin_wert:
    print("Unentschieden! Beide weichen zurueck.")
else:
    print("Niederlage! Du musst dich zurueckziehen.")


# ==================================================
# LEVEL 4 – DIE ABENTEURERTASCHE
# Konzepte: Listen
# ==================================================
print("\n--- LEVEL 4: ABENTEURERTASCHE ---")

# Eine Liste speichert mehrere Werte. Index startet bei 0.
inventar = ["Holzschild", "Bogen", "Apfel"]

# Alle Gegenstaende anzeigen
print("Dein Inventar:")
for item in inventar:
    print(f"  - {item}")

# Neues Item hinzufuegen: .append() haengt ans Ende.
inventar.append("Heiltrank")
print(f"\nNach Fund eines Heiltranks: {inventar}")

# Item entfernen: .remove() loescht den ersten passenden Eintrag.
inventar.remove("Apfel")
print(f"Apfel aufgegessen: {inventar}")

# Pruefen ob Item vorhanden: "in" gibt True oder False.
if "Bogen" in inventar:
    print("Bogen dabei – Fernkampf moeglich!")

# Bonus: Spieler kann eigene Items hinzufuegen.
neues_item = input("Was findest du in einer Truhe?\n> ")
if len(inventar) < 10:   # Inventar-Limit: max. 10 Plaetze
    inventar.append(neues_item)
    print(f"Inventar: {inventar}")
else:
    print("Tasche voll! (max. 10 Gegenstaende)")


# ==================================================
# LEVEL 5 – DER VERLORENE WALD
# Konzepte: while-Schleife
# ==================================================
print("\n--- LEVEL 5: DER VERLORENE WALD ---")
print("Du hast dich im Verlorenen Wald verirrt!")

# while True laeuft endlos – verlassen nur mit break.
while True:
    print("\nWas tust du?")
    print("1 - Nach Norden gehen")
    print("2 - Nach Osten gehen")
    print("3 - Ausgang finden")

    wahl = input("> ")

    if wahl == "1":
        print("Seltsame Musik erklingt aus den Baeumen...")
    elif wahl == "2":
        print("Ein Salia-Geist winkt dir zu.")
    elif wahl == "3":
        print("Das Licht des Auenlands leitet dich hinaus!")
        break  # Schleife verlassen
    else:
        print("Der Wald reagiert nicht.")


# ==================================================
# LEVEL 6 – DIE DUNGEON-KAEMPFE
# Konzepte: for-Schleifen
# ==================================================
print("\n--- LEVEL 6: DUNGEON-KAEMPFE ---")
print("5 Monster erwachen!\n")

siege       = 0
niederlagen = 0
unentschieden = 0

# range(1, 6) erzeugt die Zahlen 1 bis 5.
for i in range(1, 6):
    held_staerke    = random.randint(1, 10)
    monster_staerke = random.randint(1, 10)

    print(f"Monster {i}: Du {held_staerke} vs. Monster {monster_staerke}")

    if held_staerke > monster_staerke:
        print("  Sieg!")
        siege += 1
    elif held_staerke == monster_staerke:
        print("  Unentschieden!")
        unentschieden += 1
    else:
        print("  Niederlage!")
        niederlagen += 1

print(f"\nErgebnis: {siege} Siege, {niederlagen} Niederlagen, {unentschieden} Unentschieden.")


# ==================================================
# LEVEL 7 – DIE SCHATZKAMMER
# Konzepte: Dictionaries
# ==================================================
print("\n--- LEVEL 7: SCHATZKAMMER ---")

# Dictionary: Schluessel-Wert-Paare in geschweiften Klammern {}.
waffen = {
    "Master-Schwert":   100,
    "Bogen der Helden":  70,
    "Feuerstab":         60
}

# Alle Waffen anzeigen: .items() liefert Schluessel+Wert als Paare.
print("Waffen der Schatzkammer:")
for wname, wstaerke in waffen.items():
    print(f"  {wname}: {wstaerke} Staerke")

# Staerke abrufen
print(f"\nMaster-Schwert-Staerke: {waffen['Master-Schwert']}")

# Neue Waffe hinzufuegen
waffen["Blitzpfeil"] = 80
print(f"Blitzpfeil gefunden: {waffen}")

# Waffe entfernen
del waffen["Feuerstab"]
print(f"Feuerstab zersplittert: {waffen}")

# Spieler waehlt Waffe
print("\nVerfuegbare Waffen:", list(waffen.keys()))
gewaehlte = input("Welche Waffe nimmst du?\n> ")
if gewaehlte in waffen:
    print(f"{gewaehlte} ausgewaehlt! Staerke: {waffen[gewaehlte]}")
else:
    print("Diese Waffe ist nicht in der Kammer.")


# ==================================================
# LEVEL 8 – DIE KARTE VON HYRULE
# Konzepte: Tupel
# ==================================================
print("\n--- LEVEL 8: KARTE VON HYRULE ---")

# Ein Tupel ist unveraenderlich – perfekt fuer feste Koordinaten.
tempel = (20, 15)
print(f"Tempel liegt bei X={tempel[0]}, Y={tempel[1]}")

# Mehrere Orte als Tupel-Liste (Bonus)
orte = [
    ("Schloss Hyrule",    5,  5),
    ("Kakariko",          8, 10),
    ("Verlorener Wald",  12,  7),
    ("Wuesten-Tempel",   18, 20),
    ("Todesberg",        20, 15),
]

print("\nKarte von Hyrule:")
for oname, ox, oy in orte:
    print(f"  {oname}: ({ox}, {oy})")

# Spielerposition pruefen
try:
    sx = int(input("\nDeine X-Position:\n> "))
    sy = int(input("Deine Y-Position:\n> "))
except ValueError:
    sx, sy = 0, 0

if (sx, sy) == tempel:
    print("Du hast den Tempel erreicht! Die Triforce reagiert.")
else:
    print(f"Noch nicht da. Der Tempel liegt bei {tempel}.")


# ==================================================
# LEVEL 9 & ENDGEGNER – DIE RETTUNG VON HYRULE
# Konzepte: ALLES kombiniert + Klassen + Funktionen
# ==================================================
print("\n" + "=" * 50)
print("   LEVEL 9: DIE RETTUNG VON HYRULE")
print("   Besiege Ganon und rette Zelda!")
print("=" * 50)


# ---- Funktionen ----
def zeige_status(sname, herzen, rubine, inv):
    """Zeigt den aktuellen Helden-Status an."""
    print(f"\n[ {sname} | Herzen {herzen} | {rubine} Rubine | {inv} ]")

def berechne_angriff(basis, krit_chance=0.2):
    """Berechnet Angriff mit Chance auf kritischen Treffer."""
    schaden = random.randint(basis - 3, basis + 5)
    # random.random() liefert 0.0 bis 1.0 – unter krit_chance = Krit!
    if random.random() < krit_chance:
        schaden *= 2
        print("Kritischer Treffer! Master-Schwert leuchtet!")
    return schaden

def heile_herzen(herzen, max_herzen, menge):
    """Heilt Herzen, aber nicht ueber max_herzen."""
    # min() verhindert Ueberheilung.
    neue_herzen = min(herzen + menge, max_herzen)
    print(f"Geheilt: +{neue_herzen - herzen} Herzen.")
    return neue_herzen


# ---- Klasse ----
class Endgegner:
    def __init__(self, name, leben, angriff):
        # __init__ wird beim Erstellen automatisch aufgerufen.
        self.name    = name
        self.leben   = leben
        self.angriff = angriff

    def greift_an(self):
        """Gibt zufaelligen Schaden zurueck."""
        return random.randint(self.angriff - 4, self.angriff + 4)

    def ist_besiegt(self):
        """True wenn keine Lebenspunkte mehr."""
        return self.leben <= 0


# ---- Spielaufbau ----
print("\nNeues Abenteuer beginnt...")
held_name   = input("Dein Heldenname:\n> ")
held_herzen   = 100
held_max      = 100
held_rubine   = 50
held_inventar = ["Heiltrank", "Heiltrank", "Schild"]

# Schrein-Zaehler (Mini-Challenge)
schreine_gefunden = 0

# Reiseroute als Tupel (Name, X, Y)
reiseroute = [
    ("Kakariko",    8, 10),
    ("Todesberg",  20, 15),
    ("Schloss",    25, 20),
]

# Waffenkammer als Dictionary
waffenkammer = {
    "Master-Schwert":   25,
    "Blitzpfeil":       20,
    "Bomben":           15,
}

# Monster-Pool
monster_pool = [
    {"name": "Bokblin",  "leben": 35, "angriff": 10, "rubine": 10, "drop": "Bokblin-Horn"},
    {"name": "Moblin",   "leben": 50, "angriff": 14, "rubine": 15, "drop": "Moblin-Speer"},
    {"name": "Lizalfos", "leben": 40, "angriff": 11, "rubine": 12, "drop": "Eidechsenschwanz"},
]

# ---- Haendler ----
print("\nEin reisender Haendler bietet seine Waren an!")
# Preise aendern sich zufaellig (Mini-Challenge)
haendler = {
    "Heiltrank":     random.randint(8,  15),
    "Herzcontainer": random.randint(20, 35),
    "Stahlschild":   random.randint(15, 25),
}

print("Angebot:")
for item_h, preis_h in haendler.items():
    print(f"  {item_h}: {preis_h} Rubine")

kauf = input("Was kaufst du? (oder 'weiter')\n> ")
if kauf in haendler:
    preis = haendler[kauf]
    if held_rubine >= preis:
        held_rubine -= preis
        if len(held_inventar) < 10:
            held_inventar.append(kauf)
            print(f"Gekauft! {kauf} fuer {preis} Rubine.")
        else:
            print("Tasche voll!")
    else:
        print("Nicht genug Rubine!")
else:
    print("Nichts gekauft.")

# ---- Reise durch Hyrule ----
print(f"\nDeine Route:")
for oname, ox, oy in reiseroute:
    print(f"  [{ox:02d},{oy:02d}] {oname}")

print(f"\n{held_name} bricht auf...\n")

for oname, ox, oy in reiseroute:
    if held_herzen <= 0:
        break

    print(f"\n  Ort: {oname} ({ox},{oy})")

    # Zufaelliges Ereignis pro Ort
    ereignis = random.choice(["kampf", "schrein", "rast"])

    # 10% Chance auf seltenen Gegner (Mini-Challenge)
    if random.random() < 0.1:
        ereignis = "seltener_gegner"

    if ereignis in ("kampf", "seltener_gegner"):
        if ereignis == "seltener_gegner":
            m_daten = {"name": "Silber-Bokblin", "leben": 60, "angriff": 16,
                       "rubine": 30, "drop": "Silbernes Horn"}
            print(f"  Ein seltener Silber-Bokblin erscheint!")
        else:
            m_daten = random.choice(monster_pool)

        monster = Endgegner(m_daten["name"], m_daten["leben"], m_daten["angriff"])
        print(f"  {monster.name} greift an!")

        # Kampfschleife: laeuft bis einer besiegt ist.
        while not monster.ist_besiegt() and held_herzen > 0:
            s = berechne_angriff(14)
            monster.leben -= s
            schaden_m = monster.greift_an()
            held_herzen -= schaden_m
            held_herzen = max(0, held_herzen)
            print(f"  Du: -{schaden_m} | {monster.name}: -{s} "
                  f"({monster.name}: {max(0,monster.leben)}, Du: {held_herzen})")

        if monster.ist_besiegt():
            print(f"  {monster.name} besiegt! +{m_daten['rubine']} Rubine")
            held_rubine += m_daten["rubine"]
            # Drop
            if random.random() < 0.4:
                drop = m_daten["drop"]
                if len(held_inventar) < 10:
                    held_inventar.append(drop)
                    print(f"  Gefunden: {drop}")
        else:
            print("  Herzen leer – ins naechste Dorf!")

    elif ereignis == "schrein":
        # Geheimschrein (Mini-Challenge)
        schreine_gefunden += 1
        bonus = random.randrange(10, 31, 10)
        held_rubine += bonus
        print(f"  Geheimschrein entdeckt! +{bonus} Rubine (Schreine: {schreine_gefunden})")

    else:
        heilung = random.randint(10, 25)
        held_herzen = heile_herzen(held_herzen, held_max, heilung)

    zeige_status(held_name, held_herzen, held_rubine, held_inventar)

    if held_herzen <= 0:
        print("\nGame Over – Hyrule liegt in Schatten...")
        exit()

# ---- ENDGEGNER: GANON ----
print("\n" + "=" * 50)
print("   GANON ERSCHEINT!")
print("   Die dunkle Macht von Hyrule!")
print("=" * 50)

ganon = Endgegner("Ganon", 120, 17)
print(f"\nGanon: HP {ganon.leben}\n")

while not ganon.ist_besiegt() and held_herzen > 0:
    zeige_status(held_name, held_herzen, held_rubine, held_inventar)
    print(f"Ganons HP: {ganon.leben}")
    print("\nAktion:")
    print("1 - Angreifen")
    print("2 - Heilen (Heiltrank noetig)")
    print("3 - Waffe einsetzen (Waffenkammer)")
    print("4 - Fliehen")

    aktion = input("> ")

    if aktion == "1":
        s = berechne_angriff(14)
        ganon.leben -= s
        print(f"Treffer! {s} Schaden auf Ganon!")

    elif aktion == "2":
        if "Heiltrank" in held_inventar:
            held_inventar.remove("Heiltrank")
            held_herzen = heile_herzen(held_herzen, held_max, 35)
        else:
            print("Kein Heiltrank mehr!")
            continue  # Runde ohne Gegenzug wiederholen

    elif aktion == "3":
        print("Waffenkammer:", list(waffenkammer.keys()))
        gew = input("Welche Waffe?\n> ")
        if gew in waffenkammer:
            ws = waffenkammer[gew]
            ganon.leben -= ws
            print(f"{gew} eingesetzt! {ws} Schaden!")
        else:
            print("Diese Waffe ist nicht verfuegbar!")
            continue

    elif aktion == "4":
        print("Du fliehst... Ganons Dunkelheit breitet sich aus.")
        exit()

    else:
        print("Ungueltige Eingabe.")
        continue

    # Ganon schlaegt zurueck
    if not ganon.ist_besiegt():
        gs = ganon.greift_an()
        held_herzen -= gs
        held_herzen = max(0, held_herzen)
        print(f"Ganon greift an! -{gs} Herzen!")

# ---- Ergebnis ----
print("\n" + "=" * 50)
if ganon.ist_besiegt():
    print(f"{held_name} hat Ganon besiegt!")
    print("Die Triforce leuchtet auf. Hyrule ist gerettet!")
    print(f"\nEndstatistik:")
    print(f"  Herzen:          {held_herzen}")
    print(f"  Rubine:          {held_rubine}")
    print(f"  Schreine:        {schreine_gefunden}")
    print(f"  Inventar:        {held_inventar}")
else:
    print(f"{held_name} ist gefallen.")
    print("Ganons Dunkelheit verschlingt Hyrule...")
print("=" * 50)