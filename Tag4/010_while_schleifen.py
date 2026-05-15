# while - Schleife
# bedeutet -> SOLANGE etwas wahr ist

# while bedingung:
#   code

# WICHTIG IST:  - Doppelpunkte: nach Bedingung nicht vergessen!
#               - Einrücken des Codes, nach code bedingung:
#               - Bedingung muss wahr(True) sein

# Beispiel Hunde fütter
# 1) Startwert
hunger = 3

# 2) Die Bedingung die geprüft werden soll
while hunger > 0:                               # Ist 3 > 0? -> Ja, ist es
    print("Bello bekommt sein Futter.")         # Antwort Ja -> Wird der Code Ausgeführt | Antwort Nein -> Code wird nicht ausgeführt
    hunger -= 1                                 # Rechnung um Startwert zu vermindern -> Also: 3 -> 2 | 2 -> 1 | 1 -> 0


# Beispiel Katzenzimmer
zimmer = 1

while zimmer <= 5:
    print(f"Katzenzimmer {zimmer} wird gereinigt!")
    zimmer += 1

# Beispiel Tiere aufnehmen bis das Tierheim voll ist

# plaetze = 5

# while plaetze > 0:
#     tier = input("Welches Tier wird aufgenommen?\n")
    
#     print(f"{tier} wurde aufgenommen!")
    
#     plaetze -= 1
#     print(f"Noch freie Plätze: {plaetze}")

# print("Das Tierheim ist voll!")

# IHK WICHTIG:

# Definition:
# ... die while- Schleife ist eine kopfgesteuerte Schleife, 
#     bei der die Bedingung vor jedem Durchlauf geprüft wird!
# kopfgesteuert -> Bedingung wird oben im Kopf geprüft (Syntax -> while bedingung:)

# Ablauf erklären können:
# 1) Bedingung geprüft
# 2) Ist die Bedingung wahr -> wird der Schleifenblock ausgeführt
# 3) Danach wird erneut geprüft
# 4) Ist die Bedingung falsch -> wird die Schleife beendet

# Schleifenvariable MUSS verändert werden -> sonst entsteht eine Endlosschleife

# Beispiel für Endlosschleife
# zahl = 1

# while zahl <= 5:
#     print(zahl)

# Endlosschleife
# ... ist eine Schleife ohne Abbruchbedingung!

################################################################################################

# break -> Sofortiger Abbruch

while True:
    tier = input("Weches Tier?\n")
    
    if tier == "exit":
        break
    
    print(tier, "wird untersucht!")

# break
# ... beendet die Schleife sofort.

# Typische Einsatzgebiete für while-Schleife:
# - Login-Systeme
# - Menüs
# - Eingabeprüfungen
# - WDH bis Bedingung erfüllt ist
# - Spiele
# - Automaten

# Iteration
# ... ein durchlauf der Schleife

# Schleifenbedingung
# ... entscheidet ob Schleife läuft

# Beispiel Menü

while True:
    # Menü Angezeigt
    print("Tierheim Menü")
    print("1 = Hund füttern")
    print("2 = Katze streicheln")
    print("3 = Tierheim schließen")
    
    # Eingabe speichern
    auswahl = input("Bitte wähle: ")
    
    # Auswahl 1 = Hund füttern
    if auswahl == "1":
        print("Bello bekommt Futter.")
    # Auswahl 2 = Katze streicheln
    elif auswahl == "2":
        print("Luna ignoriert dich professionell!")
    # Auswahl 3 = Terheim schließt
    elif auswahl == "3":
        print("Tierheim wird geschlossen!")
        # break beendet die Schleife
        break
    # Auswahl von dem was nicht vorgegeben wurde
    else:
        print("Ungültige Eingabe!")
