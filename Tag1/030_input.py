# Input() Funktion

# name = input("Wie heißt dein Hund? ")
# print(name)

# input() gibt mir immer Text zurück, auch wenn der Benutzer eine Zahl benutzt

# Variante 1

alter = input("Wie alt bist du? ")
alter = int(alter)

print(alter)

# Schritt 1: Python zeigt uns die Frage = Wie alt bist du?
# Schritt 2: User gibt sein alter an (32)
# Schritt 3: input() Funktion speichert die "32" als Text
# Schritt 4: alter = int(alter) -> bedeutet der Text "32" wird hier in eine Zahl umgewandelt
#               -> 32 ist jetzt ein Integer
# Schritt 5: Ausgabe des Alters = 32
# Schritt 6: kann mit Alter weiter rechnen

print(alter + 5)


# Variante 2
alter = int(input("Wie alt bist du? "))