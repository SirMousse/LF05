# ============================================
#   DAS TIERHEIM-MANAGEMENT
# ============================================

# 1. Mitarbeitername abfragen
name = input("Name des Mitarbeiters: ")
print(f"\nWillkommen, {name}!\n")

# 2. Freie Plätze abfragen
plaetze = int(input("Anzahl freier Plätze im Tierheim: "))

# 3. Kranke Tiere abfragen
kranke_tiere = int(input("Anzahl kranker Tiere: "))

# --- Kapazitäts-Auswertung ---
if plaetze < 5:
    print("Das Tierheim ist fast voll.")
elif plaetze <= 15:
    print("Es sind noch einige Plätze frei.")
else:
    print("Viele Plätze verfügbar.")

# 4. Tier aufnehmen — nur wenn Plätze > 0
if plaetze > 0:

    print("\nWelches Tier soll aufgenommen werden?")
    print("  1 - Hund")
    print("  2 - Katze")
    print("  3 - Kaninchen")
    tier = input("Ihre Wahl: ").strip().lower()

    if tier == "1":
        tier = "hund"
    elif tier == "2":
        tier = "katze"
    elif tier == "3":
        tier = "kaninchen"

    # 5. Ausgabe je nach Tier
    if tier == "hund":
        print("Der Hund bekommt einen großen Auslauf.")
    elif tier == "katze":
        print("Die Katze kommt ins Katzenzimmer.")
    elif tier == "kaninchen":
        print("Das Kaninchen bekommt frisches Heu.")
    else:
        print("Unbekanntes Tier — Aufnahme nicht möglich.")
        tier = None

    # 6. Gesundheitszustand abfragen
    if tier is not None:
        gesundheit = input("\nGesundheitszustand (gesund / verletzt / kritisch): ").strip().lower()

        # 7. Nested ifs: Tier + Gesundheitszustand
        if tier == "hund":
            if gesundheit == "gesund":
                print("Der Hund ist fit und bereit zur Aufnahme.")
            elif gesundheit == "verletzt":
                print("Der Hund wird sofort behandelt.")
            elif gesundheit == "kritisch":
                print("Notfallbehandlung für den Hund wird eingeleitet!")
            else:
                print("Unbekannter Gesundheitszustand.")

        elif tier == "katze":
            if gesundheit == "gesund":
                print("Die Katze ist fit und bereit zur Aufnahme.")
            elif gesundheit == "verletzt":
                print("Die Katze wird sofort behandelt.")
            elif gesundheit == "kritisch":
                print("Notfallbehandlung für die Katze wird eingeleitet!")
            else:
                print("Unbekannter Gesundheitszustand.")

        elif tier == "kaninchen":
            if gesundheit == "gesund":
                print("Das Kaninchen ist fit und bereit zur Aufnahme.")
            elif gesundheit == "verletzt":
                print("Das Kaninchen wird sofort behandelt.")
            elif gesundheit == "kritisch":
                print("Notfallbehandlung für das Kaninchen wird eingeleitet!")
            else:
                print("Unbekannter Gesundheitszustand.")

else:
    print("\nKeine freien Plätze — es kann kein Tier aufgenommen werden.")

# 8. Tierarztstation überlastet?
if kranke_tiere > 10:
    print("\nDie Tierarztstation ist überlastet.")

# 9. Futter vorhanden?
futter = input("\nIst genug Futter vorhanden? (ja / nein): ").strip().lower()

if futter == "nein":
    print("Es muss dringend neues Futter bestellt werden.")
elif futter == "ja":
    print("Alle Tiere können versorgt werden.")
else:
    print("Ungültige Eingabe für Futterstatus.")

# ============================================
#   BONUS 1: Freiwillige Helfer
# ============================================

helfer = int(input("\nAnzahl der freiwilligen Helfer: "))

if helfer > 5:
    print("Das Tierheim hat genug Unterstützung.")
else:
    print("Es werden weitere Helfer benötigt.")

# ============================================
#   BONUS 2: Alter des Tieres
# ============================================

alter = int(input("\nAlter des aufgenommenen Tieres (in Jahren): "))

if alter < 2:
    print("Das Tier ist noch jung.")
elif alter <= 8:
    print("Das Tier ist erwachsen.")
else:
    print("Das Tier ist bereits älter.")

print("\n--- Ende der Auswertung ---")