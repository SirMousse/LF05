# -----------------------------------
# Aufgabe 1 — While-Schleife
# Thema: Mana aufladen
# -----------------------------------

# Schreibe ein Programm:
#
# - Der Spieler startet mit 0 Mana
mana = 0

# - Solange das Mana kleiner als 100 ist:
while mana < 100:
#     - soll "Mana wird aufgeladen..." ausgegeben werden
    print(f"Mana wird aufgeladen...{mana}")
    
#     - das Mana soll um 20 erhöht werden
    mana += 20

# - Wenn das Mana voll ist:
#     - soll "Zauber bereit!" ausgegeben werden
print("Zauber bereit!")


# -----------------------------------
# Aufgabe 2 — For-Schleife
# Thema: Dungeon
# -----------------------------------

# Schreibe ein Programm:
#
# - Die Schleife soll 5-mal laufen
for x in range(5):
# - Bei jedem Durchlauf:
#     - "Gegner wurde besiegt" ausgeben
    print("Gegner wurde besiegt")
# - Nach der Schleife:
#     - "Dungeon abgeschlossen" ausgeben
print("Dungeon abgeschlossen")

# Bonus:
# - Gib zusätzlich die Nummer des Gegners aus
#   Beispiel:
#   Gegner 1 wurde besiegt
#   Gegner 2 wurde besiegt

for diva in range(1, 6):
    # Bonus:
    # - Gib zusätzlich die Nummer des Gegners aus
    #   Beispiel:
    #   Gegner 1 wurde besiegt
    #   Gegner 2 wurde besiegt
    print(f"Gegner {diva} wurde besiegt")

print("Dungeon abgeschlossen")

