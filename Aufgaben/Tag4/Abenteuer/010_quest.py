# =========================
# PYTHON ABENTEUER-AUFGABEN
# RANDOM, SCHLEIFEN,
# LISTEN, TUPLE UND SETS
# =========================


# =========================
# AUFGABE 1
# Münzwurf des Kobolds
# =========================
# Nutze random.random().
# Erzeuge eine Zahl zwischen 0 und 1.
# Wenn die Zahl kleiner als 0.5 ist:
# "Kopf: Der Kobold schenkt dir einen Keks."
# Sonst:
# "Zahl: Der Kobold klaut deinen Schuh."


# =========================
# AUFGABE 2
# Würfel des Drachen
# =========================
# Nutze random.randint(1, 6).
# Lass den Spieler einmal würfeln.
# Gib die gewürfelte Zahl aus.
# Zusatz:
# Wenn eine 6 gewürfelt wird,
# erscheint ein Mini-Drache.


# =========================
# AUFGABE 3
# Goldfund im Wald
# =========================
# Nutze random.randrange(10, 101, 10).
# Der Spieler findet zufällig Gold
# in 10er-Schritten.
# Gib aus, wie viel Gold gefunden wurde.


# =========================
# AUFGABE 4
# Zaubertrank-Stärke
# =========================
# Nutze random.uniform(1.0, 10.0).
# Erzeuge eine zufällige Trankstärke.
# Runde die Zahl auf 2 Nachkommastellen.


# =========================
# AUFGABE 5
# Dreieckiger Orakelwert
# =========================
# Nutze random.triangular(1, 100, 80).
# Das Orakel bevorzugt hohe Werte.
# Gib den Wert als Prozentchance aus.


# =========================
# AUFGABE 6
# Fünf Schatztruhen
# =========================
# Nutze eine for-Schleife.
# Öffne 5 Schatztruhen.
# Jede Truhe enthält zufällig Gold
# mit random.randint(1, 20).
# Am Ende soll die Gesamtsumme
# ausgegeben werden.


# =========================
# AUFGABE 7
# Monster-Würfelrunde
# =========================
# Der Held kämpft 10 Runden.
# In jeder Runde würfelt er Schaden
# mit random.randint(1, 12).
# Speichere jeden Schaden in einer Liste.
# Gib am Ende aus:
# - alle Schadenswerte
# - Gesamtschaden
# - höchsten Schaden


# =========================
# AUFGABE 8
# Flucht aus dem Schleim-Sumpf
# =========================
# Nutze eine while-Schleife.
# Der Spieler würfelt mit
# random.randint(1, 6).
# Solange keine 6 kommt,
# steckt er fest.
# Zähle die Anzahl der Versuche.


# =========================
# AUFGABE 9
# Gold sammeln bis 100
# =========================
# Der Spieler sammelt pro Runde
# zufällig Gold mit
# random.randint(5, 25).
# Solange das Gold unter 100 ist,
# geht das Abenteuer weiter.
# Gib am Ende aus:
# - Anzahl der Runden
# - gesamtes Gold


# =========================
# AUFGABE 10
# Zufälliges Inventar
# =========================
# Erstelle eine Liste mit Items:
# Schwert, Käse, Zauberhut,
# Gummiente und Heiltrank.
# Wähle zufällig ein Item aus.
# Nutze random.randint().


# =========================
# AUFGABE 11
# Monster aus dem Tuple
# =========================
# Erstelle ein Tuple mit Monstern.
# Beispiel:
# Goblin, Schleim, Troll,
# Wütendes Huhn.
# Wähle zufällig ein Monster aus.
# Das Tuple darf nicht verändert werden.


# =========================
# AUFGABE 12
# Seltene Funde im Set
# =========================
# Erstelle ein leeres Set.
# Der Spieler findet 10-mal
# zufällig Items.
# Speichere alles im Set.
# Gib am Ende das Set aus.
# Frage:
# Warum tauchen manche Dinge
# nur einmal auf?


# =========================
# AUFGABE 13
# Abenteuerreise mit Liste
# =========================
# Der Held besucht 7 Orte.
# Nutze eine Liste mit Orten:
# Wald, Höhle, Burg, Sumpf,
# Marktplatz.
# Für jeden Tag wird zufällig
# ein Ort gewählt.
# Speichere alle Orte in einer Liste.
# Gib am Ende aus:
# - Reiseliste
# - wie oft der Wald besucht wurde
# - ob die Burg besucht wurde


# =========================
# AUFGABE 14
# Kampf gegen den Käse-Golem
# =========================
# Der Käse-Golem hat 50 Lebenspunkte.
# Der Spieler greift mit zufälligem
# Schaden an:
# random.randint(5, 15)
# Nutze eine while-Schleife,
# bis der Golem besiegt ist.
# Speichere jeden Angriff
# in einer Liste.
# Gib am Ende aus:
# - Anzahl der Angriffe
# - Angriffsliste
# - stärksten Angriff


# =========================
# AUFGABE 15
# Händler mit schlechten Preisen
# =========================
# Der Händler verkauft 5 Items.
# Für jedes Item wird ein zufälliger
# Preis mit random.uniform(1.5, 99.9)
# erzeugt.
# Speichere die Preise in einer Liste.
# Runde die Preise.
# Berechne zusätzlich
# den Durchschnittspreis.


# =========================
# AUFGABE 16
# Der Dungeon-Generator
# =========================
# Erstelle einen Dungeon
# mit 10 Räumen.
# Nutze ein Tuple mit Raumtypen:
# Monster, Schatz, Falle,
# Leer, Mysteriöse Ente.
# Speichere die Räume in einer Liste.
# Gib am Ende aus:
# - alle Räume
# - Anzahl der Monster-Räume
# - Anzahl der Schatzräume


# =========================
# AUFGABE 17
# Glücksbasierter Bosskampf
# =========================
# Der Boss hat 100 HP.
# Der Spieler startet mit 80 HP.
# In jeder Runde:
# - Spieler macht Schaden mit
#   random.randint(8, 18)
# - Boss macht Schaden mit
#   random.triangular(5, 20, 10)
# Nutze eine while-Schleife.
# Das Spiel endet,
# wenn jemand 0 HP erreicht.
# Gib am Ende aus,
# wer gewonnen hat.


# =========================
# AUFGABE 18
# Loot-System mit Set und Liste
# =========================
# Der Spieler öffnet 20 Truhen.
# Mögliche Items:
# Gold, Trank, Diamant,
# Legendärer Käse.
# Speichere:
# - alle Items in einer Liste
# - einzigartige Items in einem Set
# Gib am Ende aus:
# - komplette Loot-Liste
# - einzigartige Items
# - Anzahl verschiedener Items


# =========================
# AUFGABE 19
# Mini-Rollenspiel:
# Die Quest der Gummiente
# =========================
# Der Spieler startet mit:
# - leben = 100
# - gold = 0
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
# wenn der Spieler stirbt
# oder 100 Gold erreicht.
# Gib am Ende alle Werte aus.


# =========================
# AUFGABE 20
# Der verfluchte Abenteuer-Simulator
# =========================
# Simuliere 100 Abenteuer.
# Jedes Abenteuer hat:
# - zufällige Dauer
# - zufällige Gefahr
# - zufällige Belohnung
# - zufälligen Heldennamen
# - zufälligen Ort
# Speichere erfolgreiche Abenteuer
# in einer Liste.
# Speichere besuchte Orte in einem Set.
# Gib am Ende aus:
# - Anzahl erfolgreicher Abenteuer
# - durchschnittliche Belohnung
# - bester Fund
# - alle besuchten Orte
# - lustigste Niederlage