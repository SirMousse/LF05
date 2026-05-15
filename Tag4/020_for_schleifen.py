# for -Schleife

# Syntax
# for variable in etwas:
#   code

# for -> startet die Schleife
# variabel -> speichert den aktuellen Durchlauf
# in -> verbindet Schleife mit den Daten
# etwas -> bestimmt wie oft das ganze wdh werden soll
# : -> startet den Codeblock
# Einrückung -> gehört zur Schleife

# Nur einen Endwert
for fluff in range(3):
    print("Wuff")

# range() rezeugt eine Zahlenfolge
# WICHTIG: Die letzte Zahl wird nicht mitgezählt (Zählt: 0,1,2)

# Start- und Endwert
# range(start, stop)
for katze in range(1, 6):
    print(katze, "Miau")

for hamster in range(-5, 0):
    print(hamster, "Fluff")

# Schritweise Zählen
# range(start, stop, schritt)
for hund in range(0, 10, 2):
    print(hund, "Wuff")

for schildkröte in range(0, -5, -1):            # Negative Schrittweiten zählen IMMER rückwärts ( 0 + -1 = -1 + -1 = -2 + -1 = -3 etc. )
    print(schildkröte, "Salatblatt")

# Rückwertszählen
for ziege in range(4, -1, -1):
    print(ziege, "Stur")