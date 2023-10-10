alumnos = []

while True:
    alumno = {}
    alumno["Alumno"] = input("Ingrese el nombre del alumno (o escriba 'salir' para finalizar): ")
    
    if alumno["Alumno"].lower() == "salir":
        break
    
    notas = []
    for i in range(3):
        nota = int(input(f"Ingrese la calificación {i+1} del alumno: "))
        notas.append(nota)
    
    alumno["Notas"] = notas
    alumnos.append(alumno)

print("Listado completo de alumnos:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")
