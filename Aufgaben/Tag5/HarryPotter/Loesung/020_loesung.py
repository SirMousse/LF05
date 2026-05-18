# =====================================================
# DAS ZAUBERER-FUNKTIONSLABOR
# =====================================================


# =====================================================
# AUFGABE 1 – DIE ZAUBERER-BEGRUESSUNG
# =====================================================

# Eine Funktion wird mit "def" definiert.
# Danach kommt der Name, runde Klammern () und ein Doppelpunkt.
# Alles was eingerueckt ist, gehoert zur Funktion.
# Die Funktion tut erst etwas, wenn man sie aufruft.

def begruessung():
    print("Willkommen in Hogwarts!")

begruessung()


# =====================================================
# AUFGABE 2 – DER SCHUELER
# =====================================================

# Parameter sind Platzhalter fuer Werte, die beim Aufruf uebergeben werden.
# "name" bekommt beim Aufruf den echten Wert, z.B. "Luna".
# f-Strings: geschweifte Klammern {} fuegen den Variablenwert in den Text ein.

def begruesse_schueler(name):
    print(f"Hallo {name}, bereit fuer den Zauberunterricht?")

begruesse_schueler("Luna")
begruesse_schueler("Hermine")
begruesse_schueler("Neville")


# =====================================================
# AUFGABE 3 – ZAUBERKRAFT BERECHNEN
# =====================================================

# Mehrere Parameter werden mit Komma getrennt.
# "return" gibt einen Wert zurueck an die aufrufende Stelle.
# Ohne return liefert die Funktion nichts (None).

def berechne_zauberkraft(zauber, bonus):
    gesamt = zauber + bonus
    return gesamt

kraft = berechne_zauberkraft(12, 5)
print(f"\nZauberkraft: {kraft}")


# =====================================================
# AUFGABE 4 – MAECHTIGER ZAUBER
# =====================================================

# Die Funktion prueft zusaetzlich, ob die Kraft maechtig ist.
# Sie gibt den Wert zurueck UND zeigt eine Meldung an.

def berechne_zauberkraft_stark(zauber, bonus):
    gesamt = zauber + bonus
    if gesamt > 20:
        print("Maechtiger Zauber!")
    return gesamt

kraft1 = berechne_zauberkraft_stark(10, 8)    # 18 - normal
print(f"Zauberkraft: {kraft1}")

kraft2 = berechne_zauberkraft_stark(15, 10)   # 25 - maechtig
print(f"Zauberkraft: {kraft2}")


# =====================================================
# AUFGABE 5 – DER ZAUBERRUCKSACK
# =====================================================

# Die Funktion bekommt das Dictionary UND den Item-Namen als Parameter.
# Mit "in" pruefen wir, ob der Schluessel im Dictionary existiert.
# Das gibt True oder False zurueck – perfekt fuer if-Bedingungen.

def pruefe_item(inventar, item):
    if item in inventar:
        print(f"'{item}' gefunden! Menge: {inventar[item]}")
    else:
        print(f"'{item}' nicht im Rucksack!")

inventar = {
    "Zauberstab":   1,
    "Heiltrank":    2,
    "Schokofrosch": 5
}

pruefe_item(inventar, "Zauberstab")     # vorhanden
pruefe_item(inventar, "Heiltrank")      # vorhanden
pruefe_item(inventar, "Schokofrosch")   # vorhanden
pruefe_item(inventar, "Unsichtbarkeitsumhang")  # nicht vorhanden


# =====================================================
# AUFGABE 6 – ZAUBERER-LEVEL
# =====================================================

# Die Funktion nimmt den aktuellen Level entgegen,
# erhoeht ihn um 1 und gibt den neuen Wert zurueck.
# Wichtig: Die Variable ausserhalb aendert sich NICHT automatisch.
# Deshalb speichern wir den Rueckgabewert zurueck in der Variable.

def level_up(level):
    neues_level = level + 1
    print(f"Level Up! {level} -> {neues_level}")
    return neues_level

mein_level = 4
mein_level = level_up(mein_level)   # Rueckgabewert zurueckspeichern!
print(f"Aktuelles Level: {mein_level}")


# =====================================================
# AUFGABE 7 – DAS ZAUBERDUELL
# =====================================================

# Die Funktion bekommt Name und Zauberkraft,
# zeigt alles an und entscheidet je nach Wert den Ausgang.

def zauberduell(name, zauberkraft):
    print(f"\n{name} setzt ihren Zauber ein!")
    print(f"Zauberkraft: {zauberkraft}")
    if zauberkraft >= 50:
        print("Das Duell wurde gewonnen!")
    else:
        print("Der Gegner blockt den Zauber!")

zauberduell("Luna", 35)    # zu schwach
zauberduell("Luna", 55)    # Sieg


# =====================================================
# BONUS – ALLES KOMBINIERT
# =====================================================

# Alle Funktionen werden der Reihe nach aufgerufen
# und bauen aufeinander auf.

print("\n" + "=" * 40)
print("ZAUBERUNTERRICHT BEGINNT")
print("=" * 40)

# Schritt 1: Begruessung und Schueler vorstellen
begruessung()
begruesse_schueler("Luna")

# Schritt 2: Level erhoehen
luna_level = 4
print(f"\nStartlevel: {luna_level}")
luna_level = level_up(luna_level)

# Schritt 3: Rucksack pruefen
print("\n-- Rucksack-Check --")
pruefe_item(inventar, "Zauberstab")
pruefe_item(inventar, "Marauders Map")   # nicht vorhanden

# Schritt 4: Zauberkraft berechnen
# Das Level fliesst als Bonus in die Zauberkraft ein.
print("\n-- Duellvorbereitung --")
basis = 30
bonus = luna_level * 3
gesamt_kraft = berechne_zauberkraft_stark(basis, bonus)
print(f"Gesamte Zauberkraft: {gesamt_kraft}")

# Schritt 5: Duell starten
zauberduell("Luna", gesamt_kraft)

print("\n-- Unterricht beendet --")