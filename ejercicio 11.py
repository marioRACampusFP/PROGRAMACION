dic1 = {}
while True:
    nombre = input("Introduce el nombre del nuevo contacto: ")
   

    if nombre == "fin":
        break
      
    telefono = input(f"Introduce el teléfono de {nombre}: ")
    dic1 [nombre] = telefono

print("Esta es una agenda")
print(dic1)

contacto = (input("Escribe el nombre del contacto: "))
print (f"El número de teléfono es: {telefono}")