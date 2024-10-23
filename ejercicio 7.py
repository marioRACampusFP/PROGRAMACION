import random
numero_secreto = random.randint (1, 100)
while True:
    numero =int (input("Ingresa un número: "))
    if numero_secreto < numero:
        print("EL número secreto es más pequeño")
    elif numero_secreto > numero:
        print("El número secreto es más grande")
    else:
        print("Has acertado el número secreto")
        break