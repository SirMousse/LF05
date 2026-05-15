name1 = "Bello"
name2 = "Sir Fluffilot"
name3 = "Socken Zerstörer"

# Listen
tiere = ["Hund", "Katze", "Hamster", "Maus"]

# Einzeln
print(tiere[0])     # Hund
print(tiere[1])     # Katze
print(tiere[2])     # Hamster
print(tiere[3])     # Maus

# Gesamt
print(tiere)

# Letzte Elemt holen
# Negative Zahlen zählen von hinten
print(tiere[-1])    # Maus

# Rückwerts ausgeben der iste durch for-Schleife
for tier in reversed(tiere):            # reversed() -> dreht die Reihenfolge meiner Liste um
    print(tier)

# Listen Elemente hinzufügen
# .append() -> fügst du ein neues Tier HINTEN an der Liste an
# append = hinten rangehängt an die Liste
tiere.append("Ziege")

print(tiere)

# Elemente auch an bestimmen Positionen einfügen
# .insert() -> kannst ein Tier an eine bestimmte Position einfügen
tiere.insert(1, "Papagei")

print(tiere)

# Slicing -> mehrer Elemente an mehreren Positionen
# listenname[start:ende]-> start:ende ist der Bereich wo wir die Elemente einfügen
# davor -> ['Hund', 'Papagei', 'Katze', 'Hamster', 'Maus', 'Ziege']
tiere[2:2] = ["Alpaka", "Lama"]
# danach -> ['Hund', 'Papagei', 'Alpaka', 'Lama', 'Katze', 'Hamster', 'Maus', 'Ziege']

# wenn es tiere[2:3] wäre -> überschreibt es Index 3 (die 0,1,2,3 Stelle!)/ ersetzt
# würde so aussehen -> ['Hund', 'Papagei', 'Alpaka', 'Lama', 'Hamster', 'Maus', 'Ziege']
print(tiere)

# Elemente ändern
tiere[0] = "Welpe"      # [0] -> Index 0 soll Hund zu Welpe geändert werden

print(tiere)


# Elemente entfernen
# .remove() -> entferne ein bestimmtes Element

tiere.remove("Welpe")       # sagen welches Element, mit Namen, entfernt werden soll
print(tiere)

# Element per Position entfernen
tiere.pop(1)
print(tiere)


tiere = ['Papagei', 'Alpaka', 'Lama', 'Katze', 'Hamster', 'Maus', 'Ziege']

tier = tiere.pop(1)
print(tier)
print(tiere)


# Löschen von mehreren Elementen in einer Liste
inventar = ["Holzschwert", "Apfel", "Schild", "Zaubertrank"]

del inventar[1:3]       # del = delete | [1:3] = [start:ende] -> Index 1 und 2 werden gelöscht, 3 bleibt bestehen
print(inventar)