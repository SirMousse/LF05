# =========================
# TIERHEIM-ABENTEUER-AUFGABEN
# RANDOM, SCHLEIFEN,
# LISTEN, TUPLE UND SETS
# =========================


# =========================
# AUFGABE 1
# Neues Tier angekommen
# =========================
# Nutze random.randint(1, 4).
# Erzeuge eine zufällige Zahl.
# Je nach Zahl kommt an:
# 1 = Hund
# 2 = Katze
# 3 = Kaninchen
# 4 = sehr verwirrte Ziege
# Gib das Tier aus.


# =========================
# AUFGABE 2
# Vermittlungs-Chance
# =========================
# Nutze random.random().
# Wenn die Zahl kleiner als 0.5 ist:
# "Das Tier wurde vermittelt!"
# Sonst:
# "Das Tier klaut erstmal Snacks."


# =========================
# AUFGABE 3
# Futterlieferung
# =========================
# Nutze random.randrange(10, 101, 10).
# Das Tierheim bekommt zufällig
# Futter in 10er-Schritten.
# Gib aus, wie viele Pakete
# angekommen sind.


# =========================
# AUFGABE 4
# Energie-Level eines Welpen
# =========================
# Nutze random.uniform(1.0, 10.0).
# Erzeuge ein zufälliges
# Energie-Level.
# Runde auf 2 Nachkommastellen.


# =========================
# AUFGABE 5
# Tierarzt-Prognose
# =========================
# Nutze random.triangular(1, 100, 80).
# Der Tierarzt bevorzugt hohe Werte.
# Gib die Heilungs-Chance aus.


# =========================
# AUFGABE 6
# Spaziergang-Runden
# =========================
# Nutze eine for-Schleife.
# Ein Hund geht 8-mal spazieren.
# Jeder Spaziergang bringt
# zufällige Freude-Punkte
# mit random.randint(1, 9).
# Speichere alle Werte
# in einem String oder einer Liste.
# Gib das Ergebnis aus.


# =========================
# AUFGABE 7
# Spielstunde im Tierheim
# =========================
# Die Tiere spielen 10 Runden.
# In jeder Runde sammeln sie
# zufällige Spaß-Punkte mit
# random.randint(1, 12).
# Speichere alle Punkte
# in einer Liste.
# Gib aus:
# - alle Punkte
# - Gesamtpunkte
# - höchste Punktzahl


# =========================
# AUFGABE 8
# Die Katze versteckt sich
# =========================
# Nutze eine while-Schleife.
# Solange keine 6 gewürfelt wird,
# bleibt die Katze versteckt.
# Nutze random.randint(1, 6).
# Zähle die Anzahl der Versuche.


# =========================
# AUFGABE 9
# Spenden sammeln
# =========================
# Das Tierheim sammelt pro Runde
# zufällig Spenden mit
# random.randint(5, 25).
# Das Ziel sind 100 Euro.
# Gib aus:
# - Anzahl der Runden
# - gesamte Spenden


# =========================
# AUFGABE 10
# Tierheim-Inventar
# =========================
# Erstelle eine Liste mit:
# Leine, Napf,
# Kuscheldecke, Ball,
# sehr frecher Kater.
# Wähle zufällig ein Item aus.


# =========================
# AUFGABE 11
# Tierarten im Heim
# =========================
# Erstelle ein Tuple mit:
# Hund, Katze, Kaninchen,
# Papagei, Schildkröte,
# dramatisches Meerschweinchen.
# Wähle zufällig ein Tier aus.
# Das Tuple darf nicht verändert werden.


# =========================
# AUFGABE 12
# Seltene Tierfunde
# =========================
# Erstelle ein leeres Set.
# Das Tierheim nimmt 10-mal
# zufällige Tiere auf.
# Speichere alles im Set.
# Gib am Ende das Set aus.
# Frage:
# Warum erscheinen manche Tiere
# nur einmal?


# =========================
# AUFGABE 13
# Rundgang durchs Tierheim
# =========================
# Ein Mitarbeiter besucht 7 Bereiche.
# Nutze eine Liste mit:
# Hundehaus, Katzenzimmer,
# Tierarztzimmer, Spielplatz,
# Futterlager.
# Speichere alle besuchten Orte
# in einer Liste.
# Gib aus:
# - Ortsliste
# - wie oft das Katzenzimmer
#   besucht wurde
# - ob das Futterlager besucht wurde


# =========================
# AUFGABE 14
# Kampf gegen den Staubsauger
# =========================
# Der Staubsauger hat 50 Lebenspunkte.
# Die Katze greift mit
# random.randint(5, 15) an.
# Nutze eine while-Schleife,
# bis der Staubsauger besiegt wurde.
# Speichere jeden Angriff
# in einer Liste.
# Gib aus:
# - Anzahl der Angriffe
# - Angriffsliste
# - stärksten Angriff


# =========================
# AUFGABE 15
# Einkauf fürs Tierheim
# =========================
# Das Tierheim kauft 5 Dinge.
# Jedes Ding kostet zufällig
# zwischen 1.5 und 99.9 Euro.
# Nutze random.uniform().
# Speichere die Preise
# in einer Liste.
# Runde die Preise.
# Berechne den Durchschnitt.


# =========================
# AUFGABE 16
# Tierzimmer-Generator
# =========================
# Erstelle ein Tierheim
# mit 10 Bereichen.
# Nutze ein Tuple mit:
# Hundezimmer, Katzenzimmer,
# Spielraum, Leerer Raum,
# Raum voller quietschender Enten.
# Speichere alles in einer Liste.
# Gib aus:
# - alle Bereiche
# - Anzahl Hundezimmer
# - Anzahl Katzenzimmer


# =========================
# AUFGABE 17
# Duell gegen den Futterdieb
# =========================
# Der Futterdieb hat 100 HP.
# Der Hund startet mit 80 HP.
# In jeder Runde:
# - Hund macht Schaden mit
#   random.randint(8, 18)
# - Futterdieb macht Schaden mit
#   random.triangular(5, 20, 10)
# Nutze eine while-Schleife.
# Das Spiel endet,
# wenn jemand 0 HP erreicht.
# Gib aus, wer gewonnen hat.


# =========================
# AUFGABE 18
# Überraschungsboxen
# =========================
# Öffne 20 Überraschungsboxen.
# Mögliche Funde:
# Leckerli, Spielzeug,
# Kuscheldecke,
# Legendäre Quietscheente.
# Speichere:
# - alle Funde in einer Liste
# - einzigartige Funde in einem Set
# Gib aus:
# - komplette Fundliste
# - einzigartige Funde
# - Anzahl unterschiedlicher Funde


# =========================
# AUFGABE 19
# Mini-Tierheim-Rollenspiel
# =========================
# Der Mitarbeiter startet mit:
# - energie = 100
# - spenden = 0
# - inventar = []
# - besuchte_orte = set()
# Nutze zufällige Orte
# und zufällige Ereignisse.
# Verwende:
# - randint()
# - random()
# - uniform()
# - triangular()
# - randrange()
# Das Spiel endet,
# wenn die Energie leer ist
# oder 100 Euro Spenden erreicht wurden.
# Gib am Ende alle Werte aus.


# =========================
# AUFGABE 20
# Der verfluchte Tierheim-Simulator
# =========================
# Simuliere 100 Tierheim-Tage.
# Jeder Tag hat:
# - zufällige Dauer
# - zufällige Ereignisse
# - zufällige Belohnung
# - zufälligen Mitarbeiternamen
# - zufälligen Bereich
# Speichere erfolgreiche Tage
# in einer Liste.
# Speichere besuchte Orte
# in einem Set.
# Gib aus:
# - Anzahl erfolgreicher Tage
# - durchschnittliche Belohnung
# - bester Fund
# - alle besuchten Orte
# - lustigste Niederlage