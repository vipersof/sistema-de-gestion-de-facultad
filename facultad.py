from estudiante import Estudiante
from curso import Curso


class EstudianteNoEncontradoError(Exception):
    pass

class CursoNoEncontradoError(Exception):
    pass

class SinCuposDisponiblesError(Exception):
    pass

class EstudianteYaInscriptoError(Exception):
    pass

class EstudianteNoInscriptoError(Exception):
    pass


class Facultad:
    def __init__(self):
        self.__estudiantes = []
        self.__cursos = []

    # ------------------------------------------------------------------ #
    #  AGREGAR                                                             #
    # ------------------------------------------------------------------ #
    def agregarEstudiante(self, nombre, apellido, matricula, carrera):
        """Agrega un estudiante nuevo. Lanza ValueError si la matrícula ya existe."""
        try:
            self.buscarEstudiante(matricula)
            raise ValueError(f"Ya existe un estudiante con matrícula {matricula}.")
        except EstudianteNoEncontradoError:
            estudiante = Estudiante(nombre, apellido, matricula, carrera)
            self.__estudiantes.append(estudiante)
            print(f"✔ Estudiante '{nombre} {apellido}' agregado correctamente.")

    def agregarCurso(self, nombre, codigo, profesor, capacidad_maxima):
        """Agrega un curso nuevo. Lanza ValueError si el código ya existe."""
        try:
            self.buscarCurso(codigo)
            raise ValueError(f"Ya existe un curso con código {codigo}.")
        except CursoNoEncontradoError:
            try:
                capacidad_maxima = int(capacidad_maxima)
                if capacidad_maxima <= 0:
                    raise ValueError("La capacidad máxima debe ser mayor a 0.")
            except ValueError:
                raise ValueError("La capacidad máxima debe ser un número entero positivo.")
            curso = Curso(nombre, codigo, profesor, capacidad_maxima)
            self.__cursos.append(curso)
            print(f"✔ Curso '{nombre}' agregado correctamente.")

    # ------------------------------------------------------------------ #
    #  BUSCAR (uso interno)                                                #
    # ------------------------------------------------------------------ #
    def buscarEstudiante(self, matricula):
        """Devuelve el Estudiante con esa matrícula. Lanza EstudianteNoEncontradoError si no existe."""
        for estudiante in self.__estudiantes:
            if str(estudiante.getMatricula()) == str(matricula):
                return estudiante
        raise EstudianteNoEncontradoError(f"No se encontró ningún estudiante con matrícula {matricula}.")

    def buscarCurso(self, codigo):
        """Devuelve el Curso con ese código. Lanza CursoNoEncontradoError si no existe."""
        for curso in self.__cursos:
            if str(curso.getCodigo()) == str(codigo):
                return curso
        raise CursoNoEncontradoError(f"No se encontró ningún curso con código {codigo}.")

    # ------------------------------------------------------------------ #
    #  MOSTRAR                                                             #
    # ------------------------------------------------------------------ #
    def mostrarEstudiantes(self):
        if not self.__estudiantes:
            print("No hay estudiantes registrados.")
            return
        print("\n===== ESTUDIANTES =====")
        for estudiante in self.__estudiantes:
            print(estudiante)
        print("=======================\n")

    def mostrarCursos(self):
        if not self.__cursos:
            print("No hay cursos registrados.")
            return
        print("\n===== CURSOS =====")
        for curso in self.__cursos:
            print(curso)
        print("==================\n")

    # ------------------------------------------------------------------ #
    #  INSCRIPCIÓN                                                         #
    # ------------------------------------------------------------------ #
    def inscribirEstudiante(self, matricula, codigo_curso):

        try:
            estudiante = self.buscarEstudiante(matricula)
            curso = self.buscarCurso(codigo_curso)

            # Verificar si ya está inscripto
            if estudiante in curso.getEstudiantesInscriptos():
                raise EstudianteYaInscriptoError(
                    f"{estudiante.getNombre()} ya está inscripto en '{curso.getNombre()}'."
                )

           
            if curso.getCuposDisponibles() == 0:
                raise SinCuposDisponiblesError(
                    f"El curso '{curso.getNombre()}' no tiene cupos disponibles."
                )

            
            curso.inscribirEstudiante(estudiante)
            estudiante.inscribirCurso(curso)

            print(f"✔ {estudiante.getNombre()} {estudiante.getApellido()} "
                  f"inscripto en '{curso.getNombre()}' correctamente.")

        except EstudianteNoEncontradoError as e:
            print(f"Error: {e}")
        except CursoNoEncontradoError as e:
            print(f"Error: {e}")
        except EstudianteYaInscriptoError as e:
            print(f"Error: {e}")
        except SinCuposDisponiblesError as e:
            print(f"Error: {e}")

    # ------------------------------------------------------------------ #
    #  BAJA DE CURSO                                                       #
    # ------------------------------------------------------------------ #
    def darBajaCurso(self, matricula, codigo_curso):
        
        try:
            estudiante = self.buscarEstudiante(matricula)
            curso = self.buscarCurso(codigo_curso)

            if estudiante not in curso.getEstudiantesInscriptos():
                raise EstudianteNoInscriptoError(
                    f"{estudiante.getNombre()} no está inscripto en '{curso.getNombre()}'."
                )

            curso.darBajaEstudiante(estudiante)
            estudiante.darBajaCurso(curso)

            print(f"✔ {estudiante.getNombre()} {estudiante.getApellido()} "
                  f"dado de baja de '{curso.getNombre()}' correctamente.")

        except EstudianteNoEncontradoError as e:
            print(f"Error: {e}")
        except CursoNoEncontradoError as e:
            print(f"Error: {e}")
        except EstudianteNoInscriptoError as e:
            print(f"Error: {e}")

    # ------------------------------------------------------------------ #
    #  CONSULTAS DE ESTADO                                                 #
    # ------------------------------------------------------------------ #
    def consultarEstadoCursos(self):
       
        if not self.__cursos:
            print("No hay cursos registrados.")
            return
        print("\n===== ESTADO DE CURSOS =====")
        for curso in self.__cursos:
            print(curso)
            inscriptos = curso.getEstudiantesInscriptos()
            if inscriptos:
                for est in inscriptos:
                    print(f"     - {est.getNombre()} {est.getApellido()} "
                          f"(Matrícula: {est.getMatricula()})")
        print("============================\n")

    def consultarEstadoEstudiantes(self):
       
        if not self.__estudiantes:
            print("No hay estudiantes registrados.")
            return
        print("\n===== ESTADO DE ESTUDIANTES =====")
        for estudiante in self.__estudiantes:
            print(estudiante)
        print("=================================\n")
