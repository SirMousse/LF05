# Aufgabe: Abenteuer im Dungeon

gold = int(input("Anzahl deiner Goldmünzen: "))

if gold >= 100:
    print("Du kaufst ein legendäres Schwert")
elif gold >= 50:
    print("Du kaufst eine bessere Rüstung")
else:
    print("Du kannst dir nur einen Heiltrank leisten")