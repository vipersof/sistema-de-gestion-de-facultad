class Estudiante:
    def __init__(self, nombre, apellido, matricula, carrera):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__matricula = matricula      # identificador único
        self.__carrera = carrera
        self.__cursos_inscriptos = []     # lista de cursos en los que está inscripto

    # --- Getters ---
    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getMatricula(self):
        return self.__matricula

    def getCarrera(self):
        return self.__carrera

    def getCursosInscriptos(self):
        return self.__cursos_inscriptos

    # --- Gestión de cursos ---
    def inscribirCurso(self, curso):
        self.__cursos_inscriptos.append(curso)

    def darBajaCurso(self, curso):
        self.__cursos_inscriptos.remove(curso)

    # --- Representación legible ---
    def __str__(self):
        if not self.__cursos_inscriptos:
            cursos = "ninguno"
        else:
            cursos = ", ".join([c.getNombre() for c in self.__cursos_inscriptos])
        return (f"Nombre: {self.__nombre} {self.__apellido} "
                f"| Matrícula: {self.__matricula} "
                f"| Carrera: {self.__carrera} "
                f"| Cursos: {cursos}")
