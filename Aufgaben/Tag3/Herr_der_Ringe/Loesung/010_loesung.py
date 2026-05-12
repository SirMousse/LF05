# Aufgabe: Tor von Moria

staerke = int(input("Deine Stärke: "))

if staerke >= 100:
    print("Das Tor öffnet sich")
elif staerke >= 50:
    print("Die Wachen beobachten dich")
else:
    print("Du wirst zurückgeschickt")