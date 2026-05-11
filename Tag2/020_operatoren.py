# Operatoren

# Addition mit +
hund = 3
katze = 2

alle_tiere = hund + katze   # 3 + 2
print(alle_tiere)           # Ergebnis = 5

# links steht die Variable (alle_tiere) = rechts rechnen wie (hund + katze)

kaninchen = 4
alle_tiere = hund + katze + kaninchen       # 3 + 2 + 4
print(alle_tiere)                           # Ergebnis = 9

##############################################################################

# Subtraktion mit -

katzen = 10
vermittelt = 3

uebrig = katzen - vermittelt    # 10 - 3
print(uebrig)                   # Ergebnis = 7

hunde = 12
vermittelt = 5

uebrig = hunde - vermittelt     # 12 - 5
print(uebrig)                   # Ergebnis = 7

##############################################################################

# Multiplikation mit *
# in Python rechnen wir bei der Multiplikation nicht mit x

hunde = 4
leckerlis_pro_hund = 3

gesamt = hunde * leckerlis_pro_hund     # 4 * 3  -> ( 3 + 3 + 3 + 3)
print(gesamt)                           # Ergebnis = 12

###############################################################################

# Division mit /
# ... wird als float ausgegeben

dosen = 42
hunde = 23

pro_hund = dosen / hunde    # 42 / 23
print(pro_hund)             # Ergebnis = 1.826
print(round(pro_hund, 2))   # Funktion zum Runden -> round(zahl, anzahl der Kommazahlen)

dosen = 18
katzen = 6

pro_katze = dosen / katzen  # 18 / 6
print(pro_katze)            # Ergebnis = 3.0

###############################################################################

# Modulo mit %
# Modulo fragt: " Was bleibt übrig?"

hunde = 13

rest = hunde % 5
print(rest)

# Was passiert hier
# Aufgabe: Wir haben 13 Hunde und diese sollen in Gruppen eingeteilt werden
#          Die Gruppen sind jeweils 5 Tiere groß.
# Lösung: 1 Runde : 5 Hunde kommen in eine Gruppe (8 Hunde übrig)
#         2 Runde : 5 Hunde kommen in eine Gruppe (3 Hunde übrig)
#         3 Runde : 3 Hunde kommen in eine Gruppe 


katzen = 69 

rest = katzen % 15
print(rest)

##############################################################################

# Potenz mit **
# ** bedeuten Potenz (mal sich selbst)
# 2^4 wird in Python nicht akzeptiert

kaninchen = 2 ** 4      # (2 * 2 * 2 * 2) in unserem Beispiel wird die Zahl 2 vier Mal mit sich selbst multipliziert 
                        # Die Zahl nach den ** gibt die Anzahl der eigen Multiplikation an

print(kaninchen)        # Ergebnis = 16

##############################################################################

num = 2 + 3 * 4         # Rechenweg: 3 * 4 = 12 + 2 = 14
print(num)              # Ergebnis = 14

num1 = (2 + 3) * 4      # Rechenweg: (2 + 3) = 5 * 4 = 20
print(num1)             # Ergebnis = 20

# Priorität
# 1) Klammer                -> ()
# 2) Potenz                 -> **
# 3) Mal, Geteilt, Rest     -> * | / | %
# 4) Plus, Minus            -> + | -

num2 = 8 / 2 * 3            # Rechenweg: 8 / 2 = 4 * 3 = 12
print(num2)                 # Ergebnis = 12

num3 = 2 * 3 / 8            # Rechenweg: 2 * 3 = 6 / 8 = 0.75
print(num3)                 # Ergebnis = 0.75

# Wir rechnen IMMER bei göeicher Priorität von LINKS nach RECHTS!!!

num4 = 2 ** 3 ** 2          # Rechenweg: 3 ** 2 = 9 -> 2 ** 9 = 512
print(num4)                 # Ergebnis = 512

# POTENZEN rechnen anders!! Man rechnet von RECHTS nach LINKS!