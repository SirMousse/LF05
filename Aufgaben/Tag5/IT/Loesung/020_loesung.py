# =====================================================
# DAS IT-FUNKTIONS-TICKET-SYSTEM
# =====================================================


# AUFGABE 1 – BEGRUESSUNG
# =====================================================

# Eine Funktion wird mit "def" definiert.
# Danach kommt der Name, runde Klammern () und ein Doppelpunkt.
# Alles was eingerueckt ist, gehoert zur Funktion.
# Die Funktion tut erst etwas, wenn man sie aufruft.

def begruessung():
    print("Willkommen im IT-Support-Level 1!")

begruessung()


# AUFGABE 2 – ADMIN BEGRUESSEN
# =====================================================

# Parameter sind Platzhalter fuer Werte, die beim Aufruf uebergeben werden.
# "name" bekommt beim Aufruf den echten Wert, z.B. "RootMaster".
# f-Strings: geschweifte Klammern {} fuegen den Variablenwert ein.

def begruesse_admin(name):
    print(f"Hallo {name}, neue Tickets warten.")

begruesse_admin("RootMaster")
begruesse_admin("SysAdmin99")
begruesse_admin("patch_paula")


# AUFGABE 3 – SUPPORT-POWER BERECHNEN
# =====================================================

# Mehrere Parameter werden mit Komma getrennt.
# "return" gibt einen Wert zurueck an die aufrufende Stelle.
# Ohne return liefert die Funktion nichts (None).

def berechne_support_power(wissen, kaffee_bonus):
    gesamt = wissen + kaffee_bonus
    return gesamt

power = berechne_support_power(12, 5)
print(f"\nSupport-Power: {power}")


# AUFGABE 4 – PROBLEM FAST GELOEST
# =====================================================

# Die Funktion prueft zusaetzlich, ob die Power ausreicht.
# Sie gibt den Wert zurueck UND zeigt eine Meldung an.

def berechne_support_power_stark(wissen, kaffee_bonus):
    gesamt = wissen + kaffee_bonus
    if gesamt > 20:
        print("Problem fast geloest!")
    return gesamt

power1 = berechne_support_power_stark(10, 8)    # 18 - nicht genug
print(f"Support-Power: {power1}")

power2 = berechne_support_power_stark(15, 10)   # 25 - fast geloest
print(f"Support-Power: {power2}")


# AUFGABE 5 – HARDWARE PRUEFEN
# =====================================================

# Die Funktion bekommt das Dictionary UND den Teil-Namen als Parameter.
# Mit "in" pruefen wir, ob der Schluessel im Dictionary existiert.
# Das gibt True oder False zurueck – perfekt fuer if-Bedingungen.

def pruefe_hardware(lager, teil):
    if teil in lager:
        print(f"'{teil}' auf Lager! Menge: {lager[teil]}")
    else:
        print(f"'{teil}' nicht vorratig!")

lager = {
    "Monitor":   3,
    "Tastatur":  8,
    "LAN-Kabel": 15
}

pruefe_hardware(lager, "Monitor")     # vorhanden
pruefe_hardware(lager, "Tastatur")    # vorhanden
pruefe_hardware(lager, "Grafikkarte") # nicht vorhanden


# AUFGABE 6 – ERFAHRUNG-UP
# =====================================================

# Die Funktion nimmt den aktuellen Wert entgegen,
# erhoeht ihn um 1 und gibt den neuen Wert zurueck.
# Wichtig: Die Variable ausserhalb aendert sich NICHT automatisch.
# Deshalb speichern wir den Rueckgabewert zurueck in der Variable.

def erfahrung_up(erfahrung):
    neue_erfahrung = erfahrung + 1
    print(f"Erfahrung gestiegen: {erfahrung} -> {neue_erfahrung}")
    return neue_erfahrung

meine_erfahrung = 6
meine_erfahrung = erfahrung_up(meine_erfahrung)   # Rueckgabewert speichern!
print(f"Aktuelle Erfahrung: {meine_erfahrung}")


# AUFGABE 7 – TICKET BEARBEITEN
# =====================================================

# Die Funktion bekommt Name und Support-Power,
# zeigt alles an und entscheidet je nach Wert den Ausgang.

def ticket_bearbeiten(name, support_power):
    print(f"\n{name} bearbeitet ein Ticket!")
    print(f"Support-Power: {support_power}")
    if support_power >= 50:
        print("Ticket erfolgreich geloest!")
    else:
        print("Das Problem besteht weiterhin.")

ticket_bearbeiten("RootMaster", 35)   # zu wenig Power
ticket_bearbeiten("RootMaster", 55)   # Erfolg


# =====================================================
# BONUS – DAS IT-SUPPORT-SPIEL
# =====================================================

# Alle Funktionen werden der Reihe nach aufgerufen
# und bauen aufeinander auf.

print("\n" + "=" * 40)
print("IT-SUPPORT-SCHICHT BEGINNT")
print("=" * 40)

# Schritt 1: Begruessung und Admin vorstellen
begruessung()
begruesse_admin("RootMaster")

# Schritt 2: Erfahrung erhoehen
aktuelle_erfahrung = 6
print(f"\nStart-Erfahrung: {aktuelle_erfahrung}")
aktuelle_erfahrung = erfahrung_up(aktuelle_erfahrung)

# Schritt 3: Lager pruefen
print("\n-- Hardware-Check --")
pruefe_hardware(lager, "LAN-Kabel")
pruefe_hardware(lager, "Netzwerkswitch")   # nicht vorhanden

# Schritt 4: Support-Power berechnen
# Die Erfahrung fliesst als Bonus in die Power ein.
print("\n-- Ticket-Vorbereitung --")
wissen = 30
kaffee = aktuelle_erfahrung * 3
gesamt_power = berechne_support_power_stark(wissen, kaffee)
print(f"Gesamte Support-Power: {gesamt_power}")

# Schritt 5: Ticket bearbeiten
ticket_bearbeiten("RootMaster", gesamt_power)

print("\n-- Schicht beendet. Alle Tickets geschlossen. --")