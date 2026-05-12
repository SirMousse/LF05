# Projekt-Aufgabe: Der Server-Notfall
#
# Erstelle ein IT-Support-Programm.
#
# Nutze:
# - if
# - elif
# - else
# - nested ifs
#
# Anforderungen:
#
# 1. Frage den Namen des Technikers ab.
# 2. Frage die CPU-Auslastung ab.
# 3. Frage den verfügbaren Speicherplatz ab.
#
# Wenn CPU unter 50:
# Ausgabe -> "Server läuft stabil."
#
# Wenn CPU zwischen 50 und 85:
# Ausgabe -> "Server ist stark ausgelastet."
#
# Wenn CPU über 85:
# Ausgabe -> "Kritischer Serverzustand."
#
# 4. Nur wenn CPU über 85 ist:
#    Frage, ob ein Neustart erlaubt ist: ja/nein
#
#    Wenn ja:
#    Ausgabe -> "Server wird neu gestartet."
#
#    Wenn nein:
#    Ausgabe -> "Manuelle Fehleranalyse erforderlich."
#
# 5. Frage nach dem Problemtyp:
#    - Netzwerk
#    - Datenbank
#    - Login
#
# 6. Je nach Problemtyp soll eine andere Lösung ausgegeben werden.
#
# Bonus:
# Wenn Speicherplatz unter 10 ist:
#     Ausgabe -> "Festplatte fast voll."
#
# Ziel:
# Baue ein realistisches Entscheidungsprogramm.