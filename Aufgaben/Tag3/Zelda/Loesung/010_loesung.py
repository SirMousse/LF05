# Aufgabe: Tempel-Zugang

herzen = int(input("Anzahl gesammelter Herzen: "))

if herzen >= 15:
    print("Meistertempel betreten")
elif herzen >= 8:
    print("Neue Regionen freigeschaltet")
else:
    print("Du brauchst mehr Herzen")