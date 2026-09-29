
from abc import ABC, abstractmethod

# CLASE PERSONA

class Persona(ABC):

    def __init__(self, nombre, apellido, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_dni(self):
        return self.__dni

    @abstractmethod
    def mostrar_datos(self):
        pass


# CLASE ALUMNO

class Alumno(Persona):

    def __init__(self, nombre, apellido, dni, curso, promedio):
        super().__init__(nombre, apellido, dni)

        self.__curso = curso
        self.__promedio = promedio

    def get_curso(self):
        return self.__curso

    def get_promedio(self):
        return self.__promedio

    def mostrar_datos(self):
        print("----- DATOS DEL ALUMNO -----")
        print("Nombre:", self.get_nombre())
        print("Apellido:", self.get_apellido())
        print("DNI:", self.get_dni())
        print("Curso:", self.get_curso())
        print("Promedio:", self.get_promedio())


# ESTRATEGIA DE GUARDADO

class EstrategiaGuardado(ABC):

    @abstractmethod
    def guardar(self, datos):
        pass

# GUARDADO EN MEMORIA

class GuardadoMemoria(EstrategiaGuardado):

    def guardar(self, datos):
        print("El alumno fue guardado en la memoria RAM temporal.")

# GUARDADO EN ARCHIVO TXT


class GuardadoArchivoTXT(EstrategiaGuardado):

    def guardar(self, datos):

        with open("registro_alumnos.txt", "a", encoding="utf-8") as archivo:

            archivo.write(
                f"Nombre: {datos.get_nombre()}\n"
                f"Apellido: {datos.get_apellido()}\n"
                f"DNI: {datos.get_dni()}\n"
                f"Curso: {datos.get_curso()}\n"
                f"Promedio: {datos.get_promedio()}\n"
                f"-----------------------------\n"
            )

        print("El alumno fue guardado en registro_alumnos.txt.")


# GESTOR ACADEMICO

class GestorAcademico:

    def __init__(self, estrategia_guardado):
        self.__base_datos_alumnos = []
        self.__estrategia_guardado = estrategia_guardado

    def registrar_nuevo_alumno(self, alumno):

        # Verificar si el DNI ya existe
        for alumno_existente in self.__base_datos_alumnos:

            if alumno_existente.get_dni() == alumno.get_dni():
                print("ERROR: El DNI ya está registrado.")
                return

        # Agregar el alumno a la base de datos
        self.__base_datos_alumnos.append(alumno)

        print("Alumno registrado correctamente.")

        # Guardar usando la estrategia seleccionada
        self.__estrategia_guardado.guardar(alumno)

    def mostrar_alumnos(self):

        print("\n===== ALUMNOS REGISTRADOS =====")

        for alumno in self.__base_datos_alumnos:
            alumno.mostrar_datos()


# PROGRAMA PRINCIPAL

# Crear alumnos
alumno1 = Alumno(
    "Victoria",
    "Funes",
    "12345678",
    "4° 3°",
    8.5
)

alumno2 = Alumno(
    "Avril",
    "Perez",
    "87654321",
    "4° 4°",
    7.5
)


# GESTOR CON GUARDADO EN MEMORIA


print("\n===== GUARDADO EN MEMORIA =====")

gestor_memoria = GestorAcademico(GuardadoMemoria())

gestor_memoria.registrar_nuevo_alumno(alumno1)


# GESTOR CON GUARDADO EN TXT


print("\n===== GUARDADO EN ARCHIVO TXT =====")

gestor_txt = GestorAcademico(GuardadoArchivoTXT())

gestor_txt.registrar_nuevo_alumno(alumno2)


# INTENTAR REGISTRAR DNI REPETIDO


print("\n===== PRUEBA DE DNI REPETIDO =====")

alumno3 = Alumno(
    "Abigail",
    "Fernandez",
    "87654321",
    "4° °",
    9
)

gestor_txt.registrar_nuevo_alumno(alumno3)