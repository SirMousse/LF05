# =====================================================
# DAS HYRULE-INVENTAR
# =====================================================


# =====================================================
# TEIL 1 – Dictionary erstellen
# =====================================================

# Ein Dictionary speichert Schlüssel-Wert-Paare: { schlüssel: wert }
# Stell es dir wie ein Notizbuch vor:
# links steht der Name des Gegenstands, rechts die Menge.

inventar = {
    "Pfeile": 20,
    "Bomben": 5,
    "Heiltrank": 3,
    "Rubine": 50
}

print("=== TEIL 1: Inventar erstellt ===")
print(inventar)


# =====================================================
# TEIL 2 – Gegenstände benutzen (Werte ändern)
# =====================================================

# Mit inventar["Schlüssel"] greift man auf einen Wert zu.
# -= zieht den Wert ab und speichert das Ergebnis direkt.

inventar["Pfeile"] -= 2   # 20 - 2 = 18
inventar["Bomben"] -= 1   # 5 - 1 = 4

print("\n=== TEIL 2: Nach dem Benutzen ===")
print(f"Pfeile übrig: {inventar['Pfeile']}")
print(f"Bomben übrig: {inventar['Bomben']}")


# =====================================================
# TEIL 3 – Neuen Gegenstand hinzufügen
# =====================================================

# Neuen Eintrag hinzufügen funktioniert genauso wie beim Ändern:
# einfach einen neuen Schlüssel zuweisen, den es noch nicht gibt.
# Existiert der Schlüssel schon → Wert wird überschrieben.
# Existiert er noch nicht → neuer Eintrag wird erstellt.

inventar["Master-Schlüssel"] = 1

print("\n=== TEIL 3: Master-Schlüssel hinzugefügt ===")
print(inventar)


# =====================================================
# TEIL 4 – Prüfen ob ein Schlüssel existiert
# =====================================================

# Mit "in" prüft man, ob ein Schlüssel im Dictionary vorhanden ist.
# Das gibt True oder False zurück – perfekt für eine if-Bedingung.

print("\n=== TEIL 4: Heiltrank-Check ===")
if "Heiltrank" in inventar:
    print("Link kann geheilt werden!")
else:
    print("Kein Heiltrank vorhanden!")


# =====================================================
# TEIL 5 – Eintrag entfernen
# =====================================================

# del löscht einen Eintrag komplett aus dem Dictionary.
# Alternativ gibt es auch .pop("Schlüssel") –
# das löscht den Eintrag UND gibt den Wert zurück.

del inventar["Rubine"]

print("\n=== TEIL 5: Rubine gestohlen! ===")
print("Inventar nach dem Diebstahl:", inventar)


# =====================================================
# BONUS – Verschachteltes Dictionary
# =====================================================

# Ein Dictionary kann als Wert ein anderes Dictionary enthalten.
# Das nennt sich verschachtelt (nested).
# So kann man komplexe Objekte wie einen Spielcharakter abbilden.

held = {
    "name": "Link",
    "herzen": 10,
    "inventar": inventar   # Wir verwenden das inventar von oben!
}

print("\n=== BONUS: Der Held ===")
print(f"Name:   {held['name']}")
print(f"Herzen: {held['herzen']}")
print(f"Items:  {held['inventar']}")

# Auf verschachtelte Werte zugreifen: erst äußerer, dann innerer Schlüssel.
print(f"\nPfeile von {held['name']}: {held['inventar']['Pfeile']}")
print(f"Bomben von {held['name']}: {held['inventar']['Bomben']}")