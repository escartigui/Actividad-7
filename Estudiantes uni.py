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
                 if carnet in estudiantes:
                     print("El codigo ya esta utilizado")
                 else:
                     break

             nombre = input("Ingrese el nombre: ")
             edad = input("Ingrese la edad: ")
             carrera = input("Ingrese el nombre de la carrera: ")
             cursos = {}
             canticurs = int(input("cuantos cursos desea ingresar"))
             for n in range(canticurs):
                  print(f"curso #{n+1}")
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
                  estudiantes[carnet] = {
                     "nombre": nombre,
                    "edad": edad,
                    "carrera": carrera,
                    "cursos": cursos,
                  }
                  cursos[nomcurso] ={
                     "nota": notatarea,
                     "parcial": notaparcial,
                     "proyecto": notaproyec,

                 }
        if op == "2":
         print("\nListado de estudiantes")
         for carnet,datos in estudiantes.items():
            print(f"Carnet: {carnet}")
            print(f"nombre: {datos['nombre']}")
            print(f"edad: {datos['edad']}")
            print(f"carrera: {datos['carrera']}")
            for curso,datoss in datos['cursos'].items():
             print(f"Curso: {curso}")
             print(f"nota: {datoss['nota']}")
             print(f"parcial: {datoss['parcial']}")
             print(f"proyecto: {datoss['proyecto']}")
menu()

