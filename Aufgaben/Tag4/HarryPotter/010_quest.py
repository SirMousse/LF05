# =========================
# ZAUBERSCHUL-ABENTEUER-AUFGABEN
# RANDOM, SCHLEIFEN,
# LISTEN, TUPLE UND SETS
# =========================


# =========================
# AUFGABE 1
# Der sprechende Zauberhut
# =========================
# Nutze random.randint(1, 4).
# Erzeuge eine zufällige Zahl.
# Je nach Zahl wird der Schüler
# einem Haus zugeteilt.
# Gib das Haus aus.


# =========================
# AUFGABE 2
# Magischer Zufallstest
# =========================
# Nutze random.random().
# Wenn die Zahl kleiner als 0.4 ist:
# "Der Zauber funktioniert!"
# Sonst:
# "Der Zauber explodiert leicht beleidigt."


# =========================
# AUFGABE 3
# Berties Bohnen
# =========================
# Nutze random.randrange(5, 51, 5).
# Der Schüler findet zufällig Bohnen
# in 5er-Schritten.
# Gib aus, wie viele Bohnen gefunden wurden.


# =========================
# AUFGABE 4
# Zaubertrank-Stärke
# =========================
# Nutze random.uniform(1.0, 10.0).
# Erzeuge eine zufällige
# Zaubertrank-Stärke.
# Runde auf 2 Nachkommastellen.


# =========================
# AUFGABE 5
# Wahrsagekugel
# =========================
# Nutze random.triangular(1, 100, 75).
# Die Kugel bevorzugt hohe Werte.
# Gib die Erfolgswahrscheinlichkeit
# eines Zaubers aus.


# =========================
# AUFGABE 6
# Zauberstab-Funken
# =========================
# Nutze eine for-Schleife.
# Der Zauberstab erzeugt 8 Funken.
# Jeder Funke hat eine zufällige Stärke
# mit random.randint(1, 9).
# Speichere die Funken in einem String
# oder einer Liste.
# Gib das Ergebnis aus.


# =========================
# AUFGABE 7
# Duell-Unterricht
# =========================
# Ein Schüler zaubert 10-mal.
# Jeder Zauber verursacht Schaden
# mit random.randint(1, 12).
# Speichere alle Schadenswerte
# in einer Liste.
# Gib aus:
# - alle Schadenswerte
# - Gesamtschaden
# - stärksten Zauber


# =========================
# AUFGABE 8
# Tür zur verbotenen Abteilung
# =========================
# Nutze eine while-Schleife.
# Solange keine 6 gewürfelt wird,
# bleibt die magische Tür verschlossen.
# Nutze random.randint(1, 6).
# Zähle die Anzahl der Versuche.


# =========================
# AUFGABE 9
# Hauspunkte sammeln
# =========================
# Der Schüler sammelt pro Runde
# zufällig Hauspunkte mit
# random.randint(5, 25).
# Das Spiel endet bei 100 Punkten.
# Gib aus:
# - Anzahl der Runden
# - gesamte Hauspunkte


# =========================
# AUFGABE 10
# Magisches Inventar
# =========================
# Erstelle eine Liste mit:
# Zauberstab, Umhang,
# Schokofrosch, Feder,
# sehr verdächtige Socke.
# Wähle zufällig ein Item aus.


# =========================
# AUFGABE 11
# Magische Wesen
# =========================
# Erstelle ein Tuple mit:
# Eule, Hippogreif,
# Basilisk, Niffler,
# beleidigter Kürbis.
# Wähle zufällig ein Wesen aus.
# Das Tuple darf nicht verändert werden.


# =========================
# AUFGABE 12
# Seltene Zauberfunde
# =========================
# Erstelle ein leeres Set.
# Der Schüler findet 10-mal
# zufällige magische Gegenstände.
# Speichere alles im Set.
# Gib am Ende das Set aus.
# Frage:
# Warum erscheinen manche Dinge
# nur einmal?


# =========================
# AUFGABE 13
# Reise durch die Zauberschule
# =========================
# Der Schüler besucht 7 Orte.
# Nutze eine Liste mit:
# Große Halle, Bibliothek,
# Kerker, Gewächshaus,
# Krankenflügel.
# Speichere alle besuchten Orte
# in einer Liste.
# Gib aus:
# - Ortsliste
# - wie oft die Bibliothek besucht wurde
# - ob der Kerker besucht wurde


# =========================
# AUFGABE 14
# Kampf gegen den Bücher-Troll
# =========================
# Der Bücher-Troll hat 50 Lebenspunkte.
# Der Schüler greift mit
# random.randint(5, 15) an.
# Nutze eine while-Schleife,
# bis der Troll besiegt wurde.
# Speichere jeden Angriff
# in einer Liste.
# Gib aus:
# - Anzahl der Angriffe
# - Angriffsliste
# - stärksten Angriff


# =========================
# AUFGABE 15
# Winkelgasse-Shopping
# =========================
# Der Schüler kauft 5 magische Dinge.
# Jedes Ding kostet zufällig
# zwischen 1.5 und 99.9 Galleonen.
# Nutze random.uniform().
# Speichere die Preise
# in einer Liste.
# Runde die Preise.
# Berechne den Durchschnitt.


# =========================
# AUFGABE 16
# Schlossraum-Generator
# =========================
# Erstelle ein Schloss
# mit 10 Räumen.
# Nutze ein Tuple mit:
# Klassenzimmer, Geheimgang,
# Bibliothek, Kerker,
# Raum voller tanzender Besen.
# Speichere alles in einer Liste.
# Gib aus:
# - alle Räume
# - Anzahl Geheimgänge
# - Anzahl Bibliotheken


# =========================
# AUFGABE 17
# Duell gegen die Schatten-KI
# =========================
# Die Schatten-KI hat 100 HP.
# Der Schüler startet mit 80 HP.
# In jeder Runde:
# - Schüler macht Schaden mit
#   random.randint(8, 18)
# - Schatten-KI macht Schaden mit
#   random.triangular(5, 20, 10)
# Nutze eine while-Schleife.
# Das Spiel endet,
# wenn jemand 0 HP erreicht.
# Gib aus, wer gewonnen hat.


# =========================
# AUFGABE 18
# Loot-System in der Zauberkiste
# =========================
# Öffne 20 Zauberkisten.
# Mögliche Funde:
# Galleone, Schokofrosch,
# Zaubertrank,
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
# Mini-Zauberschul-Rollenspiel
# =========================
# Der Schüler startet mit:
# - leben = 100
# - galleonen = 0
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
# wenn der Schüler stirbt
# oder 100 Galleonen erreicht.
# Gib am Ende alle Werte aus.


# =========================
# AUFGABE 20
# Der verfluchte Zauberschul-Simulator
# =========================
# Simuliere 100 magische Missionen.
# Jede Mission hat:
# - zufällige Dauer
# - zufällige Gefahr
# - zufällige Belohnung
# - zufälligen Schülernamen
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