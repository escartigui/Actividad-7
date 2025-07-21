estudiantes = {}
def menu():
    while True:
        print("\nBienvenido a la universidad")
        print("MENU")
        print("1.Registrar Estudiantes")
        print("2.Mostrar los estudiantes y sus cursos")
        print("3.Buscar estudiantes")
        print("4.Salir")
        op = input("Seleccione una opción: ")

        if op == "1":
         cantidad = int(input("Cuantos estudiante desea ingresar"))
         for i in range(cantidad):
             print(f"Estudiante #{i+1}")
             while True:
                 carnet = input("Ingrese el numero de carnet: ")
                 estudiantes[carnet] = {}
                 if carnet in estudiantes:
                     print("El codigo ya esta utilizado")
                 else:
                     break

             nombre = input("Ingrese el nombre: ")
             edad = input("Ingrese la edad: ")
             carrera = input("Ingrese el nombre de la carrera: ")
             canticurs = int(input("cuantos cursos desea ingresar"))
             for a in range(canticurs):
                  print(f"curso #{a+1}")
                  nomcurso = input("Ingrese el nombre de los cursos")
                  while True:
                     notatarea = int(input("ingrese la nota de su tarea: "))
                     if notatarea <= 0:
                        print("verifica lo ingresado, no puede ser negativo")
                     else:
                      break
                  while True:
                     notaparcial = int(input("Ingrese la nota de su parcial: "))
                     if notaparcial <= 0:
                      print("Verifica lo ingresado, no puede ser negativo")
                     else:
                       break
                  while True:
                    notaproyec = int(input("Ingrese la nota de su proyecto: "))
                    if notaproyec <= 0:
                     print("verifica lo ingresado, no puede ser negativo")
                    else:
                      break
                  estudiantes[carnet]["canticurs"][nomcurso] = {
                     "nombre": nombre,
                    "edad": edad,
                    "carrera": carrera,
                    "ing": {
                     "nomcurso": nomcurso,
                     "nota": notatarea,
                     "parcial": notaparcial,
                     "proyecto": notaproyec,
                    }
                 }
        if op == "2":
         print("\nListado de estudiantes")
         for carnet,datos in estudiantes.items():
            promedio = (datos["nota"] + datos["parcial"] + datos["proyecto"]) / 3
            print(f"Carnet: {carnet}")
            print(f"nombre: {datos['nombre']}")
            print(f"edad: {datos['edad']}")
            print(f"carrera: {datos['carrera']}")
            print(f"nomcurso: {datos['ing']['nomcurso']}")
            print(f"nota: {datos['ing']['nota']}")
            print(f"parcial: {datos['ing']['parcial']}")
            print(f"proyecto: {datos['ing']['proyecto']}")
            print(f"promedio: {promedio:.2f}")
menu()