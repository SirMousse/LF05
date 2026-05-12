# Projekt-Aufgabe: Der Firewall-Breaker
#
# Erstelle ein Hacker-Textspiel.
#
# Nutze:
# - if
# - elif
# - else
# - nested ifs
#
# Anforderungen:
#
# 1. Frage den Hacker-Namen ab.
# 2. Frage die Sicherheitsfreigabe ab.
# 3. Frage die Passwort-Stärke ab.
#
# Wenn Sicherheitsfreigabe unter 40:
# Ausgabe -> "Zugriff verweigert."
#
# Wenn Sicherheitsfreigabe zwischen 40 und 79:
# Ausgabe -> "Eingeschränkter Zugriff erlaubt."
#
# Wenn Sicherheitsfreigabe ab 80:
# Ausgabe -> "Admin-Bereich erreichbar."
#
# 4. Nur wenn Sicherheitsfreigabe ab 80 ist:
#    Frage nach dem Sicherheitscode.
#
#    Wenn Sicherheitscode == "root123":
#    Ausgabe -> "Hauptsystem geöffnet."
#
#    Sonst:
#    Ausgabe -> "Alarm ausgelöst."
#
# 5. Frage nach der gewählten Aktion:
#    - scan
#    - decrypt
#    - logout
#
# 6. Je nach Aktion soll eine andere Ausgabe kommen.
#
# Bonus:
# Wenn Passwort-Stärke unter 50 ist:
#     Ausgabe -> "Dein eigenes System ist unsicher."
#
# Ziel:
# Baue mehrere nested ifs und verschiedene Enden ein.