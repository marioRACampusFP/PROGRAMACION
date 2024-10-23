texto = input("Escriba un texto: ")
vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
contador = 0
for i in texto:
    if i in vocales:
        contador = contador +1
print(contador)
