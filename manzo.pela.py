estudiantes = {
    "Emiliano Manzo": {"edad": 17, "materias": ["Matemáticas", "Física"]},
    "Agustin Cevini": {"edad": 16, "materias": ["Química", "Historia"]},
    "Lautaro Diaz": {"edad": 18, "materias": ["Biología", "Inglés"]}
}

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    materias = input(f"Ingrese las materias de {nombre} separadas por coma: ").split(",")
    estudiantes[nombre] = {"edad": edad, "materias": [materia.strip() for materia in materias]}
    print(f"Estudiante {nombre} agregado correctamente.")

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    for nombre, info in estudiantes.items():
        print(f"Nombre: {nombre}")
        print(f"Edad: {info['edad']}")
        print(f"Materias aprobadas: {', '.join(info['materias'])}")
        print("-" * 30)

def eliminar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Estudiante {nombre} eliminado correctamente.")
    else:
        print(f"No se encontró al estudiante {nombre}.")

def buscar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a buscar: ")
    if nombre in estudiantes:
        info = estudiantes[nombre]
        print(f"Nombre: {nombre}")
        print(f"Edad: {info['edad']}")
        print(f"Materias aprobadas: {', '.join(info['materias'])}")
    else:
        print(f"No se encontró al estudiante {nombre}.")

# Función para verificar si una palabra clave está en el nombre de algún estudiante
def verificar_palabra_clave():
    palabra = input("Ingrese la palabra clave para buscar en los nombres: ").lower()
    estudiantes_encontrados = [nombre for nombre in estudiantes if palabra in nombre.lower()]
    if estudiantes_encontrados:
        print(f"Estudiantes encontrados con la palabra '{palabra}':")
        for nombre in estudiantes_encontrados:
            print(f"- {nombre}")
    else:
        print(f"No se encontraron estudiantes con la palabra clave '{palabra}'.")

# Menú principal utilizando el match
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Eliminar estudiante")
        print("4. Buscar estudiante")
        print("5. Verificar palabra clave en nombres")
        print("6. Salir")
        
        opcion = input("Seleccione una opción (1-6): ")

        match opcion:
            case "1":
                agregar_estudiante()
            case "2":
                mostrar_estudiantes()
            case "3":
                eliminar_estudiante()
            case "4":
                buscar_estudiante()
            case "5":
                verificar_palabra_clave()
            case "6":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida, por favor ingrese un número del 1 al 6.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()