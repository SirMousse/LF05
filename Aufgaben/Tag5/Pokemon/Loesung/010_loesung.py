# =====================================================
# DER TRAINER-RUCKSACK
# =====================================================


# =====================================================
# TEIL 1 – Dictionary erstellen
# =====================================================

# Ein Dictionary speichert Schluessel-Wert-Paare: { schluessel: wert }
# Geschweifte Klammern {}, Doppelpunkt zwischen Schluessel und Wert,
# Komma zwischen den Eintraegen.

rucksack = {
    "Pokeball":   10,
    "Trank":       5,
    "Supertrank":  2,
    "Top-Beleber": 1
}

print("=== TEIL 1: Trainer-Rucksack ===")
print(rucksack)


# =====================================================
# TEIL 2 – Gegenstaende benutzen
# =====================================================

# rucksack["Schluessel"] greift auf den Wert zu.
# -= zieht den Betrag direkt ab und speichert das Ergebnis.
# rucksack["Pokeball"] -= 1  ist dasselbe wie:
# rucksack["Pokeball"] = rucksack["Pokeball"] - 1

rucksack["Pokeball"] -= 1   # 10 - 1 = 9
rucksack["Trank"]    -= 1   #  5 - 1 = 4

print("\n=== TEIL 2: Nach dem Benutzen ===")
print(f"Pokeball: {rucksack['Pokeball']}")
print(f"Trank:    {rucksack['Trank']}")


# =====================================================
# TEIL 3 – Neuen Gegenstand hinzufuegen
# =====================================================

# Einen neuen Eintrag erstellt man genau wie beim Aendern:
# einfach den neuen Schluessel zuweisen.
# Gibt es den Schluessel noch nicht -> wird er neu angelegt.
# Gibt es ihn schon -> wird der Wert ueberschrieben.

rucksack["Hyperball"] = 3

print("\n=== TEIL 3: Hyperball erhalten ===")
print(rucksack)


# =====================================================
# TEIL 4 – Pruefen ob ein Schluessel existiert
# =====================================================

# "in" prueft, ob ein Schluessel im Dictionary vorhanden ist.
# Ergebnis: True oder False – direkt nutzbar in if-Bedingungen.

print("\n=== TEIL 4: Top-Beleber-Check ===")
if "Top-Beleber" in rucksack:
    print("Ein Pokemon kann wiederbelebt werden!")
else:
    print("Kein Top-Beleber im Rucksack!")


# =====================================================
# TEIL 5 – Eintrag entfernen
# =====================================================

# del loescht einen Schluessel samt Wert komplett aus dem Dictionary.
# Nach dem Loeschen existiert der Schluessel nicht mehr.
# Tipp: .pop("Schluessel") macht dasselbe,
#        gibt aber zusaetzlich den geloeschten Wert zurueck.

del rucksack["Supertrank"]

print("\n=== TEIL 5: Supertraenke aufgebraucht ===")
print("Rucksack danach:", rucksack)


# =====================================================
# BONUS – Verschachteltes Dictionary
# =====================================================

# Ein Dictionary kann als Wert ein anderes Dictionary enthalten.
# Das nennt sich verschachtelt (nested dictionary).
# So laesst sich ein vollstaendiges Trainer-Profil abbilden.

trainer = {
    "name":    "Ash Debug",
    "orden":   8,
    "inventar": rucksack     # Das rucksack-Dictionary von oben.
}

print("\n=== BONUS: Trainer-Profil ===")
print(f"Name:     {trainer['name']}")
print(f"Orden:    {trainer['orden']}")
print(f"Inventar: {trainer['inventar']}")

# Auf verschachtelte Werte zugreifen:
# Erst aeusserer Schluessel -> dann innerer Schluessel.
print(f"\nPokeballs von {trainer['name']}: {trainer['inventar']['Pokeball']}")
print(f"Hyperballs von {trainer['name']}: {trainer['inventar']['Hyperball']}")