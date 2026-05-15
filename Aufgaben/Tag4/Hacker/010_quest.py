# =========================
# HACKER-ABENTEUER-AUFGABEN
# RANDOM, SCHLEIFEN,
# LISTEN, TUPLE UND SETS
# =========================


# =========================
# AUFGABE 1
# Der geheime Login-Code
# =========================
# Nutze random.randint(1000, 9999).
# Erzeuge einen zufälligen
# vierstelligen Hacker-Code.
# Gib den Code aus.


# =========================
# AUFGABE 2
# Firewall-Zufallstest
# =========================
# Nutze random.random().
# Wenn die Zahl kleiner als 0.3 ist:
# "Firewall entdeckt!"
# Sonst:
# "Du bist unbemerkt geblieben."


# =========================
# AUFGABE 3
# Datenpakete scannen
# =========================
# Nutze random.randrange(50, 501, 50).
# Simuliere zufällige Datenpakete
# in 50er-Schritten.
# Gib die Paketgröße aus.


# =========================
# AUFGABE 4
# Netzwerkgeschwindigkeit
# =========================
# Nutze random.uniform(10.0, 1000.0).
# Simuliere eine zufällige
# Downloadgeschwindigkeit.
# Runde auf 2 Nachkommastellen.


# =========================
# AUFGABE 5
# KI-Risikoanalyse
# =========================
# Nutze random.triangular(1, 100, 90).
# Die KI bevorzugt hohe Gefahrwerte.
# Gib die Risiko-Prozentzahl aus.


# =========================
# AUFGABE 6
# Passwort-Generator
# =========================
# Nutze eine for-Schleife.
# Erzeuge ein Passwort
# mit 8 zufälligen Zahlen.
# Speichere alles in einem String.
# Gib das Passwort aus.


# =========================
# AUFGABE 7
# Virus-Angriffe speichern
# =========================
# Der Hacker startet 10 Angriffe.
# Jeder Angriff verursacht
# zufälligen Schaden mit
# random.randint(1, 50).
# Speichere alle Schäden
# in einer Liste.
# Gib aus:
# - alle Schäden
# - Gesamtschaden
# - höchsten Schaden


# =========================
# AUFGABE 8
# Server knacken
# =========================
# Nutze eine while-Schleife.
# Solange keine 6 gewürfelt wird,
# bleibt der Server gesichert.
# Nutze random.randint(1, 6).
# Zähle die Anzahl der Versuche.


# =========================
# AUFGABE 9
# Kryptowährung farmen
# =========================
# Der Hacker farmt Coins.
# Pro Runde erhält er zufällig
# zwischen 5 und 25 Coins.
# Nutze random.randint().
# Das Spiel endet bei 100 Coins.
# Gib aus:
# - Anzahl der Runden
# - gesamte Coins


# =========================
# AUFGABE 10
# Hacker-Inventar
# =========================
# Erstelle eine Liste mit:
# Laptop, USB-Stick,
# Energy Drink, Gummiente,
# Linux-CD.
# Wähle zufällig ein Item aus.


# =========================
# AUFGABE 11
# Sicherheitsprogramme
# =========================
# Erstelle ein Tuple mit:
# Firewall, Antivirus,
# Trojaner-Scanner,
# Passwortschutz.
# Wähle zufällig
# ein Sicherheitsprogramm aus.


# =========================
# AUFGABE 12
# Seltene Datenfunde
# =========================
# Erstelle ein leeres Set.
# Der Hacker findet 10-mal
# zufällige Dateien.
# Speichere alles im Set.
# Gib am Ende das Set aus.
# Frage:
# Warum erscheinen manche
# Dateien nur einmal?


# =========================
# AUFGABE 13
# Reise durchs Darknet
# =========================
# Der Hacker besucht 7 Server.
# Nutze eine Liste mit:
# EU-Server, US-Server,
# Geheimserver, Testserver,
# Meme-Server.
# Speichere alle besuchten
# Server in einer Liste.
# Gib aus:
# - Serverliste
# - wie oft der Geheimserver
#   besucht wurde
# - ob der Meme-Server besucht wurde


# =========================
# AUFGABE 14
# Kampf gegen die Killer-KI
# =========================
# Die KI hat 50 Lebenspunkte.
# Der Hacker greift mit
# random.randint(5, 15) an.
# Nutze eine while-Schleife,
# bis die KI besiegt wurde.
# Speichere jeden Angriff
# in einer Liste.
# Gib aus:
# - Anzahl der Angriffe
# - Angriffsliste
# - stärksten Angriff


# =========================
# AUFGABE 15
# Schwarzer Markt
# =========================
# Der Hacker kauft 5 Tools.
# Jedes Tool kostet zufällig
# zwischen 1.5 und 99.9 Coins.
# Nutze random.uniform().
# Speichere die Preise
# in einer Liste.
# Runde die Preise.
# Berechne den Durchschnitt.


# =========================
# AUFGABE 16
# Netzwerk-Generator
# =========================
# Erstelle ein Netzwerk
# mit 10 Servern.
# Nutze ein Tuple mit:
# Firewall, Datenbank,
# KI-Knoten, Leerer Server,
# Verdächtige Gummiente.
# Speichere alles in einer Liste.
# Gib aus:
# - alle Server
# - Anzahl Firewalls
# - Anzahl Datenbanken


# =========================
# AUFGABE 17
# Hacker gegen Super-KI
# =========================
# Die Super-KI hat 100 HP.
# Der Hacker startet mit 80 HP.
# In jeder Runde:
# - Hacker macht Schaden mit
#   random.randint(8, 18)
# - KI macht Schaden mit
#   random.triangular(5, 20, 10)
# Nutze eine while-Schleife.
# Das Spiel endet,
# wenn jemand 0 HP erreicht.
# Gib aus, wer gewonnen hat.


# =========================
# AUFGABE 18
# Loot-System im Darknet
# =========================
# Öffne 20 Datenpakete.
# Mögliche Funde:
# Bitcoin, Passwort,
# Geheime Datei,
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
# Mini-Hacker-Rollenspiel
# =========================
# Der Hacker startet mit:
# - leben = 100
# - coins = 0
# - inventar = []
# - besuchte_server = set()
# Nutze zufällige Server
# und zufällige Ereignisse.
# Verwende:
# - randint()
# - random()
# - uniform()
# - triangular()
# - randrange()
# Das Spiel endet,
# wenn der Hacker stirbt
# oder 100 Coins erreicht.
# Gib am Ende alle Werte aus.


# =========================
# AUFGABE 20
# Der verfluchte Hacker-Simulator
# =========================
# Simuliere 100 Hacker-Missionen.
# Jede Mission hat:
# - zufällige Dauer
# - zufällige Gefahr
# - zufällige Belohnung
# - zufälligen Hacker-Namen
# - zufälligen Server
# Speichere erfolgreiche Missionen
# in einer Liste.
# Speichere besuchte Server
# in einem Set.
# Gib aus:
# - Anzahl erfolgreicher Missionen
# - durchschnittliche Belohnung
# - bester Fund
# - alle besuchten Server
# - lustigste Niederlage