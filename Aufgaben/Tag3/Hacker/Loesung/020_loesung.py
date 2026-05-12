# ============================================
#   DER FIREWALL-BREAKER
# ============================================

# 1. Hacker-Name abfragen
name = input("Hacker-Name: ")
print(f"\nVerbindung hergestellt. Willkommen, {name}.\n")

# 2. Sicherheitsfreigabe abfragen
freigabe = int(input("Sicherheitsfreigabe (0-100): "))

# 3. Passwort-Stärke abfragen
pw_staerke = int(input("Passwort-Stärke deines eigenen Systems (0-100): "))

# BONUS: Eigenes Passwort unsicher?
if pw_staerke < 50:
    print("Warnung: Dein eigenes System ist unsicher.")

# --- Freigabe-Auswertung ---
if freigabe < 40:
    print("Zugriff verweigert.")
    freigabe_status = "gesperrt"

elif freigabe < 80:
    print("Eingeschränkter Zugriff erlaubt.")
    freigabe_status = "eingeschraenkt"

else:
    print("Admin-Bereich erreichbar.")
    freigabe_status = "admin"

# 4. Sicherheitscode — nur bei Freigabe ab 80
if freigabe_status == "admin":
    sicherheitscode = input("\nSicherheitscode eingeben: ").strip()

    if sicherheitscode == "root123":
        print("Hauptsystem geöffnet.")
        code_korrekt = True
    else:
        print("Alarm ausgelöst.")
        code_korrekt = False
else:
    code_korrekt = False

# 5. Aktion abfragen
print("\nWelche Aktion wählst du?")
print("  1 - scan")
print("  2 - decrypt")
print("  3 - logout")
aktion = input("Deine Aktion: ").strip().lower()

if aktion == "1":
    aktion = "scan"
elif aktion == "2":
    aktion = "decrypt"
elif aktion == "3":
    aktion = "logout"

# 6. Ausgabe je nach Aktion
if aktion == "scan":
    print("Systemscan läuft — alle Ports werden analysiert.")
elif aktion == "decrypt":
    print("Entschlüsselung gestartet — verschlüsselte Dateien werden geknackt.")
elif aktion == "logout":
    print("Verbindung getrennt — keine Spuren hinterlassen.")
else:
    print("Unbekannte Aktion — Verbindung bleibt offen.")

# ============================================
#   VERSCHIEDENE ENDEN (nested ifs)
# ============================================

print("\n--- Systembericht ---")

if freigabe_status == "gesperrt":
    # Ende 1
    print(f"Ende 1: {name} kommt nicht rein.")
    print("Die Firewall ist unüberwindbar. Operation gescheitert.")

elif freigabe_status == "eingeschraenkt":

    if aktion == "logout":
        # Ende 2
        print(f"Ende 2: Sicherer Rückzug.")
        print(f"{name} erkennt die Grenzen und loggt sich aus. Kein Schaden, keine Spuren.")

    elif aktion == "scan":
        # Ende 3
        print(f"Ende 3: Teilerfolg.")
        print(f"{name} scannt das System im eingeschränkten Modus. Nützliche Infos — der Kern bleibt verschlossen.")

    else:
        # Ende 4
        print(f"Ende 4: Entschlüsselung scheitert.")
        print("Ohne vollen Zugriff zu wenig Rechte. Verbindung wird zwangsgetrennt.")

else:
    # Admin-Freigabe
    if not code_korrekt:
        # Ende 5
        print(f"Ende 5: Alarm ausgelöst.")
        print(f"Falscher Code trotz Admin-Freigabe. {name} muss sofort fliehen.")

    else:
        # Code korrekt — Aktion entscheidet
        if aktion == "logout":
            # Ende 6
            print(f"Ende 6: Sauberer Einbruch.")
            print(f"{name} hatte Root-Zugang und ist ruhig abgetaucht. Professionell.")

        elif aktion == "scan":
            if pw_staerke < 50:
                # Ende 7
                print(f"Ende 7: Ironie des Schicksals.")
                print(f"{name} scannt fremde Systeme — dabei ist das eigene offen wie ein Scheunentor.")
            else:
                # Ende 8
                print(f"Ende 8: Vollständiger Scan.")
                print(f"Root-Zugang plus Scan: {name} kartiert das gesamte Netzwerk. Volle Kontrolle.")

        elif aktion == "decrypt":
            # Ende 9
            print(f"Ende 9: Mission erfüllt.")
            print(f"Mit Root-Zugang und Decrypt-Tool knackt {name} alle verschlüsselten Dateien.")

        else:
            # Ende 10
            print(f"Ende 10: Unbekannte Aktion mit Root-Zugang.")
            print(f"{name} improvisiert — und kommt trotzdem durch.")