class Curso:
    def __init__(self, nombre, codigo, profesor, capacidad_maxima):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__profesor = profesor
        self.__capacidad_maxima = capacidad_maxima
        self.__estudiantes_inscriptos = []   
    def getNombre(self):
        return self.__nombre

    def getCodigo(self):
        return self.__codigo

    def getProfesor(self):
        return self.__profesor

    def getCapacidadMaxima(self):
        return self.__capacidad_maxima

    def getEstudiantesInscriptos(self):
        return self.__estudiantes_inscriptos

    def getCuposDisponibles(self):
        return self.__capacidad_maxima - len(self.__estudiantes_inscriptos)

    # --- Gestión de inscripción ---
    def inscribirEstudiante(self, estudiante):
        self.__estudiantes_inscriptos.append(estudiante)

    def darBajaEstudiante(self, estudiante):
        self.__estudiantes_inscriptos.remove(estudiante)


    def __str__(self):
        return (f"Curso: {self.__nombre} "
                f"| Código: {self.__codigo} "
                f"| Profesor: {self.__profesor} "
                f"| Inscriptos: {len(self.__estudiantes_inscriptos)}/{self.__capacidad_maxima} "
                f"| Cupos disponibles: {self.getCuposDisponibles()}")
