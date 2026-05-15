# =========================
# MITTELERDE-ABENTEUER-AUFGABEN
# RANDOM, SCHLEIFEN,
# LISTEN, TUPLE UND SETS
# =========================


# =========================
# AUFGABE 1
# Der Ring entscheidet
# =========================
# Nutze random.randint(1, 4).
# Erzeuge eine zufällige Zahl.
# Je nach Zahl passiert etwas:
# 1 = Der Ring flüstert.
# 2 = Ein Hobbit stolpert.
# 3 = Ein Ork niest.
# 4 = Gandalf schaut streng.
# Gib das Ereignis aus.


# =========================
# AUFGABE 2
# Schicksal in Mordor
# =========================
# Nutze random.random().
# Wenn die Zahl kleiner als 0.4 ist:
# "Du schleichst unbemerkt vorbei."
# Sonst:
# "Ein Ork ruft: Wer hat da Kartoffeln gesagt?"


# =========================
# AUFGABE 3
# Lembas-Brot sammeln
# =========================
# Nutze random.randrange(5, 51, 5).
# Die Gefährten finden zufällig
# Lembas-Brote in 5er-Schritten.
# Gib aus, wie viele gefunden wurden.


# =========================
# AUFGABE 4
# Elbischer Zauberwert
# =========================
# Nutze random.uniform(1.0, 10.0).
# Erzeuge eine zufällige
# elbische Zauberstärke.
# Runde auf 2 Nachkommastellen.


# =========================
# AUFGABE 5
# Palantir-Vorhersage
# =========================
# Nutze random.triangular(1, 100, 70).
# Der Palantir bevorzugt hohe Werte.
# Gib die Erfolgswahrscheinlichkeit
# der Mission aus.


# =========================
# AUFGABE 6
# Pfeile von Legolas
# =========================
# Nutze eine for-Schleife.
# Legolas schießt 8 Pfeile.
# Jeder Pfeil verursacht zufälligen
# Schaden mit random.randint(1, 9).
# Speichere alle Werte
# in einem String oder einer Liste.
# Gib das Ergebnis aus.


# =========================
# AUFGABE 7
# Ork-Kampf in Moria
# =========================
# Die Gefährten kämpfen 10 Runden.
# In jeder Runde entsteht Schaden
# mit random.randint(1, 12).
# Speichere alle Schadenswerte
# in einer Liste.
# Gib aus:
# - alle Schadenswerte
# - Gesamtschaden
# - stärksten Treffer


# =========================
# AUFGABE 8
# Tor von Moria öffnen
# =========================
# Nutze eine while-Schleife.
# Solange keine 6 gewürfelt wird,
# bleibt das Tor verschlossen.
# Nutze random.randint(1, 6).
# Zähle die Anzahl der Versuche.
# Bonus-Spruch:
# "Sprich Freund und tritt ein!"


# =========================
# AUFGABE 9
# Reiseproviant sammeln
# =========================
# Die Gefährten sammeln pro Runde
# zufällig Vorräte mit
# random.randint(5, 25).
# Das Ziel sind 100 Vorräte.
# Gib aus:
# - Anzahl der Runden
# - gesamte Vorräte


# =========================
# AUFGABE 10
# Gefährten-Inventar
# =========================
# Erstelle eine Liste mit:
# Ring, Schwert, Lembas,
# Elbenumhang, verdächtige Kartoffel.
# Wähle zufällig ein Item aus.


# =========================
# AUFGABE 11
# Wesen Mittelerdes
# =========================
# Erstelle ein Tuple mit:
# Hobbit, Elb, Zwerg,
# Ork, Balrog,
# sehr beleidigter Ent.
# Wähle zufällig ein Wesen aus.
# Das Tuple darf nicht verändert werden.


# =========================
# AUFGABE 12
# Seltene Funde im Auenland
# =========================
# Erstelle ein leeres Set.
# Die Gefährten finden 10-mal
# zufällige Gegenstände.
# Speichere alles im Set.
# Gib am Ende das Set aus.
# Frage:
# Warum erscheinen manche Dinge
# nur einmal?


# =========================
# AUFGABE 13
# Reise durch Mittelerde
# =========================
# Die Gefährten besuchen 7 Orte.
# Nutze eine Liste mit:
# Auenland, Bruchtal,
# Moria, Rohan,
# Mordor.
# Speichere alle besuchten Orte
# in einer Liste.
# Gib aus:
# - Ortsliste
# - wie oft Mordor besucht wurde
# - ob Bruchtal besucht wurde


# =========================
# AUFGABE 14
# Kampf gegen den Kartoffel-Ork
# =========================
# Der Kartoffel-Ork hat 50 Lebenspunkte.
# Der Held greift mit
# random.randint(5, 15) an.
# Nutze eine while-Schleife,
# bis der Ork besiegt wurde.
# Speichere jeden Angriff
# in einer Liste.
# Gib aus:
# - Anzahl der Angriffe
# - Angriffsliste
# - stärksten Angriff


# =========================
# AUFGABE 15
# Handel in Bree
# =========================
# Der Held kauft 5 Dinge.
# Jedes Ding kostet zufällig
# zwischen 1.5 und 99.9 Silbermünzen.
# Nutze random.uniform().
# Speichere die Preise
# in einer Liste.
# Runde die Preise.
# Berechne den Durchschnitt.


# =========================
# AUFGABE 16
# Moria-Raum-Generator
# =========================
# Erstelle Moria mit 10 Räumen.
# Nutze ein Tuple mit:
# Ork-Raum, Schatzkammer,
# Trollhöhle, Leerer Gang,
# Raum voller singender Zwerge.
# Speichere alles in einer Liste.
# Gib aus:
# - alle Räume
# - Anzahl Ork-Räume
# - Anzahl Schatzkammern


# =========================
# AUFGABE 17
# Duell gegen den Balrog
# =========================
# Der Balrog hat 100 HP.
# Der Held startet mit 80 HP.
# In jeder Runde:
# - Held macht Schaden mit
#   random.randint(8, 18)
# - Balrog macht Schaden mit
#   random.triangular(5, 20, 10)
# Nutze eine while-Schleife.
# Das Spiel endet,
# wenn jemand 0 HP erreicht.
# Gib aus, wer gewonnen hat.
# Optional:
# "Du kommst nicht vorbei!"


# =========================
# AUFGABE 18
# Loot-System in der Zwergentruhe
# =========================
# Öffne 20 Zwergentruhen.
# Mögliche Funde:
# Silber, Lembas,
# Elbenklinge,
# Legendäre Kartoffel.
# Speichere:
# - alle Funde in einer Liste
# - einzigartige Funde in einem Set
# Gib aus:
# - komplette Fundliste
# - einzigartige Funde
# - Anzahl unterschiedlicher Funde


# =========================
# AUFGABE 19
# Mini-Mittelerde-Rollenspiel
# =========================
# Der Held startet mit:
# - leben = 100
# - silber = 0
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
# wenn der Held stirbt
# oder 100 Silber erreicht.
# Gib am Ende alle Werte aus.


# =========================
# AUFGABE 20
# Der verfluchte Mittelerde-Simulator
# =========================
# Simuliere 100 Missionen
# durch Mittelerde.
# Jede Mission hat:
# - zufällige Dauer
# - zufällige Gefahr
# - zufällige Belohnung
# - zufälligen Heldennamen
# - zufälligen Ort
# Speichere erfolgreiche Missionen
# in einer Liste.
# Speichere besuchte Orte
# in einem Set.
# Gib aus:
# - Anzahl erfolgreicher Missionen
# - durchschnittliche Belohnung
# - bester Fund
# - alle besuchten Orte
# - lustigste Niederlage