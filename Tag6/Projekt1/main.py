# Komplette Datei importieren
import rechner          # import rechner bedeutet nichts anderes als das Python jetzt nach einer Datei namens rechner.py sucht
                        # -> wenn es rechner.py gefunden hat -> macht Python deren Inhalt in der main.py verfügbar

ergebnis = rechner.addieren(5, 3)       # ergebnis -> Variable die wir angeben
                                        # rechner.addieren  -> rechner steht für die Datei rechner.py + Funktion addieren in dieser Datei
                                        # (5, 3) -> Argumente die die Parameter a und b ersetzen sollen

print(ergebnis)

# Variante 2
ergebnis = rechner.addieren(58, 33)
print(ergebnis)

# Variante 3
ergebnis = rechner.addieren(75, 93)
print(ergebnis)

# Variante 4
ergebnis = rechner.addieren(8, 121)
print(ergebnis)

# Variante 5
ergebnis = rechner.addieren(89, 147)
print(ergebnis)