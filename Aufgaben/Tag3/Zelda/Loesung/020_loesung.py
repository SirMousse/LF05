# ============================================
#   DER TEMPEL DER WEISHEIT
# ============================================

# 1. Heldenname abfragen
name = input("Name des Helden: ")
print(f"\nWillkommen, {name}. Der Tempel der Weisheit öffnet seine Tore.\n")

# 2. Herzen abfragen
herzen = int(input("Anzahl der Herzen: "))

# 3. Schlüssel abfragen
schluessel = int(input("Anzahl der Schlüssel: "))

# --- Herzen-Auswertung ---
if herzen < 5:
    print("Du bist zu schwach für den Tempel.")
    herz_status = "schwach"

elif herzen <= 11:
    print("Du darfst den ersten Raum betreten.")
    herz_status = "mittel"

else:
    print("Du darfst den Bossraum betreten.")
    herz_status = "stark"

# BONUS: Schlüssel ab 3
if schluessel >= 3:
    print("Du kannst geheime Räume öffnen.")

# 4. Masterschlüssel — nur wenn Herzen ab 12
if herz_status == "stark":
    masterschluessel = input("\nIst der Masterschlüssel vorhanden? (ja/nein): ").strip().lower()

    if masterschluessel == "ja":
        print("Die Boss-Tür öffnet sich.")
    else:
        print("Die Boss-Tür bleibt verschlossen.")
else:
    masterschluessel = "nein"

# 5. Item abfragen
print("\nWelches Item hast du?")
print("  1 - Schwert")
print("  2 - Bumerang")
print("  3 - Bogen")
item = input("Dein Item: ").strip().lower()

# Eingabe normalisieren
if item == "1":
    item = "schwert"
elif item == "2":
    item = "bumerang"
elif item == "3":
    item = "bogen"

# 6. Rätsel je nach Item
if item == "schwert":
    print("Das Schwert zerschlägt den versteinerten Torwächter.")
elif item == "bumerang":
    print("Der Bumerang betäubt alle Schalter gleichzeitig — das Rätsel ist gelöst.")
elif item == "bogen":
    print("Ein Pfeil trifft das Auge des Steindrachens. Die Tür springt auf.")
else:
    print("Unbekanntes Item — das Rätsel bleibt ungelöst.")
    item = "keins"

# ============================================
#   VERSCHIEDENE ENDEN (nested ifs)
# ============================================

print("\n--- Tempel-Abschluss ---")

if herz_status == "schwach":
    # Ende 1
    print(f"Ende 1: {name} scheitert am Eingang.")
    print("Die Wächter werfen den Helden hinaus. Komm stärker zurück.")

elif herz_status == "mittel":

    if schluessel >= 3:
        # Ende 2
        print(f"Ende 2: {name} entdeckt einen Geheimraum.")
        print("Tief im Tempel wartet ein seltener Schatz — aber der Boss bleibt ungeschlagen.")
    else:
        # Ende 3
        print(f"Ende 3: {name} überlebt den ersten Raum.")
        print("Ohne Geheimschlüssel bleibt der Rest des Tempels versperrt.")

else:
    # Herzen stark
    if masterschluessel == "nein":
        # Ende 4
        print(f"Ende 4: {name} steht vor der Boss-Tür.")
        print("Ohne Masterschlüssel kein Durchgang. Die Reise war umsonst — diesmal.")

    else:
        # Masterschlüssel vorhanden — Item entscheidet

        if item == "schwert":
            # Ende 5
            print(f"Ende 5: {name} kämpft sich durch jeden Raum.")
            print("Das Schwert bricht den Fluch des Tempels. Hyrule ist gerettet!")

        elif item == "bumerang":
            # Ende 6
            print(f"Ende 6: Mit dem Bumerang löst {name} alle Fallen des Tempels.")
            print("Der Boss fällt mit einem einzigen Wurf.")

        elif item == "bogen":
            # Ende 7
            print(f"Ende 7: {name} trifft jeden Schalter aus der Ferne.")
            print("Der Boss fällt, bevor er auch nur einen Schritt machen kann.")

        else:
            # Ende 8
            print(f"Ende 8: Ohne brauchbares Item kämpft {name} mit bloßen Händen.")
            print("Gegen alle Wahrscheinlichkeit — der Boss liegt am Boden.")