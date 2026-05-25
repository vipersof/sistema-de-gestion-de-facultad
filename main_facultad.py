from facultad import Facultad


def mostrarMenu():
    print("\n========== FACULTAD ==========")
    print("1 - Agregar estudiante")
    print("2 - Agregar curso")
    print("3 - Mostrar todos los estudiantes")
    print("4 - Mostrar todos los cursos")
    print("5 - Inscribir estudiante a curso")
    print("6 - Dar de baja estudiante de curso")
    print("7 - Consultar estado de cursos")
    print("8 - Consultar estado de estudiantes")
    print("0 - Salir")
    print("==============================\n")


def main():
    facultad = Facultad()

    while True:
        mostrarMenu()

        try:
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "0":
                print("Saliendo del sistema. ¡Hasta luego!")
                break

            elif opcion == "1":
                nombre    = input("Nombre: ").strip()
                apellido  = input("Apellido: ").strip()
                matricula = input("Número de matrícula: ").strip()
                carrera   = input("Carrera: ").strip()
                facultad.agregarEstudiante(nombre, apellido, matricula, carrera)

            elif opcion == "2":
                nombre    = input("Nombre del curso: ").strip()
                codigo    = input("Código del curso: ").strip()
                profesor  = input("Profesor encargado: ").strip()
                capacidad = input("Capacidad máxima de estudiantes: ").strip()
                facultad.agregarCurso(nombre, codigo, profesor, capacidad)

            elif opcion == "3":
                facultad.mostrarEstudiantes()

            elif opcion == "4":
                facultad.mostrarCursos()

            elif opcion == "5":
                matricula     = input("Matrícula del estudiante: ").strip()
                codigo_curso  = input("Código del curso: ").strip()
                facultad.inscribirEstudiante(matricula, codigo_curso)

            elif opcion == "6":
                matricula     = input("Matrícula del estudiante: ").strip()
                codigo_curso  = input("Código del curso: ").strip()
                facultad.darBajaCurso(matricula, codigo_curso)

            elif opcion == "7":
                facultad.consultarEstadoCursos()

            elif opcion == "8":
                facultad.consultarEstadoEstudiantes()

            else:
                print("Opción inválida. Ingresá un número del 0 al 8.")

        except ValueError as e:
            print(f"Error de valor: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
