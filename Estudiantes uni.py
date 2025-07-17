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
             carnet = input("Ingrese el numero de carnet: ")
             nombre = input("Ingrese el nombre: ")
             edad = input("Ingrese el edad: ")
             carrera = input("Ingrese el carrera: ")
             canticurs = int(input("cuantos cursos desea ingresar"))
             for n in range(canticurs):
              print(f"curso #{n+1}")
              cursos = input("Ingrese el nombre de los cursos")
             while True:
              notatarea = input("ingrese la nota de su tarea: ")
             if notatarea <= 0:
                 print("verifica lo ingresado, no puede ser negativo")
             else:
                 break
menu()

