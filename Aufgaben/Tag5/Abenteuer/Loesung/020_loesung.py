# =====================================================
# DAS ABENTEUER DER FUNKTIONEN
# =====================================================


# =====================================================
# AUFGABE 1 – DIE BEGRÜSSUNG
# =====================================================

# Eine Funktion wird mit "def" definiert.
# Danach kommt der Name, dann runde Klammern () und ein Doppelpunkt.
# Alles, was zur Funktion gehört, wird eingerückt.
# Die Funktion tut erst etwas, wenn man sie AUFRUFT.

def begruessung():
    print("Willkommen in den vergessenen Ruinen!")

# Funktion aufrufen: Name + ()
begruessung()


# =====================================================
# AUFGABE 2 – DER HELD
# =====================================================

# Parameter sind Platzhalter für Werte, die beim Aufruf übergeben werden.
# Hier ist "name" der Parameter.
# Beim Aufruf z.B. begruesse_held("Arkon") bekommt name den Wert "Arkon".

def begruesse_held(name):
    print(f"Hallo {name}, dein Abenteuer beginnt!")

begruesse_held("Arkon")
begruesse_held("Zelda")
begruesse_held("Gimli")


# =====================================================
# AUFGABE 3 – DAS KAMPFSYSTEM
# =====================================================

# Eine Funktion kann mehrere Parameter haben – hier: angriff und bonus.
# "return" gibt einen Wert zurück an die Stelle, von der die Funktion aufgerufen wurde.
# Ohne return gibt die Funktion nichts zurück (None).

def berechne_schaden(angriff, bonus):
    gesamt = angriff + bonus
    return gesamt

# Den Rückgabewert können wir in einer Variable speichern.
schaden = berechne_schaden(12, 5)
print(f"\nBerechneter Schaden: {schaden}")


# =====================================================
# AUFGABE 4 – KRITISCHER TREFFER
# =====================================================

# Wir erweitern die Funktion um eine if-Bedingung.
# Die Funktion gibt den Schaden zurück UND prüft nebenbei, ob es ein Krit ist.

def berechne_schaden_krit(angriff, bonus):
    gesamt = angriff + bonus
    if gesamt > 20:
        print("Kritischer Treffer!")
    return gesamt

schaden1 = berechne_schaden_krit(12, 5)   # 17 → kein Krit
print(f"Schaden: {schaden1}")

schaden2 = berechne_schaden_krit(18, 8)   # 26 → Kritischer Treffer!
print(f"Schaden: {schaden2}")


# =====================================================
# AUFGABE 5 – DAS INVENTAR
# =====================================================

# Wir übergeben das Dictionary UND den gesuchten Item-Namen als Parameter.
# Mit "in" prüfen wir, ob der Schlüssel im Dictionary existiert.

def pruefe_item(inventar, item):
    if item in inventar:
        print(f"'{item}' gefunden! Menge: {inventar[item]}")
    else:
        print(f"'{item}' nicht im Inventar!")

inventar = {
    "Schwert": 1,
    "Heiltrank": 3
}

pruefe_item(inventar, "Schwert")     # vorhanden
pruefe_item(inventar, "Heiltrank")   # vorhanden
pruefe_item(inventar, "Bombe")       # nicht vorhanden


# =====================================================
# AUFGABE 6 – LEVEL-UP
# =====================================================

# Die Funktion nimmt den aktuellen Level entgegen,
# erhöht ihn um 1 und gibt den neuen Wert zurück.
# Wichtig: Die Variable außerhalb der Funktion ändert sich NICHT automatisch.
# Deshalb speichern wir den Rückgabewert wieder in der Variable.

def level_up(level):
    neues_level = level + 1
    print(f"Level Up! {level} → {neues_level}")
    return neues_level

mein_level = 5
mein_level = level_up(mein_level)   # Rückgabewert zurückspeichern!
print(f"Aktuelles Level: {mein_level}")


# =====================================================
# AUFGABE 7 – DER BOSSKAMPF
# =====================================================

# Die Funktion bekommt Name und Schaden, zeigt alles an
# und entscheidet je nach Schadenswert, ob der Boss besiegt wurde.

def bosskampf(name, schaden):
    print(f"\n{name} greift den Drachenwächter an!")
    print(f"Verursachter Schaden: {schaden}")
    if schaden >= 50:
        print("Der Drachenwächter wurde besiegt!")
    else:
        print("Der Drachenwächter kämpft weiter!")

bosskampf("Arkon", 35)   # zu wenig Schaden
bosskampf("Arkon", 55)   # Sieg!


# =====================================================
# BONUS-CHALLENGE – DAS TEXT-ABENTEUER
# =====================================================

# Hier rufen wir alle Funktionen hintereinander auf
# und bauen daraus eine kleine Geschichte.

print("\n" + "=" * 45)
print("       DAS ABENTEUER BEGINNT")
print("=" * 45)

# Schritt 1: Spieler begrüßen
begruessung()
begruesse_held("Arkon")

# Schritt 2: Level anzeigen und erhöhen
print("\n[VORBEREITUNG]")
arkon_level = 5
print(f"Startlevel: {arkon_level}")
arkon_level = level_up(arkon_level)

# Schritt 3: Inventar prüfen
print("\n[INVENTAR-CHECK]")
arkon_inventar = {
    "Schwert": 1,
    "Heiltrank": 2,
    "Schild": 1
}
pruefe_item(arkon_inventar, "Schwert")
pruefe_item(arkon_inventar, "Bogen")   # nicht vorhanden

# Schritt 4: Schaden berechnen
print("\n[KAMPFVORBEREITUNG]")
basis_angriff = 30
level_bonus = arkon_level * 2        # Level beeinflusst den Bonus
gesamt_schaden = berechne_schaden_krit(basis_angriff, level_bonus)
print(f"Gesamtschaden für den Bosskampf: {gesamt_schaden}")

# Schritt 5: Bosskampf starten
bosskampf("Arkon", gesamt_schaden)

print("\n[ENDE] Das Abenteuer ist abgeschlossen!")