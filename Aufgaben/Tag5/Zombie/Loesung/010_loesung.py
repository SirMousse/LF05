# =====================================================
# DAS ZOMBIE-ÜBERLEBENSKIT
# =====================================================


# TEIL 1 – Dictionary erstellen
ueberlebenskit = {
    "Konserven":     8,
    "Munition":     30,
    "Verband":       5,
    "Taschenlampe":  2
}

print("-- Aktuelles Kit --")
for gegenstand, menge in ueberlebenskit.items():
    print(f"  {gegenstand}: {menge}")


# TEIL 2 – Gegenstände verbrauchen
ueberlebenskit["Verband"]   -= 1
ueberlebenskit["Munition"]  -= 5

print("\n-- Nach Verbrauch --")
print(f"  Verband:  {ueberlebenskit['Verband']}")
print(f"  Munition: {ueberlebenskit['Munition']}")


# TEIL 3 – Neuen Gegenstand hinzufügen
ueberlebenskit["Benzinkanister"] = 1

print("\n-- Neuer Gegenstand --")
print(f"  Benzinkanister: {ueberlebenskit['Benzinkanister']}")


# TEIL 4 – Prüfen ob Gegenstand vorhanden ist
if "Taschenlampe" in ueberlebenskit:
    print("\nDie Nacht kann überlebt werden!")


# TEIL 5 – Gegenstand entfernen
del ueberlebenskit["Konserven"]

print("\n-- Nach Plünderung --")
for gegenstand, menge in ueberlebenskit.items():
    print(f"  {gegenstand}: {menge}")


# ── BONUS ─────────────────────────────────────────
# Verschachteltes Dictionary: survivor enthält
# das ueberlebenskit als Wert unter "inventar"

survivor = {
    "name":            "Alex",
    "tage_ueberlebt":  42,
    "inventar":        ueberlebenskit
}

print("\n-- Survivor-Profil --")
print(f"  Name:           {survivor['name']}")
print(f"  Tage ueberlebt: {survivor['tage_ueberlebt']}")
print(f"  Inventar:")
for gegenstand, menge in survivor["inventar"].items():
    print(f"    {gegenstand}: {menge}")