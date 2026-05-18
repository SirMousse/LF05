# Funktion

# 1) Einfach Funktionen

# def = hier erstelle ich eine Funktion
# begruessung = Name der Funktion 
# Wichtig bvei der Namensgebung von Funktionen: verständlich, eindeutig und sinnvoll sein bitte!
# () = hier können später Informationen übergeben werden!
# : = Kündigen an, jetzt beginnt unser Funktionsblock
def begruessung():
    # MUSS IMMER EINGERÜCKT SEIN!
    print("Willkommen im Tierheim!")            
    
# Funktion aufrufen!
begruessung()

# def tiere():
#     name= input("Wie heißt dein Tier?\n")
#     print("Willkommen im Tierheim", name)

# tiere()
# IHK WICHTIG:
# Parameter
# ... sind Variablen in der Funktionsdefintion, die Werte entgegennehmen.
# Einfach gesagt -> Platzhalter innerhalb einer Funktion

# Argument
# ... sind die tatsächlichen Werte, die bei Funktionsaufruf übergeben werden


# 2) Funktionen mit Parameter

def hund_hallo(name):                                   # name -> Parameter
    print("Hallo", name,"willkommen im Tierheim!")      # name -> Parameter

hund_hallo("Bello")                                     # Bello = name -> Argument   
hund_hallo("Minka") 
hund_hallo("Sir Fluffilot") 
hund_hallo("Lord Voldetort") 

# Variante 1
# Funktion aufrufen(Eingabe Funktion(Text der Eingabefunktion, was du eingeben soll...))
# hund_hallo(input("Name: "))

# Variante 2
# namen = input("Wie heißt du?\n")
# hund_hallo(namen)

############################################################

def tier_vorstellen(name, tierart):
    print(f"{name} ist ein/e {tierart}.")

tier_vorstellen("Sir Mousse", "Hund")

# 3) Funktionen mit Rückgabewerte

def berechne_futtermenge(gewicht):
    futter = gewicht * 30
    return futter                   # -> hier wird das Ergebnis zurückgegeben

menge = berechne_futtermenge(10)
print(menge)

# Unterschied print() und return

# print
# ... zeigt etwas nur an

# return
# ... gibt ein Ergebnis zurück, damit man weiterarbeiten kann.