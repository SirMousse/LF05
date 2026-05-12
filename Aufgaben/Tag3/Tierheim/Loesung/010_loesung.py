# Aufgabe: Tierheim-Verwaltung

plaetze = int(input("Anzahl freier Plätze: "))

if plaetze >= 20:
    print("Viele Plätze verfügbar")
elif plaetze >= 5:
    print("Noch einige Plätze frei")
else:
    print("Tierheim fast voll")