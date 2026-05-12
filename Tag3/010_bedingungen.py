# Bedingungen/ Entscheidungen mit if/else

# Was ist if?

# Wenn meine Bedingung wahr (True) ist -> wird der if-Block ausgeführt

# if bedingung:
#   mache_etwas

hund_hat_hunger = True

if hund_hat_hunger:
    print("Bello bekommt Futter.")

# if -> "WENN"
# hund_hat_hunger -> Bedingung
# : -> Jetzt kommt unser Codeblock
# Einrücken -> Gehört zu unserer Bedingung

# Was ist else?

# Wenn meine Bedingung falsch (False) ist -> wird der else-Block ausgeführt

# if bedingung:
#   mache_etwas
# else:
#   andere Code

alter = 18

if alter >= 18:
    print("Du darfst alleine mit den Tierheimhunden Gassi gehen!")
else:
    print("Du brauchst einen Erwachsenen, der dich begleitet!")

# Der Computer prüft:
# Ist die Bedingung WAHR?
#       -> erster Block wird ausgegeben
# Ist die Bedingung FALSCH?
#       -> wird der else-Block ausgegeben

# Was ist elif?
# elif bedeutet = else if -> ansonsten wenn

# if bedingung:
#   mache_etwas
# elif bedingung2:
#   mache_etwas
# else:
#   andere Code

animal = "Papagei"

if animal == "Hund":
    print("Der Hund bekommt Futter!")
elif animal == "Papagei":
    print("Er kann mehr reden als ein Verkäufer!")
else:
    print("Wir kennen dieses Tier nicht!")