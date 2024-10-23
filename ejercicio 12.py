nombres = []

while True:
    nombre = input("Escribe el nombre que quieras (o escribe 'fin' para terminar): ")
    if nombre == "fin":
        break
    nombres.append(nombre) 

print("\nLos nombres ingresados son:")
print(nombres)

print("\nLos nombres son:")
for nombre in nombres:
    print(nombre)