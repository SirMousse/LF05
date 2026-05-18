# =====================================================
# DAS ABENTEUER-INVENTAR
# =====================================================


# =====================================================
# TEIL 1 – Dictionary erstellen
# =====================================================

# Ein Dictionary speichert Schlüssel-Wert-Paare: { schlüssel: wert }
# Die geschweiften Klammern {} machen es zu einem Dictionary.
# Zwischen Schlüssel und Wert steht ein Doppelpunkt :
# Einträge werden mit Komma getrennt.

rucksack = {
    "Seil": 2,
    "Fackel": 5,
    "Heiltrank": 3,
    "Goldmünze": 20
}

print("=== TEIL 1: Rucksack gepackt ===")
print(rucksack)


# =====================================================
# TEIL 2 – Gegenstände benutzen
# =====================================================

# inventar["Schlüssel"] greift auf den Wert zu.
# -= subtrahiert den Betrag direkt vom gespeicherten Wert.
# inventar["Fackel"] -= 1  ist dasselbe wie:
# inventar["Fackel"] = inventar["Fackel"] - 1

rucksack["Fackel"] -= 1      # 5 - 1 = 4
rucksack["Heiltrank"] -= 1   # 3 - 1 = 2

print("\n=== TEIL 2: Nach dem Benutzen ===")
print(f"Fackeln übrig:   {rucksack['Fackel']}")
print(f"Heiltränke übrig: {rucksack['Heiltrank']}")


# =====================================================
# TEIL 3 – Neuen Gegenstand hinzufügen
# =====================================================

# Einen neuen Eintrag erstellt man genau wie beim Ändern:
# einfach den neuen Schlüssel zuweisen.
# Gibt es den Schlüssel noch nicht → wird er neu angelegt.
# Gibt es ihn schon → wird der Wert überschrieben.

rucksack["Magischer Schlüssel"] = 1

print("\n=== TEIL 3: Magischer Schlüssel gefunden ===")
print(rucksack)


# =====================================================
# TEIL 4 – Prüfen ob ein Schlüssel existiert
# =====================================================

# "in" prüft, ob ein Schlüssel im Dictionary vorhanden ist.
# Ergebnis: True oder False – direkt nutzbar in if-Bedingungen.

print("\n=== TEIL 4: Seil-Check ===")
if "Seil" in rucksack:
    print("Das Seil kann für den Abstieg benutzt werden!")
else:
    print("Kein Seil im Rucksack!")


# =====================================================
# TEIL 5 – Eintrag entfernen
# =====================================================

# del löscht einen Schlüssel samt Wert komplett aus dem Dictionary.
# Nach dem Löschen existiert der Schlüssel nicht mehr.
# Tipp: .pop("Schlüssel") macht dasselbe, gibt aber den Wert noch zurück.

del rucksack["Goldmünze"]

print("\n=== TEIL 5: Goldmünzen gestohlen! ===")
print("Rucksack nach dem Diebstahl:", rucksack)


# =====================================================
# BONUS – Verschachteltes Dictionary
# =====================================================

# Ein Dictionary kann als Wert ein anderes Dictionary enthalten.
# Das nennt man verschachtelt (nested dictionary).
# So lassen sich vollständige Spieler-Profile abbilden.

spieler = {
    "name": "Arkon",
    "level": 12,
    "inventar": rucksack    # Das rucksack-Dictionary von oben wird eingebaut!
}

print("\n=== BONUS: Spielerprofil ===")
print(f"Name:   {spieler['name']}")
print(f"Level:  {spieler['level']}")
print(f"Items:  {spieler['inventar']}")

# Auf verschachtelte Werte zugreifen:
# Erst äußerer Schlüssel → dann innerer Schlüssel.
print(f"\nSeile von {spieler['name']}: {spieler['inventar']['Seil']}")
print(f"Magische Schlüssel von {spieler['name']}: {spieler['inventar']['Magischer Schlüssel']}")