# =====================================================
# DAS HACKER-SETUP
# =====================================================


# =====================================================
# TEIL 1 – Dictionary erstellen
# =====================================================

# Ein Dictionary speichert Schluessel-Wert-Paare: { schluessel: wert }
# Geschweifte Klammern {}, Doppelpunkt zwischen Schluessel und Wert,
# Komma zwischen den Eintraegen.

tools = {
    "USB-Exploit":    4,
    "Passwortliste":  2,
    "Energydrink":    6,
    "Firewall-Bypass": 1
}

print("=== TEIL 1: Hacker-Setup ===")
print(tools)


# =====================================================
# TEIL 2 – Gegenstaende benutzen
# =====================================================

# tools["Schluessel"] greift auf den Wert zu.
# -= zieht den Betrag direkt ab und speichert das Ergebnis.
# tools["Energydrink"] -= 1  ist dasselbe wie:
# tools["Energydrink"] = tools["Energydrink"] - 1

tools["Energydrink"] -= 1     # 6 - 1 = 5
tools["USB-Exploit"] -= 1     # 4 - 1 = 3

print("\n=== TEIL 2: Nach dem Benutzen ===")
print(f"Energydrink:  {tools['Energydrink']}")
print(f"USB-Exploit:  {tools['USB-Exploit']}")


# =====================================================
# TEIL 3 – Neuen Gegenstand hinzufuegen
# =====================================================

# Einen neuen Eintrag erstellt man genau wie beim Aendern:
# einfach den neuen Schluessel zuweisen.
# Gibt es den Schluessel noch nicht -> wird er neu angelegt.
# Gibt es ihn schon -> wird der Wert ueberschrieben.

tools["VPN-Schluessel"] = 3

print("\n=== TEIL 3: VPN-Schluessel hinzugefuegt ===")
print(tools)


# =====================================================
# TEIL 4 – Pruefen ob ein Schluessel existiert
# =====================================================

# "in" prueft, ob ein Schluessel im Dictionary vorhanden ist.
# Ergebnis: True oder False – direkt nutzbar in if-Bedingungen.

print("\n=== TEIL 4: Firewall-Check ===")
if "Firewall-Bypass" in tools:
    print("Systemzugriff moeglich!")
else:
    print("Kein Firewall-Bypass vorhanden!")


# =====================================================
# TEIL 5 – Eintrag entfernen
# =====================================================

# del loescht einen Schluessel samt Wert komplett aus dem Dictionary.
# Nach dem Loeschen existiert der Schluessel nicht mehr.
# Tipp: .pop("Schluessel") macht dasselbe,
#        gibt aber zusaetzlich den geloeschten Wert zurueck.

del tools["Passwortliste"]

print("\n=== TEIL 5: Passwortliste geloescht ===")
print("Tools nach dem Loeschen:", tools)


# =====================================================
# BONUS – Verschachteltes Dictionary
# =====================================================

# Ein Dictionary kann als Wert ein anderes Dictionary enthalten.
# Das nennt sich verschachtelt (nested dictionary).
# So laesst sich ein vollstaendiges Hacker-Profil abbilden.

hacker = {
    "name":    "ZeroByte",
    "rang":    99,
    "inventar": tools        # Das tools-Dictionary von oben wird eingebaut.
}

print("\n=== BONUS: Hacker-Profil ===")
print(f"Name:     {hacker['name']}")
print(f"Rang:     {hacker['rang']}")
print(f"Inventar: {hacker['inventar']}")

# Auf verschachtelte Werte zugreifen:
# Erst aeusserer Schluessel -> dann innerer Schluessel.
print(f"\nUSB-Exploits von {hacker['name']}: {hacker['inventar']['USB-Exploit']}")
print(f"Energydrinks von {hacker['name']}: {hacker['inventar']['Energydrink']}")