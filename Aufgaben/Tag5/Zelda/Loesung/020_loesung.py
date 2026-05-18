# =====================================================
# DAS HYRULE-FUNKTIONSABENTEUER
# =====================================================


# AUFGABE 1 – BEGRUESSUNG
# =====================================================

# Eine Funktion wird mit "def" definiert.
# Danach kommt der Name, runde Klammern () und ein Doppelpunkt.
# Alles was eingerueckt ist, gehoert zur Funktion.
# Die Funktion tut erst etwas, wenn man sie aufruft.

def begruessung():
    print("Willkommen in Hyrule!")

begruessung()


# AUFGABE 2 – HELD BEGRUESSEN
# =====================================================

# Parameter sind Platzhalter fuer Werte, die beim Aufruf uebergeben werden.
# "name" bekommt beim Aufruf den echten Wert, z.B. "Link".
# f-Strings: geschweifte Klammern {} fuegen den Variablenwert ein.

def begruesse_held(name):
    print(f"Hallo {name}, das Koenigreich braucht dich.")

begruesse_held("Link")
begruesse_held("Zelda")
begruesse_held("Impa")


# AUFGABE 3 – SCHWERTSCHADEN BERECHNEN
# =====================================================

# Mehrere Parameter werden mit Komma getrennt.
# "return" gibt einen Wert zurueck an die aufrufende Stelle.
# Ohne return liefert die Funktion nichts (None).

def berechne_schwertschaden(angriff, rubin_bonus):
    gesamt = angriff + rubin_bonus
    return gesamt

schaden = berechne_schwertschaden(12, 5)
print(f"\nSchwertschaden: {schaden}")


# AUFGABE 4 – STARKER TREFFER
# =====================================================

# Die Funktion prueft zusaetzlich, ob der Schaden maechtig ist.
# Sie gibt den Wert zurueck UND zeigt eine Meldung an.

def berechne_schwertschaden_stark(angriff, rubin_bonus):
    gesamt = angriff + rubin_bonus
    if gesamt > 20:
        print("Starker Master-Schwert-Treffer!")
    return gesamt

schaden1 = berechne_schwertschaden_stark(10, 8)    # 18 - normal
print(f"Schwertschaden: {schaden1}")

schaden2 = berechne_schwertschaden_stark(15, 10)   # 25 - stark
print(f"Schwertschaden: {schaden2}")


# AUFGABE 5 – ITEM PRUEFEN
# =====================================================

# Die Funktion bekommt das Dictionary UND den Item-Namen als Parameter.
# Mit "in" pruefen wir, ob der Schluessel im Dictionary existiert.
# Das gibt True oder False zurueck – perfekt fuer if-Bedingungen.

def pruefe_item(inventar, item):
    if item in inventar:
        print(f"'{item}' dabei! Menge: {inventar[item]}")
    else:
        print(f"'{item}' nicht im Inventar!")

inventar = {
    "Bombe":    5,
    "Bogen":    1,
    "Heiltrank": 3
}

pruefe_item(inventar, "Bombe")      # vorhanden
pruefe_item(inventar, "Bogen")      # vorhanden
pruefe_item(inventar, "Boomerang")  # nicht vorhanden


# AUFGABE 6 – HERZEN-UP
# =====================================================

# Die Funktion nimmt den aktuellen Wert entgegen,
# erhoeht ihn um 1 und gibt den neuen Wert zurueck.
# Wichtig: Die Variable ausserhalb aendert sich NICHT automatisch.
# Deshalb speichern wir den Rueckgabewert zurueck in der Variable.

def herzen_up(herzen):
    neue_herzen = herzen + 1
    print(f"Herzcontainer gefunden! {herzen} -> {neue_herzen}")
    return neue_herzen

meine_herzen = 8
meine_herzen = herzen_up(meine_herzen)   # Rueckgabewert speichern!
print(f"Aktuelle Herzen: {meine_herzen}")


# AUFGABE 7 – GANON-KAMPF
# =====================================================

# Die Funktion bekommt Name und Schaden,
# zeigt alles an und entscheidet je nach Wert den Ausgang.

def ganon_kampf(name, schaden):
    print(f"\n{name} trifft Ganon!")
    print(f"Schaden: {schaden}")
    if schaden >= 50:
        print("Ganon wurde besiegt!")
    else:
        print("Ganon sammelt neue Kraft!")

ganon_kampf("Link", 35)   # zu wenig
ganon_kampf("Link", 55)   # Sieg


# =====================================================
# BONUS – DAS HYRULE-ABENTEUER
# =====================================================

# Alle Funktionen werden der Reihe nach aufgerufen
# und bauen aufeinander auf.

print("\n" + "=" * 40)
print("DAS ABENTEUER BEGINNT")
print("=" * 40)

# Schritt 1: Begruessung und Held vorstellen
begruessung()
begruesse_held("Link")

# Schritt 2: Herzen erhoehen
links_herzen = 8
print(f"\nStart-Herzen: {links_herzen}")
links_herzen = herzen_up(links_herzen)

# Schritt 3: Inventar pruefen
print("\n-- Inventar-Check --")
pruefe_item(inventar, "Heiltrank")
pruefe_item(inventar, "Enterhaken")   # nicht vorhanden

# Schritt 4: Schaden berechnen
# Die Herzen fliessen als Rubin-Bonus in den Schaden ein.
print("\n-- Kampfvorbereitung --")
basis  = 30
bonus  = links_herzen * 3
gesamt = berechne_schwertschaden_stark(basis, bonus)
print(f"Gesamter Schwertschaden: {gesamt}")

# Schritt 5: Bosskampf gegen Ganon
ganon_kampf("Link", gesamt)

print("\n-- Hyrule ist gerettet. --")