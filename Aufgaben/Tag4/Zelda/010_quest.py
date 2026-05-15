# =========================
# ZELDA-ABENTEUER-AUFGABEN
# RANDOM, SCHLEIFEN,
# LISTEN, TUPLE UND SETS
# =========================


# =========================
# AUFGABE 1
# Ein wildes Abenteuer beginnt
# =========================
# Nutze random.randint(1, 4).
# Erzeuge eine zufällige Zahl.
# Je nach Zahl passiert:
# 1 = Link findet einen Rubin.
# 2 = Navi ruft: Hey!
# 3 = Ein Huhn schaut verdächtig.
# 4 = Eine Truhe erscheint.
# Gib das Ereignis aus.


# =========================
# AUFGABE 2
# Truhe öffnen
# =========================
# Nutze random.random().
# Wenn die Zahl kleiner als 0.5 ist:
# "Du findest einen Schatz!"
# Sonst:
# "Die Truhe ist leer. Sehr unhöflich."


# =========================
# AUFGABE 3
# Rubine sammeln
# =========================
# Nutze random.randrange(5, 101, 5).
# Link findet zufällig Rubine
# in 5er-Schritten.
# Gib aus, wie viele Rubine
# gefunden wurden.


# =========================
# AUFGABE 4
# Schwert-Stärke
# =========================
# Nutze random.uniform(1.0, 10.0).
# Erzeuge eine zufällige
# Schwert-Stärke.
# Runde auf 2 Nachkommastellen.


# =========================
# AUFGABE 5
# Sheikah-Stein-Orakel
# =========================
# Nutze random.triangular(1, 100, 75).
# Das Orakel bevorzugt hohe Werte.
# Gib die Erfolgswahrscheinlichkeit
# der Mission aus.


# =========================
# AUFGABE 6
# Bogen-Training
# =========================
# Nutze eine for-Schleife.
# Link schießt 8 Pfeile.
# Jeder Pfeil verursacht zufälligen
# Schaden mit random.randint(1, 9).
# Speichere alle Werte
# in einem String oder einer Liste.
# Gib das Ergebnis aus.


# =========================
# AUFGABE 7
# Kampf gegen Bokblins
# =========================
# Link kämpft 10 Runden.
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
# Schrein öffnen
# =========================
# Nutze eine while-Schleife.
# Solange keine 6 gewürfelt wird,
# bleibt der Schrein verschlossen.
# Nutze random.randint(1, 6).
# Zähle die Anzahl der Versuche.


# =========================
# AUFGABE 9
# Ausdauer sammeln
# =========================
# Link sammelt pro Runde
# zufällig Ausdauerpunkte mit
# random.randint(5, 25).
# Das Ziel sind 100 Ausdauerpunkte.
# Gib aus:
# - Anzahl der Runden
# - gesamte Ausdauerpunkte


# =========================
# AUFGABE 10
# Links Inventar
# =========================
# Erstelle eine Liste mit:
# Schwert, Schild,
# Bogen, Bombe,
# sehr verdächtiges Huhn.
# Wähle zufällig ein Item aus.


# =========================
# AUFGABE 11
# Völker von Hyrule
# =========================
# Erstelle ein Tuple mit:
# Hylianer, Zora,
# Gorone, Gerudo,
# Krogs, beleidigtes Huhn.
# Wähle zufällig ein Volk aus.
# Das Tuple darf nicht verändert werden.


# =========================
# AUFGABE 12
# Seltene Funde in Hyrule
# =========================
# Erstelle ein leeres Set.
# Link findet 10-mal
# zufällige Gegenstände.
# Speichere alles im Set.
# Gib am Ende das Set aus.
# Frage:
# Warum erscheinen manche Dinge
# nur einmal?


# =========================
# AUFGABE 13
# Reise durch Hyrule
# =========================
# Link besucht 7 Orte.
# Nutze eine Liste mit:
# Kokiri-Wald, Todesberg,
# Hylia-See, Schloss Hyrule,
# Kakariko.
# Speichere alle besuchten Orte
# in einer Liste.
# Gib aus:
# - Ortsliste
# - wie oft Kakariko besucht wurde
# - ob Schloss Hyrule besucht wurde


# =========================
# AUFGABE 14
# Kampf gegen den Hühner-Schwarm
# =========================
# Der Hühner-Schwarm hat 50 Lebenspunkte.
# Link greift mit
# random.randint(5, 15) an.
# Nutze eine while-Schleife,
# bis der Schwarm besiegt wurde.
# Speichere jeden Angriff
# in einer Liste.
# Gib aus:
# - Anzahl der Angriffe
# - Angriffsliste
# - stärksten Angriff


# =========================
# AUFGABE 15
# Einkauf beim fahrenden Händler
# =========================
# Link kauft 5 Dinge.
# Jedes Ding kostet zufällig
# zwischen 1.5 und 99.9 Rubine.
# Nutze random.uniform().
# Speichere die Preise
# in einer Liste.
# Runde die Preise.
# Berechne den Durchschnitt.


# =========================
# AUFGABE 16
# Dungeon-Generator
# =========================
# Erstelle einen Dungeon
# mit 10 Räumen.
# Nutze ein Tuple mit:
# Bokblin-Raum, Schatzraum,
# Rätselraum, Leerer Gang,
# Raum voller wütender Hühner.
# Speichere alles in einer Liste.
# Gib aus:
# - alle Räume
# - Anzahl Bokblin-Räume
# - Anzahl Schatzräume


# =========================
# AUFGABE 17
# Duell gegen Ganons Schatten
# =========================
# Ganons Schatten hat 100 HP.
# Link startet mit 80 HP.
# In jeder Runde:
# - Link macht Schaden mit
#   random.randint(8, 18)
# - Ganons Schatten macht Schaden mit
#   random.triangular(5, 20, 10)
# Nutze eine while-Schleife.
# Das Spiel endet,
# wenn jemand 0 HP erreicht.
# Gib aus, wer gewonnen hat.


# =========================
# AUFGABE 18
# Loot-System im Tempel
# =========================
# Öffne 20 Tempeltruhen.
# Mögliche Funde:
# Rubin, Bombe,
# Herzteil,
# Legendäres Huhn.
# Speichere:
# - alle Funde in einer Liste
# - einzigartige Funde in einem Set
# Gib aus:
# - komplette Fundliste
# - einzigartige Funde
# - Anzahl unterschiedlicher Funde


# =========================
# AUFGABE 19
# Mini-Hyrule-Rollenspiel
# =========================
# Link startet mit:
# - leben = 100
# - rubine = 0
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
# wenn Link besiegt wird
# oder 100 Rubine erreicht.
# Gib am Ende alle Werte aus.


# =========================
# AUFGABE 20
# Der verfluchte Hyrule-Simulator
# =========================
# Simuliere 100 Hyrule-Missionen.
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