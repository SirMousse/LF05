# Aufgabe: Firewall-Check

sicherheitsstufe = int(input("Sicherheitsstufe des Systems: "))

if sicherheitsstufe >= 90:
    print("System maximal gesichert")
elif sicherheitsstufe >= 60:
    print("Mittlere Sicherheit")
else:
    print("System gefährdet")