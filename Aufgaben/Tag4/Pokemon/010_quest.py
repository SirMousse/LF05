# =========================
# POKEMON-ABENTEUER-AUFGABEN
# RANDOM, SCHLEIFEN,
# LISTEN, TUPLE UND SETS
# =========================


# =========================
# AUFGABE 1
# Das wilde Pokemon erscheint
# =========================
# Nutze random.randint(1, 4).
# Erzeuge eine zufällige Zahl.
# Je nach Zahl erscheint:
# 1 = Pikachu
# 2 = Glumanda
# 3 = Bisasam
# 4 = Schiggy
# Gib das Pokemon aus.


# =========================
# AUFGABE 2
# Pokeball-Wurf
# =========================
# Nutze random.random().
# Wenn die Zahl kleiner als 0.5 ist:
# "Gefangen!"
# Sonst:
# "Oh nein! Das Pokemon ist ausgebrochen."


# =========================
# AUFGABE 3
# Pokemünzen sammeln
# =========================
# Nutze random.randrange(10, 101, 10).
# Der Trainer findet zufällig
# Pokemünzen in 10er-Schritten.
# Gib aus, wie viele Münzen
# gefunden wurden.


# =========================
# AUFGABE 4
# Attacken-Stärke
# =========================
# Nutze random.uniform(1.0, 10.0).
# Erzeuge eine zufällige
# Attacken-Stärke.
# Runde auf 2 Nachkommastellen.


# =========================
# AUFGABE 5
# Pokedex-Analyse
# =========================
# Nutze random.triangular(1, 100, 70).
# Der Pokedex bevorzugt höhere Werte.
# Gib die Erfolgswahrscheinlichkeit
# einer Attacke aus.


# =========================
# AUFGABE 6
# Trainingsrunde
# =========================
# Nutze eine for-Schleife.
# Dein Pokemon trainiert 8-mal.
# Jede Trainingseinheit bringt
# zufällige Erfahrungspunkte
# mit random.randint(1, 9).
# Speichere alle Werte
# in einem String oder einer Liste.
# Gib das Ergebnis aus.


# =========================
# AUFGABE 7
# Arena-Kampf
# =========================
# Dein Pokemon kämpft 10 Runden.
# In jeder Runde verursacht es Schaden
# mit random.randint(1, 12).
# Speichere alle Schadenswerte
# in einer Liste.
# Gib aus:
# - alle Schadenswerte
# - Gesamtschaden
# - stärkste Attacke


# =========================
# AUFGABE 8
# Pokemon fangen
# =========================
# Nutze eine while-Schleife.
# Solange keine 6 gewürfelt wird,
# springt das Pokemon aus dem Pokeball.
# Nutze random.randint(1, 6).
# Zähle die Anzahl der Versuche.


# =========================
# AUFGABE 9
# Erfahrungspunkte sammeln
# =========================
# Dein Pokemon sammelt pro Runde
# zufällig EP mit
# random.randint(5, 25).
# Das Ziel sind 100 EP.
# Gib aus:
# - Anzahl der Runden
# - gesamte EP


# =========================
# AUFGABE 10
# Trainer-Inventar
# =========================
# Erstelle eine Liste mit:
# Pokeball, Trank,
# Beere, Fahrrad,
# sehr verdächtiger Karpador.
# Wähle zufällig ein Item aus.


# =========================
# AUFGABE 11
# Pokemon-Typen
# =========================
# Erstelle ein Tuple mit:
# Feuer, Wasser, Pflanze,
# Elektro, Geist,
# sehr verwirrter Käfer.
# Wähle zufällig einen Typ aus.
# Das Tuple darf nicht verändert werden.


# =========================
# AUFGABE 12
# Seltene Pokemon-Funde
# =========================
# Erstelle ein leeres Set.
# Der Trainer begegnet 10-mal
# zufälligen Pokemon.
# Speichere alles im Set.
# Gib am Ende das Set aus.
# Frage:
# Warum erscheinen manche Pokemon
# nur einmal?


# =========================
# AUFGABE 13
# Reise durch die Region
# =========================
# Der Trainer besucht 7 Orte.
# Nutze eine Liste mit:
# Alabastia, Vertania,
# Azuria, Lavandia,
# Pokecenter.
# Speichere alle besuchten Orte
# in einer Liste.
# Gib aus:
# - Ortsliste
# - wie oft das Pokecenter besucht wurde
# - ob Lavandia besucht wurde


# =========================
# AUFGABE 14
# Kampf gegen Team Fehler
# =========================
# Team Fehler hat 50 Lebenspunkte.
# Dein Pokemon greift mit
# random.randint(5, 15) an.
# Nutze eine while-Schleife,
# bis Team Fehler besiegt wurde.
# Speichere jeden Angriff
# in einer Liste.
# Gib aus:
# - Anzahl der Angriffe
# - Angriffsliste
# - stärksten Angriff


# =========================
# AUFGABE 15
# Einkauf im Pokemon-Markt
# =========================
# Der Trainer kauft 5 Items.
# Jedes Item kostet zufällig
# zwischen 1.5 und 99.9 Pokemünzen.
# Nutze random.uniform().
# Speichere die Preise
# in einer Liste.
# Runde die Preise.
# Berechne den Durchschnitt.


# =========================
# AUFGABE 16
# Höhlen-Generator
# =========================
# Erstelle eine Höhle
# mit 10 Bereichen.
# Nutze ein Tuple mit:
# Zubat-Raum, Schatz-Ecke,
# Trainer-Kampf, Leerer Gang,
# Raum voller singender Enton.
# Speichere alles in einer Liste.
# Gib aus:
# - alle Bereiche
# - Anzahl Zubat-Räume
# - Anzahl Schatz-Ecken


# =========================
# AUFGABE 17
# Duell gegen das legendäre Pokemon
# =========================
# Das legendäre Pokemon hat 100 HP.
# Dein Pokemon startet mit 80 HP.
# In jeder Runde:
# - Dein Pokemon macht Schaden mit
#   random.randint(8, 18)
# - Legendäres Pokemon macht Schaden mit
#   random.triangular(5, 20, 10)
# Nutze eine while-Schleife.
# Das Spiel endet,
# wenn jemand 0 HP erreicht.
# Gib aus, wer gewonnen hat.


# =========================
# AUFGABE 18
# Loot-System im Pokecenter
# =========================
# Öffne 20 Geschenkboxen.
# Mögliche Funde:
# Pokeball, Trank,
# Sonderbonbon,
# Legendäre Socke.
# Speichere:
# - alle Funde in einer Liste
# - einzigartige Funde in einem Set
# Gib aus:
# - komplette Fundliste
# - einzigartige Funde
# - Anzahl unterschiedlicher Funde


# =========================
# AUFGABE 19
# Mini-Pokemon-Rollenspiel
# =========================
# Der Trainer startet mit:
# - leben = 100
# - pokemuenzen = 0
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
# wenn der Trainer verliert
# oder 100 Pokemünzen erreicht.
# Gib am Ende alle Werte aus.


# =========================
# AUFGABE 20
# Der verfluchte Pokemon-Simulator
# =========================
# Simuliere 100 Trainer-Missionen.
# Jede Mission hat:
# - zufällige Dauer
# - zufällige Gefahr
# - zufällige Belohnung
# - zufälligen Trainernamen
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