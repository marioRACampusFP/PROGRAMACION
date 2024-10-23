contraseña_correcta = "Mrbasket.23"

while True:
    contraseña_ingresada = input("Escribe la contraseña: ")
    if contraseña_ingresada == contraseña_correcta:
        print("¡Acceso concedido!")
        break 
    else:
        print("Contraseña incorrecta, por favor inténtalo de nuevo") 
