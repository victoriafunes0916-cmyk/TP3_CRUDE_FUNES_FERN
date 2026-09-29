class GestorAcademico:

    def __init__(self):
        self.__base_datos_alumnos = []

    def registrar_nuevo_alumno(self, alumno):

        # Verificamos si el DNI ya existe
        for alumno_existente in self.__base_datos_alumnos:

            if alumno_existente.get_dni() == alumno.get_dni():
                print("ERROR: El DNI ya está registrado.")
                return

        # Si no está repetido, se agrega
        self.__base_datos_alumnos.append(alumno)

        print("Alumno registrado correctamente.")


    def mostrar_alumnos(self):

        print("\n===== ALUMNOS REGISTRADOS =====")

        for alumno in self.__base_datos_alumnos:
            alumno.mostrar_datos()