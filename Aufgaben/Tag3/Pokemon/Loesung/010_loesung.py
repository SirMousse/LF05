# Aufgabe: Arena-Challenge

orden = int(input("Anzahl deiner Orden: "))

if orden >= 8:
    print("Pokémon Liga freigeschaltet")
elif orden >= 4:
    print("Du darfst stärkere Arenen betreten")
else:
    print("Trainiere weiter")