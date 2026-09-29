
from abc import ABC, abstractmethod


# Clase base abstracta
class Persona(ABC):

    def __init__(self, nombre, apellido, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_dni(self):
        return self.__dni

    @abstractmethod
    def mostrar_datos(self):
        pass


# Clase Alumno que hereda de Persona
class Alumno(Persona):

    def __init__(self, nombre, apellido, dni, curso, promedio):
        super().__init__(nombre, apellido, dni)

        self.__curso = curso
        self.__promedio = promedio

    # Getters
    def get_curso(self):
        return self.__curso

    def get_promedio(self):
        return self.__promedio

    # Implementación del método abstracto
    def mostrar_datos(self):
        print("----- DATOS DEL ALUMNO -----")
        print("Nombre:", self.get_nombre())
        print("Apellido:", self.get_apellido())
        print("DNI:", self.get_dni())
        print("Curso:", self.get_curso())
        print("Promedio:", self.get_promedio())


# Crear un objeto Alumno
alumno1 = Alumno(
    "Victoria",
    "Funez",
    "12345678",
    "4° 4°",
    8.5
)

# Mostrar sus datos
alumno1.mostrar_datos()
