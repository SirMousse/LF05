# ============================================
# Tierheim-Aufgabenreihe Python
# Von leicht -> schwer
# ============================================


# ============================================
# Aufgabe 1 — Tiername prüfen
# ============================================

# Frage den Namen eines Tieres ab.
#
# Wenn der Name länger als 6 Zeichen ist:
# Ausgabe -> "Langer Tiername"
#
# Sonst:
# Ausgabe -> "Kurzer Tiername"
#
# Nutze:
# input()
# if / else
# len()

tiername = input("Tiername: ")

# Dein Code



# ============================================
# Aufgabe 2 — Freie Plätze
# ============================================

# Frage nach der Anzahl freier Plätze im Tierheim.
#
# Ab 10 freien Plätzen:
# Ausgabe -> "Es sind genug Plätze frei"
#
# Sonst:
# Ausgabe -> "Das Tierheim ist fast voll"
#
# Nutze:
# if / else
# Operatoren

plaetze = int(input("Freie Plätze: "))

# Dein Code



# ============================================
# Aufgabe 3 — Futtervorrat prüfen
# ============================================

# Frage nach dem Futtervorrat in Portionen.
#
# Unter 20:
# Ausgabe -> "Futter wird knapp"
#
# Zwischen 20 und 50:
# Ausgabe -> "Futter reicht noch eine Weile"
#
# Über 50:
# Ausgabe -> "Futterlager gut gefüllt"
#
# Nutze:
# if / elif / else

futter = int(input("Futterportionen: "))

# Dein Code



# ============================================
# Aufgabe 4 — Tieraufnahme-Code
# ============================================

# Frage nach einem geheimen Aufnahme-Code.
#
# Wenn der Code "pfote" ist:
# Ausgabe -> "Tieraufnahme erlaubt"
#
# Sonst:
# Ausgabe -> "Aufnahme-Code falsch"
#
# Nutze:
# if / else

code = input("Aufnahme-Code: ")

# Dein Code



# ============================================
# Aufgabe 5 — Gesundheitswert
# ============================================

# Frage nach dem Gesundheitswert eines Tieres.
#
# Unter 40:
# Ausgabe -> "Tier muss zum Tierarzt"
#
# Sonst:
# Ausgabe -> "Tier ist stabil"
#
# Nutze:
# Operatoren
# if / else

gesundheit = int(input("Gesundheitswert: "))

# Dein Code



# ============================================
# Aufgabe 6 — Zufällige Tierankunft
# ============================================

# Nutze random.
#
# Eine zufällige Zahl zwischen 1 und 6 entscheidet über die Ankunft.
#
# Wenn die Zahl 6 ist:
# Ausgabe -> "Notfalltier angekommen"
#
# Sonst:
# Ausgabe -> "Normale Tieraufnahme"
#
# Nutze:
# random
# if / else

import random

ankunft = random.randint(1, 6)

print(ankunft)

# Dein Code



# ============================================
# Aufgabe 7 — Impfpass vorhanden
# ============================================

# Frage:
# - Ist ein Impfpass vorhanden? (ja/nein)
#
# Wenn ja:
# Ausgabe -> "Tier kann direkt aufgenommen werden"
#
# Sonst:
# Ausgabe -> "Impfstatus muss geprüft werden"

impfpass = input("Impfpass vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 8 — Aufnahme ins Tierheim
# ============================================

# Frage:
# - Freie Plätze
# - Ist ein Impfpass vorhanden? (ja/nein)
#
# Wenn freie Plätze >= 1:
#
#     Wenn Impfpass == ja:
#     Ausgabe -> "Tier wird aufgenommen"
#
#     Sonst:
#     Ausgabe -> "Tier kommt zuerst in die Quarantäne"
#
# Sonst:
# Ausgabe -> "Keine freien Plätze vorhanden"
#
# Nutze:
# nested ifs

plaetze = int(input("Freie Plätze: "))
impfpass = input("Impfpass vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 9 — Zufälliges Tier
# ============================================

# Nutze random.
#
# Zufällig erscheint:
# - Hund
# - Katze
# - Kaninchen
#
# Je nach Tier:
# unterschiedliche Ausgabe
#
# Nutze:
# random
# if / elif / else

import random

tier = random.choice(["Hund", "Katze", "Kaninchen"])

print(tier)

# Dein Code



# ============================================
# Aufgabe 10 — Adoptionsname prüfen
# ============================================

# Frage nach dem Namen einer adoptierenden Person.
#
# Wenn der Name länger als 10 Zeichen ist:
# Ausgabe -> "Sehr langer Name im Antrag"
#
# Wenn der Name länger als 5 Zeichen ist:
# Ausgabe -> "Name akzeptiert"
#
# Sonst:
# Ausgabe -> "Name sehr kurz"
#
# Nutze:
# len()
# if / elif / else

adoptionsname = input("Name der adoptierenden Person: ")

# Dein Code



# ============================================
# Aufgabe 11 — Vermittlung prüfen
# ============================================

# Frage:
# - Alter des Tieres
# - Gesundheitswert
#
# Wenn Alter >= 1:
#
#     Wenn Gesundheitswert >= 60:
#     Ausgabe -> "Tier kann vermittelt werden"
#
#     Sonst:
#     Ausgabe -> "Tier braucht zuerst Behandlung"
#
# Sonst:
# Ausgabe -> "Tier ist noch zu jung für die Vermittlung"
#
# Nutze:
# nested ifs
# Operatoren

alter = int(input("Alter des Tieres: "))
gesundheit = int(input("Gesundheitswert: "))

# Dein Code



# ============================================
# Aufgabe 12 — Tierarzt-Notfall
# ============================================

# Nutze random.
#
# Der Zustand des Tieres ist zufällig:
# - stabil
# - verletzt
# - kritisch
#
# Frage zusätzlich nach der Anzahl freier Tierarzt-Termine.
#
# Je nach Kombination:
# unterschiedliche Ergebnisse
#
# Beispiel:
#
# Wenn Zustand kritisch UND Termine unter 1:
# Ausgabe -> "Externe Tierklinik kontaktieren"
#
# Nutze:
# random
# nested ifs
# Operatoren

import random

zustand = random.choice(["stabil", "verletzt", "kritisch"])

print("Zustand:", zustand)

termine = int(input("Freie Tierarzt-Termine: "))

# Dein Code



# ============================================
# Aufgabe 13 — Chipnummer-Rätsel
# ============================================

# Erzeuge eine Zufallszahl zwischen 1 und 10.
#
# Der Benutzer muss die richtige Chipnummer raten.
#
# Wenn richtig:
# Ausgabe -> "Chipnummer gefunden"
#
# Sonst:
# Ausgabe -> "Falsche Chipnummer"
#
# Bonus:
# Wenn die Zahl nur um 1 daneben liegt:
# Ausgabe -> "Fast richtig"
#
# Nutze:
# random
# if / elif / else
# Operatoren

import random

chipnummer = random.randint(1, 10)

tipp = int(input("Rate die Chipnummer: "))

# Dein Code



# ============================================
# Aufgabe 14 — Die Tierheim-Prüfung
# ============================================

# Frage:
# - Mitarbeitername
# - Freie Plätze
# - Futterportionen
# - Ist ein Impfpass vorhanden? (ja/nein)
#
# Wenn der Mitarbeitername länger als 6 Zeichen:
# Ausgabe -> "Mitarbeitername akzeptiert"
#
# Wenn freie Plätze >= 1:
#
#     Wenn Futterportionen >= 20:
#
#         Wenn Impfpass == ja:
#         Ausgabe -> "Tierheim-Prüfung bestanden"
#
#         Sonst:
#         Ausgabe -> "Impfpass fehlt"
#
#     Sonst:
#     Ausgabe -> "Nicht genug Futter"
#
# Sonst:
# Ausgabe -> "Keine freien Plätze"
#
# Nutze:
# len()
# nested ifs
# Operatoren

mitarbeitername = input("Mitarbeitername: ")
plaetze = int(input("Freie Plätze: "))
futter = int(input("Futterportionen: "))
impfpass = input("Impfpass vorhanden? ")

# Dein Code



# ============================================
# Aufgabe 15 — Tierheim-Finale
# ============================================

# Erstelle dein eigenes Mini-Tierheim-Abenteuer.
#
# Nutze:
# - input()
# - random
# - len()
# - if
# - elif
# - else
# - nested ifs
# - Operatoren
#
# Anforderungen:
#
# - Mindestens 5 Entscheidungen
# - Mindestens 3 verschiedene Enden
# - Mindestens 1 Zufallsereignis
# - Mindestens 1 nested if
# - Mindestens 1 len()-Abfrage
#
# Idee:
#
# Ein neues Tier kommt im Tierheim an.
# Du prüfst freie Plätze, Futter, Gesundheit,
# Impfpass und entscheidest,
# ob das Tier aufgenommen, behandelt oder vermittelt wird.