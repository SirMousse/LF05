# =====================================================
# DIE FUNKTIONEN VON MITTELERDE
# =====================================================


# AUFGABE 1 – BEGRUESSUNG
# =====================================================

# Eine Funktion wird mit "def" definiert.
# Danach kommt der Name, runde Klammern () und ein Doppelpunkt.
# Alles was eingerueckt ist, gehoert zur Funktion.
# Die Funktion tut erst etwas, wenn man sie aufruft.

def begruessung():
    print("Willkommen in Mittelerde!")

begruessung()


# AUFGABE 2 – GEFAEHRTE BEGRUESSEN
# =====================================================

# Parameter sind Platzhalter fuer Werte, die beim Aufruf uebergeben werden.
# "name" bekommt beim Aufruf den echten Wert, z.B. "Frodo".
# f-Strings: geschweifte Klammern {} fuegen den Variablenwert in den Text ein.

def begruesse_gefaehrte(name):
    print(f"Hallo {name}, die Reise zum Schicksalsberg beginnt!")

begruesse_gefaehrte("Frodo")
begruesse_gefaehrte("Samweis")
begruesse_gefaehrte("Aragorn")


# AUFGABE 3 – KAMPFKRAFT BERECHNEN
# =====================================================

# Mehrere Parameter werden mit Komma getrennt.
# "return" gibt einen Wert zurueck an die aufrufende Stelle.
# Ohne return liefert die Funktion nichts (None).

def berechne_kampfkraft(angriff, mut_bonus):
    gesamt = angriff + mut_bonus
    return gesamt

kraft = berechne_kampfkraft(12, 5)
print(f"\nKampfkraft: {kraft}")


# AUFGABE 4 – MAECHTIGER SCHLAG
# =====================================================

# Die Funktion prueft zusaetzlich, ob die Kraft maechtig ist.
# Sie gibt den Wert zurueck UND zeigt eine Meldung an.

def berechne_kampfkraft_stark(angriff, mut_bonus):
    gesamt = angriff + mut_bonus
    if gesamt > 20:
        print("Maechtiger Schlag gegen Mordor!")
    return gesamt

kraft1 = berechne_kampfkraft_stark(10, 8)    # 18 - normal
print(f"Kampfkraft: {kraft1}")

kraft2 = berechne_kampfkraft_stark(15, 10)   # 25 - maechtig
print(f"Kampfkraft: {kraft2}")


# AUFGABE 5 – ITEM PRUEFEN
# =====================================================

# Die Funktion bekommt das Dictionary UND den Item-Namen als Parameter.
# Mit "in" pruefen wir, ob der Schluessel im Dictionary existiert.
# Das gibt True oder False zurueck – perfekt fuer if-Bedingungen.

def pruefe_item(inventar, item):
    if item in inventar:
        print(f"'{item}' dabei! Menge: {inventar[item]}")
    else:
        print(f"'{item}' nicht im Gepaeck!")

inventar = {
    "Lembasbrot": 4,
    "Elbenseil":  1,
    "Schwert":    1
}

pruefe_item(inventar, "Lembasbrot")   # vorhanden
pruefe_item(inventar, "Elbenseil")    # vorhanden
pruefe_item(inventar, "Zauberstab")   # nicht vorhanden


# AUFGABE 6 – LEVEL-UP
# =====================================================

# Die Funktion nimmt den aktuellen Level entgegen,
# erhoeht ihn um 1 und gibt den neuen Wert zurueck.
# Wichtig: Die Variable ausserhalb aendert sich NICHT automatisch.
# Deshalb speichern wir den Rueckgabewert zurueck in der Variable.

def level_up(level):
    neues_level = level + 1
    print(f"Level Up! {level} -> {neues_level}")
    return neues_level

mein_level = 7
mein_level = level_up(mein_level)   # Rueckgabewert zurueckspeichern!
print(f"Aktuelles Level: {mein_level}")


# AUFGABE 7 – KAMPF GEGEN ORC
# =====================================================

# Die Funktion bekommt Name und Kampfkraft,
# zeigt alles an und entscheidet je nach Wert den Ausgang.

def kampf_gegen_orc(name, kampfkraft):
    print(f"\n{name} kaempft gegen einen Orc!")
    print(f"Kampfkraft: {kampfkraft}")
    if kampfkraft >= 50:
        print("Der Orc wurde besiegt!")
    else:
        print("Der Orc greift weiter an!")

kampf_gegen_orc("Frodo",   35)   # zu schwach
kampf_gegen_orc("Aragorn", 55)   # Sieg


# =====================================================
# BONUS – DAS MITTELERDE-ABENTEUER
# =====================================================

# Alle Funktionen werden der Reihe nach aufgerufen
# und bauen aufeinander auf.

print("\n" + "=" * 40)
print("DIE REISE BEGINNT")
print("=" * 40)

# Schritt 1: Begruessung und Gefaehrte vorstellen
begruessung()
begruesse_gefaehrte("Frodo")

# Schritt 2: Level erhoehen
frodo_level = 7
print(f"\nStartlevel: {frodo_level}")
frodo_level = level_up(frodo_level)

# Schritt 3: Gepaeck pruefen
print("\n-- Gepaeck-Check --")
pruefe_item(inventar, "Schwert")
pruefe_item(inventar, "Mithrilruestung")   # nicht vorhanden

# Schritt 4: Kampfkraft berechnen
# Das Level fliesst als Bonus in die Kampfkraft ein.
print("\n-- Kampfvorbereitung --")
basis     = 30
mut_bonus = frodo_level * 3
gesamt_kraft = berechne_kampfkraft_stark(basis, mut_bonus)
print(f"Gesamte Kampfkraft: {gesamt_kraft}")

# Schritt 5: Kampf starten
kampf_gegen_orc("Frodo", gesamt_kraft)

print("\n-- Die Reise geht weiter... --")