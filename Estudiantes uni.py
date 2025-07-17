estudiantes = {}
cantidad = int(input("Cuantos estudiante desea ingresar"))
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
         for i in range(cantidad):
             print(f"Estudiante #{i+1}")
             carnet = input("Ingrese el numero de carnet: ")
             nombre = input("Ingrese el nombre: ")
             edad = input("Ingrese el edad: ")
             carrera = input("Ingrese el carrera: ")
             cursos = input("Ingrese codigo del curso: ")


