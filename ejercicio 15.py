calificaciones = {}

while True:
    asignatura = input("Escribe la asignatura (o escribe 'fin' para terminar): ")
    if asignatura == "fin":
        break
    
    calificacion = float(input(f"Ingresa la nota de {asignatura}: "))
    calificaciones[asignatura] = calificacion
    

print("\nResumen de asignaturas y notas:")
for asignatura, calificacion in calificaciones.items():
    print(f"{asignatura}: {calificacion}")


media = sum(calificaciones.values()) / len(calificaciones)
print(f"\nLa nota media es: {media:.2f}")
