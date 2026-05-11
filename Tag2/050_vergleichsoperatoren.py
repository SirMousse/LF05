# Vergleichsoperatoren

# IHK WICHTIG:
# - Ein Vergleich ergibt IMMER einen Wahrheitswert (Boolean)
# - True bedeutet wahr
# - False bedeutet falsch
# - Vergleichsoperatoren werden oft in if-Bedingungen benutzt

# 1) Gleichheit ==
# == prüft ob zwei Werte gleich sind

tier = "Hund"

print(tier == "Hund")       # True
print(tier == "Hamster")    # False

# 2) Ungleich !=
# != prüft ob zwei Werte unterschiedlich sind

tier = "Katze"

print(tier != "Hund")       # True
print(tier != "Katze")      # False

# 3) Größer als >
# > prüft ob ein Wert größer ist als ein anderer

gewicht = 12

print(gewicht > 10)     # True
print(gewicht > 25)     # False

# IHK WICHTIG:
# Bei Zahlenvergleichen ist wichtig das in Python werden die Werte verglichen, nicht die Variablennamen!

# 4) Kleiner als <
# < prüft ob ein Wert kleiner ist als ein anderer

leckerlis = 3

print(leckerlis < 5)        # True
print(leckerlis < 2)        # False

# 5) Größer oder gleich >=
# >= prüft ob der Wert größer oder genau gleich ist

alter = 18

print(alter >= 18)      # True
print(alter >= 17)      # True
print(alter >= 28)      # False

# IHK WICHTIG:
# Viele vergessen das "oder gleich". > bedeutet größer! >= bedeutet größer oder gleich!

# 6) Kleiner oder gleich <=
# <= prüft ob der Wert kleiner oder gleich ist

temperatur = 0
print(temperatur <= 0)      # True
print(temperatur <= 5)      # True
print(temperatur <= -3)     # False


# IHK WICHTIG:
# "Hund" ist nicht dasselbe wie "hund"
# Python ist da sehr genau.

print("Hund" == "hund")     # False

# IHK WICHTIG:
# Operator in der richtigen Reihenfolge schreiben
# <=    -> RICHTIG | =<    -> FALSCH

# Vergleichsoperator
# ... Operator zum Vergleichen von Werten

# Boolean
# ... Datentyp mit True oder False

# Operand
# ... Wert links oder rechts vom Operator

# Ausdruck
# ... Kombination aus Werten, Variablen und Operatoren