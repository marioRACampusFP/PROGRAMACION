numeros = []

while True:
    entrada = input("Introduce un número (o escribe 'hecho' para terminar): ")
    if entrada == "hecho":
        break
    
    numero = int(entrada)
    numeros.append(numero)


if numeros:
   
    numero_mayor = numeros[0]
    for numero in numeros:
        if numero > numero_mayor:
            numero_mayor = numero


    print(f"El número más grande es: {numero_mayor}")