# Aufgabe: Serverraum

cpu = int(input("CPU-Auslastung in %: "))

if cpu < 50:
    print("Server läuft stabil")
elif cpu <= 80:
    print("Hohe Auslastung erkannt")
else:
    print("Warnung: Server überlastet")