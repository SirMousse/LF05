# =====================================================
# DAS TIERHEIM-FUNKTIONS-SYSTEM
# =====================================================


# AUFGABE 1 – BEGRUESSUNG
# =====================================================

# Eine Funktion wird mit "def" definiert.
# Danach kommt der Name, runde Klammern () und ein Doppelpunkt.
# Alles was eingerueckt ist, gehoert zur Funktion.
# Die Funktion tut erst etwas, wenn man sie aufruft.

def begruessung():
    print("Willkommen im Tierheim-System!")

begruessung()


# AUFGABE 2 – PFLEGER BEGRUESSEN
# =====================================================

# Parameter sind Platzhalter fuer Werte, die beim Aufruf uebergeben werden.
# "name" bekommt beim Aufruf den echten Wert, z.B. "Mia".
# f-Strings: geschweifte Klammern {} fuegen den Variablenwert ein.

def begruesse_pfleger(name):
    print(f"Hallo {name}, die Tiere warten auf dich.")

begruesse_pfleger("Mia")
begruesse_pfleger("Jonas")
begruesse_pfleger("Sara")


# AUFGABE 3 – PFLEGEPUNKTE BERECHNEN
# =====================================================

# Mehrere Parameter werden mit Komma getrennt.
# "return" gibt einen Wert zurueck an die aufrufende Stelle.
# Ohne return liefert die Funktion nichts (None).

def berechne_pflegepunkte(futter, liebe_bonus):
    gesamt = futter + liebe_bonus
    return gesamt

punkte = berechne_pflegepunkte(12, 5)
print(f"\nPflegepunkte: {punkte}")


# AUFGABE 4 – SEHR GLUECKLICH
# =====================================================

# Die Funktion prueft zusaetzlich, ob die Tiere besonders gluecklich sind.
# Sie gibt den Wert zurueck UND zeigt eine Meldung an.

def berechne_pflegepunkte_stark(futter, liebe_bonus):
    gesamt = futter + liebe_bonus
    if gesamt > 20:
        print("Die Tiere sind sehr gluecklich!")
    return gesamt

punkte1 = berechne_pflegepunkte_stark(10, 8)    # 18 - normal
print(f"Pflegepunkte: {punkte1}")

punkte2 = berechne_pflegepunkte_stark(15, 10)   # 25 - sehr gluecklich
print(f"Pflegepunkte: {punkte2}")


# AUFGABE 5 – ITEM PRUEFEN
# =====================================================

# Die Funktion bekommt das Dictionary UND den Item-Namen als Parameter.
# Mit "in" pruefen wir, ob der Schluessel im Dictionary existiert.
# Das gibt True oder False zurueck – perfekt fuer if-Bedingungen.

def pruefe_item(lager, item):
    if item in lager:
        print(f"'{item}' vorratig! Menge: {lager[item]}")
    else:
        print(f"'{item}' nicht im Lager!")

lager = {
    "Katzenfutter": 10,
    "Decken":        5,
    "Spielzeug":     8
}

pruefe_item(lager, "Katzenfutter")   # vorhanden
pruefe_item(lager, "Decken")         # vorhanden
pruefe_item(lager, "Medikamente")    # nicht vorhanden


# AUFGABE 6 – ERFAHRUNG-UP
# =====================================================

# Die Funktion nimmt den aktuellen Wert entgegen,
# erhoeht ihn um 1 und gibt den neuen Wert zurueck.
# Wichtig: Die Variable ausserhalb aendert sich NICHT automatisch.
# Deshalb speichern wir den Rueckgabewert zurueck in der Variable.

def erfahrung_up(erfahrung):
    neue_erfahrung = erfahrung + 1
    print(f"Erfahrung gestiegen: {erfahrung} -> {neue_erfahrung}")
    return neue_erfahrung

meine_erfahrung = 5
meine_erfahrung = erfahrung_up(meine_erfahrung)   # Rueckgabewert speichern!
print(f"Aktuelle Erfahrung: {meine_erfahrung}")


# AUFGABE 7 – TIER VERSORGEN
# =====================================================

# Die Funktion bekommt Name und Pflegepunkte,
# zeigt alles an und entscheidet je nach Wert den Ausgang.

def tier_versorgen(name, pflegepunkte):
    print(f"\n{name} startet die Pflegerunde!")
    print(f"Pflegepunkte: {pflegepunkte}")
    if pflegepunkte >= 50:
        print("Alle Tiere wurden erfolgreich versorgt!")
    else:
        print("Einige Tiere brauchen noch Hilfe.")

tier_versorgen("Mia",  35)   # zu wenig
tier_versorgen("Mia",  55)   # Erfolg


# =====================================================
# BONUS – DAS TIERHEIM-PROGRAMM
# =====================================================

# Alle Funktionen werden der Reihe nach aufgerufen
# und bauen aufeinander auf.

print("\n" + "=" * 40)
print("TIERHEIM-SCHICHT BEGINNT")
print("=" * 40)

# Schritt 1: Begruessung und Pfleger vorstellen
begruessung()
begruesse_pfleger("Mia")

# Schritt 2: Erfahrung erhoehen
aktuelle_erfahrung = 5
print(f"\nStart-Erfahrung: {aktuelle_erfahrung}")
aktuelle_erfahrung = erfahrung_up(aktuelle_erfahrung)

# Schritt 3: Lager pruefen
print("\n-- Lager-Check --")
pruefe_item(lager, "Spielzeug")
pruefe_item(lager, "Tierarzt-Kit")   # nicht vorhanden

# Schritt 4: Pflegepunkte berechnen
# Die Erfahrung fliesst als Liebe-Bonus in die Pflegepunkte ein.
print("\n-- Pflege-Vorbereitung --")
futter = 30
liebe  = aktuelle_erfahrung * 4
gesamt = berechne_pflegepunkte_stark(futter, liebe)
print(f"Gesamte Pflegepunkte: {gesamt}")

# Schritt 5: Tiere versorgen
tier_versorgen("Mia", gesamt)

print("\n-- Alle Tiere versorgt. Feierabend! --")