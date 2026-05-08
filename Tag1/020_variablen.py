# Variablen
# ... speichert Informationen. Ist wie ein Behälter bzw. eine Kiste, die den Inhalt verwaltet.

tier = "Hund"
# tier -> Name der Variable
# = -> sagt mir "Speichere"
# "Hund" -> gespeicherte Wert in meiner Variable

print(tier)

# STRING -> Text
# Texte nennt man in Python String
tiername = "Bello"
print(tiername)

tierart = "Katze"
name = "Poupette"
farbe = "rot"

print(tierart)
print(name)
print(farbe)


# Zahlen können auch Strings sein, aber sie müssen in Anführungszeiche stehen
alter = "5"
print(alter)

###################################################################################

# INTEGER -> ganzen Zahlen
# int = abkürzung für Integer

anzahl_beine = 4
punkte = 100

print(anzahl_beine, punkte)

# man kann mit dem Integer rechnen
jahr = 2026

print(jahr + 5)         # 2026 + 5 = 2031
print(jahr - 10)        # 2026 - 10 = 2016
print(jahr * 3)         # 2026 * 3 = 6078

# Integer kann positiv, negativ und null sein
bayern = 0
temperatur = -15

print(bayern, temperatur)

###################################################################################

# FLOAT -> Kommazahlen
# ... ist eine Zahl die eine Nachkommastelle hat. In Python schreiben wir Kommazahlen mit .

gewicht = 25.6
groesse = 0.52
preis = 2.59

# gewicht = 25,6  # das wären zwei Werte (Tuple)

# Ganze Zahlen können mit Kommazahlen verrechnet werden
print(gewicht + 1)
print(gewicht - 3)

###################################################################################

# BOOLEAN -> Wahrheitswert
# bool = Boolean
# bool hat zwei Werte -> einmal wahr(True) oder falsch(False)

ist_hund = True
ist_katze = False

print(ist_hund)     # True
print(ist_katze)    # False

###################################################################################

# Datentypen prüfen -> type()

hunde_name = "Mousse"
alter_hund = 6
gewicht_hund = 25.6
ist_hund = True

# Python ist fast alles ein sogenanntes Objekt. 
# Jedes Objekt gehört zu einer bestimmten Klasse (class)
print(type(hunde_name))         # class str -> String = Text
print(type(alter_hund))         # class int -> Integer = Ganze Zahl
print(type(gewicht_hund))       # class float -> Float = Kommazahl
print(type(ist_hund))           # class bool -> Boolean = Wahrheitswert