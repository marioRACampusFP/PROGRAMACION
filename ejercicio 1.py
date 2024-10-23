temperatura = 24
if temperatura > 25:
    print ("hace calor")
else:
    print("hace frío")

edad = 18
es_estudiante = False
if edad < 18 and es_estudiante:
    print("es un estudiante menor de edad")
elif edad < 18 and not es_estudiante:
    print ("es menor de edad pero no es estudiante")
else:
    print("es mayor de edad")

nota = 40
if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print ("notable")
elif nota >=50:
    print("aprobado")
else:
    print ("suspenso")

print ("escribe un día de la semana")
dia = input()
match dia:
    case "lunes":
        print ("hoy es lunes")
    case "martes":
        print ("hoy es martes")
    case _:
        print ("Es otro día de la semana")