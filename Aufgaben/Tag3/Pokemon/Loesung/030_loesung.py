# ============================================
# Pokemon-Aufgabenreihe Python — Lösungen
# ============================================


# ============================================
# Aufgabe 1 — Trainername prüfen
# ============================================

trainername = input("Trainername: ")

if len(trainername) > 6:
    print("Starker Trainername")
else:
    print("Kurzer Trainername")


# ============================================
# Aufgabe 2 — Pokemon-Level
# ============================================

level = int(input("Pokemon-Level: "))

if level >= 50:
    print("Dein Pokemon ist sehr stark")
else:
    print("Dein Pokemon muss noch trainieren")


# ============================================
# Aufgabe 3 — Orden prüfen
# ============================================

orden = int(input("Anzahl der Orden: "))

if orden < 4:
    print("Du darfst noch nicht zur Liga")
elif orden <= 7:
    print("Du darfst stärkere Arenen herausfordern")
else:
    print("Pokemon-Liga freigeschaltet")


# ============================================
# Aufgabe 4 — Geheimes Trainerpasswort
# ============================================

passwort = input("Geheimes Passwort: ")

if passwort == "pikachu":
    print("Geheimer Trainingsraum geöffnet")
else:
    print("Zugang verweigert")


# ============================================
# Aufgabe 5 — KP prüfen
# ============================================

kp = int(input("KP deines Pokemon: "))

if kp < 30:
    print("Pokemon braucht einen Trank")
else:
    print("Pokemon kann weiterkämpfen")


# ============================================
# Aufgabe 6 — Zufälliger Fangversuch
# ============================================

import random

fangwurf = random.randint(1, 6)

print(fangwurf)

if fangwurf == 6:
    print("Pokemon wurde gefangen")
else:
    print("Pokemon ist ausgebrochen")


# ============================================
# Aufgabe 7 — Pokeball vorhanden
# ============================================

pokeball = input("Pokeball vorhanden? ")

if pokeball == "ja":
    print("Du kannst ein Pokemon fangen")
else:
    print("Du brauchst einen Pokeball")


# ============================================
# Aufgabe 8 — Arena-Zugang
# ============================================

orden = int(input("Anzahl der Orden: "))
kampfbereit = input("Pokemon kampfbereit? ")

if orden >= 4:
    if kampfbereit == "ja":
        print("Du darfst die Arena betreten")
    else:
        print("Dein Pokemon ist nicht kampfbereit")
else:
    print("Du hast noch nicht genug Orden")


# ============================================
# Aufgabe 9 — Zufällige Begegnung
# ============================================

import random

begegnung = random.choice(["Rattfratz", "Glumanda", "Relaxo"])

print(begegnung)

if begegnung == "Rattfratz":
    print("Ein Rattfratz greift an! Es sollte kein Problem sein.")
elif begegnung == "Glumanda":
    print("Ein wildes Glumanda erscheint! Das wird ein heißer Kampf.")
else:
    print("Ein Relaxo versperrt den Weg! Wie bekommst du es weg?")


# ============================================
# Aufgabe 10 — Pokemon-Name prüfen
# ============================================

pokemon_name = input("Pokemon-Name: ")

if len(pokemon_name) > 10:
    print("Legendärer Pokemon-Name")
elif len(pokemon_name) > 5:
    print("Starker Pokemon-Name")
else:
    print("Kurzer Pokemon-Name")


# ============================================
# Aufgabe 11 — Zugang zur Pokemon-Liga
# ============================================

orden = int(input("Anzahl der Orden: "))
level = int(input("Level deines stärksten Pokemon: "))

if orden >= 8:
    if level >= 60:
        print("Du darfst die Pokemon-Liga betreten")
    else:
        print("Dein Pokemon-Level ist zu niedrig")
else:
    print("Du brauchst alle 8 Orden")


# ============================================
# Aufgabe 12 — Kampf gegen Arenaleiter
# ============================================

import random

arenaleiter = random.choice(["schwach", "mittel", "stark"])

print("Arenaleiter:", arenaleiter)

level = int(input("Pokemon-Level: "))

if arenaleiter == "schwach":
    if level >= 20:
        print("Du besiegst den Arenaleiter ohne Mühe")
    else:
        print("Selbst der schwache Arenaleiter ist zu stark")

elif arenaleiter == "mittel":
    if level >= 40:
        print("Nach hartem Kampf gewinnst du den Orden")
    else:
        print("Der Arenaleiter ist zu stark für dich")

else:
    if level >= 50:
        print("In einem epischen Kampf besiegst du den starken Arenaleiter")
    else:
        print("Du verlierst den Kampf")


# ============================================
# Aufgabe 13 — Pokeball-Zahlenrätsel
# ============================================

import random

pokeball_nummer = random.randint(1, 10)

tipp = int(input("Rate die Pokeball-Nummer: "))

if tipp == pokeball_nummer:
    print("Seltener Pokeball gefunden")
elif tipp == pokeball_nummer - 1 or tipp == pokeball_nummer + 1:
    print("Fast richtig")
else:
    print("Falscher Pokeball")


# ============================================
# Aufgabe 14 — Die Trainerprüfung
# ============================================

trainername = input("Trainername: ")
orden = int(input("Orden: "))
level = int(input("Pokemon-Level: "))
pokeball = input("Pokeball vorhanden? ")

if len(trainername) > 6:
    print("Trainername akzeptiert")

if orden >= 8:
    if level >= 60:
        if pokeball == "ja":
            print("Trainerprüfung bestanden")
        else:
            print("Pokeball fehlt")
    else:
        print("Pokemon-Level zu niedrig")
else:
    print("Nicht genug Orden")


# ============================================
# Aufgabe 15 — Pokemon-Finale
# ============================================

import random

print("\n=== POKEMON-ABENTEUER: DER WEG ZUR LIGA ===\n")

# Entscheidung 1: Trainername prüfen (len)
trainername = input("Dein Trainername: ")

if len(trainername) > 6:
    print(f"Trainername '{trainername}' akzeptiert — deine Legende beginnt.")
else:
    print(f"Kurzer Name, aber große Taten warten auf {trainername}.")

# Entscheidung 2: Orden
orden = int(input("Wie viele Orden hast du? "))

if orden < 4:
    print("Du stehst noch am Anfang deiner Reise.")
elif orden <= 7:
    print("Du machst gute Fortschritte — weiter so!")
else:
    print("Alle 8 Orden! Die Liga ruft.")

# Entscheidung 3: Pokemon-Level
level = int(input("Level deines stärksten Pokemon: "))

# Entscheidung 4: Pokeball
pokeball = input("Pokeball vorhanden? (ja/nein): ").strip().lower()

# Zufallsereignis: Wilde Begegnung auf dem Weg zur Liga
begegnung = random.choice(["Relaxo", "Arkani", "Crypto-Pokemon"])
print(f"\nAuf dem Weg zur Liga begegnest du: {begegnung}!")

if begegnung == "Relaxo":
    print("Das Relaxo schläft quer über den Weg. Du brauchst die Pokeflöte.")
elif begegnung == "Arkani":
    print("Das Arkani feuert dich an! Dein Pokemon gewinnt 5 Extra-Level.")
    level += 5
    print(f"Neues Level: {level}")
else:
    print("Ein Crypto-Pokemon greift an! Der Kampf kostet dich einen Orden.")
    orden = max(0, orden - 1)
    print(f"Verbleibende Orden: {orden}")

# Entscheidung 5: Nested ifs — Liga-Zugang
print("\n--- Liga-Prüfung ---")

if orden >= 8:
    if level >= 60:
        if pokeball == "ja":
            # Ende 1
            print("\nEnde 1: Vollständig ausgerüstet!")
            print(f"{trainername} betritt die Pokemon-Liga und besiegt alle Mitglieder des Eliteviers.")
        else:
            # Ende 2
            print("\nEnde 2: Kein Pokeball!")
            print(f"{trainername} kann das letzte Legendäre nicht fangen. Die Liga bleibt unvollständig.")
    else:
        if level >= 45:
            # Ende 3
            print("\nEnde 3: Fast bereit.")
            print(f"{trainername} scheitert knapp am Elitvier. Noch ein bisschen Training!")
        else:
            # Ende 4
            print("\nEnde 4: Zu schwache Pokemon.")
            print(f"{trainername} wird vom ersten Elitvier-Mitglied besiegt. Zurück ins Training!")
elif orden >= 4:
    # Ende 5
    print("\nEnde 5: Auf halber Strecke.")
    print(f"{trainername} hat noch nicht alle Orden. Die Reise geht weiter.")
else:
    # Ende 6
    print("\nEnde 6: Noch ein langer Weg.")
    print(f"Mit nur {orden} Orden ist {trainername} noch weit von der Liga entfernt.")