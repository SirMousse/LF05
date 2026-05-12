# ============================================
#   DER SERVER-NOTFALL
# ============================================

# 1. Technikername abfragen
name = input("Name des Technikers: ")
print(f"\nWillkommen, {name}. Incident-Management gestartet.\n")

# 2. CPU-Auslastung abfragen
cpu = int(input("CPU-Auslastung in %: "))

# 3. Speicherplatz abfragen
speicher = int(input("Verfügbarer Speicherplatz in GB: "))

# --- CPU-Auswertung ---
if cpu < 50:
    print("Server läuft stabil.")
    cpu_status = "stabil"

elif cpu <= 85:
    print("Server ist stark ausgelastet.")
    cpu_status = "hoch"

else:
    print("Kritischer Serverzustand.")
    cpu_status = "kritisch"

# BONUS: Speicherplatz unter 10
if speicher < 10:
    print("Festplatte fast voll.")

# 4. Neustart — nur wenn CPU über 85
if cpu_status == "kritisch":
    neustart = input("\nIst ein Neustart erlaubt? (ja/nein): ").strip().lower()

    if neustart == "ja":
        print("Server wird neu gestartet.")
    else:
        print("Manuelle Fehleranalyse erforderlich.")
else:
    neustart = "nein"

# 5. Problemtyp abfragen
print("\nWelcher Problemtyp liegt vor?")
print("  1 - Netzwerk")
print("  2 - Datenbank")
print("  3 - Login")
problem = input("Problemtyp: ").strip().lower()

if problem == "1":
    problem = "netzwerk"
elif problem == "2":
    problem = "datenbank"
elif problem == "3":
    problem = "login"

# 6. Lösung je nach Problemtyp
if problem == "netzwerk":
    print("Lösung: Netzwerkkabel und Router prüfen, DNS-Cache leeren.")
elif problem == "datenbank":
    print("Lösung: Datenbankdienst neu starten und Verbindungslogs prüfen.")
elif problem == "login":
    print("Lösung: Anmeldedaten zurücksetzen und Active Directory prüfen.")
else:
    print("Unbekannter Problemtyp — Ticket wird eskaliert.")
    problem = None

# ============================================
#   NESTED IFS — Entscheidungsmatrix
# ============================================

print("\n--- Abschlussbericht ---")

if cpu_status == "stabil":
    if speicher >= 10:
        # Ende 1
        print(f"Ende 1: Alles in Ordnung.")
        print(f"{name} schließt den Incident. Kein weiterer Eingriff nötig.")
    else:
        # Ende 2
        print(f"Ende 2: CPU stabil, aber Speicher kritisch.")
        print(f"{name} leitet eine Speicherbereinigung ein.")

elif cpu_status == "hoch":
    if speicher < 10:
        # Ende 3
        print(f"Ende 3: Hohe CPU-Last und volle Festplatte.")
        print(f"{name} eskaliert den Incident an den Senior-Admin.")
    else:
        # Ende 4
        print(f"Ende 4: CPU hoch, aber Speicher ausreichend.")
        print(f"{name} überwacht den Server und plant ein Wartungsfenster.")

else:
    # CPU kritisch
    if neustart == "ja":
        if problem == "netzwerk":
            # Ende 5
            print(f"Ende 5: Neustart + Netzwerkproblem.")
            print(f"Server läuft wieder — Router wird parallel getauscht.")
        elif problem == "datenbank":
            # Ende 6
            print(f"Ende 6: Neustart + Datenbankproblem.")
            print(f"Nach dem Neustart startet {name} die DB-Wiederherstellung.")
        else:
            # Ende 7
            print(f"Ende 7: Neustart erfolgreich.")
            print(f"Problem behoben. {name} dokumentiert den Vorfall.")
    else:
        # Ende 8
        print(f"Ende 8: Kein Neustart — manuelle Analyse läuft.")
        print(f"{name} analysiert die Logs und isoliert den Fehler manuell.")