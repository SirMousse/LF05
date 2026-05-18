# =====================================================
# DAS ZOMBIE-FUNKTIONS-ÜBERLEBENSTRAINING
# =====================================================


# ── AUFGABE 1 ─────────────────────────────────────
# Funktion ohne Parameter, keine Rückgabe

def begruessung():
    print("Willkommen in der Sicherheitszone!")


# ── AUFGABE 2 ─────────────────────────────────────
# Funktion mit einem Parameter

def begruesse_survivor(name):
    print(f"Hallo {name}, bleib wachsam.")


# ── AUFGABE 3 ─────────────────────────────────────
# Funktion mit zwei Parametern und Rückgabewert

def berechne_abwehrkraft(waffe, mut_bonus):
    return waffe + mut_bonus


# ── AUFGABE 4 ─────────────────────────────────────
# Funktion mit Bedingung

def pruefe_abwehr(abwehrkraft):
    if abwehrkraft > 20:
        print("Zombie-Horde zurückgedrängt!")
    else:
        print("Die Horde hält stand...")


# ── AUFGABE 5 ─────────────────────────────────────
# Funktion mit Dictionary-Prüfung

def pruefe_item(kit, item):
    if item in kit:
        print(f'"{item}" ist vorhanden. ({kit[item]})')
        return True
    else:
        print(f'"{item}" NICHT gefunden!')
        return False


# ── AUFGABE 6 ─────────────────────────────────────
# Funktion mit Rückgabe (veränderten Wert zurückgeben)

def tage_up(tage):
    tage += 1
    print(f"Tag {tage} überlebt!")
    return tage


# ── AUFGABE 7 ─────────────────────────────────────
# Funktion mit zwei Parametern und if / else

def hordenangriff(name, abwehrkraft):
    print(f"\n⚠  HORDENANGRIFF auf {name}!")
    if abwehrkraft >= 50:
        print("Die Horde wurde abgewehrt!")
    else:
        print("Die Horde kommt näher!")


# ══════════════════════════════════════════════════
# BONUS – Mini-Überlebensspiel aus allen Funktionen
# ══════════════════════════════════════════════════

def spiel():
    print("=" * 45)
    begruessung()                           # Aufgabe 1
    print("=" * 45)

    name = input("\nWie heißt du?\n> ")
    begruesse_survivor(name)                # Aufgabe 2

    # Ausrüstungs-Kit (Dictionary für Aufgabe 5)
    kit = {
        "Verband":       "Heilt 20 HP",
        "Taschenlampe":  "Sicht +10",
        "Konserve":      "Nahrung +5"
    }

    tage = 0
    leben = 100

    print("\n--- Deine Ausrüstung wird geprüft ---")
    for item in ["Verband", "Taschenlampe", "Messer"]:
        pruefe_item(kit, item)              # Aufgabe 5

    print("\n--- Überlebenstage beginnen ---")

    for _ in range(3):
        tage = tage_up(tage)               # Aufgabe 6

        waffe    = int(input(f"\nTag {tage}: Waffenstärke eingeben (z. B. 15):\n> "))
        bonus    = int(input("Mut-Bonus eingeben (z. B. 10):\n> "))

        abwehr = berechne_abwehrkraft(waffe, bonus)   # Aufgabe 3
        print(f"Abwehrkraft: {abwehr}")

        pruefe_abwehr(abwehr)              # Aufgabe 4
        hordenangriff(name, abwehr)        # Aufgabe 7

        if abwehr < 50:
            leben -= 20
            print(f"Leben: {leben} HP")

        if leben <= 0:
            print("\n☠  Du hast die Apokalypse nicht überlebt.")
            return

    print("\n" + "=" * 45)
    print(f"{name} hat {tage} Tage überlebt!")
    print(f"   Leben: {leben} HP")
    print("=" * 45)


# Einstiegspunkt
if __name__ == "__main__":
    spiel()