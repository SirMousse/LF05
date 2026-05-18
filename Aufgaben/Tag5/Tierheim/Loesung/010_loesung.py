# =====================================================
# DAS TIERHEIM-SYSTEM
# =====================================================


# TEIL 1 – Dictionary erstellen
lager = {
    "Katzenfutter":   10,
    "Hundespielzeug":  4,
    "Decken":          7,
    "Leckerlis":      15
}

print("-- Aktuelles Lager --")
for gegenstand, menge in lager.items():
    print(f"  {gegenstand}: {menge}")


# TEIL 2 – Gegenstände verbrauchen
lager["Decken"]    -= 2
lager["Leckerlis"] -= 3

print("\n-- Nach Verbrauch --")
print(f"  Decken:    {lager['Decken']}")
print(f"  Leckerlis: {lager['Leckerlis']}")


# TEIL 3 – Neuen Gegenstand hinzufügen
lager["Katzenspielzeug"] = 5

print("\n-- Neuer Gegenstand --")
print(f"  Katzenspielzeug: {lager['Katzenspielzeug']}")


# TEIL 4 – Prüfen ob Gegenstand vorhanden ist
if "Katzenfutter" in lager:
    print("\nDie Katzen sind versorgt!")


# TEIL 5 – Gegenstand entfernen
del lager["Hundespielzeug"]

print("\n-- Nach Entfernung --")
for gegenstand, menge in lager.items():
    print(f"  {gegenstand}: {menge}")


# ── BONUS ─────────────────────────────────────────
# Verschachteltes Dictionary: tierpfleger enthält
# das lager als Wert unter "inventar"

tierpfleger = {
    "name":       "Mia",
    "erfahrung":  4,
    "inventar":   lager
}

print("\n-- Tierpfleger-Profil --")
print(f"  Name:       {tierpfleger['name']}")
print(f"  Erfahrung:  {tierpfleger['erfahrung']} Jahre")
print(f"  Inventar:")
for gegenstand, menge in tierpfleger["inventar"].items():
    print(f"    {gegenstand}: {menge}")