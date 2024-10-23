numero_1= int(input("Escriba un número: "))
numero_2= int(input("Escriba un número: "))
operacion= input("Escribe la operación que quieras hacer: ")

if operacion == "+":
    print(numero_1 + numero_2)

elif operacion == "-":
    print(numero_1 - numero_2)

elif operacion == "*":
    print(numero_1 * numero_2)

elif operacion == "/" and numero_2 != 0:
    print(numero_1 / numero_2)