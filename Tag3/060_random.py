import random
# Um das random Modul zu nutzen, müssen wir es erst importieren -> import random

# 1. randint()
zahl = random.randint(1, 100)

print(zahl)

# randint(a, b)
# beide Grenzen sind mit einbezogen
# a steht für die kleinste Zahl
# b für die größte Zahl
# wird nur für ganze Zahlen genutzt und gibt zufällig eine Zahl zwischen a und b zurück (a und b eingeschlossen)

hund_num = random.randint(1, 10)

print(f"Hund Nr. {hund_num} bekommt ein Leckerli!")

# uniform()

gewicht = random.uniform(2, 12)

print(f"Die Katze wiegt momentan {gewicht} kg.")
print(f"Die Katze wiegt momentan {round(gewicht, 2)} kg.")

# uniform(a, b)
# erzeugt eine zufällige Kommazahl zwischen zwei Werten
# beide Grenzen sind mit einbezogen
# a steht für die kleinste Zahl
# b für die größte Zahl
# man kann sowohl int Zahlen als auch float zahlen eingeben, bekommt aber IMMER eine float Zahl zurück

# randrange(start, stop, schritte)
# start -> da wo wir beginnen
# stop -> da wo wir aufhören
# schritt -> In welchen Abständen gezählt wird
# stop Zahl ist NICHT mit dabei in der Ausgabe!!!

zahlen = random.randrange(0, 10, 2)

print(zahlen)

# triangular(start, stop, mode)
# start -> da wo wir beginnen
# stop -> da wo wir aufhören
# mode -> Zahl, die am häufigsten vorkommen soll
# stop Zahl ist NICHT mit dabei in der Ausgabe!!!
# man kann sowohl int Zahlen als auch float zahlen eingeben, bekommt aber IMMER eine float Zahl zurück

katzenfutter = random.triangular(1, 10, 7)

print(katzenfutter)