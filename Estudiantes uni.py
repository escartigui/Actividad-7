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
                     estudiantes[carnet] = {}
                     break

             estudiantes[carnet]["nombre"] = input("Ingrese el nombre: ")
             estudiantes[carnet]["edad"] = input("Ingrese la edad: ")
             estudiantes[carnet]["carrera"] = input("Ingrese el nombre de la carrera: ")
             estudiantes[carnet]["cursos"] = {}
             canticurs = int(input("cuantos cursos desea ingresar"))
             for a in range(canticurs):
                  print(f"curso #{a+1}")
                  codigo_curso = input("Ingrese el codigo de la curso: ")
                  nomcurso = input("Ingrese el nombre de los cursos")
                  while True:
                     tarea = int(input("ingrese la nota de su tarea: "))
                     if tarea <= 0:
                        print("verifica lo ingresado, no puede ser negativo")
                     else:
                      break
                  while True:
                     parcial = int(input("Ingrese la nota de su parcial: "))
                     if parcial <= 0:
                      print("Verifica lo ingresado, no puede ser negativo")
                     else:
                       break
                  while True:
                    proyecto = int(input("Ingrese la nota de su proyecto: "))
                    if proyecto <= 0:
                     print("verifica lo ingresado, no puede ser negativo")
                    else:
                      break
                  estudiantes[carnet]["cursos"][codigo_curso] = {
                      "nombre": nomcurso,
                      "tarea" : tarea,
                      "parcial" : parcial,
                      "proyecto" : proyecto,
                    }
        if op == "2":
         print("\nListado de estudiantes")
         for carnet,datos in estudiantes.items():
            print(f"\nCarnet: {carnet}")
            print(f"nombre: {datos['nombre']}")
            print(f"edad: {datos['edad']}")
            print(f"carrera: {datos['carrera']}")
            print("cursos: ")
            for codigo,curso in datos["cursos"].items():
                promedio = (curso["tarea"] + curso["parcial"] + curso["proyecto"])/3
                print(f"codigo: {codigo}")
                print(f"nombre: {curso['nombre']}")
                print(f"tarea: {curso['tarea']}")
                print(f"parcial: {curso['parcial']}")
                print(f"proyecto: {curso['proyecto']}")
                print(f"promedio: {promedio:.2f}")

        if op == "3":
            print("\nBusqueda de estudiantes")
            buscado = input("Ingrese carnet para la busqueda: ")
            if buscado in estudiantes:
                est = estudiantes[buscado]
                print("\n Lo encontramos")
                print(f"nombre: {est['nombre']}")
                print(f"edad: {est['edad']}")
                print(f"carrera: {est['carrera']}")
                print("cursos: ")
                for codigo,curso in est["cursos"].items():
                    promedio = (curso["tarea"]+curso["parcial"]+curso["proyecto"])/3
                    print(f"codigo: {codigo}")
                    print(f"nombre: {curso['nombre']}")
                    print(f"tarea: {curso['tarea']}")
                    print(f"parcial: {curso['parcial']}")
                    print(f"proyecto: {curso['proyecto']}")
                    print(f"promedio: {promedio:.2f}")
            else:
                print("No existe la busqueda")

        if op == "4":
                print("\nNOS VEREMOS EN OTRO MOMENTO")
                break
        else:
            print("\nIntenta de nuevo")
menu()