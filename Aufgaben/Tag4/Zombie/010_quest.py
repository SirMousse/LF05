# =========================
# ZOMBIE-ABENTEUER-AUFGABEN
# RANDOM, SCHLEIFEN,
# LISTEN, TUPLE UND SETS
# =========================


# =========================
# AUFGABE 1
# Zombie entdeckt!
# =========================
# Nutze random.randint(1, 4).
# Erzeuge eine zufällige Zahl.
# Je nach Zahl erscheint:
# 1 = Langsamer Zombie
# 2 = Rennender Zombie
# 3 = Zombie-Huhn
# 4 = Sehr verwirrter Wissenschaftler
# Gib das Ereignis aus.


# =========================
# AUFGABE 2
# Fluchtversuch
# =========================
# Nutze random.random().
# Wenn die Zahl kleiner als 0.5 ist:
# "Du entkommst den Zombies!"
# Sonst:
# "Ein Zombie klaut deinen Snack."


# =========================
# AUFGABE 3
# Vorräte finden
# =========================
# Nutze random.randrange(10, 101, 10).
# Der Überlebende findet zufällig
# Vorräte in 10er-Schritten.
# Gib aus, wie viele Vorräte
# gefunden wurden.


# =========================
# AUFGABE 4
# Waffen-Stärke
# =========================
# Nutze random.uniform(1.0, 10.0).
# Erzeuge eine zufällige
# Waffen-Stärke.
# Runde auf 2 Nachkommastellen.


# =========================
# AUFGABE 5
# Risiko-Scanner
# =========================
# Nutze random.triangular(1, 100, 80).
# Das System bevorzugt hohe Werte.
# Gib die Überlebens-Chance aus.


# =========================
# AUFGABE 6
# Training im Bunker
# =========================
# Nutze eine for-Schleife.
# Der Überlebende trainiert 8-mal.
# Jede Runde bringt zufällige
# Erfahrungspunkte mit
# random.randint(1, 9).
# Speichere alle Werte
# in einem String oder einer Liste.
# Gib das Ergebnis aus.


# =========================
# AUFGABE 7
# Zombie-Kampf
# =========================
# Der Überlebende kämpft 10 Runden.
# In jeder Runde verursacht er Schaden
# mit random.randint(1, 12).
# Speichere alle Schadenswerte
# in einer Liste.
# Gib aus:
# - alle Schadenswerte
# - Gesamtschaden
# - stärksten Treffer


# =========================
# AUFGABE 8
# Bunker-Tür öffnen
# =========================
# Nutze eine while-Schleife.
# Solange keine 6 gewürfelt wird,
# bleibt die Bunker-Tür verschlossen.
# Nutze random.randint(1, 6).
# Zähle die Anzahl der Versuche.


# =========================
# AUFGABE 9
# Essen sammeln
# =========================
# Der Überlebende sammelt pro Runde
# zufällig Nahrung mit
# random.randint(5, 25).
# Das Ziel sind 100 Vorräte.
# Gib aus:
# - Anzahl der Runden
# - gesamte Vorräte


# =========================
# AUFGABE 10
# Überlebenden-Inventar
# =========================
# Erstelle eine Liste mit:
# Taschenlampe, Axt,
# Erste-Hilfe-Set, Funkgerät,
# leicht verdächtige Bohnen.
# Wähle zufällig ein Item aus.


# =========================
# AUFGABE 11
# Arten von Zombies
# =========================
# Erstelle ein Tuple mit:
# Läufer, Tank-Zombie,
# Schleicher, Radioaktiver Zombie,
# Zombie-Clown.
# Wähle zufällig einen Zombie aus.
# Das Tuple darf nicht verändert werden.


# =========================
# AUFGABE 12
# Seltene Funde
# =========================
# Erstelle ein leeres Set.
# Der Überlebende findet 10-mal
# zufällige Gegenstände.
# Speichere alles im Set.
# Gib am Ende das Set aus.
# Frage:
# Warum erscheinen manche Dinge
# nur einmal?


# =========================
# AUFGABE 13
# Reise durch die Ruinenstadt
# =========================
# Der Überlebende besucht 7 Orte.
# Nutze eine Liste mit:
# Krankenhaus, Supermarkt,
# Polizeistation, Bunker,
# Verlassene Schule.
# Speichere alle besuchten Orte
# in einer Liste.
# Gib aus:
# - Ortsliste
# - wie oft der Bunker besucht wurde
# - ob das Krankenhaus besucht wurde


# =========================
# AUFGABE 14
# Kampf gegen den Zombie-Boss
# =========================
# Der Zombie-Boss hat 50 Lebenspunkte.
# Der Überlebende greift mit
# random.randint(5, 15) an.
# Nutze eine while-Schleife,
# bis der Boss besiegt wurde.
# Speichere jeden Angriff
# in einer Liste.
# Gib aus:
# - Anzahl der Angriffe
# - Angriffsliste
# - stärksten Angriff


# =========================
# AUFGABE 15
# Handel im Bunker
# =========================
# Der Überlebende kauft 5 Dinge.
# Jedes Ding kostet zufällig
# zwischen 1.5 und 99.9 Kronkorken.
# Nutze random.uniform().
# Speichere die Preise
# in einer Liste.
# Runde die Preise.
# Berechne den Durchschnitt.


# =========================
# AUFGABE 16
# Zufälliger Bunker-Generator
# =========================
# Erstelle einen Bunker
# mit 10 Räumen.
# Nutze ein Tuple mit:
# Schlafraum, Vorratsraum,
# Waffenlager, Leerer Raum,
# Raum voller Zombiesocken.
# Speichere alles in einer Liste.
# Gib aus:
# - alle Räume
# - Anzahl Schlafräume
# - Anzahl Waffenlager


# =========================
# AUFGABE 17
# Duell gegen den Mutanten
# =========================
# Der Mutant hat 100 HP.
# Der Überlebende startet mit 80 HP.
# In jeder Runde:
# - Überlebender macht Schaden mit
#   random.randint(8, 18)
# - Mutant macht Schaden mit
#   random.triangular(5, 20, 10)
# Nutze eine while-Schleife.
# Das Spiel endet,
# wenn jemand 0 HP erreicht.
# Gib aus, wer gewonnen hat.


# =========================
# AUFGABE 18
# Loot-System im verlassenen Haus
# =========================
# Öffne 20 Kisten.
# Mögliche Funde:
# Munition, Wasser,
# Medizin,
# Legendäre Bohnen.
# Speichere:
# - alle Funde in einer Liste
# - einzigartige Funde in einem Set
# Gib aus:
# - komplette Fundliste
# - einzigartige Funde
# - Anzahl unterschiedlicher Funde


# =========================
# AUFGABE 19
# Mini-Zombie-Rollenspiel
# =========================
# Der Überlebende startet mit:
# - leben = 100
# - vorräte = 0
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
# wenn der Überlebende besiegt wird
# oder 100 Vorräte erreicht.
# Gib am Ende alle Werte aus.


# =========================
# AUFGABE 20
# Der verfluchte Zombie-Simulator
# =========================
# Simuliere 100 Überlebens-Missionen.
# Jede Mission hat:
# - zufällige Dauer
# - zufällige Gefahr
# - zufällige Belohnung
# - zufälligen Überlebenden-Namen
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