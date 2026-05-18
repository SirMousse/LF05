# =====================================================
# DAS POKEMON-FUNKTIONSLABOR
# =====================================================


# AUFGABE 1 – TRAINER-BEGRUESSUNG
# =====================================================

# Eine Funktion wird mit "def" definiert.
# Danach kommt der Name, runde Klammern () und ein Doppelpunkt.
# Alles was eingerueckt ist, gehoert zur Funktion.
# Die Funktion tut erst etwas, wenn man sie aufruft.

def begruessung():
    print("Willkommen im Pokemon-Center!")

begruessung()


# AUFGABE 2 – TRAINER STARTEN
# =====================================================

# Parameter sind Platzhalter fuer Werte, die beim Aufruf uebergeben werden.
# "name" bekommt beim Aufruf den echten Wert, z.B. "Ash".
# f-Strings: geschweifte Klammern {} fuegen den Variablenwert ein.

def begruesse_trainer(name):
    print(f"Hallo {name}, bereit fuer den Arenakampf?")

begruesse_trainer("Ash")
begruesse_trainer("Misty")
begruesse_trainer("Brock")


# AUFGABE 3 – ATTACKEN-SYSTEM
# =====================================================

# Mehrere Parameter werden mit Komma getrennt.
# "return" gibt einen Wert zurueck an die aufrufende Stelle.
# Ohne return liefert die Funktion nichts (None).

def berechne_attacke(attacke, bonus):
    gesamt = attacke + bonus
    return gesamt

staerke = berechne_attacke(12, 5)
print(f"\nAttacken-Staerke: {staerke}")


# AUFGABE 4 – SEHR EFFEKTIV
# =====================================================

# Die Funktion prueft zusaetzlich, ob der Treffer stark ist.
# Sie gibt den Wert zurueck UND zeigt eine Meldung an.

def berechne_attacke_effektiv(attacke, bonus):
    gesamt = attacke + bonus
    if gesamt > 20:
        print("Sehr effektiver Treffer!")
    return gesamt

staerke1 = berechne_attacke_effektiv(10, 8)    # 18 - normal
print(f"Attacke: {staerke1}")

staerke2 = berechne_attacke_effektiv(15, 10)   # 25 - sehr effektiv
print(f"Attacke: {staerke2}")


# AUFGABE 5 – RUCKSACK-CHECK
# =====================================================

# Die Funktion bekommt das Dictionary UND den Item-Namen als Parameter.
# Mit "in" pruefen wir, ob der Schluessel im Dictionary existiert.
# Das gibt True oder False zurueck – perfekt fuer if-Bedingungen.

def pruefe_rucksack(rucksack, item):
    if item in rucksack:
        print(f"'{item}' im Rucksack! Menge: {rucksack[item]}")
    else:
        print(f"'{item}' nicht dabei!")

rucksack = {
    "Pokeball":   5,
    "Trank":      3,
    "Top-Beleber": 1
}

pruefe_rucksack(rucksack, "Pokeball")    # vorhanden
pruefe_rucksack(rucksack, "Trank")       # vorhanden
pruefe_rucksack(rucksack, "Hyperball")   # nicht vorhanden


# AUFGABE 6 – ORDEN SAMMELN
# =====================================================

# Die Funktion nimmt den aktuellen Wert entgegen,
# erhoeht ihn um 1 und gibt den neuen Wert zurueck.
# Wichtig: Die Variable ausserhalb aendert sich NICHT automatisch.
# Deshalb speichern wir den Rueckgabewert zurueck in der Variable.

def orden_sammeln(orden):
    neue_orden = orden + 1
    print(f"Orden erhalten! {orden} -> {neue_orden}")
    return neue_orden

meine_orden = 3
meine_orden = orden_sammeln(meine_orden)   # Rueckgabewert speichern!
print(f"Aktuelle Orden: {meine_orden}")


# AUFGABE 7 – ARENAKAMPF
# =====================================================

# Die Funktion bekommt Name und Attacken-Staerke,
# zeigt alles an und entscheidet je nach Wert den Ausgang.

def arenakampf(name, attacke):
    print(f"\n{name} setzt seine Attacke ein!")
    print(f"Attacken-Staerke: {attacke}")
    if attacke >= 50:
        print("Der Arenaleiter wurde besiegt!")
    else:
        print("Das gegnerische Pokemon kaempft weiter!")

arenakampf("Ash", 35)   # zu schwach
arenakampf("Ash", 55)   # Sieg


# =====================================================
# BONUS – ALLES KOMBINIERT
# =====================================================

# Alle Funktionen werden der Reihe nach aufgerufen
# und bauen aufeinander auf.

print("\n" + "=" * 40)
print("ARENAKAMPF BEGINNT")
print("=" * 40)

# Schritt 1: Begruessung und Trainer vorstellen
begruessung()
begruesse_trainer("Ash")

# Schritt 2: Orden erhoehen
ash_orden = 3
print(f"\nBisherige Orden: {ash_orden}")
ash_orden = orden_sammeln(ash_orden)

# Schritt 3: Rucksack pruefen
print("\n-- Rucksack-Check --")
pruefe_rucksack(rucksack, "Trank")
pruefe_rucksack(rucksack, "Volle-Erholung")   # nicht vorhanden

# Schritt 4: Attacke berechnen
# Die Orden-Zahl fliesst als Bonus in die Attacke ein.
print("\n-- Kampfvorbereitung --")
basis = 30
bonus = ash_orden * 4
gesamt = berechne_attacke_effektiv(basis, bonus)
print(f"Gesamte Attacken-Staerke: {gesamt}")

# Schritt 5: Arenakampf starten
arenakampf("Ash", gesamt)

print("\n-- Naechste Arena wartet! --")