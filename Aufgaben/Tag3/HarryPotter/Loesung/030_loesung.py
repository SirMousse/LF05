# ============================================
# Harry-Potter-Aufgabenreihe Python — Lösungen
# ============================================


# ============================================
# Aufgabe 1 — Name des Zauberschülers
# ============================================

name = input("Name des Zauberschülers: ")

if len(name) > 6:
    print("Mächtiger Zaubername")
else:
    print("Kurzer Zaubername")


# ============================================
# Aufgabe 2 — Punkte in Zauberkunde
# ============================================

punkte = int(input("Punkte in Zauberkunde: "))

if punkte >= 80:
    print("Sehr gute Zauberleistung")
else:
    print("Du musst weiter üben")


# ============================================
# Aufgabe 3 — Hauspunkte prüfen
# ============================================

hauspunkte = int(input("Hauspunkte: "))

if hauspunkte < 50:
    print("Dein Haus liegt zurück")
elif hauspunkte <= 100:
    print("Dein Haus ist gut dabei")
else:
    print("Dein Haus führt den Wettbewerb an")


# ============================================
# Aufgabe 4 — Geheimer Zauberspruch
# ============================================

zauberspruch = input("Geheimer Zauberspruch: ")

if zauberspruch == "lumos":
    print("Dein Zauberstab leuchtet")
else:
    print("Nichts passiert")


# ============================================
# Aufgabe 5 — Zauberstab-Stärke
# ============================================

stab_staerke = int(input("Zauberstab-Stärke: "))

if stab_staerke < 40:
    print("Der Zauberstab ist noch zu schwach")
else:
    print("Der Zauberstab ist einsatzbereit")


# ============================================
# Aufgabe 6 — Zufälliger Trank
# ============================================

import random

trank = random.randint(1, 6)

print(trank)

if trank == 6:
    print("Perfekter Zaubertrank")
else:
    print("Der Trank ist brauchbar")


# ============================================
# Aufgabe 7 — Bibliothekszugang
# ============================================

erlaubnis = input("Erlaubnis vorhanden? ")

if erlaubnis == "ja":
    print("Zugang zur verbotenen Abteilung erlaubt")
else:
    print("Zugang verweigert")


# ============================================
# Aufgabe 8 — Prüfung im Verwandlungsunterricht
# ============================================

punkte = int(input("Punktzahl: "))
zauberstab = input("Zauberstab dabei? ")

if punkte >= 60:
    if zauberstab == "ja":
        print("Prüfung bestanden")
    else:
        print("Ohne Zauberstab kannst du nicht antreten")
else:
    print("Prüfung nicht bestanden")


# ============================================
# Aufgabe 9 — Zufällige magische Begegnung
# ============================================

import random

begegnung = random.choice(["Troll", "Dementor", "Hippogreif"])

print(begegnung)

if begegnung == "Troll":
    print("Ein Troll greift an! Nutze Wingardium Leviosa!")
elif begegnung == "Dementor":
    print("Ein Dementor nähert sich! Denk an deine schönste Erinnerung — Expecto Patronum!")
else:
    print("Ein Hippogreif erscheint. Verbeuge dich langsam und zeige Respekt.")


# ============================================
# Aufgabe 10 — Name des Zaubertranks
# ============================================

trank_name = input("Name des Zaubertranks: ")

if len(trank_name) > 10:
    print("Komplexer Zaubertrank")
elif len(trank_name) > 5:
    print("Fortgeschrittener Zaubertrank")
else:
    print("Einfacher Zaubertrank")


# ============================================
# Aufgabe 11 — Zugang zur Kammer
# ============================================

magie_level = int(input("Magie-Level: "))
hinweise = int(input("Gefundene Hinweise: "))

if magie_level >= 70:
    if hinweise >= 3:
        print("Die geheime Kammer öffnet sich")
    else:
        print("Du hast noch nicht genug Hinweise")
else:
    print("Deine Magie ist zu schwach")


# ============================================
# Aufgabe 12 — Duell gegen einen dunklen Magier
# ============================================

import random

gegner = random.choice(["schwach", "mittel", "stark"])

print("Gegner:", gegner)

zauberkraft = int(input("Deine Zauberkraft: "))

if gegner == "schwach":
    if zauberkraft >= 20:
        print("Du besiegst den Gegner mühelos")
    else:
        print("Selbst der schwache Magier überfordert dich")

elif gegner == "mittel":
    if zauberkraft >= 40:
        print("Nach hartem Duell siegst du")
    else:
        print("Der Gegner ist zu stark für dich")

else:
    if zauberkraft >= 60:
        print("In einem epischen Duell besiegst du den dunklen Magier")
    else:
        print("Du verlierst das Duell")


# ============================================
# Aufgabe 13 — Zahlenrätsel der Zauberprüfung
# ============================================

import random

magische_zahl = random.randint(1, 10)

tipp = int(input("Rate die magische Zahl: "))

if tipp == magische_zahl:
    print("Magische Zahl erkannt")
elif tipp == magische_zahl - 1 or tipp == magische_zahl + 1:
    print("Fast richtig")
else:
    print("Falsche Zahl")


# ============================================
# Aufgabe 14 — Die Hogwarts-Prüfung
# ============================================

name = input("Name: ")
magie_level = int(input("Magie-Level: "))
hauspunkte = int(input("Hauspunkte: "))
zauberstab = input("Zauberstab vorhanden? ")

if len(name) > 6:
    print("Beeindruckender Zaubername")

if magie_level >= 80:
    if hauspunkte >= 100:
        if zauberstab == "ja":
            print("Hogwarts-Prüfung bestanden")
        else:
            print("Zauberstab fehlt")
    else:
        print("Nicht genug Hauspunkte")
else:
    print("Magie-Level zu niedrig")


# ============================================
# Aufgabe 15 — Hogwarts-Finale
# ============================================

import random

print("\n=== NACHTS IN HOGWARTS ===\n")

# Entscheidung 1: Name prüfen (len)
name = input("Dein Name: ")

if len(name) > 6:
    print(f"'{name}' — ein Name, der in Hogwarts bereits bekannt ist.")
else:
    print(f"'{name}' — kurz, aber der Mut zählt.")

# Entscheidung 2: Magie-Level
magie = int(input("Dein Magie-Level (0-100): "))

if magie < 30:
    print("Deine Magie ist noch sehr schwach für nächtliche Abenteuer.")
elif magie < 70:
    print("Du hast genug Magie für einfache Herausforderungen.")
else:
    print("Deine Magie ist beeindruckend. Hogwarts öffnet dir seine Geheimnisse.")

# Entscheidung 3: Hinweise und Zauberstab
hinweise = int(input("Gefundene Hinweise (0-10): "))
zauberstab = input("Zauberstab dabei? (ja/nein): ").strip().lower()

if hinweise < 3:
    print("Warnung: Zu wenige Hinweise — der Weg durch Hogwarts bleibt verborgen.")

# Zufallsereignis: Begegnung im Korridor
begegnung = random.choice(["Troll", "Dementor", "Peeves", "Dumbledore"])
print(f"\nIm dunklen Korridor begegnest du: {begegnung}!")

if begegnung == "Troll":
    print("Der Troll greift an! Du verlierst einen Hinweis.")
    hinweise = max(0, hinweise - 1)
    print(f"Verbleibende Hinweise: {hinweise}")
elif begegnung == "Dementor":
    print("Der Dementor saugt deine Energie. Magie -10.")
    magie = max(0, magie - 10)
    print(f"Neues Magie-Level: {magie}")
elif begegnung == "Peeves":
    print("Peeves verwirrt dich — aber du findest dabei einen versteckten Hinweis!")
    hinweise += 1
    print(f"Neue Hinweise: {hinweise}")
else:
    print("Dumbledore nickt anerkennend. Dein Magie-Level steigt um 15!")
    magie = min(100, magie + 15)
    print(f"Neues Magie-Level: {magie}")

# Entscheidung 4: Zugang zur geheimen Kammer
print("\n--- Die geheime Kammer ---")

# Entscheidung 5: Nested ifs — Finale
if magie >= 70:
    if hinweise >= 3:
        if zauberstab == "ja":
            if begegnung == "Dumbledore":
                # Ende 1
                print(f"\nEnde 1: Mit Dumbledores Segen und allem Nötigen")
                print(f"öffnet {name} die geheime Kammer und rettet Hogwarts.")
            else:
                # Ende 2
                print(f"\nEnde 2: {name} öffnet die geheime Kammer.")
                print("Das Rätsel ist gelöst. Hogwarts ist sicher.")
        else:
            # Ende 3
            print(f"\nEnde 3: Ohne Zauberstab ist {name} machtlos vor der Kammer.")
            print("Die Tür bleibt verschlossen.")
    else:
        # Ende 4
        print(f"\nEnde 4: Nicht genug Hinweise.")
        print(f"{name} irrt durch die Gänge, findet aber keinen Zugang zur Kammer.")
elif magie >= 30:
    # Ende 5
    print(f"\nEnde 5: Die Magie reicht nicht ganz.")
    print(f"{name} scheitert knapp an der Kammertür und kehrt zurück.")
else:
    # Ende 6
    print(f"\nEnde 6: Zu wenig Magie für diese Nacht.")
    print(f"{name} flüchtet zurück in den Schlafsaal. Hogwarts wartet auf einen stärkeren Helden.")