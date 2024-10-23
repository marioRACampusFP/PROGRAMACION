
edad_persona = int (input())
if edad_persona < 5:
    print("La entrada te sale gratis")
elif edad_persona >= 5 and edad_persona <=12:
    print("La entrada cuesta 5 euros")
elif edad_persona >= 13 and edad_persona <=17:
    print("La entrada cuesta 10 euros")
elif edad_persona > 18:
    print("La entrada cuesta 10 euros")



nota = int(input())
if nota > 90:
    print("La calificación es A  ")
elif nota >= 80:
    print ("La clasificación es B ")
elif nota >=70:
    print("La clasificación es C")
elif nota >=60:
    print("La clasificación es D")
else:
    print ("F")



dia = int(input())
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")  
    case 7:
        print("Domingo")
    case _:
        print("Número inválido")
        

idioma= input()
match idioma:
    case "es":
        print("Idioma elegido Español")
    case "en":
        print("Idioma elegido Inglés")
    case "fr":
        print("Idioma elegido Francés")
    case _:
        print("Idioma no soportado")


edad= int(input())
if edad < 12:
    print ("Es un niño")
elif edad <17:
    print("Es un adolescente")
elif edad < 59:
    print("Es un adulto")
else:
    print("Es un señor mayor")
    

vehiculo = str(input())
if vehiculo == "coche":
    print("vehículo de 4 ruedas")
elif vehiculo == "moto":
    print("vehículo de dos ruedas")
elif vehiculo == "bicicleta":
    print("vehículo no motorizado")
else:
    print("Tipo de vehículo no reconocido")


color = str(input())
match color:
    case "rojo":
        print("Color rojo")
    case "azul":
        print("Color azul")
    case "verde":
        print("Color verde")
    case _:
        print("este color no está disponible")
