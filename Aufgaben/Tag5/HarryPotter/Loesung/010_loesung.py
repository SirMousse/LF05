# =====================================================
# DAS ZAUBERER-INVENTAR
# =====================================================


# =====================================================
# TEIL 1 – Dictionary erstellen
# =====================================================

# Ein Dictionary speichert Schluessel-Wert-Paare: { schluessel: wert }
# Geschweifte Klammern {}, Doppelpunkt zwischen Schluessel und Wert,
# Komma zwischen den Eintraegen.

zaubertasche = {
    "Zauberstab":   1,
    "Schokofrosch": 5,
    "Heiltrank":    2,
    "Eulenfeder":   4
}

print("=== TEIL 1: Zaubertasche ===")
print(zaubertasche)


# =====================================================
# TEIL 2 – Gegenstaende benutzen
# =====================================================

# zaubertasche["Schluessel"] greift auf den Wert zu.
# -= zieht den Betrag direkt ab und speichert das Ergebnis.
# zaubertasche["Heiltrank"] -= 1  ist dasselbe wie:
# zaubertasche["Heiltrank"] = zaubertasche["Heiltrank"] - 1

zaubertasche["Heiltrank"]    -= 1   # 2 - 1 = 1
zaubertasche["Schokofrosch"] -= 1   # 5 - 1 = 4

print("\n=== TEIL 2: Nach dem Benutzen ===")
print(f"Heiltrank:    {zaubertasche['Heiltrank']}")
print(f"Schokofrosch: {zaubertasche['Schokofrosch']}")


# =====================================================
# TEIL 3 – Neuen Gegenstand hinzufuegen
# =====================================================

# Einen neuen Eintrag erstellt man genau wie beim Aendern:
# einfach den neuen Schluessel zuweisen.
# Gibt es den Schluessel noch nicht -> wird er neu angelegt.
# Gibt es ihn schon -> wird der Wert ueberschrieben.

zaubertasche["Marauders Map"] = 1

print("\n=== TEIL 3: Marauders Map hinzugefuegt ===")
print(zaubertasche)


# =====================================================
# TEIL 4 – Pruefen ob ein Schluessel existiert
# =====================================================

# "in" prueft, ob ein Schluessel im Dictionary vorhanden ist.
# Ergebnis: True oder False – direkt nutzbar in if-Bedingungen.

print("\n=== TEIL 4: Zauberstab-Check ===")
if "Zauberstab" in zaubertasche:
    print("Expelliarmus ist einsatzbereit!")
else:
    print("Kein Zauberstab gefunden!")


# =====================================================
# TEIL 5 – Eintrag entfernen
# =====================================================

# del loescht einen Schluessel samt Wert komplett aus dem Dictionary.
# Nach dem Loeschen existiert der Schluessel nicht mehr.
# Tipp: .pop("Schluessel") macht dasselbe,
#        gibt aber zusaetzlich den geloeschten Wert zurueck.

del zaubertasche["Eulenfeder"]

print("\n=== TEIL 5: Eulenfeder verschwunden ===")
print("Zaubertasche danach:", zaubertasche)


# =====================================================
# BONUS – Verschachteltes Dictionary
# =====================================================

# Ein Dictionary kann als Wert ein anderes Dictionary enthalten.
# Das nennt sich verschachtelt (nested dictionary).
# So laesst sich ein vollstaendiges Schueler-Profil abbilden.

schueler = {
    "name":    "Luna Debuggood",
    "haus":    "Ravenclaw",
    "inventar": zaubertasche     # Das zaubertasche-Dictionary von oben.
}

print("\n=== BONUS: Schueler-Profil ===")
print(f"Name:     {schueler['name']}")
print(f"Haus:     {schueler['haus']}")
print(f"Inventar: {schueler['inventar']}")

# Auf verschachtelte Werte zugreifen:
# Erst aeusserer Schluessel -> dann innerer Schluessel.
print(f"\nZauberstaebe von {schueler['name']}: {schueler['inventar']['Zauberstab']}")
print(f"Schokofroesche von {schueler['name']}: {schueler['inventar']['Schokofrosch']}")