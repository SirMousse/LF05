# =====================================================
# DAS HACKER-TERMINAL
# =====================================================


# =====================================================
# AUFGABE 1 – TERMINAL-START
# =====================================================

# Eine Funktion wird mit "def" definiert.
# Danach kommt der Name, runde Klammern () und ein Doppelpunkt.
# Alles, was eingerückt ist, gehört zur Funktion.
# Die Funktion macht erst etwas, wenn sie aufgerufen wird.

def begruessung():
    print("Willkommen im Hacker-Terminal!")

begruessung()


# =====================================================
# AUFGABE 2 – HACKER LOGIN
# =====================================================

# Parameter sind Platzhalter für Werte, die beim Aufruf übergeben werden.
# "name" bekommt beim Aufruf den echten Wert, z.B. "ZeroByte".
# f-Strings: geschweifte Klammern {} fügen den Variablenwert in den Text ein.

def begruesse_hacker(name):
    print(f"Hallo {name}, Zugriff vorbereitet.")

begruesse_hacker("ZeroByte")
begruesse_hacker("NullPointer")
begruesse_hacker("RootX")


# =====================================================
# AUFGABE 3 – HACK-POWER
# =====================================================

# Mehrere Parameter werden mit Komma getrennt.
# "return" gibt einen Wert zurück an die aufrufende Stelle.
# Ohne return liefert die Funktion nichts (None).

def berechne_hack_power(skill, tool_bonus):
    gesamt = skill + tool_bonus
    return gesamt

# Den Rückgabewert in einer Variable speichern.
hack_power = berechne_hack_power(12, 5)
print(f"\nHack-Power: {hack_power}")


# =====================================================
# AUFGABE 4 – FIREWALL-DURCHBRUCH
# =====================================================

# Die Funktion prüft zusätzlich, ob der Wert kritisch ist.
# Sie gibt die Hack-Power zurück UND zeigt eine Meldung an.

def berechne_hack_power_krit(skill, tool_bonus):
    gesamt = skill + tool_bonus
    if gesamt > 20:
        print("Firewall kritisch beschadigt!")
    return gesamt

schaden1 = berechne_hack_power_krit(10, 8)   # 18 - kein Krit
print(f"Hack-Power: {schaden1}")

schaden2 = berechne_hack_power_krit(15, 10)  # 25 - kritisch
print(f"Hack-Power: {schaden2}")


# =====================================================
# AUFGABE 5 – TOOL-CHECK
# =====================================================

# Die Funktion bekommt das Dictionary UND den Tool-Namen als Parameter.
# Mit "in" prüfen wir, ob der Schlüssel im Dictionary existiert.
# Das gibt True oder False zurück.

def pruefe_tool(tools, tool_name):
    if tool_name in tools:
        print(f"Tool gefunden: {tool_name} (Stufe {tools[tool_name]})")
    else:
        print(f"Tool nicht vorhanden: {tool_name}")

tools = {
    "USB-Exploit":   3,
    "VPN-Key":       5,
    "Passwortliste": 2
}

pruefe_tool(tools, "USB-Exploit")    # vorhanden
pruefe_tool(tools, "VPN-Key")        # vorhanden
pruefe_tool(tools, "Zero-Day")       # nicht vorhanden


# =====================================================
# AUFGABE 6 – RANG-UP
# =====================================================

# Die Funktion nimmt den aktuellen Rang entgegen,
# erhoeht ihn und gibt den neuen Wert zurueck.
# Wichtig: Die Variable ausserhalb aendert sich NICHT automatisch.
# Deshalb speichern wir den Rueckgabewert zurueck in der Variable.

def rang_up(rang):
    neuer_rang = rang + 1
    print(f"Rang erhoht: {rang} -> {neuer_rang}")
    return neuer_rang

mein_rang = 3
mein_rang = rang_up(mein_rang)   # Rueckgabewert speichern!
print(f"Aktueller Rang: {mein_rang}")


# =====================================================
# AUFGABE 7 – SYSTEMANGRIFF
# =====================================================

# Die Funktion bekommt Name und Hack-Power,
# zeigt alles an und entscheidet je nach Wert uber den Ausgang.

def systemangriff(name, hack_power):
    print(f"\n{name} greift das System an!")
    print(f"Hack-Power: {hack_power}")
    if hack_power >= 50:
        print("System erfolgreich uebernommen!")
    else:
        print("Zugriff verweigert!")

systemangriff("ZeroByte", 35)   # zu schwach
systemangriff("ZeroByte", 55)   # Erfolg


# =====================================================
# BONUS – ALLES KOMBINIERT
# =====================================================

# Alle Funktionen werden der Reihe nach aufgerufen
# und bauen aufeinander auf.

print("\n" + "=" * 40)
print("HACKER-SESSION STARTET")
print("=" * 40)

# Schritt 1: Terminal starten und Hacker begruessen
begruessung()
begruesse_hacker("NullPointer")

# Schritt 2: Rang erhoehen
aktueller_rang = 4
aktueller_rang = rang_up(aktueller_rang)

# Schritt 3: Tools pruefen
print("\n-- Tool-Check --")
pruefe_tool(tools, "VPN-Key")
pruefe_tool(tools, "Rootkit")

# Schritt 4: Hack-Power berechnen
# Der Rang beeinflusst den Bonus.
gesamt_power = berechne_hack_power_krit(30, aktueller_rang * 4)
print(f"Berechnete Hack-Power: {gesamt_power}")

# Schritt 5: Systemangriff starten
systemangriff("NullPointer", gesamt_power)

print("\n-- Session beendet --")