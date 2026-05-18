# Einzelne Funktionen ein

from rechner import addieren        # bedeutet: Von der Datei rechner.py importiere mir die Funktion addieren

print(addieren(10,2))               # hier muss man nicht nochmal rechner.addieren() schreiben sondern kann die Funktion direkt aufrufen

# MERKE
# import -> holt die Datei
# from ... import ... -> holt nur einen bestimmten Teil aus der Datei