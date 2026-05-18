import random

# ==================================================
# DIE VERLORENE KRONE VON PYTHONIA
# Ein komplettes Text-Adventure mit allen Python-Grundlagen
# ==================================================

print("=" * 50)
print("   DIE VERLORENE KRONE VON PYTHONIA")
print("=" * 50)


# ==================================================
# LEVEL 1 – DER HELD ERWACHT
# Konzepte: Variablen, print(), input()
# ==================================================
print("\n--- LEVEL 1: DER HELD ERWACHT ---")

# input() zeigt eine Frage an und wartet auf Eingabe.
# Der eingetippte Text wird als String zurückgegeben.
name = input("Wie heißt du, Abenteurer? > ")
alter = input("Wie alt bist du? > ")
klasse = input("Wähle deine Klasse (Magier / Krieger / Dieb): > ")

# f-Strings: geschweifte Klammern {} fügen Variablen direkt in den Text ein.
print(f"\nWillkommen in Pythonia!")
print(f"Hallo {name} der {klasse}!")
print(f"Du bist {alter} Jahre alt. Dein Abenteuer beginnt...")


# ==================================================
# LEVEL 2 – DIE SCHATZTRUHE
# Konzepte: if / elif / else, Zahlen vergleichen
# ==================================================
print("\n--- LEVEL 2: DIE SCHATZTRUHE ---")
print("Du findest eine Schatztruhe mit einem Zahlenschloss (1–10).")

# Die geheime Zahl – wir vergleichen die Eingabe damit.
geheime_zahl = 7
versuche = 0  # Zählt, wie viele Versuche der Spieler braucht.

while True:
    # int() wandelt den String aus input() in eine Zahl um.
    eingabe = int(input("Gib eine Zahl ein: > "))
    versuche += 1  # versuche = versuche + 1

    if eingabe == geheime_zahl:
        print(f"Richtig! Schatz gefunden nach {versuche} Versuch(en)!")
        break  # Schleife beenden, wenn die Zahl stimmt.
    elif eingabe < geheime_zahl:
        print("Die Zahl ist größer – versuch es nochmal!")
    else:
        print("Die Zahl ist kleiner – versuch es nochmal!")


# ==================================================
# LEVEL 3 – DER WÜRFEL DES SCHICKSALS
# Konzepte: random, Spielmechanik
# ==================================================
print("\n--- LEVEL 3: DER WÜRFEL DES SCHICKSALS ---")
print("Du triffst auf ein Monster! Würfel um dein Schicksal...")

# random.randint(1, 6) gibt eine zufällige ganze Zahl zwischen 1 und 6 zurück.
spieler_wuerfel = random.randint(1, 6)
monster_wuerfel = random.randint(1, 6)

print(f"Du würfelst: {spieler_wuerfel}")
print(f"Das Monster würfelt: {monster_wuerfel}")

if spieler_wuerfel > monster_wuerfel:
    print("Sieg! Du hast das Monster besiegt!")
elif spieler_wuerfel == monster_wuerfel:
    print("Unentschieden! Das Monster weicht zurück.")
else:
    print("Niederlage! Das Monster verletzt dich.")


# ==================================================
# LEVEL 4 – DAS HEILTRANK-LAGER
# Konzepte: Listen
# ==================================================
print("\n--- LEVEL 4: DAS HEILTRANK-LAGER ---")

# Eine Liste speichert mehrere Werte in einer Variablen.
# Zugriff über Index: inventar[0] ist das erste Element.
inventar = ["Schwert", "Apfel", "Heiltrank"]

# Alle Gegenstände ausgeben
print("Dein Inventar:")
for gegenstand in inventar:
    print(f"  - {gegenstand}")

# Neuen Gegenstand hinzufügen: .append() fügt ans Ende an.
inventar.append("Schild")
print(f"\nNach Fund von Schild: {inventar}")

# Gegenstand entfernen: .remove() löscht den ersten passenden Eintrag.
inventar.remove("Apfel")
print(f"Nach Essen des Apfels: {inventar}")

# Prüfen ob Item vorhanden: "in" gibt True oder False zurück.
if "Heiltrank" in inventar:
    print("Du hast einen Heiltrank dabei!")

# Bonus: Spieler kann selbst Items hinzufügen.
neues_item = input("Was findest du noch? (Item eingeben): > ")
inventar.append(neues_item)
print(f"Inventar jetzt: {inventar}")


# ==================================================
# LEVEL 5 – DIE ENDLOSSCHLEIFE DES DUNGEONS
# Konzepte: while-Schleife
# ==================================================
print("\n--- LEVEL 5: DER DUNGEON ---")
print("Du bist im Dungeon gefangen!")

# Eine while-Schleife läuft so lange, wie die Bedingung True ist.
# Hier nutzen wir while True (läuft ewig) und verlassen sie mit break.
while True:
    print("\nWas tust du?")
    print("1 - Nach links")
    print("2 - Nach rechts")
    print("3 - Ausgang suchen")

    aktion = input("> ")

    if aktion == "1":
        print("Du gehst nach links... und findest eine Wand.")
    elif aktion == "2":
        print("Du gehst nach rechts... Irrlichter folgen dir.")
    elif aktion == "3":
        print("Du findest den Ausgang! Du entkommst dem Dungeon!")
        break  # Schleife verlassen
    else:
        print("Ungültige Eingabe – versuch es nochmal.")


# ==================================================
# LEVEL 6 – DIE ARENA DER 5 MONSTER
# Konzepte: for-Schleifen
# ==================================================
print("\n--- LEVEL 6: DIE ARENA ---")
print("Du betrittst die Arena! 5 Monster warten auf dich.\n")

siege = 0
niederlagen = 0

# range(1, 6) erzeugt die Zahlen 1 bis 5.
# i nimmt bei jedem Durchlauf den nächsten Wert an.
for i in range(1, 6):
    monster_staerke = random.randint(1, 10)
    spieler_staerke = random.randint(1, 10)

    print(f"Monster {i}: Stärke {monster_staerke} | Du: Stärke {spieler_staerke}")

    if spieler_staerke > monster_staerke:
        print("  → Sieg!")
        siege += 1
    elif spieler_staerke == monster_staerke:
        print("  → Unentschieden!")
    else:
        print("  → Niederlage!")
        niederlagen += 1

print(f"\nArena-Ergebnis: {siege} Siege, {niederlagen} Niederlagen.")


# ==================================================
# LEVEL 7 – DIE BIBLIOTHEK DER ZAUBER
# Konzepte: Dictionaries
# ==================================================
print("\n--- LEVEL 7: DAS ZAUBERBUCH ---")

# Ein Dictionary speichert Schlüssel-Wert-Paare.
# zauber["Feuerball"] gibt 50 zurück.
zauber = {
    "Feuerball": 50,
    "Eislanze": 40,
    "Heilung": 30
}

# Alle Zauber anzeigen: .items() gibt Schlüssel und Wert als Paare zurück.
print("Verfügbare Zauber:")
for name_z, schaden_z in zauber.items():
    print(f"  {name_z}: {schaden_z} Schaden")

# Neuen Zauber hinzufügen
zauber["Donnerblitz"] = 60
print(f"\nDonnerblitz hinzugefügt: {zauber}")

# Zauber entfernen
del zauber["Heilung"]
print(f"Heilung vergessen: {zauber}")

# Spieler wählt einen Zauber
gewaehlter_zauber = input("\nWelchen Zauber wählst du? > ")
if gewaehlter_zauber in zauber:
    print(f"{gewaehlter_zauber} verursacht {zauber[gewaehlter_zauber]} Schaden!")
else:
    print("Dieser Zauber ist nicht bekannt.")


# ==================================================
# LEVEL 8 – DIE ALTEN RUNEN
# Konzepte: Tupel
# ==================================================
print("\n--- LEVEL 8: DIE RUNEN ---")

# Ein Tupel ist unveränderlich – perfekt für feste Koordinaten.
# Zugriff wie bei Listen: schatz[0] = X, schatz[1] = Y
schatz = (4, 7)
print(f"Der Schatz liegt bei X={schatz[0]}, Y={schatz[1]}")

# Mehrere Orte als Tupel-Liste
orte = [
    ("Dorf", 1, 1),
    ("Wald", 3, 5),
    ("Ruinen", 4, 7),
    ("Burg", 8, 2)
]

print("\nKarte von Pythonia:")
for ort_name, x, y in orte:
    print(f"  {ort_name}: ({x}, {y})")

# Spielerposition prüfen
try:
    spieler_x = int(input("\nDeine X-Position: > "))
    spieler_y = int(input("Deine Y-Position: > "))
except ValueError:
    spieler_x, spieler_y = 0, 0

if (spieler_x, spieler_y) == schatz:
    print("Du hast den Schatz gefunden!")
else:
    print(f"Kein Schatz hier. Der Schatz liegt bei {schatz}.")


# ==================================================
# LEVEL 9 & ENDGEGNER – DAS GROSSE KÖNIGREICHSSYSTEM
# Konzepte: ALLES kombiniert + Klassen + Funktionen
# ==================================================
print("\n" + "=" * 50)
print("   LEVEL 9: DER DRACHENKÖNIG")
print("=" * 50)

# ---- Funktionen ----
# Funktionen bündeln wiederverwendbaren Code.

def zeige_status(spieler_name, leben, gold, inv):
    """Zeigt den aktuellen Spielerstatus an."""
    print(f"\n[ {spieler_name} |{leben} |{gold} Gold |{inv} ]")

def berechne_schaden(basis, krit_chance=0.2):
    """Berechnet Schaden mit Chance auf kritischen Treffer."""
    schaden = random.randint(basis - 3, basis + 5)
    # random.random() gibt eine Zahl zwischen 0.0 und 1.0 zurück.
    if random.random() < krit_chance:
        schaden *= 2
        print("KRITISCHER TREFFER! Doppelter Schaden!")
    return schaden

def heile(leben, max_leben, menge):
    """Heilt den Spieler, aber nicht über max_leben."""
    neues_leben = min(leben + menge, max_leben)  # min() verhindert Überheilung
    geheilt = neues_leben - leben
    print(f"Du wirst um {geheilt} HP geheilt.")
    return neues_leben

# ---- Klasse ----
# Klassen sind Baupläne für Objekte mit eigenen Variablen und Methoden.

class Gegner:
    def __init__(self, name, leben, angriff):
        # __init__ wird beim Erstellen aufgerufen.
        # self.xyz speichert Werte im Objekt.
        self.name = name
        self.leben = leben
        self.angriff = angriff

    def greift_an(self):
        """Gibt zufälligen Schaden zurück."""
        return random.randint(self.angriff - 3, self.angriff + 3)

    def ist_besiegt(self):
        return self.leben <= 0

# ---- Spielaufbau ----
print("\nEin neues Spiel beginnt...")

spieler_name = input("Dein Heldenname: > ")
spieler_leben = 100
spieler_max_leben = 100
spieler_gold = 30
spieler_inventar = ["Heiltrank", "Heiltrank", "Schwert"]

# Städte als Tupel (Name, X, Y)
staedte = [
    ("Startdorf", 0, 0),
    ("Handelstadt", 5, 3),
    ("Drachenfestung", 9, 9)
]

# Zauber als Dictionary
zauberbuch = {
    "Feuerball": 25,
    "Eislanze": 20,
    "Blitz": 30
}

# Gegner-Liste
gegner_pool = [
    {"name": "Goblin",    "leben": 30, "angriff": 8,  "gold": 5,  "drop": "Trank"},
    {"name": "Ork",       "leben": 50, "angriff": 12, "gold": 10, "drop": "Schild"},
    {"name": "Skelett",   "leben": 40, "angriff": 10, "gold": 8,  "drop": "Knochen"},
]

# ---- Händler ----
print("\nDer Händler begrüßt dich!")
# Händlerpreise ändern sich zufällig (Mini-Challenge)
haendler = {
    "Heiltrank":    random.randint(8,  15),
    "Stärketrank":  random.randint(12, 20),
    "Eisenschwert": random.randint(25, 40),
}

print("Angebot des Händlers:")
for item_h, preis_h in haendler.items():
    print(f"  {item_h}: {preis_h} Gold")

kauf = input("Was kaufst du? (oder 'weiter'): > ")
if kauf in haendler:
    preis = haendler[kauf]
    if spieler_gold >= preis:
        spieler_gold -= preis
        spieler_inventar.append(kauf)
        print(f"Gekauft! {kauf} für {preis} Gold.")
    else:
        print("Nicht genug Gold!")
else:
    print("Du kaufst nichts.")

# ---- Reise durch Städte ----
print("\n🗺  Deine Reise durch Pythonia:")
for stadt, sx, sy in staedte:
    print(f"\nDu erreichst: {stadt} ({sx},{sy})")

    # Zufälliges Ereignis pro Stadt
    ereignis = random.choice(["kampf", "schatz", "ruhe"])

    if ereignis == "kampf" and spieler_leben > 0:
        # Zufälligen Gegner wählen
        g_daten = random.choice(gegner_pool)
        gegner = Gegner(g_daten["name"], g_daten["leben"], g_daten["angriff"])
        print(f"  ⚔  Ein {gegner.name} greift an!")

        # Kampfschleife: läuft bis einer besiegt ist
        while not gegner.ist_besiegt() and spieler_leben > 0:
            spieler_schaden = berechne_schaden(15)
            gegner.leben -= spieler_schaden
            gegner_schaden = gegner.greift_an()
            spieler_leben -= gegner_schaden
            spieler_leben = max(0, spieler_leben)
            print(f"  Du: -{gegner_schaden} HP | {gegner.name}: -{spieler_schaden} HP "
                    f"(noch {max(0, gegner.leben)} HP)")

        if gegner.ist_besiegt():
            print(f"{gegner.name} besiegt! +{g_daten['gold']} Gold")
            spieler_gold += g_daten["gold"]
            # 10% Chance auf geheime Schatztruhe (Mini-Challenge)
            if random.random() < 0.1:
                print("Geheime Schatztruhe entdeckt! +20 Gold!")
                spieler_gold += 20
            # Gegner droppt zufälliges Item (Mini-Challenge)
            if random.random() < 0.4:
                drop = g_daten["drop"]
                spieler_inventar.append(drop)
                print(f"Drop: {drop}")
        else:
            print("Du wurdest besiegt...")

    elif ereignis == "schatz":
        fund = random.randrange(10, 51, 10)
        spieler_gold += fund
        print(f"Du findest eine Schatztruhe: +{fund} Gold!")

    else:
        heilung = random.randint(10, 25)
        spieler_leben = heile(spieler_leben, spieler_max_leben, heilung)

    zeige_status(spieler_name, spieler_leben, spieler_gold, spieler_inventar)

    if spieler_leben <= 0:
        print("\n Game Over! Pythonia liegt in Dunkelheit...")
        exit()

# ---- ENDGEGNER: DER DRACHENKÖNIG ----
print("\n" + "=" * 50)
print("   ⚔  ENDGEGNER: DER DRACHENKÖNIG  ⚔")
print("=" * 50)

drache = Gegner("Drachenkönig", 120, 18)
print(f"\nDer Drachenkönig erscheint! HP: {drache.leben}\n")

# Kampfschleife bis Sieg oder Tod
while drache.leben > 0 and spieler_leben > 0:
    zeige_status(spieler_name, spieler_leben, spieler_gold, spieler_inventar)
    print(f"Drachen-HP: {drache.leben}")
    print("\nAktion wählen:")
    print("1 - Angreifen")
    print("2 - Heilen (Heiltrank nötig)")
    print("3 - Zauber wirken")
    print("4 - Fliehen")

    aktion = input("> ")

    if aktion == "1":
        # Normaler Angriff
        s = berechne_schaden(15)
        drache.leben -= s
        print(f"Du triffst für {s} Schaden!")

    elif aktion == "2":
        # Heilen mit Heiltrank
        if "Heiltrank" in spieler_inventar:
            spieler_inventar.remove("Heiltrank")
            spieler_leben = heile(spieler_leben, spieler_max_leben, 35)
        else:
            print("Kein Heiltrank mehr!")
            continue  # Runde wiederholen ohne Drachen-Angriff

    elif aktion == "3":
        # Zauber auswählen
        print("Deine Zauber:", list(zauberbuch.keys()))
        gewaehlter = input("Welchen Zauber? > ")
        if gewaehlter in zauberbuch:
            z_schaden = zauberbuch[gewaehlter]
            drache.leben -= z_schaden
            print(f"{gewaehlter}! {z_schaden} magischer Schaden!")
        else:
            print("Unbekannter Zauber!")
            continue

    elif aktion == "4":
        # Fliehen
        print("Du fliehst... Pythonia ist verloren. ")
        exit()

    else:
        print("Ungültige Eingabe!")
        continue

    # Drache schlägt zurück (außer er ist besiegt)
    if drache.leben > 0:
        drachen_schaden = drache.greift_an()
        spieler_leben -= drachen_schaden
        spieler_leben = max(0, spieler_leben)
        print(f"Der Drache trifft dich für {drachen_schaden} Schaden!")

# ---- ERGEBNIS ----
print("\n" + "=" * 50)
if drache.ist_besiegt():
    print(f" {spieler_name} hat den Drachenkönig besiegt!")
    print(f"Die Krone von Pythonia ist gerettet!")
    print(f"\nEndstatistik:")
    print(f"  Restliche HP:  {spieler_leben}")
    print(f"  Gold gesammelt: {spieler_gold}")
    print(f"  Inventar: {spieler_inventar}")
else:
    print(f" {spieler_name} ist gefallen. Pythonia weint...")
print("=" * 50)