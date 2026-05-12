# ============================================
# Zelda-Aufgabenreihe Python — Lösungen
# ============================================


# ============================================
# Aufgabe 1 — Heldenname prüfen
# ============================================

heldenname = input("Heldenname: ")

if len(heldenname) > 6:
    print("Würdiger Heldenname")
else:
    print("Kurzer Heldenname")


# ============================================
# Aufgabe 2 — Herzen prüfen
# ============================================

herzen = int(input("Anzahl Herzen: "))

if herzen >= 10:
    print("Du bist gut vorbereitet")
else:
    print("Du brauchst mehr Herzen")


# ============================================
# Aufgabe 3 — Rubine prüfen
# ============================================

rubine = int(input("Anzahl Rubine: "))

if rubine < 50:
    print("Du bist noch arm")
elif rubine < 200:
    print("Du kannst dir Ausrüstung kaufen")
else:
    print("Du bist reich genug für seltene Items")


# ============================================
# Aufgabe 4 — Geheimes Tempelwort
# ============================================

wort = input("Geheimes Wort: ")

if wort == "triforce":
    print("Der Tempel öffnet sich")
else:
    print("Der Tempel bleibt verschlossen")


# ============================================
# Aufgabe 5 — Ausdauer prüfen
# ============================================

ausdauer = int(input("Ausdauer: "))

if ausdauer < 40:
    print("Du bist zu erschöpft zum Klettern")
else:
    print("Du kannst weiterklettern")


# ============================================
# Aufgabe 6 — Zufälliger Schatzfund
# ============================================

import random

truhe = random.randint(1, 6)

print(truhe)

if truhe == 6:
    print("Du findest ein seltenes Item")
else:
    print("Du findest ein paar Rubine")


# ============================================
# Aufgabe 7 — Schlüssel vorhanden
# ============================================

schluessel = input("Schlüssel vorhanden? ")

if schluessel == "ja":
    print("Die Tür öffnet sich")
else:
    print("Die Tür bleibt verschlossen")


# ============================================
# Aufgabe 8 — Tempel-Zugang
# ============================================

herzen = int(input("Anzahl Herzen: "))
schluessel = input("Schlüssel vorhanden? ")

if herzen >= 8:
    if schluessel == "ja":
        print("Du darfst den Tempel betreten")
    else:
        print("Du brauchst einen Schlüssel")
else:
    print("Du hast nicht genug Herzen")


# ============================================
# Aufgabe 9 — Zufällige Begegnung
# ============================================

import random

begegnung = random.choice(["Bokblin", "Wächter", "Fee"])

print(begegnung)

if begegnung == "Bokblin":
    print("Ein Bokblin greift an! Zieh dein Schwert.")
elif begegnung == "Wächter":
    print("Ein Wächter entdeckt dich! Lauf so schnell du kannst.")
else:
    print("Eine Fee erscheint! Sie heilt all deine Herzen.")


# ============================================
# Aufgabe 10 — Itemname prüfen
# ============================================

item = input("Itemname: ")

if len(item) > 10:
    print("Legendäres Item")
elif len(item) > 5:
    print("Besonderes Item")
else:
    print("Einfaches Item")


# ============================================
# Aufgabe 11 — Bossraum öffnen
# ============================================

herzen = int(input("Anzahl Herzen: "))
schluessel = int(input("Anzahl Schlüssel: "))

if herzen >= 12:
    if schluessel >= 3:
        print("Der Bossraum öffnet sich")
    else:
        print("Du brauchst mehr Schlüssel")
else:
    print("Du bist zu schwach für den Bossraum")


# ============================================
# Aufgabe 12 — Kampf gegen den Tempelboss
# ============================================

import random

boss = random.choice(["schwach", "mittel", "stark"])

print("Boss:", boss)

angriffskraft = int(input("Angriffskraft: "))

if boss == "schwach":
    if angriffskraft >= 20:
        print("Du besiegst den Boss mühelos")
    else:
        print("Selbst der schwache Boss ist zu viel für dich")

elif boss == "mittel":
    if angriffskraft >= 40:
        print("Du besiegst den Boss nach hartem Kampf")
    else:
        print("Der Boss ist zu stark für dich")

else:
    if angriffskraft >= 60:
        print("In einem epischen Kampf besiegst du den starken Boss")
    else:
        print("Du verlierst den Kampf")


# ============================================
# Aufgabe 13 — Schrein-Rätsel
# ============================================

import random

schreinzahl = random.randint(1, 10)

tipp = int(input("Rate die Schreinzahl: "))

if tipp == schreinzahl:
    print("Der Schrein ist gelöst")
elif tipp == schreinzahl - 1 or tipp == schreinzahl + 1:
    print("Fast richtig")
else:
    print("Falsche Zahl")


# ============================================
# Aufgabe 14 — Die Heldenprüfung
# ============================================

heldenname = input("Heldenname: ")
herzen = int(input("Herzen: "))
rubine = int(input("Rubine: "))
masterschwert = input("Masterschwert vorhanden? ")

if len(heldenname) > 6:
    print("Heldenname akzeptiert")

if herzen >= 12:
    if rubine >= 100:
        if masterschwert == "ja":
            print("Heldenprüfung bestanden")
        else:
            print("Masterschwert fehlt")
    else:
        print("Nicht genug Rubine")
else:
    print("Nicht genug Herzen")


# ============================================
# Aufgabe 15 — Zelda-Finale
# ============================================

import random

print("\n=== DER VERGESSENE TEMPEL ===\n")

# Entscheidung 1: Heldenname prüfen (len)
heldenname = input("Dein Heldenname: ")

if len(heldenname) > 6:
    print(f"Der Name {heldenname} wird in die Tempelwände gemeißelt.")
else:
    print(f"{heldenname} — kurz, aber mutig.")

# Entscheidung 2: Herzen
herzen = int(input("Wie viele Herzen hast du? "))

if herzen < 6:
    print("Du bist kaum bereit für diesen Tempel.")
elif herzen <= 12:
    print("Deine Herzen reichen — aber gerade so.")
else:
    print("Du bist in Bestform. Der Tempel zittert.")

# Entscheidung 3: Rubine
rubine = int(input("Wie viele Rubine hast du? "))

# Entscheidung 4: Schlüssel
schluessel = int(input("Anzahl der Schlüssel: "))

# Zufallsereignis: Falle oder Schatztruhe
ereignis = random.choice(["Falle", "Schatztruhe", "Geist"])
print(f"\nIm Tempel begegnest du: {ereignis}")

if ereignis == "Falle":
    print("Die Falle schlägt zu! Du verlierst 2 Herzen.")
    herzen -= 2
elif ereignis == "Schatztruhe":
    print("Eine Schatztruhe! Du gewinnst 50 Rubine.")
    rubine += 50
else:
    print("Ein Geist flüstert dir den Bosscode zu.")

# Entscheidung 5: nested ifs — Bosskampf
print("\n--- Der Bossraum ---")

if herzen >= 8:
    if schluessel >= 2:
        if rubine >= 50:
            boss_staerke = random.choice(["mittel", "stark"])
            print(f"Der Boss erwacht — er ist {boss_staerke}!")

            if boss_staerke == "mittel":
                # Ende 1
                print(f"\nEnde 1: {heldenname} besiegt den Boss nach hartem Kampf.")
                print("Hyrule ist gerettet. Zelda dankt dem Helden.")
            else:
                if herzen >= 14:
                    # Ende 2
                    print(f"\nEnde 2: Mit voller Herzleiste überwindet {heldenname} den starken Boss.")
                    print("Eine Legende ist geboren.")
                else:
                    # Ende 3
                    print(f"\nEnde 3: Der starke Boss ist zu mächtig.")
                    print(f"{heldenname} flieht — und plant die Rückkehr.")
        else:
            # Ende 4
            print(f"\nEnde 4: Ohne Rubine fehlt die Ausrüstung für den Bosskampf.")
            print(f"{heldenname} kehrt um und sammelt mehr Vorräte.")
    else:
        # Ende 5
        print(f"\nEnde 5: Zu wenige Schlüssel — der Bossraum bleibt verschlossen.")
        print("Der Tempel wartet auf einen besser vorbereiteten Helden.")
else:
    # Ende 6
    print(f"\nEnde 6: Zu wenige Herzen für diesen Tempel.")
    print(f"{heldenname} zieht sich zurück. Noch ist es nicht die Zeit.")