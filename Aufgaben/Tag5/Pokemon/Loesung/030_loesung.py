import random

# ==================================================
# DIE REISE ZUM POKEMON-MEISTER
# Ein komplettes Pokemon-Text-Adventure
# ==================================================

print("=" * 50)
print("   DIE REISE ZUM POKEMON-MEISTER")
print("   Professor Eich wartet auf dich...")
print("=" * 50)


# ==================================================
# LEVEL 1 – DEIN ERSTES POKEMON
# Konzepte: Variablen, print(), input()
# ==================================================
print("\n--- LEVEL 1: DEIN ERSTES POKEMON ---")

# input() zeigt Text an und wartet auf Eingabe.
# Das Ergebnis ist immer ein String.
name    = input("Wie heisst du?\n> ")
alter   = input("Wie alt bist du?\n> ")
starter = input("Waehle dein Starter-Pokemon (Bisasam / Glumanda / Schiggy):\n> ")

# f-Strings: {} wird durch den Variablenwert ersetzt.
print(f"\nWillkommen in der Pokemon-Welt!")
print(f"Hallo {name}!")
print(f"Du hast {starter} gewaehlt.")
print(f"Du bist {alter} Jahre alt. Deine Reise beginnt.")


# ==================================================
# LEVEL 2 – DAS POKEMON-CENTER
# Konzepte: if / elif / else, Eingabe pruefen
# ==================================================
print("\n--- LEVEL 2: POKEMON-CENTER ---")
print("Krankenschwester Joice steht bereit.")

# while True laeuft endlos – wir verlassen mit break.
while True:
    heilung = input("Moechtest du dein Pokemon heilen? (ja / nein)\n> ")

    # .lower() wandelt die Eingabe in Kleinbuchstaben um –
    # damit "Ja" und "JA" auch erkannt werden.
    if heilung.lower() == "ja":
        print("Dein Pokemon wurde vollstaendig geheilt!")
        break
    elif heilung.lower() == "nein":
        print("Okay! Deine Reise geht weiter.")
        break
    else:
        print("Ungueltige Eingabe – bitte 'ja' oder 'nein' eingeben.")


# ==================================================
# LEVEL 3 – DER WILDE KAMPF
# Konzepte: random
# ==================================================
print("\n--- LEVEL 3: WILDER POKEMON-KAMPF ---")
print("Ein wildes Pokemon erscheint!")

# random.randint(1, 6) gibt eine zufaellige Zahl von 1 bis 6.
spieler_angriff = random.randint(1, 6)
pokemon_angriff = random.randint(1, 6)

print(f"Dein Angriff: {spieler_angriff}")
print(f"Gegner-Angriff: {pokemon_angriff}")

if spieler_angriff > pokemon_angriff:
    print("Sieg! Das wilde Pokemon flieht.")
elif spieler_angriff == pokemon_angriff:
    print("Unentschieden! Beide weichen zurueck.")
else:
    print("Niederlage! Dein Pokemon ist erschoepft.")


# ==================================================
# LEVEL 4 – DER TRAINER-RUCKSACK
# Konzepte: Listen
# ==================================================
print("\n--- LEVEL 4: TRAINER-RUCKSACK ---")

# Eine Liste speichert mehrere Werte. Index startet bei 0.
rucksack = ["Pokeball", "Trank", "Supertrank"]

# Alle Items anzeigen
print("Dein Rucksack:")
for item in rucksack:
    print(f"  - {item}")

# Neues Item hinzufuegen: .append() haengt ans Ende.
rucksack.append("Beere")
print(f"\nNach Fund einer Beere: {rucksack}")

# Item entfernen: .remove() loescht den ersten passenden Eintrag.
rucksack.remove("Trank")
print(f"Trank benutzt: {rucksack}")

# Pruefen ob Item vorhanden: "in" gibt True oder False.
if "Pokeball" in rucksack:
    print("Pokeball bereit – du kannst Pokemon fangen!")

# Bonus: Spieler kann eigene Items hinzufuegen.
neues_item = input("Was findest du im Gras?\n> ")
if len(rucksack) < 10:   # Inventar-Limit: max. 10 Plaetze
    rucksack.append(neues_item)
    print(f"Rucksack: {rucksack}")
else:
    print("Rucksack voll! (max. 10 Plaetze)")


# ==================================================
# LEVEL 5 – DER VERIRRTE WALD
# Konzepte: while-Schleife
# ==================================================
print("\n--- LEVEL 5: VERTANIA-WALD ---")
print("Du hast dich im Wald verlaufen!")

# while True laeuft endlos – wir verlassen mit break.
while True:
    print("\nWas tust du?")
    print("1 - Nach links gehen")
    print("2 - Nach rechts gehen")
    print("3 - Ausgang gefunden")

    wahl = input("> ")

    if wahl == "1":
        print("Ein Zubat flattert auf dich zu!")
    elif wahl == "2":
        print("Du hoerst Wasser rauschen...")
    elif wahl == "3":
        print("Endlich! Du hast den Ausgang gefunden.")
        break  # Schleife verlassen
    else:
        print("Der Wald schweigt.")


# ==================================================
# LEVEL 6 – DIE TRAINER-KAEMPFE
# Konzepte: for-Schleifen
# ==================================================
print("\n--- LEVEL 6: TRAINER-KAEMPFE ---")
print("5 Trainer wollen kaempfen!\n")

siege        = 0
niederlagen  = 0
unentschieden = 0

# range(1, 6) erzeugt die Zahlen 1 bis 5.
for i in range(1, 6):
    spieler_staerke  = random.randint(1, 10)
    trainer_staerke  = random.randint(1, 10)

    print(f"Trainer {i}: Du {spieler_staerke} vs. Gegner {trainer_staerke}")

    if spieler_staerke > trainer_staerke:
        print("  Sieg!")
        siege += 1
    elif spieler_staerke == trainer_staerke:
        print("  Unentschieden!")
        unentschieden += 1
    else:
        print("  Niederlage!")
        niederlagen += 1

print(f"\nErgebnis: {siege} Siege, {niederlagen} Niederlagen, {unentschieden} Unentschieden.")


# ==================================================
# LEVEL 7 – DER POKEDEX
# Konzepte: Dictionaries
# ==================================================
print("\n--- LEVEL 7: POKEDEX ---")

# Dictionary: Schluessel-Wert-Paare in geschweiften Klammern {}.
pokemon_db = {
    "Pikachu": 55,
    "Glurak":  100,
    "Relaxo":  85
}

# Alle Pokemon anzeigen: .items() liefert Schluessel+Wert als Paare.
print("Dein Pokedex:")
for pname, pstaerke in pokemon_db.items():
    print(f"  {pname}: {pstaerke} KP")

# Staerke abrufen
print(f"\nGlurak-Staerke: {pokemon_db['Glurak']}")

# Neues Pokemon hinzufuegen
pokemon_db["Evoli"] = 45
print(f"Evoli hinzugefuegt: {pokemon_db}")

# Pokemon entfernen
del pokemon_db["Relaxo"]
print(f"Relaxo weggeschlafen: {pokemon_db}")

# Spieler waehlt Pokemon
print("\nVerfuegbare Pokemon:", list(pokemon_db.keys()))
gewaehltes = input("Wen schickst du in den Kampf?\n> ")
if gewaehltes in pokemon_db:
    print(f"{gewaehltes} kaempft! KP: {pokemon_db[gewaehltes]}")
else:
    print("Dieses Pokemon ist nicht in deinem Pokedex.")


# ==================================================
# LEVEL 8 – DIE KARTE DER REGION
# Konzepte: Tupel
# ==================================================
print("\n--- LEVEL 8: REGIONS-KARTE ---")

# Ein Tupel ist unveraenderlich – perfekt fuer feste Koordinaten.
arena = (15, 9)
print(f"Arena liegt bei X={arena[0]}, Y={arena[1]}")

# Mehrere Orte als Tupel-Liste (Bonus)
orte = [
    ("Alabastia",      1,  1),
    ("Vertania City",  4,  5),
    ("Azuria City",    8,  9),
    ("Lavandia",      12,  7),
    ("Pokemon Liga",  15,  9),
]

print("\nRegions-Karte:")
for oname, x, y in orte:
    print(f"  {oname}: ({x}, {y})")

# Spielerposition pruefen
try:
    sx = int(input("\nDeine X-Position:\n> "))
    sy = int(input("Deine Y-Position:\n> "))
except ValueError:
    sx, sy = 0, 0

if (sx, sy) == arena:
    print("Du hast die Arena erreicht! Der Kampf beginnt.")
else:
    print(f"Noch nicht da. Die Arena liegt bei {arena}.")


# ==================================================
# LEVEL 9 & ENDGEGNER – DIE POKEMON-LIGA
# Konzepte: ALLES kombiniert + Klassen + Funktionen
# ==================================================
print("\n" + "=" * 50)
print("   LEVEL 9: DIE POKEMON-LIGA")
print("   Werde zum Pokemon-Meister!")
print("=" * 50)


# ---- Funktionen ----
def zeige_status(sname, kp, geld, inv):
    """Zeigt den aktuellen Trainer-Status an."""
    print(f"\n[ {sname} | KP {kp} | {geld} Poke-Dollar | {inv} ]")

def berechne_angriff(basis, krit_chance=0.2):
    """Berechnet Angriff mit Chance auf kritischen Treffer."""
    schaden = random.randint(basis - 3, basis + 5)
    # random.random() liefert 0.0 bis 1.0 – unter krit_chance = Krit!
    if random.random() < krit_chance:
        schaden *= 2
        print("Kritischer Treffer!")
    return schaden

def heile_pokemon(kp, max_kp, menge):
    """Heilt das Pokemon, aber nicht ueber max_kp."""
    # min() verhindert Ueberheilung.
    neue_kp = min(kp + menge, max_kp)
    print(f"Pokemon geheilt: +{neue_kp - kp} KP.")
    return neue_kp


# ---- Klasse ----
class Gegner_Trainer:
    def __init__(self, name, kp, angriff):
        # __init__ wird beim Erstellen automatisch aufgerufen.
        self.name    = name
        self.kp      = kp
        self.angriff = angriff

    def greift_an(self):
        """Gibt zufaelligen Schaden zurueck."""
        return random.randint(self.angriff - 4, self.angriff + 4)

    def ist_besiegt(self):
        """True wenn keine KP mehr."""
        return self.kp <= 0


# ---- Spielaufbau ----
print("\nNeue Trainer-Session startet...")
trainer_name   = input("Dein Trainer-Name:\n> ")
trainer_kp      = 100
trainer_max_kp  = 100
trainer_geld    = 500
trainer_inventar = ["Trank", "Trank", "Pokeball"]

# Shiny-Chance (Mini-Challenge)
shiny_gefangen = 0

# Orte als Tupel (Name, X, Y)
liga_route = [
    ("Alabastia",    1, 1),
    ("Azuria-Arena", 8, 9),
    ("Pokemon-Liga", 15, 9),
]

# Pokedex als Dictionary
pokedex = {
    "Pikachu":  20,
    "Glurak":   35,
    "Turtok":   30,
}

# Gegner-Pool
gegner_pool = [
    {"name": "Team-Rocket-Heiko", "kp": 35, "angriff": 10, "geld": 100, "drop": "Supertrank"},
    {"name": "Arenaleiterin Misty", "kp": 50, "angriff": 14, "geld": 200, "drop": "Hyperball"},
    {"name": "Rival Gary",         "kp": 45, "angriff": 12, "geld": 150, "drop": "Beere"},
]

# ---- PokeMarkt ----
print("\nPokeMarkt: Willkommen!")
# Preise aendern sich zufaellig (Mini-Challenge)
pokemart = {
    "Trank":     random.randint(100, 200),
    "Supertrank": random.randint(200, 350),
    "Pokeball":  random.randint(150, 250),
}

print("Angebot:")
for item_p, preis_p in pokemart.items():
    print(f"  {item_p}: {preis_p} Poke-Dollar")

kauf = input("Was kaufst du? (oder 'weiter')\n> ")
if kauf in pokemart:
    preis = pokemart[kauf]
    if trainer_geld >= preis:
        trainer_geld -= preis
        if len(trainer_inventar) < 10:
            trainer_inventar.append(kauf)
            print(f"Gekauft! {kauf} fuer {preis} Poke-Dollar.")
        else:
            print("Rucksack voll!")
    else:
        print("Nicht genug Geld!")
else:
    print("Nichts gekauft.")

# ---- Reise durch die Region ----
print(f"\nDeine Route:")
for oname, ox, oy in liga_route:
    print(f"  [{ox:02d},{oy:02d}] {oname}")

print(f"\n{trainer_name} bricht auf...\n")

for oname, ox, oy in liga_route:
    if trainer_kp <= 0:
        break

    print(f"\n  Ort: {oname} ({ox},{oy})")

    # Zufaelliges Ereignis pro Ort
    ereignis = random.choice(["kampf", "wildes_pokemon", "rast"])

    # 5% Shiny-Chance (Mini-Challenge)
    if random.random() < 0.05:
        ereignis = "shiny"

    if ereignis in ("kampf", "shiny"):
        if ereignis == "shiny":
            print(f"  Ein schillerndes Pikachu erscheint!")
            shiny_gefangen += 1
            trainer_geld += 300
            print(f"  Shiny gefangen! +300 Poke-Dollar")
        else:
            g_daten = random.choice(gegner_pool)
            gegner  = Gegner_Trainer(g_daten["name"], g_daten["kp"], g_daten["angriff"])
            print(f"  {gegner.name} fordert dich heraus!")

            # Kampfschleife: laeuft bis einer besiegt ist.
            while not gegner.ist_besiegt() and trainer_kp > 0:
                s = berechne_angriff(14)
                gegner.kp -= s
                gegenschaden = gegner.greift_an()
                trainer_kp -= gegenschaden
                trainer_kp = max(0, trainer_kp)
                print(f"  Du: -{gegenschaden} KP | {gegner.name}: -{s} KP "
                      f"({gegner.name}: {max(0,gegner.kp)} KP, Du: {trainer_kp} KP)")

            if gegner.ist_besiegt():
                print(f"  {gegner.name} besiegt! +{g_daten['geld']} Poke-Dollar")
                trainer_geld += g_daten["geld"]
                # Drop
                if random.random() < 0.4:
                    drop = g_daten["drop"]
                    if len(trainer_inventar) < 10:
                        trainer_inventar.append(drop)
                        print(f"  Erhalten: {drop}")
            else:
                print("  Dein Pokemon ist ohnmaechtig...")

    elif ereignis == "wildes_pokemon":
        p_liste = list(pokedex.keys())
        neues_p = random.choice(p_liste)
        print(f"  Ein wildes {neues_p} erscheint und schliesst sich dir an!")

    else:
        heilung = random.randint(10, 25)
        trainer_kp = heile_pokemon(trainer_kp, trainer_max_kp, heilung)

    zeige_status(trainer_name, trainer_kp, trainer_geld, trainer_inventar)

    if trainer_kp <= 0:
        print("\nDeine Pokemon sind alle ohnmaechtig. Ab ins Pokemon-Center!")
        exit()

# ---- ENDGEGNER: POKEMON-MEISTER ----
print("\n" + "=" * 50)
print("   DER POKEMON-MEISTER WARTET!")
print("=" * 50)

meister = Gegner_Trainer("Pokemon-Meister Eich", 120, 17)
print(f"\n{meister.name}: KP {meister.kp}\n")

while not meister.ist_besiegt() and trainer_kp > 0:
    zeige_status(trainer_name, trainer_kp, trainer_geld, trainer_inventar)
    print(f"Gegner-KP: {meister.kp}")
    print("\nAktion:")
    print("1 - Angreifen")
    print("2 - Heilen (Trank noetig)")
    print("3 - Pokemon aus Pokedex einsetzen")
    print("4 - Fliehen")

    aktion = input("> ")

    if aktion == "1":
        s = berechne_angriff(14)
        meister.kp -= s
        print(f"Treffer! {s} Schaden!")

    elif aktion == "2":
        if "Trank" in trainer_inventar:
            trainer_inventar.remove("Trank")
            trainer_kp = heile_pokemon(trainer_kp, trainer_max_kp, 35)
        else:
            print("Kein Trank mehr!")
            continue  # Runde ohne Gegenzug wiederholen

    elif aktion == "3":
        print("Dein Pokedex:", list(pokedex.keys()))
        gew = input("Welches Pokemon?\n> ")
        if gew in pokedex:
            ps = pokedex[gew]
            meister.kp -= ps
            print(f"{gew} greift an! {ps} Schaden!")
        else:
            print("Dieses Pokemon kennst du nicht!")
            continue

    elif aktion == "4":
        print("Du fliehst... der Titel bleibt beim Meister.")
        exit()

    else:
        print("Ungueltige Eingabe.")
        continue

    # Meister schlaegt zurueck
    if not meister.ist_besiegt():
        ms = meister.greift_an()
        trainer_kp -= ms
        trainer_kp = max(0, trainer_kp)
        print(f"Der Meister antwortet mit {ms} Schaden!")

# ---- Ergebnis ----
print("\n" + "=" * 50)
if meister.ist_besiegt():
    print(f"{trainer_name} ist der neue Pokemon-Meister!")
    print("Die Legende hat ihren Anfang genommen.")
    print(f"\nEndstatistik:")
    print(f"  Restliche KP:   {trainer_kp}")
    print(f"  Poke-Dollar:    {trainer_geld}")
    print(f"  Shinys gefangen: {shiny_gefangen}")
    print(f"  Inventar:       {trainer_inventar}")
else:
    print(f"{trainer_name} ist gescheitert.")
    print("Doch jede Niederlage macht dich staerker!")
print("=" * 50)