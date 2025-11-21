a = float(input("Primo numero: "))
b = float(input("Secondo numero: "))
operazione = input("Operazione (+, -, *, /): ")

if operazione == "+":
    risultato = a + b
elif operazione == "-":
    risultato = a - b
elif operazione == "*":
    risultato = a * b
elif operazione == "/":
    if b != 0:
        risultato = a / b
    else:
        print("Errore: divisione per zero!")
        exit()  # ferma il programma
else:
    print("Operazione non valida!")
    exit()

print("Il risultato è:", risultato)
