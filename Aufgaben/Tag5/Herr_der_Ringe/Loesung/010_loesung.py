# =====================================================
# DAS INVENTAR VON MITTELERDE
# =====================================================


# =====================================================
# TEIL 1 – Dictionary erstellen
# =====================================================

# Ein Dictionary speichert Schluessel-Wert-Paare: { schluessel: wert }
# Geschweifte Klammern {}, Doppelpunkt zwischen Schluessel und Wert,
# Komma zwischen den Eintraegen.

reisegepaeck = {
    "Lembasbrot":  6,
    "Elbenseil":   1,
    "Heilkraeuter": 3,
    "Goldring":    1
}

print("=== TEIL 1: Reisegepaeck ===")
print(reisegepaeck)


# =====================================================
# TEIL 2 – Gegenstaende benutzen
# =====================================================

# reisegepaeck["Schluessel"] greift auf den Wert zu.
# -= zieht den Betrag direkt ab und speichert das Ergebnis.
# reisegepaeck["Lembasbrot"] -= 2  ist dasselbe wie:
# reisegepaeck["Lembasbrot"] = reisegepaeck["Lembasbrot"] - 2

reisegepaeck["Lembasbrot"]   -= 2   # 6 - 2 = 4
reisegepaeck["Heilkraeuter"] -= 1   # 3 - 1 = 2

print("\n=== TEIL 2: Nach dem Benutzen ===")
print(f"Lembasbrot:   {reisegepaeck['Lembasbrot']}")
print(f"Heilkraeuter: {reisegepaeck['Heilkraeuter']}")


# =====================================================
# TEIL 3 – Neuen Gegenstand hinzufuegen
# =====================================================

# Einen neuen Eintrag erstellt man genau wie beim Aendern:
# einfach den neuen Schluessel zuweisen.
# Gibt es den Schluessel noch nicht -> wird er neu angelegt.
# Gibt es ihn schon -> wird der Wert ueberschrieben.

reisegepaeck["Zwergenaxt"] = 1

print("\n=== TEIL 3: Zwergenaxt hinzugefuegt ===")
print(reisegepaeck)


# =====================================================
# TEIL 4 – Pruefen ob ein Schluessel existiert
# =====================================================

# "in" prueft, ob ein Schluessel im Dictionary vorhanden ist.
# Ergebnis: True oder False – direkt nutzbar in if-Bedingungen.

print("\n=== TEIL 4: Elbenseil-Check ===")
if "Elbenseil" in reisegepaeck:
    print("Der Abstieg kann beginnen!")
else:
    print("Kein Elbenseil dabei!")


# =====================================================
# TEIL 5 – Eintrag entfernen
# =====================================================

# del loescht einen Schluessel samt Wert komplett aus dem Dictionary.
# Nach dem Loeschen existiert der Schluessel nicht mehr.
# Tipp: .pop("Schluessel") macht dasselbe,
#        gibt aber zusaetzlich den geloeschten Wert zurueck.

del reisegepaeck["Goldring"]

print("\n=== TEIL 5: Goldring verloren ===")
print("Reisegepaeck danach:", reisegepaeck)


# =====================================================
# BONUS – Verschachteltes Dictionary
# =====================================================

# Ein Dictionary kann als Wert ein anderes Dictionary enthalten.
# Das nennt sich verschachtelt (nested dictionary).
# So laesst sich ein vollstaendiges Helden-Profil abbilden.

held = {
    "name":    "Frodon",
    "level":   20,
    "inventar": reisegepaeck    # Das reisegepaeck-Dictionary von oben.
}

print("\n=== BONUS: Helden-Profil ===")
print(f"Name:     {held['name']}")
print(f"Level:    {held['level']}")
print(f"Inventar: {held['inventar']}")

# Auf verschachtelte Werte zugreifen:
# Erst aeusserer Schluessel -> dann innerer Schluessel.
print(f"\nLembasbrot von {held['name']}: {held['inventar']['Lembasbrot']}")
print(f"Elbenseil von {held['name']}: {held['inventar']['Elbenseil']}")