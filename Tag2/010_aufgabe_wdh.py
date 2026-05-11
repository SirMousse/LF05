# Aufgabe: Hund und Katze tauschen

# In zwei Variablen befinden sich ein Hund und eine Katze.
# Tausche die Inhalte der Variablen, sodass am Ende:
# - in "hund" die Katze gespeichert ist
# - in "katze" der Hund gespeichert ist

korb_a = "Hund"
korb_b = "Katze"

print(f"Vor dem Tauschen: im Korb a liegt der {korb_a} und im Korb b liegt die {korb_b}.")

# Zwischenspeicher
temp_korb = korb_a

# Tauschen
korb_a = korb_b
korb_b = temp_korb

print(f"Nach dem Tausch: in Korb a ist die {korb_a} und in Korb b ist der {korb_b}.")