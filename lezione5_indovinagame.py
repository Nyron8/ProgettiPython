import random

numero_segretissimo = random.randint(1, 100)
tentativo = None

while tentativo != numero_segretissimo:
    tentativo = int(input("Indovina il numero (1-100): "))

    if tentativo < numero_segretissimo:
        print("Troppo basso!")
    elif tentativo > numero_segretissimo:
        print("Troppo alto!")
    else:
        print("BRAVO! Hai indovinato!")
