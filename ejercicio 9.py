contador = 0
suma = 0
while True:
    numero = int(input("Escribe un número: "))
    contador += 1
    if numero == 0:
        break
    suma = suma + numero
    promedio = suma / contador
print ("La media es: ", promedio)
print ("La suma es: ", suma)
print ("La cantidad de números es: ", contador)

