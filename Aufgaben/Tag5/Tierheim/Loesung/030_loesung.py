import random

# ==================================================
# RETTUNG DER PFOTENINSEL
# Ein komplettes Tierheim-Management-Adventure
# ==================================================

print("=" * 50)
print("   RETTUNG DER PFOTENINSEL")
print("   Das Tierheim braucht deine Hilfe!")
print("=" * 50)


# ==================================================
# LEVEL 1 – DAS ERSTE TIER
# Konzepte: Variablen, print(), input()
# ==================================================
print("\n--- LEVEL 1: WILLKOMMEN ---")

# input() zeigt Text an und wartet auf Eingabe.
# Das Ergebnis ist immer ein String.
name        = input("Wie heisst du?\n> ")
alter       = input("Wie alt bist du?\n> ")
lieblingstier = input("Dein Lieblingstier (Hund / Katze / Kaninchen / Vogel):\n> ")

# f-Strings: {} wird durch den Variablenwert ersetzt.
print(f"\nWillkommen im Tierheim Pfoteninsel!")
print(f"Hallo {name}!")
print(f"Du bist {alter} Jahre alt.")
print(f"Heute kuemmerst du dich um {lieblingstier}e.")


# ==================================================
# LEVEL 2 – DIE ADOPTION
# Konzepte: if / elif / else, Eingabe pruefen
# ==================================================
print("\n--- LEVEL 2: ADOPTIONS-KONTROLLE ---")
print("Ein Besucher moechte ein Tier adoptieren.")

# while True laeuft endlos – wir verlassen mit break.
while True:
    antwort = input("Ist das Tier geimpft? (ja / nein)\n> ")

    # .lower() macht die Eingabe kleingeschrieben,
    # damit "Ja" und "JA" auch erkannt werden.
    if antwort.lower() == "ja":
        print("Adoption erlaubt! Das Tier bekommt ein neues Zuhause.")
        break
    elif antwort.lower() == "nein":
        print("Adoption nicht erlaubt. Das Tier muss zuerst geimpft werden.")
        break
    else:
        print("Ungueltige Eingabe – bitte 'ja' oder 'nein' eingeben.")


# ==================================================
# LEVEL 3 – DAS ZUFALLSTIER
# Konzepte: random
# ==================================================
print("\n--- LEVEL 3: NEUES TIER ANGEKOMMEN ---")

# Dictionary als Nachschlagewerk: Zahl -> Tierart
tier_dict = {1: "Hund", 2: "Katze", 3: "Kaninchen", 4: "Vogel"}

# random.randint(1, 4) gibt eine zufaellige Zahl von 1 bis 4.
zufall = random.randint(1, 4)
print(f"Heute ist ein {tier_dict[zufall]} angekommen!")


# ==================================================
# LEVEL 4 – DAS FUTTERLAGER
# Konzepte: Listen
# ==================================================
print("\n--- LEVEL 4: FUTTERLAGER ---")

# Eine Liste speichert mehrere Werte. Index startet bei 0.
futter = ["Hundefutter", "Katzenfutter", "Karotten"]

# Alle Futtersorten anzeigen
print("Futterlager:")
for sorte in futter:
    print(f"  - {sorte}")

# Neues Futter hinzufuegen: .append() haengt ans Ende.
futter.append("Vogelfutter")
print(f"\nNach Lieferung: {futter}")

# Futter entfernen: .remove() loescht den ersten passenden Eintrag.
futter.remove("Karotten")
print(f"Karotten leer: {futter}")

# Pruefen ob Futter vorhanden: "in" gibt True oder False.
if "Katzenfutter" in futter:
    print("Katzenfutter ist vorratig!")

# Bonus: Spieler kann neue Futtersorten hinzufuegen.
neue_sorte = input("Welches Futter lieferst du nach?\n> ")
if len(futter) < 10:   # Lager-Limit: max. 10 Plaetze
    futter.append(neue_sorte)
    print(f"Lager: {futter}")
else:
    print("Lager ist voll! (max. 10 Sorten)")


# ==================================================
# LEVEL 5 – DIE TAEGLICHE ROUTINE
# Konzepte: while-Schleife
# ==================================================
print("\n--- LEVEL 5: TAGESROUTINE ---")
print("Der Arbeitstag beginnt!")

# while True laeuft endlos – verlassen nur mit break.
while True:
    print("\nWas tust du?")
    print("1 - Tiere fuettern")
    print("2 - Kaefig reinigen")
    print("3 - Feierabend machen")

    wahl = input("> ")

    if wahl == "1":
        tier_nr = random.randint(1, 10)
        print(f"Tier {tier_nr} wurde gefuettert.")
    elif wahl == "2":
        print("Kaefig gereinigt. Die Tiere sind happy!")
    elif wahl == "3":
        print("Feierabend! Alle Tiere sind versorgt.")
        break  # Schleife verlassen
    else:
        print("Unbekannte Aktion.")


# ==================================================
# LEVEL 6 – DIE TIERKONTROLLE
# Konzepte: for-Schleifen
# ==================================================
print("\n--- LEVEL 6: TIERKONTROLLE ---")
print("5 Tiere werden untersucht...\n")

gesunde_tiere = 0

# range(1, 6) erzeugt die Zahlen 1 bis 5.
for i in range(1, 6):
    # Zufaellige Gesundheits- und Stimmungswerte
    gesundheit = random.randint(1, 10)
    stimmung   = random.randint(1, 3)   # 1=gut, 2=muede, 3=braucht Hilfe

    print(f"Tier {i}: Gesundheit {gesundheit}/10", end=" | ")

    if stimmung == 1:
        print("Gesund")
        gesunde_tiere += 1
    elif stimmung == 2:
        print("Muede")
    else:
        print("Braucht Hilfe!")

print(f"\nGesunde Tiere: {gesunde_tiere} / 5")


# ==================================================
# LEVEL 7 – DIE TIERDATENBANK
# Konzepte: Dictionaries
# ==================================================
print("\n--- LEVEL 7: TIERDATENBANK ---")

# Dictionary: Schluessel-Wert-Paare in geschweiften Klammern {}.
tiere = {
    "Bello":   "Hund",
    "Minka":   "Katze",
    "Hoppel":  "Kaninchen"
}

# Alle Tiere anzeigen: .items() liefert Schluessel+Wert als Paare.
print("Registrierte Tiere:")
for tier_name, tier_art in tiere.items():
    print(f"  {tier_name}: {tier_art}")

# Tierart abrufen
print(f"\nBello ist ein: {tiere['Bello']}")

# Neues Tier hinzufuegen
tiere["Tweety"] = "Vogel"
print(f"Tweety aufgenommen: {tiere}")

# Tier entfernen
del tiere["Hoppel"]
print(f"Hoppel adoptiert: {tiere}")

# Bonus: Spieler sucht nach Tier
suche = input("Nach welchem Tier suchst du?\n> ")
if suche in tiere:
    print(f"Gefunden! {suche} ist ein {tiere[suche]}.")
else:
    print(f"{suche} ist nicht im Tierheim.")


# ==================================================
# LEVEL 8 – DIE KARTE DES TIERHEIMS
# Konzepte: Tupel
# ==================================================
print("\n--- LEVEL 8: TIERHEIM-KARTE ---")

# Ein Tupel ist unveraenderlich – perfekt fuer feste Koordinaten.
hundebereich = (5, 2)
print(f"Hundebereich: X={hundebereich[0]}, Y={hundebereich[1]}")

# Mehrere Bereiche als Tupel-Liste (Bonus)
bereiche = [
    ("Hundehaus",   5,  2),
    ("Katzenhaus",  3,  7),
    ("Vogelraum",   8,  4),
    ("Lager",       1,  9),
    ("Buero",       6,  6),
]

print("\nTierheim-Karte:")
for bname, bx, by in bereiche:
    print(f"  {bname}: ({bx}, {by})")

# Spielerposition pruefen
try:
    px = int(input("\nDeine X-Position:\n> "))
    py = int(input("Deine Y-Position:\n> "))
except ValueError:
    px, py = 0, 0

if (px, py) == hundebereich:
    print("Du bist im Hundehaus! Die Hunde bellen freudig.")
else:
    print(f"Falscher Bereich. Hundehaus liegt bei {hundebereich}.")


# ==================================================
# LEVEL 9 & ENDGEGNER – DAS GROSSE TIERHEIM-SYSTEM
# Konzepte: ALLES kombiniert + Klassen + Funktionen
# ==================================================
print("\n" + "=" * 50)
print("   LEVEL 9: DIE TIERHEIM-KRISE!")
print("   Zu viele Tiere, zu wenig Futter!")
print("=" * 50)


# ---- Funktionen ----
def zeige_status(sname, energie, geld, inv):
    """Zeigt den aktuellen Mitarbeiter-Status an."""
    print(f"\n[ {sname} | Energie {energie} | {geld} Euro | {inv} ]")

def versorge_tier(energie, max_energie, menge):
    """Stellt Energie wieder her, aber nicht ueber max_energie."""
    # min() verhindert Ueberheilung.
    neue_energie = min(energie + menge, max_energie)
    print(f"Kurze Pause: +{neue_energie - energie} Energie.")
    return neue_energie

def berechne_massnahme(basis, krit_chance=0.2):
    """Berechnet Wirkung einer Massnahme mit Krit-Chance."""
    wirkung = random.randint(basis - 3, basis + 5)
    # random.random() liefert 0.0 bis 1.0 – unter krit_chance = Krit!
    if random.random() < krit_chance:
        wirkung *= 2
        print("Perfekte Massnahme! Doppelte Wirkung!")
    return wirkung


# ---- Klasse ----
class Krise:
    def __init__(self, name, staerke, schaden):
        # __init__ wird beim Erstellen automatisch aufgerufen.
        self.name    = name
        self.staerke = staerke
        self.schaden = schaden

    def verschlimmert_sich(self):
        """Gibt zufaelligen Schaden zurueck."""
        return random.randint(self.schaden - 3, self.schaden + 4)

    def ist_behoben(self):
        """True wenn keine Staerke mehr."""
        return self.staerke <= 0


# ---- Spielaufbau ----
print("\nNeue Schicht beginnt...")
mitarbeiter_name   = input("Dein Name:\n> ")
mitarbeiter_energie = 100
mitarbeiter_max    = 100
mitarbeiter_geld   = 200
mitarbeiter_inv    = ["Futterportion", "Futterportion", "Erste-Hilfe-Set"]

# Tierheim-Bereiche als Tupel (Name, X, Y)
tierheim_bereiche = [
    ("Eingangsbereich", 1, 1),
    ("Hundestation",    5, 2),
    ("Katzentrakt",     3, 7),
]

# Tierdatenbank als Dictionary
tierheim_db = {
    "Bello":  "Hund",
    "Minka":  "Katze",
    "Tweety": "Vogel",
}

# Krisen-Pool
krisen_pool = [
    {"name": "Futterknappheit", "staerke": 35, "schaden": 10, "geld": 40,  "drop": "Spendenquittung"},
    {"name": "Krankes Tier",    "staerke": 45, "schaden": 13, "geld": 60,  "drop": "Tierarztbericht"},
    {"name": "Fluchtversuch",   "staerke": 30, "schaden":  9, "geld": 30,  "drop": "Halsband"},
]

# ---- Spendenstand ----
print("\nSpendenaufruf gestartet!")
# Spenden sind zufaellig (Mini-Challenge)
spendenstand = {
    "Futterportion":   random.randint(5,  12),
    "Medikamente":     random.randint(15, 25),
    "Spielzeug-Paket": random.randint(8,  18),
}

print("Verfuegbare Spenden:")
for item_s, preis_s in spendenstand.items():
    print(f"  {item_s}: {preis_s} Euro")

kauf = input("Was kaufst du? (oder 'weiter')\n> ")
if kauf in spendenstand:
    preis = spendenstand[kauf]
    if mitarbeiter_geld >= preis:
        mitarbeiter_geld -= preis
        if len(mitarbeiter_inv) < 10:
            mitarbeiter_inv.append(kauf)
            print(f"Gekauft! {kauf} fuer {preis} Euro.")
        else:
            print("Inventar voll! (max. 10 Plaetze)")
    else:
        print("Nicht genug Geld!")
else:
    print("Nichts genommen.")

# ---- Runde durch das Tierheim ----
print(f"\nTierheim-Karte:")
for bname, bx, by in tierheim_bereiche:
    print(f"  [{bx},{by}] {bname}")

print(f"\n{mitarbeiter_name} beginnt die Runde...\n")

for bname, bx, by in tierheim_bereiche:
    if mitarbeiter_energie <= 0:
        break

    print(f"\n  Bereich: {bname} ({bx},{by})")

    # Zufaelliges Ereignis
    ereignis = random.choice(["krise", "seltenes_tier", "ruhe"])

    # 10% Notfall-Chance (Mini-Challenge)
    if random.random() < 0.1:
        ereignis = "notfall"

    if ereignis in ("krise", "notfall"):
        if ereignis == "notfall":
            k_daten = {"name": "Notfall: Schwer verletztes Tier", "staerke": 50,
                       "schaden": 15, "geld": 80, "drop": "Veterinärausweis"}
            print(f"  NOTFALL: Schwer verletztes Tier eingeliefert!")
        else:
            k_daten = random.choice(krisen_pool)

        krise = Krise(k_daten["name"], k_daten["staerke"], k_daten["schaden"])
        print(f"  Krise: {krise.name}")

        # Krisenbewaeltigungs-Schleife
        while not krise.ist_behoben() and mitarbeiter_energie > 0:
            w = berechne_massnahme(12)
            krise.staerke -= w
            aufwand = krise.verschlimmert_sich()
            mitarbeiter_energie -= aufwand
            mitarbeiter_energie = max(0, mitarbeiter_energie)
            print(f"  Massnahme: -{aufwand} Energie | Krise: -{w} Staerke "
                  f"(Krise: {max(0,krise.staerke)}, Energie: {mitarbeiter_energie})")

        if krise.ist_behoben():
            print(f"  {krise.name} behoben! +{k_daten['geld']} Euro")
            mitarbeiter_geld += k_daten["geld"]
            # Drop
            if random.random() < 0.4:
                drop = k_daten["drop"]
                if len(mitarbeiter_inv) < 10:
                    mitarbeiter_inv.append(drop)
                    print(f"  Erhalten: {drop}")
        else:
            print("  Energie erschoepft...")

    elif ereignis == "seltenes_tier":
        # Seltenes Tier (Mini-Challenge)
        seltene = ["Schildkroete", "Igel", "Frettchen", "Minischwein"]
        tier = random.choice(seltene)
        tierheim_db[tier] = "Exotisch"
        mitarbeiter_geld += 50
        print(f"  Seltenes Tier aufgenommen: {tier}! +50 Euro Foerderung")

    else:
        rep = random.randint(10, 20)
        mitarbeiter_energie = versorge_tier(mitarbeiter_energie, mitarbeiter_max, rep)

    zeige_status(mitarbeiter_name, mitarbeiter_energie, mitarbeiter_geld, mitarbeiter_inv)

    if mitarbeiter_energie <= 0:
        print("\nDu bist erschoepft. Bitte nach Hause gehen!")
        exit()

# ---- ENDGEGNER: DIE GROSSE KRISE ----
print("\n" + "=" * 50)
print("   GROSSE TIERHEIM-KRISE!")
print("   Uberfuellung + Futternotstand + Krankheit")
print("=" * 50)

grosse_krise = Krise("Grosse Pfoteninsel-Krise", 120, 15)
print(f"\nKrisen-Staerke: {grosse_krise.staerke}\n")

while not grosse_krise.ist_behoben() and mitarbeiter_energie > 0:
    zeige_status(mitarbeiter_name, mitarbeiter_energie, mitarbeiter_geld, mitarbeiter_inv)
    print(f"Krisen-Staerke: {grosse_krise.staerke}")
    print("\nAktion:")
    print("1 - Tiere versorgen")
    print("2 - Energie erhoehen (Futterportion noetig)")
    print("3 - Spenden einsetzen (aus Inventar)")
    print("4 - Aufgeben")

    aktion = input("> ")

    if aktion == "1":
        w = berechne_massnahme(12)
        grosse_krise.staerke -= w
        print(f"Tiere versorgt! -{w} Krisen-Staerke!")

    elif aktion == "2":
        if "Futterportion" in mitarbeiter_inv:
            mitarbeiter_inv.remove("Futterportion")
            mitarbeiter_energie = versorge_tier(mitarbeiter_energie, mitarbeiter_max, 30)
        else:
            print("Keine Futterportion mehr!")
            continue  # Runde ohne Gegenzug wiederholen

    elif aktion == "3":
        spendbar = [i for i in mitarbeiter_inv if i not in ("Futterportion", "Erste-Hilfe-Set")]
        if spendbar:
            print("Einsetzbare Spenden:", spendbar)
            gew = input("Was einsetzten?\n> ")
            if gew in mitarbeiter_inv:
                mitarbeiter_inv.remove(gew)
                grosse_krise.staerke -= 25
                print(f"{gew} eingesetzt! -25 Krisen-Staerke!")
            else:
                print("Nicht im Inventar!")
                continue
        else:
            print("Keine einsetzbaren Spenden!")
            continue

    elif aktion == "4":
        print("Du verlaeesst das Tierheim. Die Krise bleibt bestehen...")
        exit()

    else:
        print("Ungueltige Eingabe.")
        continue

    # Krise verschlimmert sich
    if not grosse_krise.ist_behoben():
        k_schaden = grosse_krise.verschlimmert_sich()
        mitarbeiter_energie -= k_schaden
        mitarbeiter_energie = max(0, mitarbeiter_energie)
        print(f"Die Krise verursacht -{k_schaden} Energie!")

# ---- Ergebnis ----
print("\n" + "=" * 50)
if grosse_krise.ist_behoben():
    print(f"{mitarbeiter_name} hat die Krise gemeistert!")
    print("Pfoteninsel ist gerettet. Alle Tiere sind versorgt!")
    print(f"\nEndstatistik:")
    print(f"  Energie:        {mitarbeiter_energie}")
    print(f"  Geld:           {mitarbeiter_geld} Euro")
    print(f"  Inventar:       {mitarbeiter_inv}")
    print(f"  Tiere im Heim:  {list(tierheim_db.keys())}")
else:
    print(f"{mitarbeiter_name} hat die Energie verloren.")
    print("Das Tierheim benoetigt dringend Hilfe...")
print("=" * 50)