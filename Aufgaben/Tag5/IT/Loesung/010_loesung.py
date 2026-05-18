# =====================================================
# DAS IT-LAGER
# =====================================================


# =====================================================
# TEIL 1 – Dictionary erstellen
# =====================================================

# Ein Dictionary speichert Schluessel-Wert-Paare: { schluessel: wert }
# Geschweifte Klammern {}, Doppelpunkt zwischen Schluessel und Wert,
# Komma zwischen den Eintraegen.

hardware = {
    "Tastatur":  5,
    "Monitor":   3,
    "USB-Stick": 10,
    "LAN-Kabel": 12
}

print("=== TEIL 1: IT-Lager ===")
print(hardware)


# =====================================================
# TEIL 2 – Gegenstaende benutzen
# =====================================================

# hardware["Schluessel"] greift auf den Wert zu.
# -= zieht den Betrag direkt ab und speichert das Ergebnis.
# hardware["Monitor"] -= 1  ist dasselbe wie:
# hardware["Monitor"] = hardware["Monitor"] - 1

hardware["Monitor"]   -= 1   # 3 - 1 = 2
hardware["USB-Stick"] -= 2   # 10 - 2 = 8

print("\n=== TEIL 2: Nach der Ausgabe ===")
print(f"Monitor:   {hardware['Monitor']}")
print(f"USB-Stick: {hardware['USB-Stick']}")


# =====================================================
# TEIL 3 – Neuen Gegenstand hinzufuegen
# =====================================================

# Einen neuen Eintrag erstellt man genau wie beim Aendern:
# einfach den neuen Schluessel zuweisen.
# Gibt es den Schluessel noch nicht -> wird er neu angelegt.
# Gibt es ihn schon -> wird der Wert ueberschrieben.

hardware["SSD"] = 4

print("\n=== TEIL 3: SSD eingelagert ===")
print(hardware)


# =====================================================
# TEIL 4 – Pruefen ob ein Schluessel existiert
# =====================================================

# "in" prueft, ob ein Schluessel im Dictionary vorhanden ist.
# Ergebnis: True oder False – direkt nutzbar in if-Bedingungen.

print("\n=== TEIL 4: LAN-Kabel-Check ===")
if "LAN-Kabel" in hardware:
    print("Netzwerkverbindung moeglich!")
else:
    print("Kein LAN-Kabel auf Lager!")


# =====================================================
# TEIL 5 – Eintrag entfernen
# =====================================================

# del loescht einen Schluessel samt Wert komplett aus dem Dictionary.
# Nach dem Loeschen existiert der Schluessel nicht mehr.
# Tipp: .pop("Schluessel") macht dasselbe,
#        gibt aber zusaetzlich den geloeschten Wert zurueck.

del hardware["Tastatur"]

print("\n=== TEIL 5: Tastaturen aussortiert ===")
print("Lager nach Aussortierung:", hardware)


# =====================================================
# BONUS – Verschachteltes Dictionary
# =====================================================

# Ein Dictionary kann als Wert ein anderes Dictionary enthalten.
# Das nennt sich verschachtelt (nested dictionary).
# So laesst sich ein vollstaendiges Admin-Profil abbilden.

admin = {
    "name":    "RootMaster",
    "rechte":  "Administrator",
    "inventar": hardware       # Das hardware-Dictionary von oben.
}

print("\n=== BONUS: Admin-Profil ===")
print(f"Name:     {admin['name']}")
print(f"Rechte:   {admin['rechte']}")
print(f"Inventar: {admin['inventar']}")

# Auf verschachtelte Werte zugreifen:
# Erst aeusserer Schluessel -> dann innerer Schluessel.
print(f"\nMonitore von {admin['name']}: {admin['inventar']['Monitor']}")
print(f"LAN-Kabel von {admin['name']}: {admin['inventar']['LAN-Kabel']}")