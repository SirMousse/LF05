# Aufgabe:
# Schreibe ein Programm, das den Benutzer nach einem Passwort fragt.
#
# Wenn das Passwort richtig ist:
# Ausgabe -> Zugang erlaubt
#
# Wenn das Passwort falsch ist:
# Ausgabe -> Falsches Passwort

password = "Mousse09"

anfrage = input("Wie lautet dein Passwort?\n")

if anfrage == password:
    print("Du bist eingelogged!")
else:
    print("Versuche es noch einmal!")