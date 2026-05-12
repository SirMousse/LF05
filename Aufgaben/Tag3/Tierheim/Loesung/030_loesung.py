# ============================================
# Tierheim-Aufgabenreihe Python — Lösungen
# ============================================


# ============================================
# Aufgabe 1 — Tiername prüfen
# ============================================

tiername = input("Tiername: ")

if len(tiername) > 6:
    print("Langer Tiername")
else:
    print("Kurzer Tiername")


# ============================================
# Aufgabe 2 — Freie Plätze
# ============================================

plaetze = int(input("Freie Plätze: "))

if plaetze >= 10:
    print("Es sind genug Plätze frei")
else:
    print("Das Tierheim ist fast voll")


# ============================================
# Aufgabe 3 — Futtervorrat prüfen
# ============================================

futter = int(input("Futterportionen: "))

if futter < 20:
    print("Futter wird knapp")
elif futter <= 50:
    print("Futter reicht noch eine Weile")
else:
    print("Futterlager gut gefüllt")


# ============================================
# Aufgabe 4 — Tieraufnahme-Code
# ============================================

code = input("Aufnahme-Code: ")

if code == "pfote":
    print("Tieraufnahme erlaubt")
else:
    print("Aufnahme-Code falsch")


# ============================================
# Aufgabe 5 — Gesundheitswert
# ============================================

gesundheit = int(input("Gesundheitswert: "))

if gesundheit < 40:
    print("Tier muss zum Tierarzt")
else:
    print("Tier ist stabil")


# ============================================
# Aufgabe 6 — Zufällige Tierankunft
# ============================================

import random

ankunft = random.randint(1, 6)

print(ankunft)

if ankunft == 6:
    print("Notfalltier angekommen")
else:
    print("Normale Tieraufnahme")


# ============================================
# Aufgabe 7 — Impfpass vorhanden
# ============================================

impfpass = input("Impfpass vorhanden? ")

if impfpass == "ja":
    print("Tier kann direkt aufgenommen werden")
else:
    print("Impfstatus muss geprüft werden")


# ============================================
# Aufgabe 8 — Aufnahme ins Tierheim
# ============================================

plaetze = int(input("Freie Plätze: "))
impfpass = input("Impfpass vorhanden? ")

if plaetze >= 1:
    if impfpass == "ja":
        print("Tier wird aufgenommen")
    else:
        print("Tier kommt zuerst in die Quarantäne")
else:
    print("Keine freien Plätze vorhanden")


# ============================================
# Aufgabe 9 — Zufälliges Tier
# ============================================

import random

tier = random.choice(["Hund", "Katze", "Kaninchen"])

print(tier)

if tier == "Hund":
    print("Der Hund bekommt einen großen Auslauf.")
elif tier == "Katze":
    print("Die Katze kommt ins ruhige Katzenzimmer.")
else:
    print("Das Kaninchen bekommt frisches Heu und Gemüse.")


# ============================================
# Aufgabe 10 — Adoptionsname prüfen
# ============================================

adoptionsname = input("Name der adoptierenden Person: ")

if len(adoptionsname) > 10:
    print("Sehr langer Name im Antrag")
elif len(adoptionsname) > 5:
    print("Name akzeptiert")
else:
    print("Name sehr kurz")


# ============================================
# Aufgabe 11 — Vermittlung prüfen
# ============================================

alter = int(input("Alter des Tieres: "))
gesundheit = int(input("Gesundheitswert: "))

if alter >= 1:
    if gesundheit >= 60:
        print("Tier kann vermittelt werden")
    else:
        print("Tier braucht zuerst Behandlung")
else:
    print("Tier ist noch zu jung für die Vermittlung")


# ============================================
# Aufgabe 12 — Tierarzt-Notfall
# ============================================

import random

zustand = random.choice(["stabil", "verletzt", "kritisch"])

print("Zustand:", zustand)

termine = int(input("Freie Tierarzt-Termine: "))

if zustand == "stabil":
    print("Kein Tierarzt nötig — Tier wird normal aufgenommen.")

elif zustand == "verletzt":
    if termine >= 1:
        print("Tier wird zum Tierarzt gebracht.")
    else:
        print("Kein Termin frei — Tier wird beobachtet.")

else:
    if termine >= 1:
        print("Notfallbehandlung eingeleitet.")
    else:
        print("Externe Tierklinik kontaktieren")


# ============================================
# Aufgabe 13 — Chipnummer-Rätsel
# ============================================

import random

chipnummer = random.randint(1, 10)

tipp = int(input("Rate die Chipnummer: "))

if tipp == chipnummer:
    print("Chipnummer gefunden")
elif tipp == chipnummer - 1 or tipp == chipnummer + 1:
    print("Fast richtig")
else:
    print("Falsche Chipnummer")


# ============================================
# Aufgabe 14 — Die Tierheim-Prüfung
# ============================================

mitarbeitername = input("Mitarbeitername: ")
plaetze = int(input("Freie Plätze: "))
futter = int(input("Futterportionen: "))
impfpass = input("Impfpass vorhanden? ")

if len(mitarbeitername) > 6:
    print("Mitarbeitername akzeptiert")

if plaetze >= 1:
    if futter >= 20:
        if impfpass == "ja":
            print("Tierheim-Prüfung bestanden")
        else:
            print("Impfpass fehlt")
    else:
        print("Nicht genug Futter")
else:
    print("Keine freien Plätze")


# ============================================
# Aufgabe 15 — Tierheim-Finale
# ============================================

import random

print("\n=== TIERHEIM-AUFNAHME ===\n")

# Entscheidung 1: Mitarbeitername (len)
mitarbeiter = input("Name des Mitarbeiters: ")

if len(mitarbeiter) > 6:
    print(f"Willkommen, {mitarbeiter}. Dienst beginnt.")
else:
    print(f"Willkommen, {mitarbeiter}!")

# Entscheidung 2: Freie Plätze
plaetze = int(input("Freie Plätze im Tierheim: "))

# Entscheidung 3: Futter
futter = int(input("Futterportionen vorhanden: "))

if futter < 20:
    print("Warnung: Futter wird knapp.")

# Zufallsereignis: Welches Tier kommt an?
tier = random.choice(["Hund", "Katze", "Kaninchen", "Notfalltier"])
print(f"\nNeues Tier angekommen: {tier}")

# Entscheidung 4: Gesundheit
gesundheit = int(input("Gesundheitswert des Tieres (0-100): "))

# Entscheidung 5: Impfpass
impfpass = input("Impfpass vorhanden? (ja/nein): ").strip().lower()

# Nested ifs — Aufnahme-Entscheidung
print("\n--- Aufnahme-Entscheidung ---")

if plaetze >= 1:

    if gesundheit >= 60:

        if impfpass == "ja":
            if tier == "Notfalltier":
                # Ende 1
                print(f"Ende 1: Notfalltier sofort aufgenommen und versorgt.")
                print("Dank schneller Reaktion überlebt das Tier.")
            else:
                # Ende 2
                print(f"Ende 2: {tier} wird regulär aufgenommen.")
                print(f"Alles in Ordnung — {tier} findet ein neues Zuhause.")

        else:
            # Ende 3
            print(f"Ende 3: {tier} kommt in die Quarantäne.")
            print("Impfstatus wird nachgereicht — Aufnahme in 7 Tagen möglich.")

    else:
        if gesundheit < 30:
            # Ende 4
            print(f"Ende 4: Kritischer Zustand.")
            print(f"{tier} wird sofort zum Notfalltierarzt gebracht.")
        else:
            # Ende 5
            print(f"Ende 5: {tier} braucht Behandlung vor der Aufnahme.")
            print("Tierarzttermin wird gebucht.")

else:
    if futter >= 20:
        # Ende 6
        print(f"Ende 6: Kein freier Platz — {tier} wird an Partnertierheim weitergeleitet.")
    else:
        # Ende 7
        print(f"Ende 7: Kein Platz, kein Futter.")
        print("Notfallprotokoll wird ausgelöst. Externe Hilfe angefordert.")