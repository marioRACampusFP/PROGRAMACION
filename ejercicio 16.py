menu = {
    "Cola cao": (1.9, 75),
    "Capuchino": (3, 100),
    "Donut": (1.5, 90),
    "Bocata de bacon XXL": (5, 450),
    "Coca cola": (2, 140)
}

print("Menu: ")
for producto, (precio, calorias) in menu.items():
    print(f"- {producto}: {precio}€ ({calorias} cal)")

pedido = []
total_precio = 0
total_calorias = 0

while True:
    producto = input ("Escribe el nombre del producto que quieras meter en la lista (o 'fin' para terminar): ")
    if producto == 'fin':
        break

    if producto in menu:
        pedido.append(producto)
        precio, calorias = menu[producto]
        total_precio += precio
        total_calorias += calorias
        print(f"Has metido el siguiente producto {producto}")


print("\n Tu pedido es: ")
for item in pedido:
    print(f"- {item}")

print(f"\nTotal para pagar: {total_precio}€")
print(f"Calorías totales: {total_calorias} cal")
