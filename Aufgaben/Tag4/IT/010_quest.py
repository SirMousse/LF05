# =========================
# IT-ABENTEUER-AUFGABEN
# RANDOM, SCHLEIFEN,
# LISTEN, TUPLE UND SETS
# =========================


# =========================
# AUFGABE 1
# Der zufällige Support-Fall
# =========================
# Nutze random.randint(1, 4).
# Erzeuge eine zufällige Zahl.
# Je nach Zahl passiert etwas:
# 1 = Drucker streikt.
# 2 = WLAN ist beleidigt.
# 3 = Passwort wurde vergessen.
# 4 = Tastatur macht Kunst.
# Gib das Ereignis aus.


# =========================
# AUFGABE 2
# Server-Status
# =========================
# Nutze random.random().
# Wenn die Zahl kleiner als 0.4 ist:
# "Server läuft stabil."
# Sonst:
# "Server macht kurz dramatische Geräusche."


# =========================
# AUFGABE 3
# Tickets bearbeiten
# =========================
# Nutze random.randrange(5, 51, 5).
# Das IT-Team bekommt zufällig Tickets
# in 5er-Schritten.
# Gib aus, wie viele Tickets
# angekommen sind.


# =========================
# AUFGABE 4
# Download-Geschwindigkeit
# =========================
# Nutze random.uniform(1.0, 100.0).
# Erzeuge eine zufällige
# Download-Geschwindigkeit in MB/s.
# Runde auf 2 Nachkommastellen.


# =========================
# AUFGABE 5
# System-Risikoanalyse
# =========================
# Nutze random.triangular(1, 100, 75).
# Das System bevorzugt höhere Werte.
# Gib die Risiko-Prozentzahl aus.


# =========================
# AUFGABE 6
# Acht Log-Einträge
# =========================
# Nutze eine for-Schleife.
# Erzeuge 8 zufällige Log-Level.
# Jeder Log-Level ist eine Zahl
# von 1 bis 9 mit random.randint(1, 9).
# Speichere alle Werte
# in einem String oder einer Liste.
# Gib das Ergebnis aus.


# =========================
# AUFGABE 7
# Bug-Jagd im Code
# =========================
# Das IT-Team prüft 10 Dateien.
# In jeder Datei werden zufällig
# Bugs gefunden mit random.randint(1, 12).
# Speichere alle Bug-Zahlen
# in einer Liste.
# Gib aus:
# - alle Bug-Zahlen
# - Gesamtzahl der Bugs
# - höchste Bug-Zahl


# =========================
# AUFGABE 8
# Router neu starten
# =========================
# Nutze eine while-Schleife.
# Solange keine 6 gewürfelt wird,
# startet der Router weiter neu.
# Nutze random.randint(1, 6).
# Zähle die Anzahl der Versuche.
# Bonus-Ausgabe:
# "Haben Sie ihn schon aus- und eingeschaltet?"


# =========================
# AUFGABE 9
# Speicherplatz freiräumen
# =========================
# Das System räumt pro Runde
# zufällig Speicher frei mit
# random.randint(5, 25).
# Das Ziel sind 100 GB.
# Gib aus:
# - Anzahl der Runden
# - freigeräumter Speicher


# =========================
# AUFGABE 10
# IT-Inventar
# =========================
# Erstelle eine Liste mit:
# Laptop, Maus, Tastatur,
# USB-Stick, sehr müder Drucker.
# Wähle zufällig ein Item aus.


# =========================
# AUFGABE 11
# Netzwerkgeräte
# =========================
# Erstelle ein Tuple mit:
# Router, Switch, Server,
# Access Point, beleidigter Drucker.
# Wähle zufällig ein Gerät aus.
# Das Tuple darf nicht verändert werden.


# =========================
# AUFGABE 12
# Einzigartige Fehlermeldungen
# =========================
# Erstelle ein leeres Set.
# Das System erzeugt 10-mal
# zufällige Fehlermeldungen.
# Speichere alles im Set.
# Gib am Ende das Set aus.
# Frage:
# Warum erscheinen manche Fehler
# nur einmal?


# =========================
# AUFGABE 13
# Reise durchs Firmennetzwerk
# =========================
# Der Admin besucht 7 Systeme.
# Nutze eine Liste mit:
# Mailserver, Datenbank,
# Webserver, Backup-System,
# Meme-Ordner.
# Speichere alle besuchten Systeme
# in einer Liste.
# Gib aus:
# - Systemliste
# - wie oft die Datenbank besucht wurde
# - ob der Meme-Ordner besucht wurde


# =========================
# AUFGABE 14
# Kampf gegen den Bug-Golem
# =========================
# Der Bug-Golem hat 50 Lebenspunkte.
# Der Admin greift mit
# random.randint(5, 15) an.
# Nutze eine while-Schleife,
# bis der Bug-Golem besiegt wurde.
# Speichere jeden Angriff
# in einer Liste.
# Gib aus:
# - Anzahl der Angriffe
# - Angriffsliste
# - stärksten Angriff


# =========================
# AUFGABE 15
# IT-Einkauf
# =========================
# Das Team kauft 5 Geräte.
# Jedes Gerät kostet zufällig
# zwischen 1.5 und 99.9 Credits.
# Nutze random.uniform().
# Speichere die Preise
# in einer Liste.
# Runde die Preise.
# Berechne den Durchschnitt.


# =========================
# AUFGABE 16
# Serverraum-Generator
# =========================
# Erstelle einen Serverraum
# mit 10 Bereichen.
# Nutze ein Tuple mit:
# Rack, Switch-Schrank,
# Backup-Ecke, Leerer Platz,
# Raum voller Kabelsalat.
# Speichere alles in einer Liste.
# Gib aus:
# - alle Bereiche
# - Anzahl Racks
# - Anzahl Switch-Schränke


# =========================
# AUFGABE 17
# Duell gegen die Absturz-KI
# =========================
# Die Absturz-KI hat 100 HP.
# Der Admin startet mit 80 HP.
# In jeder Runde:
# - Admin macht Schaden mit
#   random.randint(8, 18)
# - KI macht Schaden mit
#   random.triangular(5, 20, 10)
# Nutze eine while-Schleife.
# Das Spiel endet,
# wenn jemand 0 HP erreicht.
# Gib aus, wer gewonnen hat.


# =========================
# AUFGABE 18
# Loot-System im Serverraum
# =========================
# Öffne 20 Hardware-Kisten.
# Mögliche Funde:
# RAM, SSD,
# Netzwerkkabel,
# Legendäre Gummiente.
# Speichere:
# - alle Funde in einer Liste
# - einzigartige Funde in einem Set
# Gib aus:
# - komplette Fundliste
# - einzigartige Funde
# - Anzahl unterschiedlicher Funde


# =========================
# AUFGABE 19
# Mini-IT-Rollenspiel
# =========================
# Der Admin startet mit:
# - leben = 100
# - credits = 0
# - inventar = []
# - besuchte_systeme = set()
# Nutze zufällige Systeme
# und zufällige Ereignisse.
# Verwende:
# - randint()
# - random()
# - uniform()
# - triangular()
# - randrange()
# Das Spiel endet,
# wenn der Admin abstürzt
# oder 100 Credits erreicht.
# Gib am Ende alle Werte aus.


# =========================
# AUFGABE 20
# Der verfluchte IT-Simulator
# =========================
# Simuliere 100 IT-Missionen.
# Jede Mission hat:
# - zufällige Dauer
# - zufällige Gefahr
# - zufällige Belohnung
# - zufälligen Admin-Namen
# - zufälliges System
# Speichere erfolgreiche Missionen
# in einer Liste.
# Speichere besuchte Systeme
# in einem Set.
# Gib aus:
# - Anzahl erfolgreicher Missionen
# - durchschnittliche Belohnung
# - bester Fund
# - alle besuchten Systeme
# - lustigste Niederlage